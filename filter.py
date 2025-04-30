import sys
import string

# Получаем путь к input.txt из аргументов командной строки
input_file_path = sys.argv[1]

# Открываем файл input.txt для чтения
with open(input_file_path, 'r', encoding='utf-8') as file:
    # Читаем содержимое файла
    text = file.read()

# Разбиваем текст на слова и удаляем знаки препинания
words = text.split()
cleaned_words = [word.strip(string.punctuation) for word in words]

# Ищем слова, содержащие '23'
words_with_23 = [word for word in cleaned_words if '23' in word]

# Сохраняем найденные слова в новый файл output.txt
with open('output.txt', 'w', encoding='utf-8') as output_file:
    for word in words_with_23:
        output_file.write(word + '\n')

print("Слова, содержащие '23', были сохранены в output.txt.")
