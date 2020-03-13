from collections import defaultdict

def count_pairs(l, sum):
    # dictionary counting how many times each number appears on the list
    # (same purpose as collection.Counter)
    occurrences = defaultdict(int)
    # O (n)
    for number in l:
        occurrences[number] += 1

    pair_counter = 0
    # O (n)
    for number in occurrences:
        complement = abs(number - sum)

        # complement has to be in input
        # and dont count pair (x,y) twice (e.g. (y,x))
        if complement in occurrences and number < complement:
            pair_counter += occurrences[number] * occurrences[complement]

        if number == complement:
            pair_counter += (occurrences[number] * (occurrences[number] - 1))//2
    
    return pair_counter