from kuhn3p import betting, deck, Player

class Individual(Player):
    def __init__(self):
        #opponents have the same relative position, the same opponent will always be before me
        # initialse the player
        self.oppAaspl1 = [[0.9, 0.8, 0.5, 0.3], [0, 0.1, 0.5, 0.9], [0, 0.1, 0.5, 0.9], [0, 0.1, 0.5, 0.9]]
        self.oppAaspl2 = [[0.7, 0.4, 0.7, 0.8], [0.1, 0.1, 0.4, 1], [0, 0, 0.7, 1], [0, 0, 0.7, 1]]
        self.oppAaspl3 = [[0.1, 0.1, 0.6, 0.7], [0, 0.1, 0.7, 0.9], [0, 0, 0.4, 0.7], [0, 0, 0.3, 1]]
        
        self.oppBaspl1 = [[0.9, 0.8, 0.5, 0.3], [0, 0.1, 0.5, 0.9], [0, 0.1, 0.5, 0.9], [0, 0.1, 0.5, 0.9]]
        self.oppBaspl2 = [[0.7, 0.4, 0.7, 0.8], [0.1, 0.1, 0.4, 1], [0, 0, 0.7, 1], [0, 0, 0.7, 1]]
        self.oppBaspl3 = [[0.1, 0.1, 0.6, 0.7], [0, 0.1, 0.7, 0.9], [0, 0, 0.4, 0.7], [0, 0, 0.3, 1]]
        
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
            if state == 0:
                #print 'p1 at node 0'
                # at decision node 0
                if self.p1node0(card) == 1:
                    return betting.BET
                else:
                    return betting.CHECK
            elif state == 3:
                #print 'p1 at node 1'
                # at decision node 1
                if self.p1node1(card) == 1:
                    return betting.CALL
                else:
                    return betting.FOLD
            elif state == 6:
                #print 'p1 at node 2'                
                # at decision node 2
                if self.p1node2(card) == 1:
                    return betting.CALL
                else:
                    return betting.FOLD
            elif state == 9:
                #print 'p1 at node 3'
                # at decision node 3
                if self.p1node3(card) == 1:
                    return betting.CALL
                else:
                    return betting.FOLD
            else:
                print 'Something went wrong as p1'
        
        if self.position == 1:
            if state == 1:
                #print 'p2 at node 0'
                # at decision node 0
                if self.p2node0(card) == 1:
                    return betting.BET
                else:
                    return betting.CHECK
            elif state == 4:
                #print 'p2 at node 1'
                # at decision node 1
                if self.p2node1(card) == 1:
                    return betting.CALL
                else:
                    return betting.FOLD
            elif state == 7:
                #print 'p2 at node 2'
                # at decision node 2
                if self.p2node2(card) == 1:
                    return betting.CALL
                else:
                    return betting.FOLD
            elif state == 10:
                #print 'p2 at node 3'
                # at decision node 3
                if self.p2node3(card) == 1:
                    return betting.CALL
                else:
                    return betting.FOLD
            else:
                print 'Something went wrong as p2'
                
        if self.position == 2:
            if state == 2:
                #print 'p3 at node 0'
                # at decision node 0
                if self.p3node0(card) == 1:
                    return betting.BET
                else:
                    return betting.CHECK
            elif state == 5:
                #print 'p3 at node 1'
                # at decision node 1
                if self.p3node1(card) == 1:
                    return betting.CALL
                else:
                    return betting.FOLD
            elif state == 8:
                #print 'p3 at node 2'
                # at decision node 2
                if self.p3node2(card) == 1:
                    return betting.CALL
                else:
                    return betting.FOLD
            elif state == 11:
                #print 'p3 at node 3'
                # at decision node 3
                if self.p3node3(card) == 1:
                    return betting.CALL
                else:
                    return betting.FOLD
            else:
                print 'Something went wrong as p3'

        print 'Oh god why are we here?'
        return betting.BET
    
    def end_hand(self, position, card, state, shown_cards):
        print betting.to_string(state)
        print shown_cards
        print state
        amount = 0.1
        # need to update the matrices 
        if state == 12:
            # everybody checked
            if position == 0:
                self.decrement(self.pl2, 0, shown_cards[1], amount)
                self.decrement(self.pl3, 0, shown_cards[2], amount)                
            if position == 1:
                self.decrement(self.pl1, 0, shown_cards[0], amount)
                self.decrement(self.pl3, 0, shown_cards[2], amount)
            if position == 2:
                self.decrement(self.pl1, 0, shown_cards[0], amount)
                self.decrement(self.pl2, 0, shown_cards[1], amount)
        elif state == 21:
            if position == 0:
                self.decrement(self.pl2, 0, shown_cards[1], amount)
                self.increment(self.pl3, 0, shown_cards[2], amount)  
                self.increment(self.pl2, 2, shown_cards[1], amount)
            elif position == 1:
                self.increment(self.pl3, 0, shown_cards[2], amount)
            elif position == 2:
                self.decrement(self.pl2, 0, shown_cards[1], amount)
                self.increment(self.pl2, 2, shown_cards[1], amount)
        elif state == 18:
            if position == 0:
                self.increment(self.pl3, 0, shown_cards[2], amount)  
            elif position == 1:
                self.decrement(self.pl1, 0, shown_cards[0], amount)
                self.increment(self.pl3, 0, shown_cards[2], amount)
                self.increment(self.pl1, 1, shown_cards[0], amount)
            elif position == 2:
                self.decrement(self.pl1, 0, shown_cards[0], amount)
                self.decrement(self.pl1, 1, shown_cards[0], amount)
        elif state == 24:
            if position == 0:
                self.decrement(self.pl2, 0, shown_cards[1], amount)  
                self.increment(self.pl3, 0, shown_cards[2], amount)  
                self.increment(self.pl2, 3, shown_cards[1], amount)                  
            elif position == 1:
                self.decrement(self.pl1, 0, shown_cards[0], amount)
                self.increment(self.pl3, 0, shown_cards[2], amount)
                self.increment(self.pl1, 1, shown_cards[0], amount)
            elif position == 2:
                self.decrement(self.pl1, 0, shown_cards[0], amount)
                self.decrement(self.pl2, 0, shown_cards[1], amount)                  
                self.increment(self.pl1, 1, shown_cards[0], amount)
                self.increment(self.pl2, 3, shown_cards[1], amount)
        elif state == 20:
            if position == 0:
                self.increment(self.pl2, 0, shown_cards[1], amount)
            elif position == 1:
                self.decrement(self.pl1, 0, shown_cards[0], amount)
                self.increment(self.pl1, 2, shown_cards[0], amount)
            elif position == 2:
                self.decrement(self.pl1, 0, shown_cards[0], amount)
                self.increment(self.pl1, 2, shown_cards[0], amount)
                self.increment(self.pl2, 0, shown_cards[1], amount)                
        elif state == 17:
            if position == 0:
                self.increment(self.pl2, 0, shown_cards[0], amount)
                self.increment(self.pl3, 1, shown_cards[2], amount)
            elif position == 1:
                self.increment(self.pl3, 1, shown_cards[2], amount)
            elif position == 2:
                self.increment(self.pl2, 0, shown_cards[0], amount)
        elif state == 23:
            if position == 0:
                self.increment(self.pl2, 0, shown_cards[1], amount)
                self.increment(self.pl3, 1, shown_cards[2], amount)
            elif position == 1:
                self.decrement(self.pl1, 0, shown_cards[0], amount)
                self.increment(self.pl3, 1, shown_cards[2], amount)
                self.increment(self.pl1, 3, shown_cards[0], amount)    
            elif position == 2:
                self.decrement(self.pl1, 0, shown_cards[0], amount)
                self.increment(self.pl2, 0, shown_cards[1], amount)
                self.increment(self.pl1, 3, shown_cards[0], amount)                    
        elif state == 19:
            if position == 0:
                self.increment(self.pl3, 2, shown_cards[2], amount)
            elif position == 1:
                self.increment(self.pl1, 0, shown_cards[0], amount)
                self.increment(self.pl3, 2, shown_cards[2], amount)
            elif position == 2:
                self.increment(self.pl1, 0, shown_cards[0], amount)
        elif state == 16:
            if position == 0:
                self.increment(self.pl2, 1, shown_cards[1], amount)
            elif position == 1:
                self.increment(self.pl1, 0, shown_cards[0], amount)
            elif position == 2:
                self.increment(self.pl2, 1, shown_cards[1], amount)
                self.increment(self.pl1, 0, shown_cards[0], amount)
        elif state == 22:
            if position == 0:
                self.increment(self.pl2, 1, shown_cards[1], amount)
                self.increment(self.pl3, 3, shown_cards[2], amount)
            elif position == 1:
                self.increment(self.pl1, 0, shown_cards[0], amount)
                self.increment(self.pl3, 3, shown_cards[2], amount)
            elif position == 2:
                self.increment(self.pl2, 1, shown_cards[1], amount)
                self.increment(self.pl3, 3, shown_cards[2], amount)           

    def increment(self, matrix, node, card, amount):
        if card == None:
            return
        matrix[node][card] += amount
        if matrix[node][card] > 1:
            matrix[node][card] = 1
                
    def decrement(self, matrix, node, card, amount):
        if card == None:
            return
        matrix[node][card] -= amount
        if matrix[node][card] < 0:
            matrix[node][card] = 0
        
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
            self.p1 = 0
        else:
            self.p1 = 1
        
        if c < _c:
            self.p2 = 0
        else:
            self.p2 = 1
            
        if d < _d:
            self.p3 = 0
        else:
            self.p3 = 1
            
        g = b*self.p1 + _b*(1-self.p1) + c*self.p2 + _c*(1-self.p2) + d*self.p3 + _d*(1-self.p3) + e
        
        if a < g:
            p0 = 0
        else:
            p0 = 1
        
        return p0
    
    def p1node1(self, card):
        return self.p1
    
    def p1node2(self, card):
        return self.p2
            
    def p1node3(self, card):
        return self.p3
    
    def p2node0(self, card):
        # f = aq0 + (1-q0)(bq2 + _b(1-q2) + cq3 + _c(1-q3) + d)
        # to maximise this, find q2, q3 by comparing b and b', c and c'
        # now can compare a and coefficient of (1-pq) - call this e
        a = 0
        b = 0
        _b = 0
        c = 0
        _c = 0
        d = 0
        for x in range (deck.num_cards()): 
            # player 1 cards
            for y in range(deck.num_cards()):
                # player 3 cards
                if x != y and x != card and y != card:
                    a += (1/6)*(1-self.pl1[0][x])*((1-self.pl3[1][y])*(1-self.pl1[2][x])*self.payoff(card, -1, -1, 4) + (1-self.pl3[1][y])*self.pl1[2][x]*self.payoff(card, x, -1, 5) + self.pl3[1][y]*(1-self.pl1[3][x])*self.payoff(card, -1, y, 5) + self.pl3[1][y]*self.pl1[3][x]*self.payoff(card, x, y, 6))
                    b += (1/6)*(1-self.pl1[0][x])*self.pl3[0][y]*(1-self.pl1[1][x])*self.payoff(card, -1, y, 5)
                    _b += (1/6)*(1-self.pl1[0][x])*self.pl3[0][y]*(1-self.pl1[1][x])*self.payoff(-1, -1, y, 4)
                    c += (1/6)*(1-self.pl1[0][x])*self.pl3[0][y]*self.pl1[1][x]*self.payoff(card, x, y, 6)
                    _c += (1/6)*(1-self.pl1[0][x])*self.pl3[0][y]*self.pl1[1][x]*self.payoff(-1, x, y, 5)
                    d += (1/6)*(1-self.pl1[0][x])*(1-self.pl3[0][y])*self.payoff(card, x, y, 3)
        if b < _b:
            self.q2 = 0
        else:
            self.q2 = 1
        
        if c < _c:
            self.q3 = 0
        else:
            self.q3 = 1
            
        e = b*self.q2 + _b*(1-self.q2) + c*self.q3 + _c*(1-self.q3) + d
        
        if a < e:
            q0= 0
        else:
            q0 = 1
        
        return q0
    
    def p2node1(self, card):
        a = 0
        _a = 0
        for x in range (deck.num_cards()): 
            # player 1 cards
            for y in range(deck.num_cards()):
                # player 3 cards
                if x != y and x != card and y != card:
                    a += (1/6)*self.pl1[0][x]*((1-self.pl3[3][y])*self.payoff(card, x, -1, 5) + self.pl3[3][y]*self.payoff(card, x, y, 6))
                    _a += (1/6)*self.pl1[0][x]*((1-self.pl3[2][y])*self.payoff(-1, x, -1, 4) + self.pl3[2][y]*self.payoff(-1, x, y, 5))
        
        if a < _a:
            q1 = 0
        else:
            q1 = 1
            
        return q1
    
    def p2node2(self, card):
        return self.q2
            
    def p2node3(self, card):
        return self.q3
    
    def p3node0(self, card):
        a = 0
        _a = 0
        for x in range (deck.num_cards()): 
            # player 1 cards
            for y in range(deck.num_cards()):
                # player 3 cards
                if x != y and x != card and y != card:
                    a += (1/6)*(1-self.pl1[0][x])*(1-self.pl2[0][y])*((1-self.pl1[1][x])*(1-self.pl2[2][y])*self.payoff(card, -1, -1, 4) + (1-self.pl1[1][x])*self.pl2[2][y]*self.payoff(card, -1, y, 5) + self.pl1[1][x]*(1-self.pl2[3][y])*self.payoff(card, x, -1, 5) + self.pl1[1][x]*self.pl2[3][y]*self.payoff(card, x, y, 6))
                    _a += (1/6)*(1-self.pl1[0][x])*(1-self.pl2[0][y])*self.payoff(card, x, y, 3)
        
        if a < _a:
            r0 = 0
        else:
            r0 = 1
            
        return r0
    
    def p3node1(self, card):
        a = 0
        _a = 0
        for x in range (deck.num_cards()): 
            # player 1 cards
            for y in range(deck.num_cards()):
                # player 3 cards
                if x != y and x != card and y != card:
                    a += (1/6)*(1-self.pl1[0][x])*(self.pl2[0][y])*((1-self.pl1[3][x])*self.payoff(card, -1, y, 5) + self.pl1[3][x]*self.payoff(card, x, y, 6))
                    _a += (1/6)*(1-self.pl1[0][x])*(self.pl2[0][y])*((1-self.pl1[2][x])*self.payoff(-1, -1, y, 4) + self.pl1[2][x]*self.payoff(-1, x, y, 5))
        if a < _a:
            r1 = 0
        else:
            r1 = 1
            
        return r1
    
    def p3node2(self, card):
        a = 0
        _a = 0
        for x in range (deck.num_cards()): 
            # player 1 cards
            for y in range(deck.num_cards()):
                # player 3 cards
                if x != y and x != card and y != card:
                    a += (1/6)*self.pl1[0][x]*(1-self.pl2[1][y])*self.payoff(card, x, -1, 5)
                    _a += (1/6)*self.pl1[0][x]*(1-self.pl2[1][y])*self.payoff(-1, x, -1, 4)

        if a < _a:
            r2 = 0
        else:
            r2 = 1
            
        return r2
    
    def p3node3(self, card):
        a = 0
        _a = 0
        for x in range (deck.num_cards()): 
            # player 1 cards
            for y in range(deck.num_cards()):
                # player 3 cards
                if x != y and x != card and y != card:
                    a += (1/6)*self.pl1[0][x]*self.pl2[1][y]*self.payoff(card, x, y, 6)
                    _a += (1/6)*self.pl1[0][x]*self.pl2[1][y]*self.payoff(-1, x, y, 5)

        if a < _a:
            r3 = 0
        else:
            r3 = 1
            
        return r3
            
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
    def __str__(self):
        return 'Individual'
