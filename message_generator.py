from nltk import CFG
from nltk.parse.generate import generate, demo_grammar

table = []



def gen_grammar(subject, verb, name, count):
	g1 ="""
	S -> W TR SUB '?'
	W -> 'who' | 'what' | 'when' | 'where' | 'why' | 'how'
	TR -> 'is' | 'was'
	SUB -> 'the %s' | '%s'
	"""%(subject, name)
	grammar1 = CFG.fromstring(g1)
	for sentence in generate(grammar1, n=20):
		table.append((' '.join(sentence) , count))

def gen_grammar_plural(subject, verb, name, count):
	g1 ="""
	S -> W TR SUB '?'
	W -> 'who' | 'what' | 'when' | 'where' | 'why' | 'how'
	TR -> 'are' | 'were'
	SUB -> 'the %s'
	"""%(subject, )
	grammar1 = CFG.fromstring(g1)
	for sentence in generate(grammar1, n=20):
		print ' '.join(sentence)

def gen_grammar2(subject, verb, name, count):
	g1 ="""
	S -> W TR SUB V '?'
	W -> 'who' | 'what' | 'when' | 'where' | 'why' | 'how'
	TR -> 'does' | 'did'
	SUB -> 'the %s' | '%s'
	V -> '%s'
	"""%(subject, name, verb)
	grammar1 = CFG.fromstring(g1)
	for sentence in generate(grammar1, n=20):
		print ' '.join(sentence)

def gen_grammar2_plural(subject, verb, count):
	g1 ="""
	S -> W A SUB V '?'
	W -> 'who' | 'what' | 'when' | 'where' | 'why' | 'how'
	TR -> 'do' | 'will' | 'have'
	A -> TR | TR PRE
	PRE -> 'the'
	SUB -> '%s'
	V -> '%s'
	"""%(subject, verb)
	grammar1 = CFG.fromstring(g1)
	for sentence in generate(grammar1, n=20):
		print ' '.join(sentence)

def gen_grammar3_past(subject, verb, name, count):
	g1 ="""
	S -> W TR SUB V '?'
	W -> 'who' | 'what' | 'when' | 'where' | 'why' | 'how'
	TR -> 'has'
	SUB -> 'the %s' | '%s'
	V -> '%s'
	"""%(subject, name, verb)
	grammar1 = CFG.fromstring(g1)
	for sentence in generate(grammar1, n=20):
		print ' '.join(sentence)

def gen_grammar3_past_plural(subject, verb, count):
	g1 ="""
	S -> W TR SUB V '?'
	W -> 'who' | 'what' | 'when' | 'where' | 'why' | 'how'
	TR -> 'have'
	SUB -> 'the %s' | '%s'
	V -> '%s'
	"""%(subject, subject, verb)
	grammar1 = CFG.fromstring(g1)
	for sentence in generate(grammar1, n=20):
		print ' '.join(sentence)

gen_grammar2_plural('bottles', 'run', 10)
