'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    target = "th"
    count = 0
    w = word.find(target)

    if w >=0:
        count += 1
        word = word[w +len(target):]
        count += count_th(word)
    return count
