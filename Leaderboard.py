import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='fahim123',
        database='connect_four'
    )

def fetch_player_data(cursor, player):
    cursor.execute("SELECT Wins, Loses FROM leaderboard WHERE Username = %s",(player,))
    result = cursor.fetchone()
    if result:
        return result[0], result[1]  # Wins, Loses
    return 0, 0  # Default for new players

def update_leaderboard(cursor, player, wins, losses, win_loss_ratio):
    cursor.execute("SELECT * FROM leaderboard WHERE Username = %s", (player,))
    if cursor.fetchone():
        query = "UPDATE leaderboard SET Wins = %s, Loses = %s, WintoLoseRatio = %s WHERE Username = %s"
        cursor.execute(query, (wins, losses, win_loss_ratio, player))
    else:
        query = "INSERT INTO leaderboard (Username, Wins, Loses, WintoLoseRatio) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (player, wins, losses, win_loss_ratio))

def display_leaderboard(cursor):
    cursor.execute("SELECT * FROM leaderboard ORDER BY Wins DESC, Loses ASC")
    leaderboard = cursor.fetchall()
    print("\n--- Leaderboard ---")
    print(f"{'Username':<15} {'Wins':<5} {'Loses':<5} {'Win-to-Lose Ratio':<15}")
    print("-" * 45)
    for row in leaderboard:
        print(f"{row[0]:<15} {row[1]:<5} {row[2]:<5} {row[3]:<15}")

# Connect Four game logic
ROW, COLUMN = 6, 7

def initialize_board():
    return [[" " for _ in range(COLUMN)] for _ in range(ROW)]

def board_maker(board):
    print("╔═╦═╦═╦═╦═╦═╦═╗")
    for row in board:
        print("╠" + "╬".join(row) + "╣")
    print("╚═╩═╩═╩═╩═╩═╩═╝")

def is_valid_move(board, column):
    return board[0][column] == " "

def slot_drop(board, column, disc):
    for row in range(ROW - 1, -1, -1):
        if board[row][column] == " ":
            board[row][column] = disc
            break

def win_condition(board, disc):
    for row in range(ROW):
        for column in range(COLUMN):
            if board[row][column] == disc:
                # Horizontal
                if column + 3 < COLUMN and all(board[row][column + i] == disc for i in range(4)):
                    return True
                # Vertical
                if row + 3 < ROW and all(board[row + i][column] == disc for i in range(4)):
                    return True
                # Diagonal (down-right)
                if row + 3 < ROW and column + 3 < COLUMN and all(board[row + i][column + i] == disc for i in range(4)):
                    return True
                # Diagonal (down-left)
                if row + 3 < ROW and column - 3 >= 0 and all(board[row + i][column - i] == disc for i in range(4)):
                    return True
    return False

def true_game(player1, player2, cursor, connection):
    board = initialize_board()
    turn = 0
    while True:
        board_maker(board)
        if turn % 2 == 0:
            player_in_play, disc = player1, "○"
        else:
            player_in_play, disc = player2, "●"

        print(player_in_play, "'s turn")

        while True:
            try:
                column = int(input("Choose a column (1-7): ")) - 1
                if 0 <= column < COLUMN and is_valid_move(board, column):
                    break
                else:
                    print("Invalid column or column is full, try again!")
            except ValueError:
                print("Invalid input, enter a number!")

        slot_drop(board, column, disc)

        if win_condition(board, disc):
            board_maker(board)
            print(player_in_play, "won the game!!!")
            
            # Update database based on winner
            if player_in_play == player1:
                wins1, losses1 = fetch_player_data(cursor, player1)
                wins2, losses2 = fetch_player_data(cursor, player2)
                update_leaderboard(cursor, player1, wins1 + 1, losses1, f"{wins1 + 1}:{losses1}")
                update_leaderboard(cursor, player2, wins2, losses2 + 1, f"{wins2}:{losses2 + 1}")
            else:
                wins1, losses1 = fetch_player_data(cursor, player1)
                wins2, losses2 = fetch_player_data(cursor, player2)
                update_leaderboard(cursor, player1, wins1, losses1 + 1, f"{wins1}:{losses1 + 1}")
                update_leaderboard(cursor, player2, wins2 + 1, losses2, f"{wins2 + 1}:{losses2}")
            
            connection.commit()
            break

        if all(board[0][column] != " " for column in range(COLUMN)):
            board_maker(board)
            print("It's a draw!!")
            break

        turn += 1

# Main program loop
while True:
    game_info = connect_to_database()
    focalor = game_info.cursor()

    player1 = input("Player 1 (○): ")
    player2 = input("Player 2 (●): ")

    true_game(player1, player2, focalor, game_info)

    display_leaderboard(focalor)

    focalor.close()
    game_info.close()

    if input("Play again? (y/n): ").lower() != "y":
        break
