def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = get_characters(text)
    report = get_list_dict(characters)
    report.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    list_of_characters(report)
    print(f"--- End report ---")
        

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_characters(text):
    book_lower = text.lower()
    amnt_chars = {}
    for b in book_lower:
        if b.isalpha():
            if b not in amnt_chars:
                amnt_chars[b] = 1
            else:
                amnt_chars[b] += 1
    return amnt_chars
    
def get_list_dict(characters):
    list_of_dict = []
    for char, count in characters.items():
        list_of_dict.append({"char": char, "count": count})
    return list_of_dict

def sort_on(report):
    return report["count"]

def list_of_characters(report):
    for r in report:
        print(f"The '{r['char']}' character was found {r['count']} times")


main()