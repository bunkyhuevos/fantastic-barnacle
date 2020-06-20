hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
    hours = float(hours)
    rate = float(rate)
except:
    print("Please enter number.")
    quit()
if hours > 40:
    rate = float(rate)
    hours = float(hours)
    overtime = (hours - 40.0) * (rate * 1.5)
    pay = overtime + (40 * rate)
    print ('Pay:', pay)
elif hours <= 40:
    pay = hours * rate
    print ('Pay:', pay)
