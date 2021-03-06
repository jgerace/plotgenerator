from collections import OrderedDict

A_clauses = [
	"A Person in Love",
	"A Married Person",
	"A Lawless Person",
	"An Erring Person",
	"A Benevolent Person",
	"A Protecting Person",
	"A Person of Ideals",
	"A Person Influenced by an Obligation",
	"A Person Subjected to Adverse Conditions",
	"A Resentful Person",
	"A Person Swayed by Pretense",
	"A Subtle Person",
	"A Person Influenced by the Occult and the Mysterious",
	"A Normal Person",
	"Any Person",
]

B_clauses = {
	1: 'Engaging in a difficult enterprise when promised a reward for high achievement',
	2: 'Falling in love at a time when certain obligationa forbid love',
	3: 'Seeking to demonstrate the power of love by a test of courage',
	4: 'Being impelled by inordinate fancy to exercise mistaken judgment in a love affair',
	5: 'Becoming involved in a hopeless love affair, and seeking t9 make the best of a disheartening situation',
	6: 'Challenging, in a quest of love, the relentless truth that "East is East, and West is West, and never the twain shall meet"',
	7: 'Becoming involved in a love affair that encounters unforeseen obstacles',
	8: 'Confronting a situation in which wealth is made conditional upon a certain course of action in a love affair',
	9: 'Being put to a test in which love will be lost if more material fortunes are advanced',
	10: 'Suffering an estrangement due to mistaken judgment',
	11: 'Confronting a situation in which courage and devotion alone can save the fortunes of one beloved',
	12: 'Falling into misfortune through disloyalty in love',
	13: 'Seeking by craftiness to escape misfortune',
	14: 'Falling into misfortune through the wiles of a crafty schemer',
	15: 'Finding a sustaining power in misfortune',
	16: 'Being delivered from misfortune by one who, in confidence, confesses a secret of transgression',
	17: 'Bearing patiently with misfortunes and seeking to attain cherished aims honorably',
	18: 'Rebelling against a power that controls personal abilities and holds them in subjection',
	19: 'Meeting with misfortune and being cast away in a primitive, isolated and savage environment',
	20: 'Becoming involved with conditions in which misfortune is indicated',
	21: 'Falling into misfortune through mistaken judgment',
	22: 'Following a wrong course through mistaken judgment',
	23: 'Becoming involved in a complication that has to do with mistaken judgment and suspicion',
	24: 'Becorning the victim of mistaken judg- ment in carrying out an enterprise',
	25: 'Seeking to save a person who is accused of transgression',
	26: 'Seeking secretly to preserve another from danger',
	27: "Refusing to betray another's secret and calmly facing persecution because of the refusal",
	28: 'Facing a situation in which the misfortunes of one greatly esteemed call for courage and sagacious enterprise',
	29: 'Aiding another to hide from the world a fateful secret',
	30: 'Enlisting whole-heartedly in the service of a needy unfortunate and conferring aid of the utmost value',
	31: 'Living a lonely, cheerless life and seeking companionship',
	32: 'Seeking to conceal identity because of a lofty idealism',
	33: 'Resisting secretly and from an honorable motive a mandate considered discreditable',
	34: 'Embarking upon an enterprise of insurrection in the hope of ameliorating certain evil conditions',
	35: 'Becoming involved in a complication that challenges the value of cherished ideals',
	36: 'Undergoing an experience that results in a remarkable character change',
	37: 'Seeking against difficulties to realize a cherished ideal',
	38: 'Committing a grievous mistake and seeking in secret to live down its evil results',
	39: 'Forsaking cherished ambitions to carry out an obligation',
	40: 'Embarking upon an enterprise in which one obligation is opposed by another obligation',
	41: 'Finding an obligation at variance with ambition, inclination or necessity',
	42: 'Falling into misiortune while seeking honorably to discharge an obligation',
	43: 'Seeking to overcome personal limitations in carrying out an enterprise',
	44: 'Seeking by unusual methods to conquer personal limitations',
	45: 'Seeking to forward an enterprise and encountering family sentiment as an obstacle',
	46: 'Seeking retaliation for a grievous wrong that is either real or fancied',
	47: 'Finding (apparently) an object greatly coveted, and obtaining (apparently) the object',
	48: 'Assuming the character of a criminal in a perfectly honest enterprise',
	49: 'Assuming a fictitious character when embarking upon a certain enterprise',
	50: 'Being impelled by an unusual motive to engage in crafty enterprise',
	51: 'Devising a clever and plausible delusion in order to forward certain ambitious plans',
	52: 'Encountering a would-be transgressor and seeking to prevent a transgression',
	53: 'Opposing the plans of a crafty schemer',
	54: 'Becoming involved in a puzzling complication that has to do with an object possessing mysterious powers',
	55: 'Becoming involved in a mysterious complication and seeking to make the utmost of a bizarre experience',
	56: 'Seeking to test the value of a mysterious communication and becoming involved in weird complexities',
	57: 'Seeking to unravel a puzzling complication',
	58: 'Engaging in an enterprise and then mysteriously disappearing',
	59: 'Engaging in an enterprise and becoming involved with the occuh and the fantastic',
	60: 'Becoming involved, through curiosity aroused by mystery, in a strange enterprise',
	61: 'Becoming aware of an important secret that calls for decisive action',
	62: 'Becoming involved in any sort of complication',
}

C_clauses = {
	1: 'Pays a grim penalty in an unfortunate undertaking',
	2: 'Emerges happily from a serious entanglement',
	3: 'Foils a guilty plotter and defeats a subtle plot',
	4: 'Undertakes a role that leads straight to catastrophe',
	5: 'Emerges from a trying ordeal with sorely garnered wisdom',
	6: 'Makes the supreme sacrifice in carrying out an undertaking',
	7: 'Reverses certain opinions when their fallacy is revealed',
	8: 'Achieves a spiritual victory',
	9: 'Achieves success and happiness in a hard undertaking',
	10: 'Meets with an experience whereby an error is corrected',
	11: 'Discovers the folly of trying to appear otherwise than as one is in reality',
	12: 'Rescues integrity from a serious entanglement',
	13: 'Comes finally to the blank wall of enigma',
	14: 'Achieves a complete and permanent character transformation',
	15: 'Meets any fate, good or evil',
}



MALE_CHARS = OrderedDict([
	('A', 'male protagonist'),
	('A-2', 'male friend of A'),
	('A-3', 'male rival or enemy of A'),
	('A-4', 'male stranger'),
	('A-5', 'male criminal'),
	('A-6', 'male officer of the law'),
	('A-7', 'male inferior, employee'),
	('A-8', 'male utility symbol'),
	('A-9', 'male superior, employer, one in authority'),
	('F-A', 'father of A'),
	('M-A', 'mother of A'),
	('BR-A', 'brother of A'),
	('SR-A', 'sister of A'),
	('SN-A', 'son of A'),
	('D-A', 'daughter of A'),
	('U-A', 'uncle of A'),
	('AU-A', 'aunt of A'),
	('CN-A', 'male cousin of A'),
	('NW-A', 'nephew of A'),
	('NC-A', 'niece of A'),
	('GF-A', 'grandfather of A'),
	('GM-A', 'grandmother of A'),
	('SF-A', 'stepfather of A'),
	('SM-A', 'stepmother of A'),
	('GCH-A', 'grandchild of A'),
	('AX', 'a mysterious male person or one of unusual character'),
	('CH', 'a child'),
	('X', 'an inanimate object, an object of mystery, an uncertain quantity'),
])

FEMALE_CHARS = OrderedDict([
	('B', 'female protagonist'),
	('B-2', 'female friend of B'),
	('B-3', 'female rival or enemy of B'),
	('B-4', 'female stranger'),
	('B-5', 'female criminal'),
	('B-6', 'female officer of the law'),
	('B-7', 'female inferior, employee'),
	('B-8', 'female utility symbol'),
	('B-9', 'female superior, employer, one in authority'),
	('F-B', 'father of B'),
	('M-B', 'mother of B'),
	('BR-B', 'brother of B'),
	('SR-B', 'sister of B'),
	('SN-B', 'son of B'),
	('D-B', 'daughter of B'),
	('U-B', 'uncle of B'),
	('AU-B', 'aunt of B'),
	('CN-B', 'female cousin of B'),
	('NW-B', 'nephew of B'),
	('NC-B', 'niece of B'),
	('GF-B', 'grandfather of B'),
	('GM-B', 'grandmother of B'),
	('SF-B', 'stepfather of B'),
	('SM-B', 'stepmother of B'),
	('GCH-B', 'grandchild of B'),
	('BX', 'a mysterious female person or one of unusual character'),
])
