print('Welcome to my Farm Calculator')
print('Lets get started!')
area = int(input('How many plots of land you have? '))
crops = int(input('How many crops can you plant in each plot? '))
cropType = int(input('How many different crops are you planning to plant? '))

cropAmount = area * crops
seeds = cropAmount / cropType

print('You should buy ' + str(seeds) + ' seeds for each crop.')