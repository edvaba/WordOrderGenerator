import random

'''
A sentence generator which can be used to generate quirky phrases, product ideas, or for language word order study.

GRAMMAR RULES (SVO for English/Mandarin Chinese/most European languages):
A subject is the person or thing that does the action
A verb is the action
The object is the person or thing that is affected by the action
EG. Simon ate apples

SOV languages:
Eg. Simon apples ate


'''

# File paths (change these to your actual file names or paths)
verbpath = 'verbs.txt'
adverbpath = 'adverb.txt'
nounpath = 'nouns.txt'
adjectivepath = 'adjectives.txt'

# Function to read words from a file and store them in a list
def load_words(file_path):
    words = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                words.extend(line.strip().split())
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return words

# Lists to store words from each file. Call the load_words function to load words from file path into the respective lists
verblist = load_words(verbpath)
nounlist = load_words(nounpath)
adverblist = load_words(adverbpath)
adjectivelist = load_words(adjectivepath)

# 100 sentence generation function: draw a random choice for a word from each list of adjectives, adverbs, nouns and verbs, and write to output.txt file in the current directory. Change 'w' to 'a' if you want to keep adding to the file.
def gen_sen():
    with open("output.txt", 'w', encoding='UTF-8') as file:
        for i in range(0, 100):
            print(f'{random.choice(verblist)} {random.choice(adverblist)}, {random.choice(verblist)} {random.choice(adjectivelist)} {random.choice(adverblist)} {random.choice(verblist)} {random.choice(nounlist)}')
            file.write(f'{random.choice(verblist)} {random.choice(adverblist)}, {random.choice(verblist)} {random.choice(adjectivelist)} {random.choice(adverblist)} {random.choice(verblist)} {random.choice(nounlist)}\n')
    file.close()

# display how many words are available in each list
def checkStats():
    print(f'Verbs: {len(verblist)}')
    print(f'Nouns: {len(nounlist)}')
    print(f'Adverbs: {len(adverblist)}')
    print(f'Adjectives: {len(adjectivelist)}')

def main():
    gen_sen()
    checkStats()
# calls the main function
main()
