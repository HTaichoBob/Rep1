
grade = float(input("Enter your grade: "))

if grade >= 90 and grade <= 100:
      print("You're a Superstar! You received an A.")
elif grade >= 90:
    print("You received an A.")
elif grade >= 80:
        print("You received a B.")
elif grade >= 70:
        print("You received a C.")
elif grade >= 60:
        print("You received a D.")
else:
    print("You received an F. Please retake the course.")

