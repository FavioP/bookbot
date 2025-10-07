from stats import word_counter, char_counter, sort_dict, output_formatted

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    book_text = book_text.lower()
    word_count = word_counter(book_text)
    letter_count = char_counter(book_text)
    letter_count = sort_dict(letter_count)
    output_formatted(word_count,letter_count)

main()
