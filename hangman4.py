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

selected_word = a1[randint(0, len(a)-1)]
vowels = ['a', 'e', 'i', 'o', 'u']

credit = 100
t_guess = 10
num_guess = 1
guess_list = []
match_board = ['-'] * len(selected_word)
print(str(len(selected_word)) + '-letter word ' + "".join(match_board))
while num_guess < t_guess + 1:
    print('')
    guess = input('Guess! ==> ')
    guess_list.append(guess)
    print('')
    if guess in match_board:
        print('You already guessed the letter.')
    j = 0
    for l in selected_word:
        if guess == l:
            match_board[j] = guess
        j += 1
    # the number of letters in selected word
    print("'" + guess + "'" + ' frequecy: ' + str(selected_word.count(guess))) 
    if match_board == selected_word:
        print("".join(selected_word))
        print('')
        print('Congratulaions!')
        credit += 120 + (t_guess - num_guess) * 10
        print(credit)
        break
    num_guess += 1
    if guess in vowels:
        credit -= 15 * selected_word.count(guess) 
    else:
        credit -= 10
    print("".join(match_board))
    print('')
    print('number of guess: ' + str(num_guess - 1))
    print("".join(guess_list))
    print(credit)
    if num_guess == 6: 
        open = 'open'
        while open.isnumeric() == False:
            print('')
            open = input('Open a letter! (input which letter you want to open) ==> ') # select a letter to open
            if open.isnumeric() == False:
                print('')
                print('Please input number.')
            else:
                match_board[int(open)] = selected_word[int(open)]
                print("".join(match_board)) # show the match board with an opened letter    
        if int(open) == 0:
            credit -= 75
        elif int(open) == 1:
            credit -= 25
        else:
            int(open) >= 2
            credit -= 10
        print(credit)
    if num_guess == t_guess:
        print('The last chance!')
    if num_guess == t_guess + 1:
        print('You could not make it. The word is')
        print("".join(selected_word))
