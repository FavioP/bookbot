import sys
from stats import word_counter, char_counter, sort_dict, output_formatted

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    book_text = book_text.lower()
    word_count = word_counter(book_text)
    letter_count = char_counter(book_text)
    letter_count = sort_dict(letter_count)
    output_formatted(word_count,letter_count,book_path)

main()
