import random
from kuhn3p import betting, deck, Player

class Individual(Player):
    def __init__(self):
        #opponents have the same relative position, the same opponent will always be before me
        # initialse the player
        self.oppAaspl1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.oppAaspl2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.oppAaspl3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        
        self.oppBaspl1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.oppBaspl2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.oppBaspl3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        

        
    def start_hand(self, position, card):
        self.position = position
        # create new variables for which matrices to use
        if position == 0:
            # I am player 1
            self.pl2 = self.oppAaspl2
            self.pl3 = self.oppBaspl3
        if position == 1:
            self.pl3 = self.oppAaspl3
            self.pl1 = self.oppBaspl1
        if position == 2:
            self.pl1 = self.oppAaspl1
            self.pl2 = self.oppBaspl2
        

    def act(self, state, card):
        #betting.actor could give the opponent NOPE
        if self.position == 0:
            if betting.to_decision(state) == 0:
                # at decision node 0
                if self.p1node0(card) == 1:
                    return betting.BET
                else:
                    return betting.CHECK
            elif betting.to_decision(state) == 1:
                # at decision node 1
                if self.p1node1(card) == 1:
                    return betting.CALL
                else:
                    return betting.FOLD
            elif betting.to_decision(state) == 2:
                # at decision node 2
                if self.p1node2(card) == 1:
                    return betting.CALL
                else:
                    return betting.FOLD
            elif betting.to_decision(state) == 3:
                # at decision node 3
                if self.p1node3(card) == 1:
                    return betting.CALL
                else:
                    return betting.FOLD
            else:
                print 'Something went wrong'
        
        if self.position == 1:
            
        return betting.BET
            
            
        
    def p1node0(self, card):
        # f = ap0 + (1-p0)(bp1 + b'(1-p1) + cp2 + c'(1-p2) + dp3 + d'(1-p3) + e)
        # to maximise this, find p1, p2, p3 by comparing b and b', c and c', d and d'
        # now can compare a and coefficient of (1-p0) - call this g
        a = 0
        b = 0
        _b = 0
        c = 0
        _c = 0
        d = 0
        _d = 0
        e = 0
        for x in range (deck.num_cards()): 
            # player 2 cards
            for y in range(deck.num_cards()):
                # player 3 cards
                if x != y and x != card and y != card:
                    a += (1/6)*((1-self.pl2[1][x])*(1-self.pl3[2][y])*self.payoff(card, -1, -1, 4) + (1-self.pl2[1][x])*self.pl3[2][y]*self.payoff(card, -1, y, 5) + self.pl2[1][x]*(1-self.pl3[3][y])*self.payoff(card, x, -1, 5) + self.pl2[1][x]*self.pl3[3][y]*self.payoff(card, x, y, 6))
                    b += (1/6)*((1-self.pl2[0][x])*self.pl3[0][y]*(1-self.pl2[3][x])*self.payoff(card, -1, y, 5) + (1-self.pl2[0][x])*self.pl3[0][y]*self.pl2[3][x]*self.payoff(card, x, y, 6))
                    _b += (1/6)*((1-self.pl2[0][x])*self.pl3[0][y]*(1-self.pl2[2][x])*self.payoff(-1, -1, y, 5) + (1-self.pl2[0][x])*self.pl3[0][y]*self.pl2[2][x]*self.payoff(-1, x, y, 6))
                    c += (1/6)*(self.pl2[0][x]*(1-self.pl3[1][y])*self.payoff(card, x, -1, 5))
                    _c += (1/6)*(self.pl2[0][x]*(1-self.pl3[1][y])*self.payoff(-1, x, -1, 4))
                    d += (1/6)*(self.pl2[0][x]*self.pl3[1][y]*self.payoff(card, x, y, 6))
                    _d += (1/6)*(self.pl2[0][x]*self.pl3[1][y]*self.payoff(-1, x, y, 6))
                    e += (1/6)*((1-self.pl2[0][x])*(1-self.pl3[0][y])*self.payoff(card, x, y, 3))
        if b < _b:
            p1 = 0
        else:
            p1 = 1
        
        if c < _c:
            p2 = 0
        else:
            p2 = 1
            
        if d < _d:
            p3 = 0
        else:
            p3 = 1
            
        g = b*p1 + _b*(1-p1) + c*p2 + _c*(1-p2) + d*p3 + _d*(1-p3) + e
        
        if a < g:
            p0 = 0
        else:
            p0 = 1
        
        return p0
    
    def p1node1(self, card):
        b = 0
        _b = 0
        
        for x in range (deck.num_cards()): 
            # player 2 cards
            for y in range(deck.num_cards()):
                # player 3 cards
                if x != y and x != card and y != card:
                    b += (1/6)*((1-self.pl2[0][x])*self.pl3[0][y]*(1-self.pl2[3][x])*self.payoff(card, -1, y, 5) + (1-self.pl2[0][x])*self.pl3[0][y]*self.pl2[3][x]*self.payoff(card, x, y, 6))
                    _b += (1/6)*((1-self.pl2[0][x])*self.pl3[0][y]*(1-self.pl2[2][x])*self.payoff(-1, -1, y, 5) + (1-self.pl2[0][x])*self.pl3[0][y]*self.pl2[2][x]*self.payoff(-1, x, y, 6))
        if b < _b:
            p1 = 0
        else:
            p1 = 1
        
        return p1
    
    def p1node2(self, card):
        c = 0
        _c = 0
        for x in range (deck.num_cards()): 
            # player 2 cards
            for y in range(deck.num_cards()):
                # player 3 cards
                if x != y and x != card and y != card:
                    c += (1/6)*(self.pl2[0][x]*(1-self.pl3[1][y])*self.payoff(card, x, -1, 5))
                    _c += (1/6)*(self.pl2[0][x]*(1-self.pl3[1][y])*self.payoff(-1, x, -1, 4))
        if c < _c:
            p2 = 0
        else:
            p2 = 1
        
        return p2
            
    def p1node3(self, card):
        d = 0
        _d = 0
        for x in range (deck.num_cards()): 
            # player 2 cards
            for y in range(deck.num_cards()):
                # player 3 cards
                if x != y and x != card and y != card:
                    d += (1/6)*(self.pl2[0][x]*self.pl3[1][y]*self.payoff(card, x, y, 6))
                    _d += (1/6)*(self.pl2[0][x]*self.pl3[1][y]*self.payoff(-1, x, y, 6))
        if d < _d:
            p3 = 0
        else:
            p3 = 1
        
        return p3
            
    def payoff(self, playerCard, card1, card2, pay):
        if playerCard == -1:
            # player has folded
            return -1
        elif playerCard == max(playerCard, card1, card2):
            if pay == 3:
                return pay - 1
            else:
                return pay - 2
        else:
            if pay == 3:
                return -1
            else:
                return -2

        

    #def expValue(self, card):
        

   # def __str__(self):
        #return 'Individual' % (self.bluff)
