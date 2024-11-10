import inflect

words = inflect.engine().number_to_words(5, andword="")
print(words)