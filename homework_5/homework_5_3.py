import string

user_input_string = input("Введіть рядок: ")

string_without_punctuation = ""
for element in user_input_string:
    if element not in string.punctuation:
        string_without_punctuation += element

title_string = string_without_punctuation.title()

string_without_spaces = title_string.replace(" ", "")

string_with_hashtag = '#' + string_without_spaces

if len(string_with_hashtag) > 140:
    string_with_hashtag_until_140 = string_with_hashtag[:140]
    print(string_with_hashtag_until_140)
else:
    print(string_with_hashtag)