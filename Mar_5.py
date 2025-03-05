##Today i learned about how it asked me what i like and how to code at etc..
from re import T


myName = input("What's your name?:")
if myName == "Dharshwath":
  print("Welcome Dude!")
  print("You're just the baldest dude I've ever seen")
else:
  print("who on earth are you?!")
  
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs == "cat":
    print("Meow")
else:
    print("Woof")
drink = input("Do you prefer coffee or tea?")
if drink == "coffee":
    print("Tea is better.")
else:
  print("Excellent choice.")
  print("Which character are you from 'Avengers?'")
  print()
  print("Answer these questions and let's find out.")
  print()
  print("Please use Y or N for yes or no.")
  likeGreen = input("Do you like the color green?:")
  if likeGreen == "Y":
    print("You must be the Hulk!")
    IronIsCool = input("Do you think building robots is cool?: ")
    if IronIsCool == "Y":
      print("You must be Iron Man. Cool suit!")
      TimeTravel = input("Do you like travelling through time?:")
      if TimeTravel =="Y":
        print("You must be Captain America!")
      Strong = input("Are you super strong?:")
      if Strong == "Y":
        print("You have got to be Thor!")
      else:
        print("I guess you are not like anyone from 'Avengers.'")
