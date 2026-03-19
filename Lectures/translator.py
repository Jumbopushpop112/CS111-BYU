def translate(sentence,dict):
    """ returns the corresponding word-for-word translation of SENTENCE using the words in DICT """
    # your code here
    new_sentence = sentence.split()
    new_string = ""
    for word in new_sentence:
        new_string += dict[word] + " "
    return new_string.strip()

def create_translator_dict(list_of_pairs):
    """ returns a dictionary created from a list of lists which each contain a pair of two words: 
        the first word is the source word and the second word is its translation
    """
    # your code here, using a dictionary comprehension
    return {pair[0]:pair[1] for pair in list_of_pairs}

my_dict = create_translator_dict([['this','esto'],['is','es'],['a','una'],['test','prueba']])
print(translate('this is a test',my_dict))   # "esto es una prueba"