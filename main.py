def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    characters = count_characters(text)
    print(f"The Word Count is {count}")
    print(f"The Character Count is: {characters}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    split_text = text.split()
    return len(split_text)

def count_characters(text):
    characters = {}
    lowered_text = text.lower()
    for i in lowered_text:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    return characters

main()