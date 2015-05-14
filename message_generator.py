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

# with open('names.csv','rb') as csvreader:
# 	reader = csv.reader(csvreader, delimiter=' ', quotechar='|')
# 	for row in reader:
# 		names.append(row[0].lower())


def gen_grammar(verb, direct_object, count):
	try:
		verb = en.verb.present_participle(verb)
	except KeyError:
		return
	if verb != "":
		g1 ="""
		S -> WA TR SUB V DO '?' | W TR SUB V '?' 
		W -> 'who' | 'what' | 'when' | 'where' | 'why' | 'how'
		WA -> 'when' | 'where' | 'why' | 'how'
		TR -> 'is' | 'was'
		SUB -> PRO
		PRO -> 'he' |'she'
		V -> '%s'
		DO -> 'the %s'
		"""%(verb, direct_object)
		grammar1 = CFG.fromstring(g1)
		multiplier = 1
		with open('sentences.csv', 'ab') as csvwriter:
			writer = csv.writer(csvwriter)
			for sentence in generate(grammar1, n=999):
				sentence = ' '.join(sentence)
				if sentence.find('who') == 0:
					multiplier = 1
				if sentence.find('what') == 0:
					multiplier = 1
				if sentence.find('when') == 0:
					multiplier = 2
				if sentence.find('where') == 0:
					multiplier = 2
				if sentence.find('why') == 0:
					multiplier = 4
				if sentence.find('how') == 0:
					multiplier = 4
				writer.writerow((' '.join(sentence) , multiplier*count))

def gen_grammar_plural(verb, direct_object, count):
	try:
		verb = en.verb.present_participle(verb)
	except KeyError:
		return
	if verb != "":
		g1 ="""
		S -> WA TR SUB V DO '?' | W TR SUB V '?' 
		W -> 'who' | 'what' | 'when' | 'where' | 'why' | 'how'
		WA -> 'when' | 'where' | 'why' | 'how'
		TR -> 'are' | 'were'
		SUB -> 'they' | 'you'
		V -> '%s'
		DO -> 'the %s'
		"""%(verb, direct_object)
		grammar1 = CFG.fromstring(g1)
		multiplier = 1
		with open('sentences.csv', 'ab') as csvwriter:
			writer = csv.writer(csvwriter)
			for sentence in generate(grammar1, n=999):
				sentence = ' '.join(sentence)
				if sentence.find('who') == 0:
					multiplier = 1
				if sentence.find('what') == 0:
					multiplier = 1
				if sentence.find('when') == 0:
					multiplier = 2
				if sentence.find('where') == 0:
					multiplier = 2
				if sentence.find('why') == 0:
					multiplier = 4
				if sentence.find('how') == 0:
					multiplier = 4
				writer.writerow((' '.join(sentence) , multiplier*count))

def gen_grammar2(verb, direct_object, count):
	g1 ="""
	S -> WA TR SUB V DO'?' | W TR SUB V '?' 
	W -> 'who' | 'what' | 'when' | 'where' | 'why' | 'how'
	WA -> 'when' | 'where' | 'why' | 'how'
	TR -> 'does' | 'did'
	SUB -> PRO
	PRO -> 'he' | 'she'
	V -> '%s'
	DO -> 'the %s'
	"""%(verb, direct_object)
	grammar1 = CFG.fromstring(g1)
	multiplier = 1
	with open('sentences.csv', 'ab') as csvwriter:
		writer = csv.writer(csvwriter)
		for sentence in generate(grammar1, n=999):
			sentence = ' '.join(sentence)
			if sentence.find('who') == 0:
				multiplier = 1
			if sentence.find('what') == 0:
				multiplier = 1
			if sentence.find('when') == 0:
				multiplier = 2
			if sentence.find('where') == 0:
				multiplier = 2
			if sentence.find('why') == 0:
				multiplier = 4
			if sentence.find('how') == 0:
				multiplier = 4
			writer.writerow((' '.join(sentence) , multiplier*count))

def gen_grammar2_plural(verb, direct_object, count):
	g1 ="""
	S -> WA TR SUB V DO'?' | W TR SUB V '?' 
	W -> 'who' | 'what' | 'when' | 'where' | 'why' | 'how'
	WA -> 'when' | 'where' | 'why' | 'how'
	TR -> 'do' | 'will' | 'have'
	SUB -> PRO
	PRO -> 'they' | 'you'
	V -> '%s'
	DO -> 'the %s'
	"""%(verb, direct_object)
	grammar1 = CFG.fromstring(g1)
	multiplier = 1
	with open('sentences.csv', 'ab') as csvwriter:
		writer = csv.writer(csvwriter)
		for sentence in generate(grammar1, n=999):
			sentence = ' '.join(sentence)			
			if sentence.find('who') == 0:
				multiplier = 1
			if sentence.find('what') == 0:
				multiplier = 1
			if sentence.find('when') == 0:
				multiplier = 2
			if sentence.find('where') == 0:
				multiplier = 2
			if sentence.find('why') == 0:
				multiplier = 4
			if sentence.find('how') == 0:
				multiplier = 4
			writer.writerow((' '.join(sentence) , multiplier*count))

def gen_grammar3_past(verb, direct_object, count):
	g1 ="""
	S -> W TR SUB V '?' | WA TR SUB V DO '?' 
	W -> 'who' | 'what' | 'when' | 'where' | 'why' | 'how'
	WA -> 'when' | 'where' | 'why' | 'how'
	TR -> 'has'
	SUB -> PRO
	PRO -> 'he' | 'she'
	V -> '%s'
	DO -> 'the %s'
	"""%(verb, direct_object)
	grammar1 = CFG.fromstring(g1)
	multiplier = 1
	with open('sentences.csv', 'ab') as csvwriter:
		writer = csv.writer(csvwriter)
		for sentence in generate(grammar1, n=999):
			sentence = ' '.join(sentence)
			if sentence.find('who') == 0:
				multiplier = 1
			if sentence.find('what') == 0:
				multiplier = 1
			if sentence.find('when') == 0:
				multiplier = 2
			if sentence.find('where') == 0:
				multiplier = 2
			if sentence.find('why') == 0:
				multiplier = 4
			if sentence.find('how') == 0:
				multiplier = 4		
			writer.writerow((' '.join(sentence) , multiplier*count))

def gen_grammar3_past_plural(verb, direct_object, count):
	g1 ="""
	S -> W TR SUB V '?' | WA TR SUB V DO '?' 
	W -> 'who' | 'what' | 'when' | 'where' | 'why' | 'how'
	WA -> 'when' | 'where' | 'why' | 'how'
	TR -> 'have'
	SUB -> PRO
	PRO -> 'they' |'you'
	V -> '%s'
	DO -> 'the %s'
	"""%(verb, direct_object)
	grammar1 = CFG.fromstring(g1)
	multiplier = 0
	with open('sentences.csv', 'ab') as csvwriter:
		writer = csv.writer(csvwriter)
		for sentence in generate(grammar1, n=999):
			if sentence.find('who') == 0:
				multiplier = 1
			if sentence.find('what') == 0:
				multiplier = 1
			if sentence.find('when') == 0:
				multiplier = 2
			if sentence.find('where') == 0:
				multiplier = 2
			if sentence.find('why') == 0:
				multiplier = 4
			if sentence.find('how') == 0:
				multiplier = 4
			writer.writerow((' '.join(sentence) , multiplier*count))

for x in range(0,600):
	for y in range(0,300):
		gen_grammar(present_verbs[x][0], singular_nouns[y][0], int(present_verbs[x][1]) + int(singular_nouns[y][1]))
		gen_grammar_plural(present_verbs[x][0], plural_nouns[y][0], int(present_verbs[x][1]) + int(plural_nouns[y][1]))
		gen_grammar2(present_verbs[x][0], singular_nouns[y][0], int(present_verbs[x][1]) + int(singular_nouns[y][1]))
		gen_grammar2_plural(present_verbs[x][0], plural_nouns[y][0], int(present_verbs[x][1]) + int(plural_nouns[y][1]))
		gen_grammar3_past(past_verbs[x][0], singular_nouns[y][0], int(past_verbs[x][1]) + int(singular_nouns[y][1]))
		gen_grammar3_past(past_verbs[x][0], plural_nouns[y][0], int(past_verbs[x][1]) + int(plural_nouns[y][1]))
