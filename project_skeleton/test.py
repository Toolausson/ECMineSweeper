import random

# Define dimensions
r = 5  # Number of rows
c = 8  # Number of columns
game_arr = []

# Initialize the game_arr with empty lists
for _ in range(r):
    game_arr.append([0] * c)

# Set the bobchance
bomb_chance = 0.25


for i in range(0,r):
    for j in range(0,c):
        if (random.random() <= bomb_chance):
            is_bomb = -1 #BOMB
        else:
            is_bomb = 0 #NO BOMB
        print(str(i)+","+str(j))
        game_arr[i][j] = is_bomb

#game_arr = [[random.randrange(100,199) for _ in range(c)] for _ in range(r)]

# Print the array
for row in game_arr:
    print(row)

print("---s-")


def count_neighbour_bombs(rr,cr):
    for ri in range(-1,2):
        for ci in range(-1,2):
            rpos = rr + ri
            cpos = cr + ci
            #kollar att grannarna inte ligger utanför spelplanen + (att man inte räknar in sig själv (i onödan eftersom man inte ska komma in i loopen om det är en mina))
            if ((rpos > -1 and rpos < r) and (cpos > -1 and cpos < c) and (rpos != rr or cpos != cr)):
                print("-- "+ str(rpos) +","+ str(cpos) +" -- "+str(game_arr[rpos][cpos]))
                #print(rr)
                if (game_arr[rpos][cpos] == -1):
                    game_arr[rr][cr] += 1
                    #print("B"+str(game_arr[rr][cr])+"A" )
                    print(game_arr[rr][cr])


def create_game_arr():
    for ril in range(0,r):
        for cil in range(0,c):
            #print("-ril-- "+str(ril))
            #print("-cil-- "+str(cil))
            if (game_arr[ril][cil] != -1): #checks if contains bopmb (value -1)
                #print("val:"+ str(game_arr[ril][cil]))
                count_neighbour_bombs(ril,cil)
 



create_game_arr()

for row in game_arr:
    print(row)

print("________")
