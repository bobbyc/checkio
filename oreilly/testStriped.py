#([aeiouy]{1}[bcdfgjklmnpqrstvwxz]{1})+[aeiouy]?|([bcdfgjklmnpqrstvwxz]{1}[aeiouy]{1})+[bcdfgjklmnpqrstvwxz]?


def checkio(text):

    import re
	#replace this for solution
    lower = text.lower()
    tokens = re.split( r'\W', lower)
    match = [ x for x in tokens if re.search(r'^([aeiouy]{1}[bcdfghjklmnpqrstvwxz]{1})+[aeiouy]?$|^([bcdfghjklmnpqrstvwxz]{1}[aeiouy]{1})+[bcdfgjklmnpqrstvwxz]?$', x)]
    return len(match)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio("My name is ...") == 3, "bobby"
	assert checkio("Hello world") == 0, "Hey"
	assert checkio("A quantity of striped words.") == 1, "Only of"
	assert checkio("Dog,cat,mouse,bird.Human.") == 3, "hahah"
