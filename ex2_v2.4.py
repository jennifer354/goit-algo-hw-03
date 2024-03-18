import random
min = int(input('Enter min: '))
if min <1 :
        print ("Error")
max = int(input('Enter max: '))
if max >1000:
            print ("Error2")
quantity = int(input('Enter quantity: '))
random_numbers = [random.randint(min,max) for _ in range (quantity)]
print(random_numbers)

    
        
    








    