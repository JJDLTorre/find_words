import wget
import os

filename = './dictionaries/en/en_US.dic'
if not os.path.isfile(filename):
    url = 'https://github.com/LibreOffice/dictionaries/raw/master/en/en_US.dic'
    filename = wget.download(url)


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


def main():
    letters_to_match = input("Letters :")
    with open(filename, 'r') as f:
        lines = f.readlines()
        line_count = len(lines)
        print(f"Line_count: {line_count}")
        for word_flag in lines:
            word_flag_strip = word_flag.strip()
            if '/' in word_flag_strip:
                word = word_flag_strip.split('/')[0]
            else:
                word = word_flag_strip

            # This is the invers
            if (not word.isalpha()) or (not word.islower()) or (len(word) < 3):
                continue

            if not match_letters(letters_to_match, word):
                continue

            print(word)


if __name__ == "__main__":
    main()
