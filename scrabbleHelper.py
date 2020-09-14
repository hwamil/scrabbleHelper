#! python3

from itertools import combinations as combo
import enchant
from bs4 import BeautifulSoup as bs
import requests as req
from textwrap import fill


print('')
print('welcome to scrabble helper'.upper().center(65, '*'))
print('remember that you can\'t use abbreviations in the game'.upper().center(65, '*'))

while True:
    print('')
    word = ''.join(input('Letters you have in scrabble: ').strip().split(' '))
    d = enchant.Dict("en_US")
    a = [combo(word, i) for i in range(1, len(word) + 1)]
    b = list()
    v = 'aeiou'

    for f in range(len(a)):
        for g in list(a[f]):
            g = ''.join(g).strip()
            if g not in b:
                b.append(''.join(g))

    words = sorted([i for i in b if d.check(i)], key=len)
    print('\nword list\n'.upper().center(65, '*'))

    for word in words:
        word = word.ljust(15, ' ')
        word = word + '<'
        print(word.ljust(30, '-'))

    while True:

        try:
            print('')
            look = input('Look up a definition? [y/n]: ').lower()

            if look == 'y':
                print('')
                look = input('Which word?: ').lower()

                if look in words:
                    print('\nLoading...\n')
                    webDictionary = req.get(
                        'https://www.dictionary.com/browse/' + look + '?s=t')
                    page = bs(webDictionary.text, 'lxml')
                    definitions = page.find("div", "e1hk9ate4")
                    definitions = definitions.find_all("div", "e1q3nk1v3")

                else:
                    print('That word is not in your possibles :/')
                    break

                print(''.center(65, '-'))
                print('\"' + look.upper() + '\"')
                print('')

                for n, d in enumerate(definitions):
                    print(str(n + 1) + ') ' + fill(d.text.strip(), 40))
                    print('')
                print(''.center(65, '-') + '\n')

            elif look == 'n':
                break

            else:
                print('\nwhat?')

        except AttributeError:
            print(
                "I wasn't able to retrieve any definitions from dictionary.com :(")
