pet_age = 5
pet_type = "Cat"

if (pet_type == "Cat" ):
    if(pet_age > 5):
        print("Senior cat")
    else:
        print("Puppy food")
elif(pet_type == "Dog"):
    if pet_age < 2:
        print("Puppy food")
    else:
        print("Adult dog food")
else:
    print("Invalid pet type")