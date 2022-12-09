from candy_game_function import *

game_conditions()

user1 = input("Введите имя 1го игрока: ")
user2 = input("Введите имя 2го игрока: ")

num1, num2 = choice_first(user1, user2)

winner(game(num1, num2), num1, num2)