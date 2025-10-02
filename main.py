from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    word_count = count_words(text)
    letters = count_char(text)
    print(sys.argv)
    print_report(path, word_count, letters)

def get_book_text(path):
    with open(path) as book:
        book_contents = book.read()
        return book_contents

def print_report(path, word_count, char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in char_count:
        print(f"{char}: {char_count[char]}")
    print("============= END ===============")
main()