# Assesment Week 4

def confirm_length(word):

    # Complete the condition statement using a string operation. 
    if len(word) > 0: 
        # Complete the return statement using a string operation.
        return len(word) 
    else:
        return 0


print(confirm_length("a")) # Should print 1
print(confirm_length("This is a long string")) # Should print 21
print(confirm_length("Monday")) # Should print 6
print(confirm_length("")) # Should print 0



def highlight_word(sentence, word):
    # Complete the return statement using a string method.
    return sentence.replace(word, word.upper())


print(highlight_word("Have a nice day", "nice"))
# Should print: "Have a NICE day"
print(highlight_word("Shhh, don't be so loud!", "loud"))
# Should print: "Shhh, don't be so LOUD!"
print(highlight_word("Automating with Python is fun", "fun"))
# Should print: "Automating with Python is FUN"



def sort_distance(distances):
    distances.sort() # Sort the list
    distances.reverse() # Reverse the order of the list
    return distances


print(sort_distance([2,4,0,15,8,9]))
# Should print [15, 9, 8, 4, 2, 0]



def even_numbers(first, last):
  return [x for x in range(first,last,2)]


print(even_numbers(4, 14)) # Should print [4, 6, 8, 10, 12]
print(even_numbers(0, 9))  # Should print [0, 2, 4, 6, 8]
print(even_numbers(2, 7))  # Should print [2, 4, 6]



def countries(countries_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.
    for key,country in countries_dict.items():
        # Use a string method to format the required string.
        result += "{},".format(country) 
    return result

print(countries({"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia":["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))

# Should print:
# ['Kenya', 'Egypt', 'Nigeria']
# ['China', 'India', 'Thailand']
# ['Ecuador', 'Bolivia', 'Brazil']



def setup_guests(guest_list):
    # loop over the guest list and add each guest to the dictionary with
    # an initial value of 0
    result = {} # Initialize a new dictionary 
    for name in guest_list: # Iterate over the elements in the list 
        result["{}".format(name)] = 0 # Add each list element to the dictionary as a key with 
            # the starting value of 0
    return result

guests = ["Adam","Camila","David","Jamal","Charley","Titus","Raj","Noemi","Sakira","Chidi"]

print(setup_guests(guests))
# Should print {'Adam': 0, 'Camila': 0, 'David': 0, 'Jamal': 0, 'Charley': 0, 'Titus': 0, 'Raj': 0, 'Noemi': 0, 'Sakira': 0, 'Chidi': 0}



def count_numbers(text):
  # Initialize a new dictionary.
  dictionary = {} 
  # Complete the for loop to iterate through each "text" character.
  for char in text:
    # Complete the if-statement using a string method to check if the
    # character is a number.
    if char.isdigit():
      # Complete the if-statement using a logical operator to check if 
      # the number is not already in the dictionary.
      if char not in dictionary:
        # Use a dictionary operation to add the number as a key
        # and set the initial count value to zero.
        dictionary[char] = 0
      # Use a dictionary operation to increment the number count value 
      # for the existing key.
      dictionary[char] += 1
  return dictionary

print(count_numbers("1001000111101"))
# Should be {'1': 7, '0': 6}

print(count_numbers("Math is fun! 2+2=4"))
# Should be {'2': 2, '4': 1}

print(count_numbers("This is a sentence."))
# Should be {}

print(count_numbers("55 North Center Drive"))
# Should be {'5': 2}