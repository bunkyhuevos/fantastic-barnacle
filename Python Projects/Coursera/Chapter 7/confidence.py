fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('Invalid file name: ', fname)
    quit()
count = 0.0
total = 0.0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        atpos = line.find(':')
        subtotal = line[atpos+1:]
        subtotal = float(subtotal)
        total = total + subtotal
        count = count + 1

print('Average spam confidence:', total/count)
