from random import *

a = ['alliteration','unidentified', 'intermittent', 'pennsylvania', 'exacerbation',\
    'independence', 'commensalism', 'intelligence', 'relationship', 'thanksgiving',\
    'professional', 'organization', 'sporadically', 'intimidating', 'abolitionist',\
    'appreciation', 'annunciation', 'malnutrition', 'architecture', 'biodiversity',\
    'acceleration', 'interdiction', 'trigonometry', 'communicator', 'bodybuilding',\
    'perspiration', 'resurrection', 'constipation', 'civilization', 'velociraptor',\
    'retrocession', 'expectations', 'ambidextrous', 'cytoskeleton', 'exasperation',\
    'abbreviation', 'voluminosity', 'colonization', 'interception', 'championship',\
    'acquaintance', 'depreciation', 'consequences', 'grandparents', 'repository',\
    'scarlet', 'delta', 'gamma', 'lima', 'fold', 'given', 'hang', 'tell', 'fashion',\
    'information'] # given words
a1 =[]
for word in a:
    b = []
    for letter in word:
        b.append(letter)
    a1.append(b)
#print(a1)

selected_word = a1[randint(0, len(a)-1)]
#print(selected_word)

t_guess = 10
num_guess = 1
match_board = ['-'] * len(selected_word)
print("".join(match_board))
while num_guess < t_guess + 1:
    print('')
    guess = input('Guess! ==> ')
    print('')
    if guess in match_board:
        print('You already guessed the letter.')
    j = 0
    for l in selected_word:
        if guess == l:
            match_board[j] = guess
        j += 1
    print("'" + guess + "'" + ' frequecy: ' + str(selected_word.count(guess)))
    if match_board == selected_word:
        print("".join(selected_word))
        print('')
        print('Congratulaions!')
        break
    num_guess += 1
    print("".join(match_board))
    print('')
    print('number of guess: ' + str(num_guess - 1))
    if num_guess == t_guess:
        print('The last chance!')
    if num_guess == t_guess + 1:
        print('You could not make it. The word is')
        print("".join(selected_word))
