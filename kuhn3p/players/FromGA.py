import random
from kuhn3p import betting, Player

class FromGA(Player):
    def __init__(self, rng=random.Random()):
        self.p1 = [[0.0993, 0.159, 0.0137, 0.281], [0.0, 0.0, 0.651, 1.0], [0.0859, 0.0141, 0.575, 1.0], [0.0, 0.0, 0.106, 0.84]]
        self.p2 = [[0.207, 0.173, 0.0, 0.457], [0.0, 0.0208, 0.432, 1.0], [0.175, 0.00844, 0.496, 1.0], [0.0, 0.0, 0.0394, 0.919]]
        self.p3 = [[0.0449, 0.658, 0.158, 0.994], [0.0, 0.0185, 0.169, 1.0], [0.101, 0.0237, 0.488, 0.917], [0.0, 0.0, 0.126, 1.0]]
        self.rng   = rng 
    
    def start_hand(self, position, card):
        self.position = position

    def act(self, state, card):
        if self.position == 0:
            if state == 0:
                #print 'p1 at node 0'
                # at decision node 0
                if self.p1[0][card] > self.rng.random():
                    return betting.BET
                else:
                    return betting.CHECK
            elif state == 3:
                
                #print 'p1 at node 1'
                # at decision node 1
                if self.p1[1][card] > self.rng.random():
                    return betting.CALL
                else:
                    return betting.FOLD
            elif state == 6:
                #print 'p1 at node 2'                
                # at decision node 2
                if self.p1[2][card] > self.rng.random():
                    return betting.CALL
                else:
                    return betting.FOLD
            elif state == 9:
                #print 'p1 at node 3'
                # at decision node 3
                if self.p1[3][card] > self.rng.random():
                    return betting.CALL
                else:
                    return betting.FOLD
            else:
                print 'Something went wrong as p1'
        
        if self.position == 1:
            if state == 1:
                #print 'p2 at node 0'
                # at decision node 0
                if self.p2[0][card] > self.rng.random():
                    return betting.BET
                else:
                    return betting.CHECK
            elif state == 4:
                #print 'p2 at node 1'
                # at decision node 1
                if self.p2[1][card] > self.rng.random():
                    return betting.CALL
                else:
                    return betting.FOLD
            elif state == 7:
                #print 'p2 at node 2'
                # at decision node 2
                if self.p2[2][card] > self.rng.random():
                    return betting.CALL
                else:
                    return betting.FOLD
            elif state == 10:
                #print 'p2 at node 3'
                # at decision node 3
                if self.p2[3][card] > self.rng.random():
                    return betting.CALL
                else:
                    return betting.FOLD
            else:
                print 'Something went wrong as p2'
                
        if self.position == 2:
            if state == 2:
                #print 'p3 at node 0'
                # at decision node 0
                if self.p3[0][card] > self.rng.random():
                    return betting.BET
                else:
                    return betting.CHECK
            elif state == 5:
                #print 'p3 at node 1'
                # at decision node 1
                if self.p3[1][card] > self.rng.random():
                    return betting.CALL
                else:
                    return betting.FOLD
            elif state == 8:
                #print 'p3 at node 2'
                # at decision node 2
                if self.p3[2][card] > self.rng.random():
                    return betting.CALL
                else:
                    return betting.FOLD
            elif state == 11:
                #print 'p3 at node 3'
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
        return 'FromGA'
