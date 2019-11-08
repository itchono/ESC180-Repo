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
            
            # check to see where n-gram occurs in remaining list
            if ng_tuple == tuple(words[j:j+n]): # check if sequence is correct
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

    See above functions for more detail on each specifi sublayer

    >>> build_ngram_model(['the', 'child', 'will', 'the', 'child', 'can', 'the', 'child', 'will', 'the', 'child', 'may', 'go', 'home', '.'], 2)
    {('the', 'child'): [['will', 'can', 'may'], [0.5, 0.25, 0.25]], ('child', 'will'): [['the'], [1.0]], ('will', 'the'): [['child'], [1.0]], 
    ('child', 'can'): [['the'], [1.0]], ('can', 'the'): [['child'], [1.0]], ('child', 'may'): [['go'], [1.0]], ('may', 'go'): [['home'], [1.0]], ('go', 'home'): [['.'], [1.0]]}
    '''
    return probify_ngram_counts(prune_ngram_counts(build_ngram_counts(words, n), 15)) # combine functions

def gen_bot_list(ngram_model, seed, num_tokens=0):
    '''
    (dict<n-gram>, tuple<str>, int) -> list<str>

    gen_bot_list returns a randomly generated list of tokens beginning with the first three tokens of seed,
    and selecting all subsequent tokens using gen_next_token (utilities.py). 

    it is assumed that the seed size and gram size are the same.

    list is terminated once length reaches num_tokens, or if current ngram is not in the model, or the current ngram has no proceeding outputs.

    See spec doc for examples.
    '''
    result = []
    # initialize empty list

    if num_tokens < len(seed):
        for i in range(0, num_tokens):
            result.append(seed[i])
    else:
        result[0:len(seed)] = seed # populate with first N tokens

        n_len = 0 # length of each n-gram must be determined
        for k in ngram_model.keys():
            n_len = len(k) # length of key will be length of gram
        
        # use last n_len words of seed to generate next
        n_pos = 0 # position pointer for where to generate next n-gram (should always by zero given spec doc)
        # THIS IS MADE UNDER THE STRICT ASSUMPTION THAT SEED LENGTH WILL ALWAYS BE EQUAL TO N-GRAM LENGTH

        current_n = ['']*n_len
        for i in range(n_len):
            current_n[i] = result[i+n_pos]
        current_n = tuple(current_n)

        while len(result) < num_tokens and current_n in ngram_model.keys() and utilities.check_open_ngram(current_n, ngram_model):
        # take advantage of lazy evaluation to check conditions in sequence
        # validate all conditions to proceed
            result.append(utilities.gen_next_token(current_n, ngram_model))
            n_pos += 1 # advance pointer to next position to start generating next n-gram

            current_n = ['']*n_len
            for i in range(n_len):
                current_n[i] = result[i+n_pos]
            current_n = tuple(current_n)
            
    return result

def gen_bot_text(token_list, bad_author):
    '''
    (list<str>, bool) -> str

    gen_bot_text takes in a list of tokens and returns a string depending on the bool input
    if true: returns the list concatenated into a strin
    if false: processes it with grammar rules as per spec doc.

    See spec doc for examples.
    '''
    if bad_author:
        return ' '.join(token_list)
        # return raw spaced string
    else:
        cap_list = ['']*len(token_list)

        for i in range(len(token_list)):
            cap_list[i] = str(token_list[i]).capitalize() if str(token_list[i]).capitalize() in utilities.ALWAYS_CAPITALIZE else token_list[i]
            # capitalize if needed
        # now that we have properly capitalized list, we move onto the other grammar rules

        # begin with first letter captialized
        clean_list = []
        clean_list.append(str(cap_list[0]).capitalize())
        
        i = 1 # pointer for while loop
        while i < len(token_list):
            if cap_list[i-1] in utilities.END_OF_SENTENCE_PUNCTUATION:
                # case: end of sentence punctuation
                clean_list.append(str(cap_list[i]).capitalize()) # append next word as capital
                if not (cap_list[i] in utilities.VALID_PUNCTUATION):
                    i += 1
                else:
                    # special case: two points of punctuation directly after sentence start
                    clean_list.pop()
            if cap_list[i] in utilities.VALID_PUNCTUATION:
                # case: other punctuation
                temp = clean_list[-1] # last word element of current list
                clean_list.pop() # remove previous
                clean_list.append(str(temp) + str(cap_list[i])) # append without space
            else:
                clean_list.append(cap_list[i])
            i+=1
        return ' '.join(clean_list) # turn to string


def write_story(file_name, text, title, student_name, author, year):
    '''
    (str, str, str, str, str, number) -> None

    write_story writes a story to a file given output filename, input text string,
    parameters for publishing etc.

    Basically puts a string into a file container.
    '''
    
    with open(file_name, 'w') as file:
        # TITLE PAGE
        file.write('\n'*10) # 10 newline chars
        file.write(title + ': ' + str(year) + ', UNLEASHED\n')
        file.write(student_name + ', inspired by ' + author + '\n')
        file.write('Copyright year published (' + str(year) + '), publisher: EngSci press')
        file.write('\n'*17)

        # MAIN BODY

        # VARIABLE SETUP
        i = 0 # string pointer
        ch = 1 # chapter number

        lines = 0 # lines in current page
        pages = 0 # pages in current chapter
        chars = 0 # chars in line

        pgtot = 1 # total number of pages

        while i < len(text): # main loop controlling flow so long as string exists
            pages = 0
            while pages < 12 and i<len(text):
                if pages == 0:
                    # CHAPTER - write header
                    file.write('\nCHAPTER ' + str(ch) + '\n\n')
                    ch += 1
                    lines = 2
                else:
                    # otherwise just reset pointer and write blank line
                    lines = 0
                    file.write('\n')
                while lines < 28:
                    # page - max of 30 lines; 28 of text. 
                    chars = 0
                    # write main body
                    while chars < 90 and i<len(text):
                        # line
                        if text[i:].find(' ') > (90 - chars):
                            # end of line position
                            chars = 90 # skip to next line
                        else:
                            if text[i+1:].find(' ') >= (90 - chars) and text[i] == ' ':
                                # problem case: space followed by word which would spill over to the next line
                                chars = 90
                                # skip to next line
                            elif not (chars == 0 and text[i] == ' '):
                                # do not write space at beginning of line
                                file.write(text[i])
                                chars += 1
                            i += 1 # advance pointer   

                    file.write('\n')
                    lines += 1                    
                # when done
                # write page bottom
                file.write('\n' + str(pgtot))

                #increment vars
                pages += 1
                pgtot += 1
        # DONE

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

    # n_gram_model = build_ngram_model(['the', 'child', 'will', 'the', 'child', 'can', 'the','child', 'will', 'the', 'child', 'may', 'go', 'home', '.'], 2)

    # print(n_gram_model)
    n_gram_model = {('the', 'child'): [['will', 'can','may'],
    [0.5, 0.25, 0.25]], \
    ('child', 'will'): [['the'], [1.0]], \
    ('will', 'the'): [['child'], [1.0]], \
    ('can', 'the'): [['child'], [1.0]], \
    ('child', 'may'): [['go'], [1.0]], \
    ('may', 'go'): [['home'], [1.0]], \
    ('go', 'home'): [['.'], [1.0]]}

    utilities.random.seed(10)

    print(gen_bot_list(n_gram_model, ('the', 'child'), 5))
    print(gen_bot_list(n_gram_model, ('the', 'child'), 5))

    print(gen_bot_text(['this', 'is', 'a', 'string', 'of', 'text','.', 'which', 'needs', 'to', 'be', 'created', '.','and', 'i', ',', '.', 'Giorno', 'Giovanna', 'have', 'a', 'piano', '.'], False))
    
    '''
    # Text generation test
    
    token_list = parse_story("308.txt")
    text = gen_bot_text(token_list, False)
    write_story('test_gen_bot_text_student.txt', text, 'Three Men in a Boat', 'Jerome K. Jerome', 'Jerome K. Jerome', 1889)


    # Write story test
    
    text = ' '.join(parse_story('308.txt'))
    write_story('test_write_story_student.txt', text, 'Three Men in a Boat', 'Jerome K. Jerome', 'Jerome K. Jerome', 1889)
    

    # fun test
    
    token_list = parse_story("18155.txt")
    print('building model...')
    n_gram_model = build_ngram_model(parse_story("18155.txt"), 2)
    print('generating words...')
    text = gen_bot_text(gen_bot_list(n_gram_model, ('there', 'was'), len(token_list)), False)
    print('making story...')
    write_story('three_pigs_test.txt', text, 'Three Men in a Boat', 'Jerome K. Jerome', 'Jerome K. Jerome', 1889)
    '''
    
