
import os

def test_words_with_23():
    # Создаем тестовый input.txt файл
    with open('input.txt', 'w', encoding='utf-8') as f:
        f.write("This is a test 23word and another 23example.")

    # Запускаем основной код
    os.system('python filter.py')  # Замените your_script.py на имя вашего скрипта

    # Проверяем output.txt
    with open('output.txt', 'r', encoding='utf-8') as f:
        output_words = f.read().splitlines()

    # Проверяем, что в output.txt содержатся правильные слова
    assert '23word' in output_words
    assert '23example' in output_words
    assert len(output_words) == 2  # Должно быть 2 слова

    # Удаляем тестовые файлы
    os.remove('input.txt')
    os.remove('output.txt')
