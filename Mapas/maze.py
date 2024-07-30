import os
import random
import readchar

# Variables and constants of map dimensions and user's location
POS_X = 0
POS_Y = 1
NUM_OF_MAP_OBJECTS = 11

obstacle_definition = """\
###########################
                       ####
##################     ####
##################     ####
###########                
###################   #####
##############           ##
#######            ########
#############              
####################    ###
####       ########       #
########                ###
######## #########         
#####    ###########   ####
###########################\
"""

my_possition = [0, 1]
tail_length = 0
tail = []
map_objects = []

end_game = False
died = False

# Create Obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

# Main Loop
while not end_game:
    os.system('cls')
    # generate random objects in the map
    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_possition = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

        if new_possition not in map_objects and new_possition != my_possition and \
                obstacle_definition[new_possition[POS_Y]][new_possition[POS_X]] != "#":
            map_objects.append(new_possition)

    # Draw map
    print('+' + '-' * MAP_WIDTH * 2 + '+')

    for coordinate_y in range(MAP_HEIGHT):
        print('|', end='')

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = "  "
            object_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = " o"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = " X"
                    tail_in_cell = tail_piece

            if my_possition[POS_X] == coordinate_x and my_possition[POS_Y] == coordinate_y:
                char_to_draw = " @"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1
                if tail_in_cell:
                    died = True
                    end_game = True

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"
            if my_possition[POS_X] == obstacle_definition and my_possition[POS_Y] == obstacle_definition:
                died = True
                end_game = True

            print(f'{char_to_draw}', end="")
        print('|')

    print('+' + '-' * MAP_WIDTH * 2 + '+')

    direction = input(readchar.readchar(''))

    if direction == 'w' or direction == 'W':
        new_possition = [my_possition[POS_X], (my_possition[POS_Y] - 1) % MAP_HEIGHT]

    elif direction == 's' or direction == 'S':
        new_possition = [my_possition[POS_X], (my_possition[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "a" or direction == 'A':
        new_possition = [(my_possition[POS_X]) % MAP_WIDTH - 1, my_possition[POS_Y]]

    elif direction == 'd' or direction == 'D':
        new_possition = [(my_possition[POS_X] + 1) % MAP_WIDTH, my_possition[POS_Y]]

    elif direction == 'q' or direction == 'Q':
        end_game = True

    if new_possition:
        if obstacle_definition[new_possition[POS_Y]][new_possition[POS_X]] != "#":
            tail.insert(0, my_possition.copy())
            tail = tail[:tail_length]
            my_possition = new_possition

if died:
    print('Has muerto')
    input("Enter para seguir...")
