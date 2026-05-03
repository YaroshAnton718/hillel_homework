import string
import keyword

flag = True
string_punctuation_without_underline = string.punctuation.replace("_", "")

user_input_string = input("Enter a string: ")

for element in user_input_string:
    if element in string_punctuation_without_underline or element == " ":
        flag = False

if user_input_string[0].isdigit() or not user_input_string.islower():
    flag = False

user_input_words = user_input_string.split()
for word in user_input_words:
    if word in keyword.kwlist:
        flag = False

print(f"{user_input_string} => {flag}")