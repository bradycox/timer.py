#!/usr/bin/python3

"""
converters.py: Convert natural language digits within phrases to integers,
keeping unmatched strings intact.
"""


def word_to_num(phrase):
    """
    Convert number words in a phrase to digits, keeping unmatched strings.

    Supports numbers up to 999,999,999 within a mixed phrase.

    Args:
        phrase (str): The phrase containing number words and other text.

    Returns:
        str: A string with number words converted to digits and other text
             unchanged.
    """
    num_dict = {
        'zero': 0, 'a': 1, 'an': 1, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
        'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
        'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
        'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
        'eighty': 80, 'ninety': 90
    }
    parts = phrase.lower().replace('-', ' ').split()
    output = []
    number_started = False
    current_number = 0
    for part in parts:
        if part in num_dict:
            current_number += num_dict[part]
            number_started = True
        elif part == "hundred" and number_started:
            current_number *= 100
        elif part == "thousand" and number_started:
            current_number *= 1000
        elif part == "million" and number_started:
            current_number *= 1000000
        elif part == "and" and number_started:
            continue  # Skip "and" in numbers
        else:
            if number_started:
                output.append(str(current_number))
                current_number = 0
                number_started = False
            output.append(part)
    if number_started:
        output.append(str(current_number))

    return ' '.join(output)


# Example usage
if __name__ == "__main__":
    test_phrases = [
        "one hundred and twenty five minutes",
        "two hundred and thirty one people",
        "ninety nine red balloons",
        "a journey of a thousand miles begins with a single step",
        "a journey of four million and four miles begins the same way",
        "journey of two billion four hundred and seventy seven miles? nah."
    ]
    for phrase in test_phrases:
        print(f"Original: {phrase}")
        print(f"Converted: {word_to_num(phrase)}\n")
