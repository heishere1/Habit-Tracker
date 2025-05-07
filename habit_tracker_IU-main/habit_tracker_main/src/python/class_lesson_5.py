# Define a class to represent a dog at the shelter
class Dog:
    # Constructor: runs automatically when a new dog is created
    def __init__(self, name, breed, color, sex):
        # Save the dog's name in the instance variable self.name
        self.name = name
       
        # Store the breed (e.g., Beagle, Bulldog)
        self.breed = breed
       
        # Store the dog's color (e.g., black, brown)
        self.color = color
       
        # Store the dog's sex (Male or Female)
        self.sex = sex
       
        # Default value: dog is not adopted yet
        self.adopted = False
       
        # Start with an empty vaccine list for each new dog
        self.vaccines = []


    # Method to add a vaccine to this dog's record
    def add_vaccine(self, vaccine_name):
        self.vaccines.append(vaccine_name)  # Add the name to the list


    # Method to mark this dog as adopted
    def adopt(self):
        self.adopted = True  # Change the adoption status to True


    # Method to print all stored information about the dog
    def print_info(self):
        print("----- DOG INFORMATION -----")
        print("Name:", self.name)
        print("Breed:", self.breed)
        print("Color:", self.color)
        print("Sex:", self.sex)
        print("Adopted:", "Yes" if self.adopted else "No")
       
        # Print vaccines if any are present
        if self.vaccines:
            # Join list of vaccines into a single string separated by commas
            print("Vaccines received:", ", ".join(self.vaccines))
        else:
            print("Vaccines received: None yet")
        print("---------------------------\n")


new_dog = Dog("Elegant", "bullpurity", "bright", "male")
new_dog.print_info()

new_dog.add_vaccine("Rabies")

new_dog.adopt()
# Print updated information for Bella's new owners
new_dog.print_info()
