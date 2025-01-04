
def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        num_of_words = word_number(file_contents)
        print(f"{num_of_words} words found in the document\n")

        dic = char_numbers(file_contents)
        for item in dic:
            print(f"The '{item}' character was found {dic[item]} times")
        print("--- End report ---")
        

def word_number(text):
    words = text.split()
    length = len(words)
    return length

def char_numbers(text):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r","t", "u", "v", "w", "x", "y", "z"]
    sum = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter in letters: 
            if letter in sum:
                sum[letter] += 1
            else:
                sum[letter] = 1

    return sum


main()
