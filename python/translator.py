import sys

# Define the Braille alphabet mapping
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', # Add the rest
    # Add capital sign, number sign, etc.
}

# Reverse mapping for Braille to English
english_alphabet = {v: k for k, v in braille_alphabet.items()}

def translate_to_braille(text):
    result = []
    for char in text:
        # Handle capitalization, numbers, and spaces
        if char.isupper():
            result.append(braille_alphabet['capital'])
            char = char.lower()
        result.append(braille_alphabet.get(char, ''))
    return ''.join(result)

def translate_to_english(braille_text):
    result = []
    cells = [braille_text[i:i+6] for i in range(0, len(braille_text), 6)]
    for cell in cells:
        # Handle special symbols and translate
        result.append(english_alphabet.get(cell, ''))
    return ''.join(result)

if __name__ == '__main__':
    input_text = sys.argv[1]
    
    if all(char in "O." for char in input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))

