marks=float(input("please enter your marks: "))

if marks>=90 and marks<=100:
    print(f"you have passed with excellent marks \n your marks {marks}")
elif marks<90 and marks>=80:
    print(f"you have passed with good marks \n your marks {marks}")
elif marks<80 and marks>=70:
    print(f"ypu have passed with average marks \n your marks {marks}")
elif marks<70 and marks>=60:
    print(f"you have passed with satisfactory marks \n your marks {marks}")
elif marks<60 and marks>=50:
    print("you have passed")
else:
    print("you have unfortunately failed")

