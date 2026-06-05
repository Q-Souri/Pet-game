

import random
import time

# Base class: Pet
# Subclasses: Dog, Cat
# Attributes: name, hunger, happiness, energy. (Attributes are things an object HAS.)
# Methods: eat(), sleep(), play(), show_status(). (Methods are things an object DOES.)
# Different behaviour: Dog and Cat have different play() methods
# Interaction: user chooses pet, feeds it, plays, sleeps, checks status, quits

# This is our base class / parent class.
#A class is like a blueprint for creating something.
#In this case the blueprint is for a virtual pet.

class Pet:
 #This method runs automatically when we create a new pet.
    # It gives the pet a name and starting values.
    #"__init__ is used to initialize new objects with starting values. 
    # self, refers to the current object and allows each pet to store and manage its own data independently."
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.energy = 5

        #This method feeds the pet.
        # All pets can eat, so this method belongs in the base "pet class".
    def eat(self):
        print(f"\nFeeding {self.name}...")
        time.sleep(1)

        #Hunger goes down because the pet has eaten.
        #max(0, ...) stops hunger from going below 0.
        self.hunger = max(0, self.hunger - 2)

        #Energy goes up a little after eating.
        #min(10, ...) stops energy from going above 10. 
        self.energy = min(10, self.energy + 1)
        print(f"{self.name} enjoyed the meal!")

        # This method lets the pet sleep.
    def sleep(self):
        print(f"\n{self.name} is sleeping...")
        time.sleep(1)

        #Sleeping gives the pet more energy.
        self.energy = min(10, self.energy + 3)
        print(f"{self.name} woke up refreshed!")

        # This method shows the pet's current condition.
    def show_status(self):
        print("\n----------------------")
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}/10")
        print(f"Happiness: {self.happiness}/10")
        print(f"Energy: {self.energy}/10")
        print("------------------------")


# Dog is a subclass of pet.
# This means Dog inherits the common pet behaviours:
# eat(), sleep(), and show_status().
class Dog(Pet):

    #Dogs have their own version of play().
    def play(self):
        dog_games = ["played fetch", "chased a ball", "caught a frisbee", "ran around the garden"]
        print(f"\n{self.name} is playing...")
        time.sleep(1)

        #random.choice picks one game from the list.
        game = random.choice(dog_games)

        # playing makes the dog happier.
        self.happiness = min(10, self.happiness + 3)

        #playing uses energy.
        self.energy = max(0, self.energy -2)

        #paying makes the dof a little hungry.
        self.hunger = min(10, self.hunger + 1)

        print(f"{self.name} {game}!")

 # Cats have their own version of play().
class Cat(Pet):
    def play(self):
        cat_games = ["chased a laser pointer", "played with yarn", "pounced on a toy mouse", "climbed onto a shelf"]

        print(f"\n{self.name} is playing...")
        time.sleep(1)

     # random.choice picks one activity from the list.
        game = random.choice(cat_games)

      # playing makes the cat happier.
        self.happiness = min(10, self.happiness + 2)

      # Cats use slightly less energy than dogs in this game.
        self.energy = max(0, self.energy - 1)
                  
      # Playng makes the cat a little hungry.
        self.hunger = min(10, self.hunger + 1)

        print(f"{self.name} {game}!")

      # This is where the game starts.
print("Welcome to virtual Pet!")

      # The player chooses the type of pet.
pet_type = input("Choose your pet: dog or cat: ").lower()

      # The player gives the pet a name.
pet_name = input("Enter your pet name:  ")

      # This creates a Dog object if the player chooses dog.
if pet_type == "dog":
    pet = Dog(pet_name)

      # Otherwise, it creates a Cat object.
else:
    pet = Cat(pet_name)

print(f"\nGreat! You adopted {pet.name}!")

       # This loop keeps the game running until the player chooses to quit.
while True:
    print("\nwhat would you like to do?")
    print("1. Feed")
    print("2. Play")
    print("3. Sleep")
    print("4. Check Status")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pet.eat()

    elif choice == "2":
          pet.play()

    elif choice == "3":
          pet.sleep()

    elif choice == "4":
          pet.show_status()

    elif choice == "5":
          print(f"\nGoodbye! {pet.name} will miss you!")
          break
             
    else:
        print("Please enter a number between 1 and 5.")


       # Pet is the parent class. Dog and Cat are child classes.
       # They inherit common behaviours like eating and sleeping,
       # but they each have their own play method.
       # That means the same action, play, works differently depending on the pet type.
              
                  
            
