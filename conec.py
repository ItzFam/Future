#god help me + im sad
import mysql.connector


while True:
    # Connect to the database
    game_info = mysql.connector.connect(
        host='localhost',
        user='root',
        password='fahim123',
        database='connect_four'
    )

    focalor = game_info.cursor()

    def player_info():
        # Initialize variables
        win1 = 0
        win2 = 0
        lose1 = 0
        lose2 = 0
        ratio1 = None
        ratio2 = None

        # Ask for user details
        option = input("Do you have an existing account (y/n)?: ").lower()

        if option == 'n':  # New account
            player1 = input("Player 1(○): ")
            player2 = input("Player 2(●): ")

            win_or_lose = input("Did player1 Win or Lose (W/L)?: ").upper()
            
            # Update win/loss counts based on input
            if win_or_lose == 'W':
                win1 += 1
                lose2 += 1
            elif win_or_lose == 'L':
                lose1 += 1
                win2 += 1
            else:
                print("Invalid Input")
                return None, None, None, None, None, None, None, None

            ratio1 = f"{win1}:{lose1}"  # Calculate win/loss ratio for player1
            ratio2 = f"{win2}:{lose2}"  # Calculate win/loss ratio for player2

        elif option == 'y':  # Existing account
            player1 = input("Player 1(○): ")
            player2 = input("Player 2(●): ")

            win_or_lose = input("Did player1 Win or Lose (W/L)?: ").upper()
            
            # Update win/loss counts based on input
            if win_or_lose == 'W':
                win1 += 1
                lose2 += 1
            elif win_or_lose == 'L':
                lose1 += 1
                win2 += 1
            else:
                print("Invalid Input")
                return None, None, None, None, None, None, None, None

            # Fetch current data for existing users
            focalor.execute("SELECT Wins, Loses FROM leaderboard WHERE Username = %s", (player1,))
            result1 = focalor.fetchone()
            if result1:
                win1 += result1[0]
                lose1 += result1[1]

            focalor.execute("SELECT Wins, Loses FROM leaderboard WHERE Username = %s", (player2,))
            result2 = focalor.fetchone()
            if result2:
                win2 += result2[0]
                lose2 += result2[1]

            ratio1 = f"{win1}:{lose1}"
            ratio2 = f"{win2}:{lose2}"

        else:
            print("Invalid option!")
            return None, None, None, None, None, None, None, None

        return win1, win2, lose1, lose2, ratio1, ratio2, player1, player2

    # Get player data
    win1, win2, lose1, lose2, ratio1, ratio2, player1, player2 = player_info()

    if player1 and player2:  # Ensure input is valid before executing queries
        # Check if player1 exists
        focalor.execute("SELECT * FROM leaderboard WHERE Username = %s", (player1,))
        if focalor.fetchone():
            query1 = "UPDATE leaderboard SET Wins = %s, Loses = %s, WintoLoseRatio = %s WHERE Username = %s"
            focalor.execute(query1, (win1, lose1, ratio1, player1))
        else:
            query1 = "INSERT INTO leaderboard (Username, Wins, Loses, WintoLoseRatio) VALUES (%s, %s, %s, %s)"
            focalor.execute(query1, (player1, win1, lose1, ratio1))

        # Check if player2 exists
        focalor.execute("SELECT * FROM leaderboard WHERE Username = %s", (player2,))
        if focalor.fetchone():
            query2 = "UPDATE leaderboard SET Wins = %s, Loses = %s, WintoLoseRatio = %s WHERE Username = %s"
            focalor.execute(query2, (win2, lose2, ratio2, player2))
        else:
            query2 = "INSERT INTO leaderboard (Username, Wins, Loses, WintoLoseRatio) VALUES (%s, %s, %s, %s)"
            focalor.execute(query2, (player2, win2, lose2, ratio2))

        # Commit the changes
        game_info.commit()

        print("Data inserted/updated successfully!")

    # Display the leaderboard
    focalor.execute("SELECT * FROM leaderboard ORDER BY Wins DESC, Loses ASC")
    leaderboard = focalor.fetchall()

    print("\n--- Leaderboard ---")
    print(f"{'Username':<15} {'Wins':<5} {'Loses':<5} {'Win-to-Lose Ratio':<15}")
    print("-" * 45)
    for row in leaderboard:
        print(f"{row[0]:<15} {row[1]:<5} {row[2]:<5} {row[3]:<15}")

    # Close the cursor and connection
    focalor.close()
    game_info.close()



    #defines the lines and such
    ROW = 6
    COLUMN = 7
    board = []

    for i in range(ROW):
        row = []
        for j in range(COLUMN):
            row.append(' ')
        board.append(row)

    # prints the board
    def boardMaker():
        print("╔═╦═╦═╦═╦═╦═╦═╗")
        for i in board:
            print("╠" + "╬".join(i) + "╣")

        print("╚═╩═╩═╩═╩═╩═╩═╝")

    #valid move: if the slot is open or no
    def isValidMove(column):
        return board[0][column] == ' '

    # define function to drop disc
    def slotDrop(column, disc):
        for row in range((ROW - 1), -1, -1):
            if board[row][column] == ' ':
                board[row][column] = disc
                break

    def winCondition(disc):
        # testfor wincondition

        for row in range(ROW):
            for column in range(COLUMN):
                if board[row][column] == disc:
                    # Check horizontal
                    if column + 3 < COLUMN and all(board[row][column + i] == disc for i in range(4)):
                        return True
                    # Check vertical
                    if row + 3 < ROW and all(board[row + i][column] == disc for i in range(4)):
                        return True
                    # Check diagonal (down-right)
                    if row + 3 < ROW and column + 3 < COLUMN and all(board[row + i][column + i] == disc for i in range(4)):
                        return True
                    # Check diagonal (down-left)
                    if row + 3 < ROW and column - 3 >= 0 and all(board[row + i][column - i] == disc for i in range(4)):
                        return True
        return False
    #true game "the meat"

    def trueGame():

        turn = 0
        while True:

            boardMaker()
            if turn % 2 == 0:
                playerInPlay = player1
                disc = "○"

            else:
                playerInPlay = player2
                disc = "●"

            print(playerInPlay,"'s turn")

            #player input here

            while True:
                try:
                    column = int(input("Choose a column(1-7): "))
                    trueColumn = column - 1
                    if 0 <= trueColumn < COLUMN and isValidMove(trueColumn):
                        break

                    else:
                        print("Invalid column or column is full, try again!")

                except ValueError:
                    print("Invalid input, enter a number!")

            slotDrop((trueColumn), disc)

            if winCondition(disc):
                boardMaker()
                print(playerInPlay, "won the game!!!")
                break
            
            if all(board[0][column] != ' ' for column in range(COLUMN)):
                boardMaker()
                print("Its a draw!!")
                break

            turn = turn+1

    trueGame()
