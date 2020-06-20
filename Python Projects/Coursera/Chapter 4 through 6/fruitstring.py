fruit = input('Type a fruit: ')
fruit = fruit.lower()
count = fruit.count('a')
index = len(fruit)

if 'n' in fruit:
    print("There's an 'n' in " + fruit + "!")

if fruit < 'banana':
    print("Your fruit, " + fruit + ", comes before banana.")

if fruit > 'banana':
    print("Your fruit, " + fruit + ", comes after banana.")

print('There are', index, 'characters in', fruit)
print('The first character is ' + fruit[0] + '.')
print('The last character is ' + fruit[-1] + '.')
print("The letter 'a' appeared", count, "times.")
