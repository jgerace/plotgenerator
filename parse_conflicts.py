import argparse
import parse
import ujson


def get_subconflicts(lines, num_sub_conflicts):
    subconflicts = []

    start = 0
    for idx in xrange(num_sub_conflicts):
        # print "parsing subconflict!"
        subconflict = {
            'id': lines[start].rstrip(),
            'lead_ins': lines[start+1].rstrip(),
            'text': lines[start+2].rstrip(),
            'follow_ups': lines[start+3].rstrip()
        }
        # print subconflict
        subconflicts.append(subconflict)
        start += 4

    # print "start: ", start
    return subconflicts, start


def get_conflicts(lines, num_conflicts):
    conflicts = []

    start = 0
    for idx in xrange(num_conflicts):
        # print "parsing conflict idx ", idx
        # print "line: ", lines[start]
        # print "start idx: ", start
        conflict_id = int(lines[start])
        # print "conflict id: ", conflict_id
        num_sub_conflicts = int(lines[start+1])
        # print "num subconflicts: ", num_sub_conflicts
        subconflicts, advance = get_subconflicts(lines[start+2:], num_sub_conflicts)
        conflict = {
            "id": conflict_id,
            "subconflicts": subconflicts
        }
        start += advance + 2
        conflicts.append(conflict)

    return conflicts


def parse_action(action):
    lines = action.split('\n')
    lines = [l for l in lines if l != '']
    action_id = parse.search('({:d})', lines[0])[0]
    # print "action id: ", action_id
    num_conflicts = int(lines[1])
    # print "num conflicts: ", num_conflicts
    conflicts = get_conflicts(lines[2:], num_conflicts)
    action = {
        'id': action_id,
        'conflicts': conflicts
    }
    return action


def main(input_file):
    num_actions = 0
    actions = []
    with open(input_file, 'r') as fin:
        actions = fin.read().split('----------')

    conflicts = {}
    for action in actions:
        # print "parsing action!!!!"
        obj = parse_action(action)
        action_id = obj['id']
        if not conflicts.get(action_id):
            conflicts[action_id] = []
            conflicts[action_id] = obj
        else:
            conflicts[action_id]['conflicts'] += obj['conflicts']

    print conflicts

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse Plotto conflicts')
    parser.add_argument('--file', type=str, default='./test2.txt')
    args = parser.parse_args()
    main(args.file)