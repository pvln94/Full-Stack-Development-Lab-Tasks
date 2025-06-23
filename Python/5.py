import string

def get_unique_words(sentence):
    if not sentence.strip():
        return []
    
    # Remove punctuation and convert to lowercase
    translator = str.maketrans("", "", string.punctuation)
    words = sentence.translate(translator).lower().split()
    
    # Use set for unique words and sort them
    unique_words = sorted(set(words))
    return unique_words

def main():
    sentence = input("Enter a sentence: ")
    unique_words = get_unique_words(sentence)
    
    if not unique_words:
        print("No valid words found.")
    else:
        print("\nUnique words in alphabetical order:")
        for word in unique_words:
            print(word)

if __name__ == "__main__":
    main()