# Quiz 2 Week 4

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]  

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]



def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    say += word[1:] + word[0] + "ay "  
    # Turn the list back into a phrase
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"



def group_list(group, users):
  return group + ": " + ", ".join(users)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"



def guest_list(guests):
	for guest in guests:
		name = guest[0]
		age = guest[1]
		job = guest[2]
		print("{} is {} years old and works as {}" .format(name, age, job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""