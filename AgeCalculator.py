print('')
print('Welcome to my Age Calculator!')
print('')
born = int(input('What year where you born? '))
print()
print('Did your Birthday pass since this year started? ')
bday = input('(Y)es or (N)o? ')
print()

today = int(input('What year is it? '))

if bday == 'N' :
    today = today - 1

age = today - born
print()
print('You are ' + str(age) + (' years old!'))
print()

if age < 20 : 
    print('Wow you are a little kid.')
    print('Did you ask your mommy if you can use this program?')
    print()
elif age == 21 :
    print('Do not get ahead of yourself')
    print()
elif age > 50 : 
    print('You should start making Funeral Arrangements')
    print('You are running out of time')
    print()
else :
    print('Invite me to your next birthday party!')
    print()