cache = {}

def levenshtein(s1, s2):
    """
    Returns levenshtein distance between message and goal
    """

    if (s1, s2) in cache:
        return cache[s1, s2]
    if s1 == '':
        return(len(s2))
    if s2 == '':
        return(len(s1))

    if s1[-1] == s2[-1]:
        cost = 0
    else:
        cost = 1
    res =  min(levenshtein(s1[:-1], s2)+1,
               levenshtein(s1, s2[:-1])+1,
               levenshtein(s1[:-1], s2[:-1])+cost)
    cache [s1, s2] = res
    return res






if __name__ == '__main__':
    print(levenshtein('beta', 'pedal'))
