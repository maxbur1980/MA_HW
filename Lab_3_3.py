import random

word_list = ['table', 'function', 'authentification', 'car', 'robot']
word = list(random.choice(word_list))
my_word = ['_' for i in range(len(word))]
attempt = 0
print('The word is: ', my_word)

while not word == my_word:
    letter = input('Enter a letter: ')
    for i in range(len(word)):
        if word[i] == letter:
            my_word[i] = letter
    attempt += 1
    print(my_word)

print('Congratulations! You win with {} attempts!'.format(attempt))


