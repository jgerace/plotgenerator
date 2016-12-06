from flask import Flask, render_template
from random import randint
from conflicts import CONFLICTS
from plotto import *
import re
import ujson

app = Flask(__name__)

"""
Table: Protagonist (A)
	id
	description
	
Table: Action (B)
	id
	description
	
Table: Termination (C)
	id
	description
	
Table: Conflict
	pk
	id
	order_label - a, b, c, etc as in book
	action_id - FK in Action
	description

Table: LeadIn
	id
	conflict_id - FK in Conflict
	
Table: FollowUp
	id
	conflict_id - FK in Conflict


"""

SUBCONFLICTS_ONLY = []

for action in CONFLICTS.values():
	conflicts = action['conflicts']

	subconflicts = []
	for c in conflicts:
		subconflicts += c['subconflicts']
		for s in subconflicts:
			SUBCONFLICTS_ONLY.append(s['text'])


def _get_random_masterplot():
	A_choice = randint(0, 14)
	B_choice = randint(1, 62)
	C_choice = randint(1, 15)
	
	return (A_choice, B_choice, C_choice)


def _get_random_conflict():
	conflict_choice = randint(0, len(SUBCONFLICTS_ONLY)-1)
	temp = SUBCONFLICTS_ONLY[conflict_choice]
	temp_split = temp.split('*')
	for t in reversed(temp_split):
		if t != '':
			temp = t

	temp = re.sub(r'\([^)]*\)', '', temp.strip())
	return temp + '.'


@app.route('/terminations', methods=['GET'])
def terminations():
	return render_template('terminations.html', terminations=C_clauses)


@app.route('/actions', methods=['GET'])
def actions():
	return render_template('actions.html', actions=B_clauses)


@app.route('/characters', methods=['GET'])
def characters():
	try:
		return render_template('characters.html', characters=A_clauses)
	except Exception as e:
		print e


@app.route('/about', methods=['GET'])
def about():
	return render_template('about.html')


@app.route('/', methods=['GET'])
def index():
	A, B, C = _get_random_masterplot()
	conflict = _get_random_conflict()
	try:
		return render_template('index.html',
								character=A_clauses[A],
								action=B_clauses[B],
								termination=C_clauses[C],
								conflict=conflict,
								male_abbr=MALE_CHARS,
								female_abbr=FEMALE_CHARS)
	except Exception as e:
		print e
	
if __name__ == "__main__":
	try:
		app.run()
	except Exception as e:
		print e
