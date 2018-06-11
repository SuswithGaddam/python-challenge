import re

file = open("sample_file.txt", "r")

paragraph = file.read()

#print(paragraph)

#solution:

words = re.findall(r'\w+', paragraph)

num_of_words = len(words)

sentences = re.findall(r'\.', paragraph)

num_of_sentences = len(sentences)

letters = re.findall(r'\S', paragraph)

avg_letter_per_word = len(letters)/len(words)

avg_sent_length = len(words)/len(sentences)

# print(avg_sent_length)
# print(avg_letter_per_word)
# print(num_of_sentences)
# print(num_of_words)

summary =  (f"Paragraph Analysis\n"
            f"---------------------------------\n"
            f"Approximate Word Count: {num_of_words}\n"
            f"Approximate Sentence Count: {num_of_sentences}\n"
            f"Average Letter Count: {avg_letter_per_word}\n"
            f"Average Sentence Length: {avg_sent_length}\n")

print(summary)
