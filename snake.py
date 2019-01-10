'''
Author : Tanmay Sawaji
Github : https://github.com/tanmaysawaji
'''

import pygame
import random

def play_snake():
	# Creating the game window
	pygame.init()
	win_width = 100
	win_height = 100
	win = pygame.display.set_mode((win_width, win_height))
	pygame.display.set_caption("Snake")
	clock = pygame.time.Clock()

	# Initializations
	x = 50
	y = 50
	width = 1
	height = 1
	direction = "right"
	food = (70, 80)
	snake = [(x-2, y), (x-1, y), (x, y)]


	# The actual snake game
	run = True
	while run:
		# Adjust speed of the game
		pygame.time.delay(100)

		# Close button to quit the game
		for event in pygame.event.get():
			if event.type == 12:
				run = False

		# Record the keystroke and decide direction
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and direction != "right":
			direction = "left"
		if keys[pygame.K_RIGHT] and direction != "left":
			direction = "right"
		if keys[pygame.K_UP] and direction != "down":
			direction = "up"
		if keys[pygame.K_DOWN] and direction != "up":
			direction = "down"

		# Update x and y in the direction of motion
		if direction == "right":
			x += 1
		if direction == "left":
			x -= 1
		if direction == "up":
			y -= 1
		if direction == "down":
			y += 1

		# Termination conditions
		if x < 0 or x >= win_width or y < 0 or y >= win_height or (x,y) in snake:
			run = False

		# Increase length of snake if the snake eats food and respawn food
		snake.append((x,y))
		if snake[-1] == food:
			food_flag = True
			while food_flag:
				foodx = random.randint(0,99)
				foody = random.randint(0,99)
				if (foodx, foody) not in snake:
					food = (foodx, foody)
					food_flag = False
		else:
			snake.pop(0)


		# Drawing everything on the canvas
		win.fill((0,0,0))
		pygame.draw.rect(win, (0, 255, 0), (food[0], food[1], 1 , 1))
		for pos in snake:
			pygame.draw.rect(win, (255, 255, 255), (pos[0], pos[1], 1, 1))
		print(len(snake))
		pygame.display.update()
	pygame.quit()

if __name__ == "__main__":
	play_snake()