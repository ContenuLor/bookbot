from stats import sort_dict
from stats import get_num_words
import sys

def get_book_text (file_path):
	with open(file_path) as f:
		file_contents= f.read()
		return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        file_path = sys.argv[1]
        book_text = get_book_text(file_path)
        sorted_letter_count = sort_dict(book_text)
        num_words = get_num_words(book_text)
        
        print(
        "============ BOOKBOT ============\n"
        "Analyzing book found", file_path, "\n"
        "----------- Word Count ----------\n"
        "Found", num_words ,"total words\n"
        "--------- Character Count -------\n"
        )
        for item in sorted_letter_count:
            if item["char"].isalpha():
                print(f'{item["char"]}: {item["num"]}')

if __name__ == "__main__": main()