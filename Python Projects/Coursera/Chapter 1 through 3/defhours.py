def computepay():
    hours = input("Enter hours worked:")
    rate = input("Enter hourly wage:")
    hours = float(hours)
    rate = float(rate)
    if hours > 40:
        rate = float(rate)
        hours = float(hours)
        overtime = (hours - 40.0) * (rate * 1.5)
        pay = overtime + (40 * rate)
        return pay
    elif hours <= 40:
        pay = hours * rate
        return pay
print ("Pay", computepay())
