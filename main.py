# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagrams(value,word):
    if sorted(first_string) == sorted(second_string):
        return True
    else:
        return False

first_string = input("Enter the first word: ")
second_string = input("Enter the second word: ")


find_anagrams(first_string, second_string)
print(find_anagrams('python1','yptho1n'))

def find_anagrams(value,word):
    if sorted(first_string) > sorted(second_string):
        return True
    else:
        return False

first_string = str(input("Enter the first word: "))
second_string = str(input("Enter the second word: "))


find_anagrams(first_string, second_string)
print(find_anagrams('effiong','gffione'))