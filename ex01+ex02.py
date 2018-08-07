def rotate_word(word, rotation):
    new_word = ''
    for letter in word:
        new_word += chr((ord(letter) - 97 + rotation) % 26 + 97)
    return new_word


def create_word_dict(path='words.txt'):
    file = open(path)
    words = set()
    for line in file:
        words.add(line.strip())
    return words


def print_rotate_pairs(words):
    for word in words:
        for rotation in range(1, 14):
            rotated = rotate_word(word, rotation)
            if rotated in words:
                print(word, rotated, sep=', ')


def main():
    print_rotate_pairs(create_word_dict())

if __name__ == '__main__':
    main()
    print(rotate_word('orra', 13))