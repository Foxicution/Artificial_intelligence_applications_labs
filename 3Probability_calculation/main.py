from random import random


def read_txt(path):
    with open(path) as file:
        data = []
        lines = file.readlines()
        for line in lines:
            line = line.split()
            node_name = line.pop(0)
            parent_no = int(line.pop(0))
            parents = [int(x) for x in line[0:parent_no]]
            accuracies = [float(x) for x in line[parent_no:]]
            data.append((node_name, parent_no, parents, accuracies))
    return data


def decision(probability):
    return '1' if random() < probability else '0'


def create_conditional_vector(conditions, rules):
    conditional = []
    for rule in rules:
        if any(rule[0] in s for s in conditions):
            if '-' + rule[0] in conditions:
                conditional.append('0')
            else:
                conditional.append('1')
        else:
            conditional.append(None)
    return conditional


def read_console():
    node_to_find = input("Type the node who's probability you want to know: ")
    conditions = input("Type the nodes (e.g. A or -A) that are conditional: ").split()
    iteration_count = int(input("Type the number of iterations you want to simulate (more -> better results): "))
    return node_to_find, conditions, iteration_count


if __name__ == '__main__':
    network = read_txt('network.txt')
    print(network)
    find, when, iterations = read_console()
    # Program
    fnd = create_conditional_vector(find, network)
    cond = create_conditional_vector(when, network)
    table = []
    for a in range(iterations):
        row = []
        weight = 1
        for c, node in enumerate(network):
            prob_i = '0'
            for i in node[2]:
                prob_i += row[i]
            if cond[c] is None:
                row.append(decision(node[3][int(prob_i, 2)]))
            else:
                row.append(cond[c])
                weight *= node[3][int(prob_i, 2)] if cond[c] == '1' else (1 - node[3][int(prob_i, 2)])
        row.append(weight)
        table.append(row)
    numerator = 0
    denominator = 0
    index = None
    for i, member in enumerate(fnd):
        if member is not None:
            index = i
    for row in table:
        denominator += row[-1]
        if row[index] == fnd[index]:
            numerator += row[-1]
        print(row)
    likelihood = numerator / denominator
    print(likelihood)
