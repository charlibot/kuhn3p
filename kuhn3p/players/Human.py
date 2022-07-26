from kuhn3p import betting, Player

class Human(Player):
	def __init__(self):
		pass
	
	def start_hand(self, position, card):
		print
		print 'Starting new hand. Human is in position: ' + str(position+1) + ' with card: ' + str(card)

	def act(self, state, card):
		print "Human's turn to act. Previous play: " + betting.to_nonterminal_string(state)
		while(True):			
			action = raw_input("Please input action (0 for check/fold and 1 for bet/call)")
			if action == '0':
				if state < 3:
					# options are check and bet
					return betting.CHECK
				else:
					return betting.FOLD
			elif action == '1':
				if state < 3:
					return betting.BET
				else:
					return betting.CALL
			else:
				print 'wrong input try again' 
			
	def end_hand(self, position, card, state, shown_cards):
		print 'Hand finished with play: ' + betting.to_string(state) + '. Shown cards are: ' + str(shown_cards)

	def __str__(self):
		return 'Human'
