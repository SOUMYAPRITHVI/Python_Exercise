import Exe25

sentence = "All good things come to those who wait."
words = Exe25.break_words(sentence)
print(words)
sorted_words=Exe25.sort_words(words)
print(sorted_words)
Exe25.print_first_word(words)
Exe25.print_last_word(words)
print(words)
Exe25.print_first_word(sorted_words)
Exe25.print_last_word(sorted_words)
print(sorted_words)
sorted_words=Exe25.sort_sentence(sentence)
print(sorted_words)
Exe25.print_first_and_last(sentence)
Exe25.print_first_and_last_sorted(sentence)