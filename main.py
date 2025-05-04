from stats import word_count
def get_book_text(path): # it makes file into a string
    with open(path, encoding="utf-8") as f:
        return f.read()
def main():
    book_text = get_book_text('books/frankenstein.txt')
    words = word_count(book_text)
    print(f"{words} words found in the document")
main()
    