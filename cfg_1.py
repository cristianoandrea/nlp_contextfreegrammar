grammar_rules = {
    "S": [
        ["NP", "VP"],  # Declarative
        ["NP", "VP", "."],
        ["NP", "VP", "?"],
        ["VP"],  # Imperative
        ["VP", "."],
        ["Aux", "VP", "NP"],
        ["Wh-NP", "VP"],
        ["Wh-NP", "Aux", "NP", "VP"],
        ["SQ"],
        ["SBARQ"]
    ],
    "SQ": [
        ["MD", "NP", "VP", "."],
        ["VBD", "NP", "VP"]
    ],
    "SBARQ": [
        ["WHADVP", "SQ"]
    ],
    "NP": [
        ["NP", "VP"],
        ["DT", "JJ"],
        ["PRP"],
        ["JJ", "NNS"],
        ["PRP$", "NN"],
        ["NN"],
        ["NNS"],
        ["NNP"],
        ["PP"],
        ["PRP$", "JJ", "NN", "CC", "NN"],
        ["NP", "PP"],
        ["DT", "ADJP", "NN"],
        ["PRP"],
        ["DT", "NN"],
        ["JJ", "NN"]
    ],
    "VP": [
        ["VBD", "NP", "PP", "NP-TMP"],
        ["VB", "NP", "NP-TMP"],
        ["VBP", "NP"],
        ["VBP", "PP"],
        ["VBZ", "NP"],
        ["VB", "ADVP", "ADVP"],
        ["VBD", "ADVP", "PP"],
        ["VB", "RB", "VP"],
        ["VB", "PP"]
    ],
    "PP": [
        ["IN", "NN"],
        ["IN", "NP"],
        ["TO", "NP"]
    ],
    "NP-TMP": [
        ["NN"],
        ["DT", "NN"]
    ],
    "ADVP": [
        ["RB", "RB"],
        ["here"],
        ["lastly"]
    ],
    "VBD": [
        ["bought"], ["helped"], ["watched"], ["did"], ["was"]
    ],
    "VBP": [
        ["tell"]
    ],
    "VBZ": [
        ["is"]
    ],
    "VB": [
        ["come"], ["listen"], ["do"]
    ],
    "DT": [
        ["a"], ["the"], ["this"], ["every"]
    ],
    "JJ": [
        ["present"], ["historical"], ["national"], ["beautiful"], ["loud"]
    ],
    "PRP$": [
        ["my"], ["our"]
    ],
    "PRP": [
        ["enjoy"], ["you"]
    ],
    "RBS": [
        ["most"]
    ],
    "NN": [
        ["friend"], ["yesterday"], ["mother"], ["dinner"], ["culture"], ["history"], ["fruit"], 
        ["summer"], ["tonight"], ["village"], ["school"], ["music"]
    ],
    "NNS": [
        ["novels"], ["Epics"]
    ],
    "NNP": [
        ["Watermelon"]
    ],
    "IN": [
        ["with"], ["of"], ["from"]
    ],
    "CC": [
        ["and"]
    ],
    "MD": [
        ["Will"]
    ],
    "WRB": [
        ["when"]
    ],
    "TO": [
        ["to"]
    ],
    ".": [
        ["."],
        ["?"]
    ]
}