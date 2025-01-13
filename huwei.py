
import mysql.connector

while True:
    
    game_info = mysql.connector.connect(host='localhost', user='root', password='fahim123', database='connect_four')

    focalor = game_info.cursor()

    def player_info():

        win1 = 0
        win2 = 0
        lose1 = 0
        lose2 = 0
        ratio1 = 0
        ratio2 = 0

        option = input("Do you have an existing account (y/n): ")

        user1 = input("Enter the name of player 1: ")
        user2 = input("Enter the name of player 2: ")

        win_or_lose = input("Did user1 Win or Lose (W/L)?: ")
        
        if win_or_lose == 'W':
            win1 += 1
            lose2 += 1

        elif win_or_lose == 'L':
            lose1 += 1
            win2 += 1

        else:
            print("Invalid Input")
            

        ratio1 = str(win1)+":"+str(lose1)
        ratio2 = str(win2)+":"+str(lose2)

        return win1,win2,lose1,lose2,ratio1,ratio2,user1,user2
    
    win1,win2,lose1,lose2,ratio1,ratio2,user1,user2 = player_info()

    query1 = "INSERT INTO leaderboard (username, wins, losses, ratio) VALUES (%s, %s, %s, %s)"
    query2 = "INSERT INTO leaderboard (username, wins, losses, ratio) VALUES (%s, %s, %s, %s)"

     
    focalor.execute(query1, (user1, win1, lose1, ratio1))
    focalor.execute(query2, (user2, win2, lose2, ratio2))

    game_info.commit()

    print("Data inserted successfully!")
