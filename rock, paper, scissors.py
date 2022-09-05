import random
while True:
    game = input('Choose a game\n' + 'Rock Paper Scissors / Odd or Even\n' + '(RPS, OrE)\n')

    if game == 'RPS':
        print('Ok lets start')
        player_choice = input('Choose one \n' + 'Rock, Paper or Scissors\n')
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        print('You choose: ' + player_choice)
        print('Computer choose: ' + computer_choice)
        if player_choice == computer_choice:
            print('It is a draw!')
        elif player_choice == 'Rock' and computer_choice == 'Scissors':
            print('You won!')
        elif player_choice == 'Paper' and computer_choice == 'Rock':
            print('You won!')
        elif player_choice == 'Scissors' and computer_choice == 'Paper':
            print('You won!')
        else:
            print('You lost :(')

    # Odd or even
    elif game == 'OrE':
        what_win = input('Choose Odd or Even\n')
        if what_win == 'Odd':
            player_number = input('Choose your number\n')
            computer_number = random.choice([1, 2])
            print('This was your number: ' + player_number)
            print('This was the computer number: ' + str(computer_number))
            if int(player_number) + computer_number % 2 == 0:
                print('Sorry you lost')
            else:
                print('Congrats you won!')
        elif what_win == 'Even':
            player_number = input('Choose your number\n')
            computer_number = random.choice([1, 2])
            print('This was your number: ' + player_number)
            print('This was the computer number: ' + str(computer_number))
            if int(player_number) + computer_number % 2 == 1:
                print('Sorry you lost')
            else:
                print('Congrats you won!')

    # Do you wish to play again?
    stop = input('Do you wish to play again (y, n)?\n')
    if stop == 'y':
        pass
    elif stop == 'n':
        break