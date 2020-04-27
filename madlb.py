#!/usr/bin/python3
import random

# this first step creates variable names and assigns them tuples
noun = ("car", "bus", "ball", "plane", "cup",)
verb = ("jump", "sit", "run", "think", "smile",)
superhero = ("Batman", "Superman", "Wonder Woman", "Batgirl",)
animal = ("dog", "cat", "horse", "octopus", "bird", "rat",)
people = ("Justin", "Belinda", "Joseph", "Glenn", "Rob", "Tunde", "Jessica",)
places = ("Colorado Springs", "Denver", "Houston", "Seattle",)
season = ("spring", "summer", "fall", "winter",)

# this second step defines the way the program will implement a random picking of an element  # within the tuples by counting the elements then picking a random value within to assign the
# value
def elem(tuple):
    value = random.randint(0,len(tuple)-1)
    return tuple[value]

# this third step uses an if statement to recognise whether name = main( is it using the      # primary script or is it being called by an import statement)
# so if program is using primary script then print...
if __name__ == '__main__':
    print("Every " + elem(season) + ", " + elem(superhero) + \
    " is joined by the " + elem(animal) + \
    ", who's secret identity is " + elem(people) + \
    ".  They attempt to " + elem(verb) + \
    ", which rarely succeeds. So instead they chase down a " + \
    "villain in " + elem(places) + " who was trying to steal a " + \
    elem(noun) + ".")

