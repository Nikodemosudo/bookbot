"""Generates a text analysis report for Frankenstein.
    Reads the book file and produces a report containing:
    - Total word count
    - Frequency of each alphabetical character (sorted from most to least common)
"""
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    characters = count_characters(text)
    sorted_chars = get_sorted_chars(characters)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document.")
    for char_dict in sorted_chars:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times.")

    
""" Opens and reads the contents of a file at the given path. """
def get_book_text(path):
    with open(path) as f:
        return f.read()

"""Returns the total word count in the given text."""
def count_words(text):
    split_text = text.split()
    return len(split_text)

"""Creates a frequency dictionary of characters in the text.
    Converts text to lowercase first to ensure case-insensitive counting.
"""
def count_characters(text):
    characters = {}
    lowered_text = text.lower()
    for i in lowered_text:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    return characters

"""Converts character frequency dictionary to a sorted list of dictionaries.
    Only includes alphabetic characters, sorted by frequency in descending order.
"""
def get_sorted_chars(characters):
    sort_list = []

    for i in characters:
        if i.isalpha():
            sort_list.append({
                "char": i,
                "num": characters[i]
            })
    sort_list.sort(reverse=True, key=sort_on)    
    return sort_list

""" Sets key for sorting """
def sort_on(dict):
    return dict["num"]
    
    
main()