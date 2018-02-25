import re

special_chars_remover = re.compile("[^\w'|_]")

def main():
    sentence = input()
    bow = create_BOW(sentence)

    print(bow)

def create_BOW(sentence):
    bow = {}
    for token in [word for word in remove_special_characters(sentence.lower()).split() if len(word)]:
        if token in bow.keys():
            bow[token] += 1
        else:
            bow[token] = 1
    
    return bow

def remove_special_characters(sentence):
    return special_chars_remover.sub(' ', sentence)

if __name__ == "__main__":
    main()
