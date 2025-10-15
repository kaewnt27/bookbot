from stats import get_num_words, get_char_dict

def get_book_text(path):
	path = "books/frankenstein.txt"
	with open(path) as f:
		return f.read()

def main():
	book_path = "books.frankenstein.txt"
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	chars_dict = get_char_dict(text)
	print(f"Found {num_words} total words")
	print(chars_dict)

main()
