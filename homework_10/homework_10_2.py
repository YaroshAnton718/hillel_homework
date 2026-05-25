import string

def first_word(text):
    """ Пошук першого слова """
    text_without_punctuation = text
    punctuation_string = string.punctuation
    punctuation_string = punctuation_string.replace("'", "")
    for i in range(len(punctuation_string)):
        text_without_punctuation = text_without_punctuation.replace(punctuation_string[i], ' ')

    word_list = text_without_punctuation.split()

    return word_list[0]

first_word("don't touch it")
first_word(".., and so on ...")
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
