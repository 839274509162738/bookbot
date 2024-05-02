def main():
    book_path = "./books/frankenstein.txt"
    try:
        text = getText(book_path)
        w_count = wordCount(text)
        print(f"{w_count} words found in {book_path}")
    except Exception as e:
        print(e)

def wordCount(string):
    if not string:
        raise ValueError("Error: empty string")
    words = string.split()
    return len(words)

def getText(path):
    if not path:
        raise ValueError("Error: empty path")
    with open(path) as f:
        return f.read()
        
main()