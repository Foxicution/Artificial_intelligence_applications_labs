def read_txt(path):
    with open(path) as file:
        data = []
        lines = file.readlines()
        for line in lines:
            line = line.rstrip('\n')
            data.append(set(line.split(' or ')))
        return data


def new_sentence_proc(sentence):
    # check if always true
    for character in sentence:
        if 'not' in character:
            tmp = character.replace('not', '')
            if tmp in sentence:
                return None
        else:
            tmp = 'not' + character
            if tmp in sentence:
                return None
    return sentence


def add_sentences(logic_base, parents):
    # Simplification done using sets
    for i, sentence in enumerate(logic_base): # naudot while (antras zemyn)
        #logic_base[i] = set(logic_base[i])
        for character in sentence:
            for n in range(0, i, 1): # ziuret i virsu
                #logic_base[n] = set(logic_base[n])
                if 'not' in character:
                    tmp = character.replace('not', '')
                else:
                    tmp = 'not' + character
                if tmp in logic_base[n]:
                    sentence1 = logic_base[i].copy()
                    sentence1.remove(character)
                    sentence2 = logic_base[n].copy()
                    sentence2.remove(tmp)
                    new_sentence = sentence1.union(sentence2)
                    new_sentence = new_sentence_proc(new_sentence)
                    # Check if not already in logic base
                    if new_sentence is not None and new_sentence not in logic_base:
                        # Check if weaker
                        if not any(sentence.issubset(new_sentence) for sentence in logic_base):
                            logic_base.append(new_sentence)
                            parents.append((i, n))
    return logic_base, parents


def write_to_file(logic_base, parents):
    with open('results.txt', 'w') as file:
        for i, sentence in enumerate(logic_base):
            line = ' or '.join(list(sentence))
            line = line + ' Parents:' + str(parents[i]) if parents[i] is not None else line
            file.write(line + '\n')


if __name__ == '__main__':
    initial_rules = read_txt('data/test6.txt')
    print(initial_rules)
    initial_parents = [None for x in initial_rules]
    new_logic_base, new_parents = add_sentences(initial_rules, initial_parents)
    print(new_logic_base)
    print(new_parents)
    write_to_file(new_logic_base, new_parents)
