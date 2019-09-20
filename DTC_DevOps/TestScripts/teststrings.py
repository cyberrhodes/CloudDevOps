# use predefined string constants
import string


# predefined string constants can be used in common scenarios
print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.punctuation)

# Use the constants to filter information out
test_string1 = "The allegory of the cave by socrates is an amazing artifact"
test_string2 = "masters2020"
test_string3 = "123456"

result = "".join([a for a in test_string1 if a in string.ascii_letters])
print(result)

# String testing methods
print(test_string1.isalnum())
print(test_string2.isalpha())

print(any([a.isalpha() for a in test_string1]))

print(test_string3.isnumeric())


test_string1 = "The allegory of the cave by socrates is an amazing artifact"

# startsWith and endsWith functions
print(test_string1.startswith("The"))
print(test_string1.startswith("the"))
print(test_string1.endswith("artifact"))


# the find and rfind functions
print(test_string1.find("the"))
print(test_string1.rfind("the"))
print("the" in test_string1)


# using replace
newStr = test_string1.replace("cave", "hotel")
print(newStr)


# counting instances of substrings
print(test_string1.count("socrates"))













