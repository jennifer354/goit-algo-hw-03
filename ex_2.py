import random
def get_numbers_ticket (l):
l = list(range(1, 36))
print(l)
random.shuffle(l)
print(l)
print(random.choice(l))
print(random.sample(l, k=5))
print (get_numbers_ticket)

