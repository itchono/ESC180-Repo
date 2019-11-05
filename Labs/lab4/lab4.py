import utilities

def parse_story(file_name):
    '''
    (str) -> list<str>

    parse_story takes in a filename, file_name, 
    and returns the text in the file as an ordered list, with bad characters removed.

    >>> parse_story('test_text_parsing.txt')
    ['the', 'code', 'should', 'handle', 'correctly', 'the',
    'following', ':', 'white', 'space', '.', 'sequences', 'of',
    'punctuation', 'marks', '?', '!', '!', 'periods', 'with',
    'or', 'without', 'spaces', ':', 'a', '.', '.', 'a', '.', 'a',
    "don't", 'worry', 'about', 'numbers', 'like', '1', '.', '5',
    'remove', 'capitalization']
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

    for i in range(len(counts)):
        probs[i] = counts[i]/tot
    return probs


if __name__ == "__main__":
    out_arr = parse_story('test_text_parsing.txt')
    sample = ['the', 'code', 'should', 'handle', 'correctly', 'the',
    'following', ':', 'white', 'space', '.', 'sequences', 'of',
    'punctuation', 'marks', '?', '!', '!', 'periods', 'with',
    'or', 'without', 'spaces', ':', 'a', '.', '.', 'a', '.', 'a',
    "don't", 'worry', 'about', 'numbers', 'like', '1', '.', '5',
    'remove', 'capitalization']
    print(out_arr == sample)
    print(get_prob_from_count([10, 20, 40, 30]))

