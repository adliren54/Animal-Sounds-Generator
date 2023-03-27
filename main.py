exit = ""
while exit != "yes":
  animal = input("What animal do you want?: ")
  if animal == "Cow":
    print("A cow goed moo")
  elif animal == "Lesser Spotted Lemur":
    print("Umm... the Lesser Spotted Lemur goes Awooga?")
  else:
    print("Sorry we don't have that animal yet. Please wait for our update!")
  exit = input("Do you want to exit?: ")