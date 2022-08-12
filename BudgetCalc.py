print('Welcome to The Budget Calculator')
print('Lets get started!')
print('Please type one of the letters in the parenthesis')

percent = input('Do you get paid (W)eekly or (B)i-weekly? ')

if percent.upper() == 'W':
    percent = .1
    check = int(input('How much do you get paid a week? $'))
    saveAmount = check * percent
    print('You should save $' + str(saveAmount) + ' every week.')
elif percent.upper() == 'B':
    percent = .2
    check = int(input('How much do you get paid every two weeks? $'))
    saveAmount = check * percent
    print('You should save $' + str(saveAmount) + ' every two weeks.')
else :
    print('Wrong input please restart the program')