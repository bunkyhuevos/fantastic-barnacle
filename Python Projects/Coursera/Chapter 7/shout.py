fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('Invalid file name: ', fname)
    exit()
text = fhand.read()
text = text.rstrip()
text = text.upper()
print(text)
