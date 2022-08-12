print('Welcome to my Salary Calculator')
print()
print('Lets get started!')
print()
print('Please type one of the letters in the parenthesis')
time = input('Are you (F)ull Time or (P)art Time? ')

if time.upper() == 'F':
    time = 40
    hourRate = float(input('How much do you get paid an hour? $'))
    weeklyRate = time * hourRate
    print('Your weekly check is $' + str(weeklyRate))
    biweeklyRate = weeklyRate * 2
    print('Your bi-weekly check is $' + str(biweeklyRate))
    yearlySalary = weeklyRate * 48
    print('Your yearly salary is $' + str(yearlySalary))
elif time.upper() == 'P':
    time = 20
    hourRate = float(input('How much do you get paid an hour? $'))
    weeklyRate = time * hourRate 
    print('Your weekly check is $' + str(weeklyRate))
    biweeklyRate = weeklyRate * 2
    print('Your bi-weekly check is $' + str(biweeklyRate))
    yearlySalary = weeklyRate * 48
    print('Your yearly salary is $' + str(yearlySalary))
else :
    print('Wrong input please restart the program')