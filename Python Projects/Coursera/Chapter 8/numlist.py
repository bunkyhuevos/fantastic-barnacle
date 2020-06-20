numlist = list()
while (True):
    inp = input("Enter a number. Type 'done' when finished. >> ")
    if inp == 'done' : break
    try:
        value = float(inp)
    except:
        print('Invalid input')
        continue
    numlist.append(value)
    print(numlist)

average = sum(numlist) / len(numlist)
print('Entries:', len(numlist))
print('Sum:', sum(numlist))
print('Average:', average)
