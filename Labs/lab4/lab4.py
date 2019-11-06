import utilities

def parse_story(file_name):
    '''
    (str) -> list<str>

    parse_story takes in a filename, file_name, 
    and returns the text in the file as an ordered list, with bad characters removed.

    >>> parse_story('test_text_parsing.txt')
    ['the', 'code', 'should', 'handle', 'correctly', 'the', 'following', ':', 'white', 'space', '.', 'sequences', 'of',
    'punctuation', 'marks', '?', '!', '!', 'periods', 'with', 'or', 'without', 'spaces', ':', 'a', '.', '.', 'a', '.', 'a',
    "don't", 'worry', 'about', 'numbers', 'like', '1', '.', '5', 'remove', 'capitalization']
    '''
    with open(file_name, 'r') as file:
        # this ensures file autocloses without damage

        data_str = file.read() # reads full file as a string
        clean_str = ''
        for i in range(0, len(data_str)):
            valid_p = data_str[i] in utilities.VALID_PUNCTUATION

            # only append if meets the conditions outlined in spec doc
            if (data_str[i].isalnum or valid_p) and not (data_str[i] in utilities.BAD_CHARS):
                
                clean_str += (' ' + data_str[i] + ' ') if valid_p else data_str[i]
                # adds spaces to clean punctuation between words if it's valid punctuation

        return clean_str.lower().split() # convert to list


def get_prob_from_count(counts):
    '''
    (list<number>) -> list<float>

    get_prob_from_count returns a list of probabilities derived from counts, where counts is a list of counts of occurrences of
    a token after the previous n-gram.

    >>> get_prob_from_count([10, 20, 40, 30])
    [0.1, 0.2, 0.4, 0.3]
    '''

    tot = sum(counts) # sum up number
    probs = [0] * len(counts)

    for i in range(0, len(counts)):
        probs[i] = counts[i]/tot
    return probs

def build_ngram_counts(words, n):
    '''
    (list<str>, int) -> dict

    build_ngram_counts returns a dictionary of n-grams and the counts of the words that follow the n-gram.
    The key will be the tuple containing words in a sequence.

    >>> build_ngram_counts(words, 2)
    returns dicts with keys of 2 words in sequence and 
    '''

    result = {} # empty dict

    # generate n-grams

    for i in range(0, len(words) - n):
        # main loop. used to define starting positions for each n-gram

        # no tokens proceed the 2nd-last n-gram, thus it does not need to be len(words) - n + 1.
        
        ng_list = [''] * n # prototype list for n-gram

        for j in range(i, i+n): # loop used to cycls through words for n-gram
            ng_list[j-i] = words[j] # puts word at position j into position 0, 1 ...n of the n-gram
        
        #n-gram is complete at this point
        ng_tuple = tuple(ng_list)
        result[ng_tuple] = [[],[]] # initialize count lists
        
        for j in range(0, len(words) - n):
            # secondary loop. checks where the previously found n-grams occur again
            seq = True

            # check to see where n-gram occurs in list
            pos = 0
            while True and pos < n:
                # use while loop to perform linear search of array for sequence
                if not words[j+pos] == ng_list[pos]:
                    seq = False
                pos += 1
                
            if seq:
                # if n-gram appears at position j, add next word after --> position j + n
                word = words[j+n]
                if word in result[ng_tuple][0]:
                    # if duplicate
                    # add 1 to occurrences
                    result[ng_tuple][1][result[ng_tuple][0].index(word)] += 1
                else:
                    # if first time
                    result[ng_tuple][0].append(word)
                    result[ng_tuple][1].append(1)
                    # create entries

    return result

def prune_ngram_counts(counts, prune_len):
    '''
    (dict, int) -> dict

    prune_ngram_counts takes in a n-grams-with-counts dict with the same format as build_ngram_counts, 
    and removes entries in counts with low frequency. it will keep the prune_len highest frequency words. 
    If there is a tie, it will keep all tied words.

    >>> prune_ngram_counts({('i', 'love'): [['js', 'py3', 'c', 'no'], [20, 20, 10, 2]], ('u', 'r'): [['cool', 'nice', 'lit', 'kind'], [8, 7, 5, 5]],
    ('toronto', 'is'): [['six', 'drake']], [2, 3]]}, 3)
    {('i', 'love'): [['js', 'py3', 'c'], [20, 20, 10]], ('u', 'r'): [['cool', 'nice', 'lit', 'kind'], [8, 7, 5, 5]], ('toronto', 'is'): [['six', 'drake'], [2, 3]]}
    '''
    result = {} # new empty dict for output

    for k in counts.keys():
        survivors = [[], []]
        # init new array of survivors that will replace current counts
        
        # get list of frequencies from max to min using reverse sort
        freqs = sorted(counts[k][1], reverse=True)

        n = len(counts[k][1]) if (len(counts[k][1]) < prune_len) else prune_len
        # adjust prune length to fit array

        for i in range(0, len(counts[k][1])):
            # takes the n most frequent elements, appends to survivors
            if counts[k][1][i] >= freqs[n-1]:
                survivors[0].append(counts[k][0][i])
                survivors[1].append(counts[k][1][i])

        result[k] = survivors

    return result 

def probify_ngram_counts(counts):
    '''
    (dict) -> dict

    probify_ngram_counts takes in a dict with the same output format as prune_ngram_counts, and converts the counts
    into probabilities.

    >>> probify_ngram_counts({('i', 'love'): [['js', 'py3', 'c'], [20, 20, 10]], ('u', 'r'): [['cool', 'nice', 'lit', 'kind'], [8, 7, 5, 5]], ('toronto', 'is'): [['six', 'drake'], [2, 3]]})
    {('i', 'love'): [['js', 'py3', 'c'], [0.4, 0.4, 0.2]], ('u', 'r'): [['cool', 'nice', 'lit', 'kind'], 
    [0.32, 0.28, 0.2, 0.2]], ('toronto', 'is'): [['six', 'drake'], [0.4, 0.6]]}
    '''
    result = {} # new empty dict for output

    for k in counts.keys():
        result[k] = [counts[k][0], get_prob_from_count(counts[k][1])]
        # use preexisting function to convert to probabilities
    return result

def build_ngram_model(words, n):
    '''
    (list<str>, int) -> dict

    build_ngram_model returns a dict representing an n-gram-count model, given a size of n-gram (n) and an input set of words (words).
    This will take the **15 most common words, and show each count as a probability.

    >>> build_ngram_model(['the', 'child', 'will', 'the', 'child', 'can', 'the', 'child', 'will', 'the', 'child', 'may', 'go', 'home', '.'], 2)

    '''
    return probify_ngram_counts(prune_ngram_counts(build_ngram_counts(words, n), 15))

def 

if __name__ == "__main__":

    '''
    out_arr = parse_story('test_text_parsing.txt')
    sample = ['the', 'code', 'should', 'handle', 'correctly', 'the', 'following', ':', 'white', 'space', '.', 'sequences', 'of',
    'punctuation', 'marks', '?', '!', '!', 'periods', 'with', 'or', 'without', 'spaces', ':', 'a', '.', '.', 'a', '.', 'a',
    "don't", 'worry', 'about', 'numbers', 'like', '1', '.', '5', 'remove', 'capitalization']
    print(out_arr == sample)
    print(get_prob_from_count([10, 20, 40, 30]))

    print(build_ngram_counts(['the', 'child', 'will', 'go', 'out', 'to', 'play',',', 'and', 'the', 'child', 'can', 'not', 'be', 'sad', 'anymore','.'], 
    2))

    pruned = prune_ngram_counts({('i', 'love'): [['js', 'py3', 'c', 'no'], [20, 20, 10, 2]], ('u', 'r'): [['cool', 'nice', 'lit', 'kind'], [8, 7, 5, 5]],
    ('toronto', 'is'): [['six', 'drake'], [2, 3]]}, 3)

    print(pruned)

    print(probify_ngram_counts(pruned))
    '''
    # prelim testing

    print(build_ngram_model(['the', 'child', 'will', 'the', 'child', 'can', 'the','child', 'will', 'the', 'child', 'may', 'go', 'home', '.'], 
    2))

