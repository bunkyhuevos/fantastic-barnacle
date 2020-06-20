def computegrade():
    score = input("Enter Score: ")
    try:
        score = float(score)
    except:
        print ("Please enter a number.")
        quit()
    if score > 1:
        grade = "Please enter value between 0.0 and 1.0"
    elif score >= 0.9:
        grade = "A"
    elif score >= 0.8:
        grade = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.6:
        grade = "D"
    elif score <= 0.5:
        grade = "F"
    return grade
print("Grade:", computegrade())
