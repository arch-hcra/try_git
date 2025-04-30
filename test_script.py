import os
import tempfile

def test_words_with_23():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as temp_input:
        temp_input.write("This is a test 23word and another 23example.")
        temp_input_path = temp_input.name

    os.system(f'python filter.py {temp_input_path}') 

    with open('output.txt', 'r', encoding='utf-8') as f:
        output_words = f.read().splitlines()

    assert '23word' in output_words
    assert '23example' in output_words
    assert len(output_words) == 2

    os.remove('output.txt')
