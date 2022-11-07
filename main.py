import pygame
import logging
import time

from constants import WIDTH, HEIGHT, FPS, DEBUG_LOGGING
from graphics.scenes.puzzle import puzzle_scene
from puzzles import puzzles
from watersort import game,bfs_solve,dfs_solve,printState

def main(width, height,starting_scene, moves):
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((width, height))
    start_status = True
    active_scene = starting_scene
    counter=0
    while active_scene is not None:
        pressed_keys = pygame.key.get_pressed()

        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                logging.info("attempting to quit game")
                active_scene.Terminate()
            else:
                filtered_events.append(event)

        # active_scene.ProcessInput()
        # logging.info(active_scene_class_name + ": ProcessInput()")
        # active_scene.ProcessInput(filtered_events, pressed_keys)
    
        # active_scene.ProcessInput(filtered_events,pressed_keys)

        
        # time.sleep(5)
        

        # active_scene.Update()

        active_scene.Render(screen, filtered_events)

        if start_status == True:
            time.sleep(2)
            start_status = False
        else:
            if (counter >= len(moves)):
                continue
            else:
                # print(counter)
                move = moves[counter]
                # print(move)

                active_scene.Update(move)
            
            counter+=1

        active_scene = active_scene.next

filename="input.txt"
print("Nhap level ban muon giai: ")
level = int(input())
g = game(filename,level)
last_state, moves, all_nodes, visited_nodes, repeated_nodes, time_run = dfs_solve(g.space)
# a.space,moves,repeated_nodes, times = bfs_solve(a.space)
if len(moves) > 0:
    print("Total moves: " + str(len(moves)))
    print("Number of states have been reached: " + str(all_nodes))
    print("Number of states have been visited: " + str(visited_nodes))
    print("Solved time: " +str(time_run))
    print("Repeated nodes: " + str(repeated_nodes))

    next_puzzle = puzzles.get_puzzle(level-1)
    main(WIDTH, HEIGHT, puzzle_scene.PuzzleScene(next_puzzle),moves)
else:
    print("Can not solve!!!")