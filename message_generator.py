from nltk import CFG
from nltk.parse.generate import generate, demo_grammar
import csv
import inflect
import en

p = inflect.engine()

table = []
present_verbs = []
past_verbs = []
singular_nouns = []
plural_nouns = []
names = []

with open('verbs.csv','rb') as csvreader:
	reader = csv.reader(csvreader, delimiter=',', quotechar='|')
	for row in reader:
		present_verbs.append((row[0], row[1]))
		past_verbs.append((row[2], row[3]))

with open('nouns.csv','rb') as csvreader:
	reader = csv.reader(csvreader, delimiter=',', quotechar='|')
	for row in reader:
		singular_nouns.append((row[0], row[1]))
		plural_nouns.append((p.plural(row[0]), row[1]))

with open('names.csv','rb') as csvreader:
	reader = csv.reader(csvreader, delimiter=' ', quotechar='|')
	for row in reader:
		names.append(row[0].lower())


def gen_grammar(verb, name, direct_object, count):
	try:
		verb = en.verb.present_participle(verb)
	except KeyError:
		return
	if verb != "":
		g1 ="""
		S -> W TR SUB V DO '?' | W TR SUB V '?' 
		W -> 'who' | 'what' | 'when' | 'where' | 'why' | 'how'
		TR -> 'is' | 'was'
		SUB -> PRO | '%s'
		PRO -> 'he' |'she'
		V -> '%s'
		DO -> '%s'
		"""%(name, verb, direct_object)
		grammar1 = CFG.fromstring(g1)
		for sentence in generate(grammar1, n=999):
			table.append((' '.join(sentence) , count))

def gen_grammar_plural(verb, name, direct_object, count):
	try:
		verb = en.verb.present_participle(verb)
	except KeyError:
		return
	if verb != "":
		g1 ="""
		S -> W TR SUB V DO '?' | W TR SUB V '?' 
		W -> 'who' | 'what' | 'when' | 'where' | 'why' | 'how'
		TR -> 'are' | 'were'
		SUB -> 'they' | 'you'
		V -> '%s'
		DO -> '%s'
		"""%(verb, direct_object)
		grammar1 = CFG.fromstring(g1)
		for sentence in generate(grammar1, n=999):
			table.append((' '.join(sentence) , count))

def gen_grammar2(verb, name, direct_object, count):
	g1 ="""
	S -> W TR SUB V DO'?' | W TR SUB V '?' 
	W -> 'who' | 'what' | 'when' | 'where' | 'why' | 'how'
	TR -> 'does' | 'did'
	SUB -> PRO | '%s'
	PRO -> 'he' | 'she'
	V -> '%s'
	DO -> 'the %s'
	"""%(name, verb, direct_object)
	grammar1 = CFG.fromstring(g1)
	for sentence in generate(grammar1, n=999):
		table.append((' '.join(sentence) , count))

def gen_grammar2_plural(verb, direct_object, count):
	g1 ="""
	S -> W TR SUB V DO'?' | W TR SUB V '?' 
	W -> 'who' | 'what' | 'when' | 'where' | 'why' | 'how'
	TR -> 'do' | 'will' | 'have'
	SUB -> PRO
	PRO -> 'they' | 'you'
	V -> '%s'
	DO -> 'the %s'
	"""%(verb)
	grammar1 = CFG.fromstring(g1)
	for sentence in generate(grammar1, n=999):
		table.append((' '.join(sentence) , count))

def gen_grammar3_past(verb, name, direct_object, count):
	g1 ="""
	S -> W TR SUB V '?' | W TR SUB V DO '?' 
	W -> 'who' | 'what' | 'when' | 'where' | 'why' | 'how'
	TR -> 'has'
	SUB -> PRO | '%s'
	PRO -> 'he' | 'she'
	V -> '%s'
	DO -> '%s'
	"""%(name, verb, direct_object)
	grammar1 = CFG.fromstring(g1)
	for sentence in generate(grammar1, n=999):
		table.append((' '.join(sentence) , count))

def gen_grammar3_past_plural(verb, direct_object, count):
	g1 ="""
	S -> W TR SUB V '?' | W TR SUB V DO '?' 
	W -> 'who' | 'what' | 'when' | 'where' | 'why' | 'how'
	TR -> 'have'
	SUB -> PRO
	PRO -> 'they' |'you'
	V -> '%s'
	DO -> '%s'
	"""%(verb, direct_object)
	grammar1 = CFG.fromstring(g1)
	for sentence in generate(grammar1, n=999):
		table.append((' '.join(sentence) , count))

for x in range(0,50):
	for y in range(0,50):
		for z in range(0,10):
			gen_grammar(present_verbs[x][0], names[z], singular_nouns[y][0], 10)
print len(table)