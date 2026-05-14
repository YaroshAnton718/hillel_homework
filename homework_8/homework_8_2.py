import string

def is_palindrome(text):
    string_without_punctuation = ""
    for element in text:
        if element not in string.punctuation:
            string_without_punctuation += element

    string_lower_case = string_without_punctuation.lower().replace(" ", "")

    i = len(string_lower_case) - 1
    reverse_string = ""
    while i >= 0:
        reverse_string += string_lower_case[i]
        i -= 1

    if string_lower_case == reverse_string:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
