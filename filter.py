import sys
import string


input_file_path = sys.argv[1]


with open(input_file_path, 'r', encoding='utf-8') as file:
   text = file.read()


words = text.split()
cleaned_words = [word.strip(string.punctuation) for word in words]


words_with_23 = [word for word in cleaned_words if '23' in word]


with open('output.txt', 'w', encoding='utf-8') as output_file:
    for word in words_with_23:
        output_file.write(word + '\n')

print("'23', save in output.txt.")
