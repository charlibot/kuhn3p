from kuhn3p import betting, deck, Player

class StateFindingMission(Player):
    
    def __init__(self):
        pass

    def start_hand(self, position, card):
        self.position = position

    def act(self, state, card):
        for x in range(25):
            if betting.can_bet(x):
                print 'can bet', x
            if betting.facing_bet(x):
                print 'facing bet', x
            if betting.facing_bet_call(x):
                print 'facing bet call', x
            if betting.facing_bet_fold(x):
                print 'facing bet fold', x
        
        
        return betting.CALL
        
        
    def end_hand(self, position, card, state, shown_cards):
        print 'position: ' + str(state) + ' ' + betting.to_string(state)
        print


