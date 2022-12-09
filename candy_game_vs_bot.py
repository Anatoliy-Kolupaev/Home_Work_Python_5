from candy_game_function import *

game_conditions()

user1 = input("Введите ваше имя: ")
user2 = 'БОТ'

num1, num2 = choice_first(user1, user2)

winner(game(num1, num2), num1, num2)
