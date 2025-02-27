def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None

def main():
    filename = input("Enter the file name: ")
    word_count = count_words_in_file(filename)
    if word_count is not None:
        print(f"The file '{filename}' contains {word_count} words.")

if __name__ == "__main__":
    main()
