# Player that is uses the GA parameters.

import random
from kuhn3p import betting, Player

class GABot(Player):
    def __init__(self, position, array):
        # converts the array into the [node][card] matrix
        matrix = []
        for x in range(4):
            matrix.append([])
            for y in range(4):
                matrix[x].append(array[x * 4 + y])
        if position == 0:
            self.p1 = matrix
        elif position == 1:
            self.p2 = matrix
        elif position == 2:
            self.p3 = matrix
        self.rng = random.Random() 
                
    
    def start_hand(self, position, card):
        self.position = position

    def act(self, state, card):
        # for each state, randomly select a probability and bet/call 
        # if the matrix entry is greater than that probability
        if self.position == 0:
            if state == 0:
                # at decision node 0
                if self.p1[0][card] > self.rng.random():
                    return betting.BET
                else:
                    return betting.CHECK
            elif state == 3:
                # at decision node 1
                if self.p1[1][card] > self.rng.random():
                    return betting.CALL
                else:
                    return betting.FOLD
            elif state == 6:
                # at decision node 2
                if self.p1[2][card] > self.rng.random():
                    return betting.CALL
                else:
                    return betting.FOLD
            elif state == 9:
                # at decision node 3
                if self.p1[3][card] > self.rng.random():
                    return betting.CALL
                else:
                    return betting.FOLD
            else:
                print 'Something went wrong as p1'
        
        if self.position == 1:
            if state == 1:
                # at decision node 0
                if self.p2[0][card] > self.rng.random():
                    return betting.BET
                else:
                    return betting.CHECK
            elif state == 4:
                # at decision node 1
                if self.p2[1][card] > self.rng.random():
                    return betting.CALL
                else:
                    return betting.FOLD
            elif state == 7:
                # at decision node 2
                if self.p2[2][card] > self.rng.random():
                    return betting.CALL
                else:
                    return betting.FOLD
            elif state == 10:
                # at decision node 3
                if self.p2[3][card] > self.rng.random():
                    return betting.CALL
                else:
                    return betting.FOLD
            else:
                print 'Something went wrong as p2'
                
        if self.position == 2:
            if state == 2:
                # at decision node 0
                if self.p3[0][card] > self.rng.random():
                    return betting.BET
                else:
                    return betting.CHECK
            elif state == 5:
                # at decision node 1
                if self.p3[1][card] > self.rng.random():
                    return betting.CALL
                else:
                    return betting.FOLD
            elif state == 8:
                # at decision node 2
                if self.p3[2][card] > self.rng.random():
                    return betting.CALL
                else:
                    return betting.FOLD
            elif state == 11:
                # at decision node 3
                if self.p3[3][card] > self.rng.random():
                    return betting.CALL
                else:
                    return betting.FOLD
            else:
                print 'Something went wrong as p3'

        print 'error has occurred'
        return betting.BET

    def __str__(self):
        return 'GABot'
