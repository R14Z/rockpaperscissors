print("Welcome, you are going to play rock paper scissors, there will be three rounds.") 

# constant 
rock = "rock"
paper = "paper"
scissors = "scissors"
points_r1 = 0
points_r2 = 0

# first inputs 
r1_player_1 = input("Rock, paper or scissors? ").lower() 
r1_player_2 = input("Rock, paper or scissors? ").lower()

# decisions (first round) 


# combinations w rock (1st round)
if r1_player_2 == "rock" and r1_player_1 == "scissors":
    points_r2 += 1 
    print("Player 2 gained one point")
elif r1_player_1 == "rock" and r1_player_2 == "scissors":
    points_r1 += 1 
    print("Player 1 has gained a point")

if r1_player_1 == "rock" and r1_player_2 == "paper":
    points_r2 += 1
    print("Player 2 has gained one point")
elif r1_player_1 == "paper" and r1_player_2 == "rock": 
    points_r1 += 1 
    print("Player 1 has gained a point")

# combinations with paper and scissors (1st round)
if r1_player_1 == "paper" and r1_player_2 == "scissors":
    points_r1 += 1
    print("Player 2 has gained a point")
elif r1_player_2 == "paper" and r1_player_1 == "scissors":
    points_r2 += 1
    print("Player 1 has gained a point")

# Second round 
print("SECOND ROUND!")
r2_player_1 = input("Player 1 enter rock paper or scissors ")
r2_player_2 = input("Player 2 enter rock paper or scissors ")

# combinations w rock (2nd round)
if r2_player_2 == "rock" and r2_player_1 == "scissors":
    points_r2 += 1 
    print("Player 2 gained one point")
elif r2_player_1 == "rock" and r2_player_2 == "scissors":
    points_r1 += 1 
    print("Player 1 has gained a point")

if r2_player_1 == "rock" and r2_player_2 == "paper":
    points_r2 +=  1
    print("Player 2 has gained one point")
elif r2_player_1 == "paper" and r2_player_2 == "rock": 
    points_r1 += 1 
    print("Player 1 has gained a point")

# combinations with paper and scissors (2nd round)
if r2_player_1 == "paper" and r2_player_2 == "scissors":
    points_r1 += 1
    print("Player 2 has gained a point")
elif r2_player_2 == "paper" and r2_player_1 == "scissors":
    points_r2 += 1
    print("Player 1 has gained a point")
    
# THIRD ROUND
print("THIRD ROUND! LAST ROUND.")
r3_player_1 = input("Player 1 enter rock paper or scissors ")
r3_player_2 = input("Player 2 enter rock paper or scissors ")

# combinations w rock (2nd round)
if r3_player_2 == "rock" and r3_player_1 == "scissors":
    points_r2 += 1 
    print("Player 2 gained one point")
elif r3_player_1 == "rock" and r3_player_2 == "scissors":
    points_r1 += 1 
    print("Player 1 has gained a point")

if r3_player_1 == "rock" and r3_player_2 == "paper":
    points_r2 += 1
    print("Player 2 has gained one point")
elif r3_player_1 == "paper" and r3_player_2 == "rock": 
    points_r1 += 1 
    print("Player 1 has gained a point")

# combinations with paper and scissors (3rd round)
if r3_player_1 == "paper" and r3_player_2 == "scissors":
    points_r1 += 1
    print("Player 2 has gained a point")
elif r3_player_2 == "paper" and r3_player_1 == "scissors":
    points_r2 += 1
    print("Player 1 has gained a point")

# draws 
if r1_player_1 == "rock" and r1_player_2 == "rock": 
    print("Draw!") 
elif r1_player_1 == "paper" and r1_player_2 == "paper":
    print("Draw!") 
elif r1_player_1 == "scissors" and r1_player_2 == "scissors":
    print("Draw!")

if r2_player_1 == "rock" and r2_player_2 == "rock": 
    print("Draw!") 
elif r2_player_1 == "paper" and r2_player_2 == "paper":
    print("Draw!") 
elif r2_player_1 == "scissors" and r2_player_2 == "scissors":
    print("Draw!")
    
if r3_player_1 == "rock" and r3_player_2 == "rock": 
    print("Draw!") 
elif r3_player_1 == "paper" and r3_player_2 == "paper":
    print("Draw!") 
elif r3_player_1 == "scissors" and r3_player_2 == "scissors":
    print("Draw!")

# scores 
print(f'Scores: \n Player 1: {points_r1} \n Player 2: {points_r2}')
if points_r1 > points_r2:
    print("Player 1 won!")
elif points_r1 == points_r2:
    print("DRAW!")
else:
    print("Player 2 won!")