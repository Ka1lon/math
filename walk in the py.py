# dice_roll
import random
for x in range (1, 11):
    random_number = random.randint(1,6)
    print(random_number)

#double_dice_roll
import random
for x in range(1,11):
    throw_1 = random.randint(1,6)
    throw_2 = random.randint(1,6)
    total = throw_1 + throw_2
    print(total)
    if total == 7: print ('seven thrown')
    if total == 11:print ('eleven thrown')
    if throw_1 == throw_2: print ('double thrown')
    if total >=5 and total <=9: print ('not bad')
#can use 'or' here^^as well instead
#can use 'not statement to mean the same as above
    if not (total < 5 or total > 9:
            print ('not bad')

#else clause
a = 7
if a > 7:
    print('a is big')
else:
    print('a is small')

#while clause
import random
throw_1 = random.randint(1,6)
throw_2 = random.randint(1,6)
while not (throw_1 == 6 and throw_2 == 6):
    total = throw_1 + throw_2
    print(total)
    throw_1 = random.randint(1,6)
    throw_2 = random.randint(1,6)
print('double six thrown')


