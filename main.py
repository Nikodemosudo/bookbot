def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    print(f"The Word Count is {count}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    split_text = text.split()
    return len(split_text)

main()