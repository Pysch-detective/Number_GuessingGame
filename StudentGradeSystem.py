# Project 2: Student Grade System
print("Welcome to the Grade System")
subjects = ["Tel", "Hin", "Eng", "Maths", "Social"]
total = 0

while True:
    marks = input("Enter to continue to children marks or Stop to exit: ").lower()
    if marks == "stop":
        print("Thank u for using this")
        break
    elif marks == "enter":
        for sub in subjects:
            submarks = int(input(f"please enter the makrs of {sub}: "))
            total = total + submarks
        print(total)
        Average = (total / 300) * 100
        print(Average)
        if Average > 90:
            print("Grade A")
        elif Average > 80:
            print("Grade B")
        elif Average > 70:
            print("Grade C")
        elif Average > 60:
            print("Grade D")
        else:
            print("Fail")
