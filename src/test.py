import nltk

grammar = nltk.CFG.fromstring(
    """
    S -> NP VP
    NP -> Det N | Det Adj N
    VP -> V NP | V
    Det -> 'the' | 'a'
    Adj -> 'big' | 'small'
    N -> 'cat' | 'dog'
    V -> 'chases' | 'sleeps'
    """
)

parser = nltk.ChartParser(grammar)

sentence = ["the", "big", "cat", "chases", "a", "dog"]

for tree in parser.parse(sentence):
    tree.pretty_print()
