import re
def get_matching_words():
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
    matches = []
    for word in words:
        if re.search(r'v', word):
            matches.append(word)
    print matchev
        if re.search(r"ss",word):
            matches.append(word)
        elif re.search(r"\w*e\b", word):
            matches.append(word)
        elif re.search(r"\w*b\wb", word):
            matches.append(word)
        elif re.search(r"\w*b\w+b", word):
            matches.append(word)
        elif re.search(r"\w*b\w*b", word):
            matches.append(word)
        elif re.search(r"\w*a\w*e\w*i\w*o\w*u", word):
            matches.append(word)
        elif re.search(r")




get_matching_words()
