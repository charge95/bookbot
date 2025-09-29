def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print(text)
    print(count_words(text))

def get_book_text(path):
    with open(path) as book:
        book_contents = book.read()
        return book_contents

def count_words(text):
    words = text.split()
    return f"Found {len(words)} total words"

main()