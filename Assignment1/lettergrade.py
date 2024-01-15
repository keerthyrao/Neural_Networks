score = int(input("enter score"))
percentage= round(float((score/1800)*100),2)
#print(percentage)

if percentage>=90.00 and percentage<=100:
    print("The pupil will get Grade A")
elif percentage>=80.00 and percentage<=89.99:
    print("The pupil will get Grade B")
elif percentage>=70.00 and percentage<=79.99:
    print("The pupil will get Grade C")
elif percentage>=60.00 and percentage<=69.99:
    print("The pupil will get Grade D")
elif percentage<60.00:
    print("The pupil will get Grade F")