alphabet_size = 256


def calculate_hash(pattern, primary_number):
    reducing_hash_number = 1

    for i in range(len(pattern) - 1):
        reducing_hash_number = (reducing_hash_number * alphabet_size) % primary_number

    return reducing_hash_number


def rabin_karp_search(text, pattern, primary_number=101):
    positions_array = []
    text_hash_value = 0
    pattern_hash_value = 0

    reducing_hash_number = calculate_hash(pattern, primary_number)

    for i in range(len(pattern)):
        text_hash_value = (alphabet_size * text_hash_value + ord(text[i])) % primary_number
        pattern_hash_value = (alphabet_size * pattern_hash_value + ord(pattern[i])) % primary_number

    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash_value == text_hash_value:
            matches_number = 0
            for j in range(len(pattern)):
                if pattern[j] == text[j + i]:
                    matches_number += 1
                else:
                    break
            if matches_number == len(pattern):
                positions_array.append(i)

        if i < len(text) - len(pattern):
            text_hash_value = (alphabet_size * (text_hash_value - ord(text[i]) * reducing_hash_number) + ord(
                text[i + len(pattern)])) % primary_number
            text_hash_value = text_hash_value + primary_number if text_hash_value < 0 else text_hash_value
    return positions_array


if __name__ == '__main__':
    text = "BBCLLNMNLLN"
    pattern = "LLN"

    print(rabin_karp_search(text, pattern))
