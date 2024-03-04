import random
import os
import time

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to draw the game board
def draw_board(snake, food, width, height):
    clear_screen()
    for y in range(height):
        for x in range(width):
            if (x, y) in snake:
                print('██', end='')
            elif (x, y) == food:
                print('🍎', end='')
            else:
                print('  ', end='')
        print()

# Function to generate new food
def generate_food(snake, width, height):
    food = None
    while food is None:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if (x, y) not in snake:
            food = (x, y)
    return food

# Main function to run the game
def main():
    width = 20
    height = 10
    snake = [(0, 0)]
    direction = 'right'
    food = generate_food(snake, width, height)

    while True:
        draw_board(snake, food, width, height)
        print(f'Score: {len(snake)}')

        # Get user input
        direction = input('Enter direction (w/a/s/d): ').lower()
        if direction not in ['w', 'a', 's', 'd']:
            print('Invalid direction!')
            continue

        # Move snake
        head = snake[0]
        if direction == 'w':
            new_head = (head[0], head[1] - 1)
        elif direction == 'a':
            new_head = (head[0] - 1, head[1])
        elif direction == 's':
            new_head = (head[0], head[1] + 1)
        elif direction == 'd':
            new_head = (head[0] + 1, head[1])

        # Check if snake hits walls or itself
        if (new_head[0] < 0 or new_head[0] >= width or
                new_head[1] < 0 or new_head[1] >= height or
                new_head in snake):
            print('Game Over!')
            break

        snake.insert(0, new_head)

        # Check if snake eats food
        if new_head == food:
            food = generate_food(snake, width, height)
        else:
            snake.pop()

        # Slow down the game
        time.sleep(0.1)

if __name__ == '__main__':
    main()
