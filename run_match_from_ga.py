#Run a match between 2 opponent modeling bots and one GA 
#bot with parameters passed in on the command line.

from kuhn3p import deck, dealer, players, betting

import sys
import os

# get the variables from command line
num_hands = int(sys.argv[1])
count = int(sys.argv[2])
gen_num = int(sys.argv[3])
ga_position = int(sys.argv[4])

# setup the probability of betting/calling from command line's remaining variables
ga_array = []
for x in range(5, len(sys.argv)):
    ga_array.append(float(sys.argv[x]))
    
# setup the file to write the total bankroll, actions and cards to
directoryname = '/directory/' + str(gen_num) + '/' + str(ga_position)
filename = str(gen_num) + '_' + str(count) + '_' + str(ga_position) + '.txt'
if not os.path.exists(directoryname):
    os.makedirs(directoryname)
f = open(directoryname + '/' + filename, 'w')

# assign the players, replacing the appropriate opponent modeler with the GA bot 
the_players = [players.KuhnYouHandleIt(), players.KuhnYouHandleIt(), players.KuhnYouHandleIt() ]
the_players[ga_position] = players.GABot(ga_position, ga_array)

total = [0, 0, 0]
# We want to fix the positions so the_players[i] is in seat i
for hand in range(num_hands):
    first = 0
    second = 1
    third = 2

    this_players = [the_players[first], the_players[second], the_players[third]]
    cards = deck.shuffled()
    (state, delta) = dealer.play_hand(this_players, cards)

    st = '|'
    for i in range(3):
        total[(first + i) % 3] += delta[i]
        st += str(total[(first + i) % 3]) + '|'
        
    f.write(str(hand) + ':' + betting.to_string(state) + ':' + str(cards) + ':' + st + '\n')

print total[ga_position]
