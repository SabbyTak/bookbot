def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    charcount = charactercount(text)
    char_lists = listofdicts(charcount)

    # print(charcount)
    # print(num_words)
    # print(listofdicts(charcount))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found int he document")
    for occ in char_lists:
        print(f"The '{occ["char"]}' character was found {occ["num"]} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    return len(words)

def charactercount(character):
    new_dict = {}
    string = character
    lowertest = string.lower()
    # mystring = lowertest.split()
    # character_list = list(lowertest)
    unique_char = set(lowertest)
    for char in unique_char:
        counter = 0
        for uniq in lowertest:
            if uniq == char:
                counter += 1
        new_dict[char] = counter
    return new_dict

def sortedon(char_list):
    return char_list["num"]

def listofdicts(dict):
    char_list = []
    for char, num in dict.items():
        if char.isalpha():
            nums = {"char": char, "num" : num}
            char_list.append(nums)

    char_list.sort(reverse=True,key=sortedon)
    return (char_list)

main()