import random
min = int(input('Enter min: '))
max = int(input('Enter max: '))
quantity = int(input('Enter quantity: '))
random_numbers = [random.randint(min,max) for _ in range (quantity)]
print(random_numbers)
def get_numbers_ticket (min,max):
    if min <1 or max > 1000:
        print ("Error")
    else:
        print (f'Ваші лотерейні числа: {get_numbers_ticket}')
