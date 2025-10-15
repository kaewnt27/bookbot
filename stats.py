def get_book_text():
        with open("books/frankenstein.txt") as f:
                file_contents = f.read()
                return file_contents

def get_num_words():
        file_contents = get_book_text()
        words = file_contents.split()
        num_words = len(words)
        return num_words

def character_counts():
	file_contents = get_book_text()
	lower_text = file_contents.lower()
	char_list = list(lower_text)
	unique_char = set(lower_text)
	unique_char_count = []

	for each_char in unique_char:
		char_count = 0
		for char in char_list:
			if(each_char == char):
				char_count +=1
		unique_char_count.append(char_count)
	
	unique_char_list = list(unique_char)
	combine_set = {}
	for i in range (0, len(unique_char_list)):
		combine_set[unique_char_list[i]] = unique_char_count[i]

	print(combine_set)

def main():
	character_counts()

main()
