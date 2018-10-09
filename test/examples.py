# Figure 3.7 on page 117
GRAPH_3_7 = {
    'a': [('b', 2), ('c', 5), ('d', 7)],
    'b': [('a', 2), ('c', 8), ('d', 3)],
    'c': [('a', 5), ('b', 8), ('d', 1)],
    'd': [('a', 7), ('b', 3), ('c', 1)],
}


# Figure 3.10 on page 123
GRAPH_3_10 = {
    'a': ['c', 'd', 'e'],
    'b': ['e', 'f'],
    'c': ['a', 'd', 'f'],
    'd': ['a', 'c'],
    'e': ['a', 'b', 'f'],
    'f': ['b', 'c', 'e'],
    'g': ['h', 'j'],
    'h': ['i', 'g'],
    'i': ['h', 'j'],
    'j': ['i', 'g'],
}


# Figure 3.12a on page 127
GRAPH_3_12A = {
    'a': ['b', 'e'],
    'b': ['a', 'c', 'f'],
    'c': ['b', 'd', 'g'],
    'd': ['c', 'h'],
    'e': ['a', 'f'],
    'f': ['b', 'e', 'g'],
    'g': ['c', 'f', 'h'],
    'h': ['d', 'g'],
}


# Figure 3.12b on page 127
GRAPH_3_12B = {
    'a': ['b', 'e'],
    'b': ['a', 'c', 'f'],
    'c': ['b', 'd', 'g'],
    'd': ['c'],
    'e': ['a'],
    'f': ['b'],
    'g': ['c'],
}


# Figure 4.5 on page 139
GRAPH_4_5 = {
    'a': ['b', 'c'],
    'b': ['a', 'c'],
    'c': [],
    'd': ['c', 'e'],
    'e': [],
}


# Figure 4.6 on page 140
GRAPH_4_6 = {
    'C1': ['C3'],
    'C2': ['C3'],
    'C3': ['C4', 'C5'],
    'C4': ['C5'],
    'C5': [],
}


# Diagram (a) from problem 1 of exercises 4.2
GRAPH_4_2_EX_1A = {
    'a': ['b', 'c'],
    'b': ['e', 'g'],
    'c': ['f'],
    'd': ['a', 'b', 'c', 'f', 'g'],
    'e': [],
    'f': [],
    'g': ['e', 'f'],
}


# Diagram (b) from problem 1 of exercises 4.2
GRAPH_4_2_EX_1B = {
    'a': ['b'],
    'b': ['c'],
    'c': ['d'],
    'd': ['g'],
    'e': ['a'],
    'f': ['b', 'c', 'e', 'g'],
    'g': ['e'],
}


# Figure 9.3 on page 321
GRAPH_9_3 = {
    'a': [('b', 3), ('f', 5), ('e', 6)],
    'b': [('a', 3), ('c', 1), ('f', 4)],
    'c': [('b', 1), ('d', 6), ('f', 4)],
    'd': [('c', 6), ('e', 8), ('f', 5)],
    'e': [('a', 6), ('d', 8), ('f', 2)],
    'f': [('a', 5), ('b', 4), ('c', 4), ('d', 5), ('e', 8)],
}