import random
from kuhn3p import betting, Player

class FromGA(Player):
    def __init__(self, rng=random.Random()):
        self.p1 = [[0.0103, 0.00380, 0.147, 0.210], [0.0569, 0.0814, 0.970, 0.911], [0.0625, 0.199, 0.150, 0.966], [0.047, 0.0406, 0.311, 0.685]]
        self.p2 = [[0.108, 0.0204, 0.0584, 0.948], [0.0274, 0.0639, 0.107, 0.924], [0.103, 0.0305, 0.517, 0.999], [0.200, 0.00488, 0.0366, 0.856]]
        self.p3 = [[0.125, 0.137, 0.0429, 0.846], [0.154, 0.0827, 0.186, 0.927], [0.0870, 0.00753, 0.229, 0.784], [0.0598, 0.0545, 0.857, 0.940]]
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
