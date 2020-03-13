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

        # only count pair (x,y), not (y,x)
        if number < complement and complement in occurrences:
            pair_counter += occurrences[number] * occurrences[complement]

        elif number == complement:
            pair_counter += (occurrences[number] * (occurrences[number] - 1))//2
    
    return pair_counter