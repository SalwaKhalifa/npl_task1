import nltk

def print_tokenized_words(text):
    words = nltk.word_tokenize(text)
    for word in words:
        print(word)

def print_tokenized_sentences(text):
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        print(sentence)

def print_output_using_split(text):
    output = text.split(" ")
    for item in output:
        print(item)

# Get text input from the user
user_text = input("Enter a text: ")

# Ask the user to choose an option
choice = input("Choose an option:\n1. Print tokenized words\n2. Print tokenized sentences\n3. Print output using split function\n")

# Process the chosen option
if choice == "1":
    print("Tokenized words:")
    print_tokenized_words(user_text)
elif choice == "2":
    print("Tokenized sentences:")
    print_tokenized_sentences(user_text)
elif choice == "3":
    print("Output using split function:")
    print_output_using_split(user_text)
else:
    print("Invalid choice. Please choose 1, 2, or 3.")

#NLTK is a leading platform for building Python programs to work with human 
#language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all, 
#NLTK is a free, open source, community-driven project.