

def main():
    with open("en_US.dic", 'r') as f:
        lines = f.readlines()
        line_count = len(lines)
        print(f"Line_count: {line_count}")
        for word_flag in lines:
            word = word_flag.split('/')[0]

            if (not word.isalpha()) or (not word.islower()) or (len(word) < 3) or (len(word) != 5):
                continue

            letters_to_match = 'moneyl'

            if not match_letters(letters_to_match, word):
                continue

            print(word)


def match_letters(letters_to_match, word):

    # The word must have the same or fewer characters than the letters_to_match
    if len(word) > len(letters_to_match):
        return False

    sorted_c_to_match = sorted(letters_to_match)

    for c in sorted(list(word)):

        if c in sorted_c_to_match:
            sorted_c_to_match.remove(c)
        else:
            return False

    return True


if __name__ == "__main__":
    main()
