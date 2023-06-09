#Assesment Week 2

IP_address = "192.168.1.10"
host_name = "Printer Server 1"
print(IP_address + " is the IP address of " + host_name)
# Should print "192.168.1.10 is the IP address of Printer Server 1"


number = 4
if number * 4 < 15:
 print(number / 4)
elif number < 5:
 print(number + 3)
else:
 print(number * 2 % 5)


def clothing_type(temp):
    if temp < 32:
        clothing = "T-Shirt"
    elif temp < 50:
        clothing = "Sweatshirt"
    elif temp < 65:
        clothing = "Jacket"
    else:
        clothing = "Heavy Coat"
    return clothing


print(clothing_type(72)) # Should print T-Shirt
print(clothing_type(55)) # Should print Sweatshirt
print(clothing_type(65)) # Should print Sweatshirt
print(clothing_type(50)) # Should print Jacket
print(clothing_type(45)) # Should print Jacket
print(clothing_type(32)) # Should print Heavy Coat
print(clothing_type(0)) # Should print Heavy Coat


test_num = 12
if test_num > 15:
    print(test_num / 4)
else:
    print(test_num + 3)

def letter_translator(letter):
    if letter == "a":
        letter_position = 1
    elif letter == "b":
        letter_position = 2
    elif letter == "c":
        letter_position = 3
    elif letter == "d":
        letter_position = 4
    else:
        letter_position = "unknown"
    return letter_position


print(letter_translator("a")) # Should print 1
print(letter_translator("b")) # Should print 2
print(letter_translator("c")) # Should print 3
print(letter_translator("d")) # Should print 4
print(letter_translator("e")) # Should print unknown
print(letter_translator("A")) # Should print unknown
print(letter_translator("")) # Should print unknown


def sum(x, y):
        return(x+y)
print(sum(sum(1,2), sum(3,4)))

def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to
    # keep just the fractional part of the quotient 
    if denominator == 0 or numerator == 0:
        part = 0
    else:
        part = (numerator % denominator)/denominator
    return part


print(fractional_part(5, 5)) # Should print 0
print(fractional_part(5, 4)) # Should print 0.25
print(fractional_part(5, 3)) # Should print 0.66...
print(fractional_part(5, 2)) # Should print 0.5
print(fractional_part(5, 0)) # Should print 0
print(fractional_part(0, 5)) # Should print 0