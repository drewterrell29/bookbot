import sys
from stats import count_words,count_letters

def get_book_text(filepath): 
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
     if len(sys.argv) != 2:
         print(f"Usage: python3 main.py <path_to_book>")
         sys.exit(1)
     book_location = sys.argv[1]
     book = get_book_text(book_location)

     num_words = count_words(book)
     num_letters = count_letters(book)
     print("============ BOOKBOT ============")
     print(f"Analyzing book found at {book_location}...")
     print("----------- Word Count ----------")
     print(f"Found {num_words} total words")
     print("--------- Character Count -------")
     for key,value in num_letters.items():
         print(f"{key}: {value}")
     print("============= END ===============")

main()