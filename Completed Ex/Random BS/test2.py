def age_permitted(ages):
    if age < 18:
        print("Underage")
    elif age > 98:
        print("OVERAGE!")
    else:
        print("Age accepted")

age = int(input("Insert your age: "))
print(age_permitted(age))
