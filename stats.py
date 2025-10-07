#A file that contains functions for analyzing the text

def get_num(dictionary):
    return dictionary["num"]

def word_counter(string):
    words = string.split()
    return len(words)

def char_counter(string):
    words = string.split()
    characters = {}
    for word in words:
        for letter in word:
            if letter in characters:
                characters[letter] += 1
            else:
                characters[letter] = 1
    return characters

def sort_dict(letters):
    char_counter = []
    for key in letters:
        tmp = {"char": key, "num": letters[key]}
        char_counter.append(tmp)
    char_counter = sorted(char_counter, key=get_num, reverse=True)
    return char_counter

def output_formatted(word_count,letters):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in letters:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")
