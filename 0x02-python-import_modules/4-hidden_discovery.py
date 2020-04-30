#!/usr/bin/python3
def print_dir():
    for word in dir(hidden_4):
        if word[0] != '_' and word[0] != '_':
            print(word)

if __name__ == "__main__":
    import hidden_4
    print_dir()
