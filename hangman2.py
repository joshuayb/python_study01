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

t_guess = 9
num_guess = 1
match_board = ['*'] * len(selected_word)
print(match_board)
while num_guess < t_guess + 1:
    guess = input('Guess! ==> ')
    j = 0
    for l in selected_word:
        if guess == l:
            match_board[j] = guess
        j += 1
    if match_board == selected_word:
        print('Congratulaions!')
        print("".join(selected_word))
        break
    num_guess += 1
    print(match_board)
    print('number of guess: ' + str(num_guess))
    if num_guess == t_guess:
        print('The last chance!')
    if num_guess == t_guess + 1:
        print('You could not make it. The word is')
        print("".join(selected_word))
