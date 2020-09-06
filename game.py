# Write your code here
import random


def read_rating_file(name):
    rating_file = open("rating.txt", "r")

    for line in rating_file:
        if line.split()[0] == name:
            return int(line.split()[1])

    rating_file.close()
    return 0


def parameters_game(list_opt):
    if list_opt == '':
        options.extend(['scissors', 'rock', 'paper'])
    else:
        list_opt = list_opt.split(',')
        for i in list_opt:
            if i not in all_options:
                print("This option does not exist - {}".format(i))
            else:
                options.append(i)


user_losses = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}

all_options = ['scissors', 'rock', 'paper', 'snake', 'water', 'dragon', 'devil', 'gun',
               'fire', 'human', 'tree', 'wolf', 'sponge', 'air', 'lightning']
options = []
exit_input = "!exit"
rating_request = "!rating"

user_name = input("Enter your name: ")
print(f'Hello, {user_name} ')

list_options = input()
parameters_game(list_options)  # Removes unnecessary options
print("Okay, let's start")

rating_score = read_rating_file(user_name)

while True:

    user_guess = input('Player choice: ')

    if user_guess == exit_input:
        print("Bye!")
        break
    elif user_guess == rating_request:
        print(f'Your rating: {rating_score}')
    elif user_guess not in options:
        print("Invalid input")
        continue
    else:
        random_option = random.choice(options)
        #  print(random_option)

        if random_option == user_guess:
            print(f'There is a draw ({random_option})')
            rating_score += 50
        elif random_option in user_losses[user_guess]:
            print(f'Well done. The computer chose {random_option} and failed')
            rating_score += 100
        else:
            print(f'Sorry, but the computer chose {random_option}')
