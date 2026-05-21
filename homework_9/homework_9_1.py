import string

def popular_words (text, words):
    string_without_punctuation = ""
    for element in text:
        if element not in string.punctuation:
            string_without_punctuation += element

    string_lower_case = string_without_punctuation.lower().split()
    dictionary_of_words = {}
    for i in range(len(string_lower_case)):
        if string_lower_case[i] in dictionary_of_words:
            dictionary_of_words[string_lower_case[i]] += 1
        else:
            dictionary_of_words[string_lower_case[i]] = 1

    print(dictionary_of_words)
    popular_words_dictionary = {}
    for i in range(len(words)):
        if words[i] in dictionary_of_words:
            popular_words_dictionary[words[i]] = dictionary_of_words[words[i]]
        else:
            popular_words_dictionary[words[i]] = 0

    return popular_words_dictionary

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
