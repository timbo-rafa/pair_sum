from pair_sum import count_pairs
from collections import Counter

class Pair_Sum_Test:
    def basic_test(self):
        l = [1,2,2,2,4,5]
        sum = 6

        ans = count_pairs(l, sum)

        # (1,5)
        # (2,4)
        # (2,4)
        # (2,4)
        assert ans == 4

    def sequence_test(self):
        l = [n for n in range(10)]
        sum = 6

        ans = count_pairs(l, sum)

        # (0,6)
        # (1,5)
        # (2,4)
        print(ans)
        assert ans == 3
    
    def only_twos_and_fours_test(self):
        l = [2,2,2,4,4,4]
        sum = 6

        ans = count_pairs(l, sum)

        # first 2
        # (2,4)
        # (2,4)
        # (2,4)
        # second 2
        # (2,4)
        # (2,4)
        # (2,4)
        # third 2
        # (2,4)
        # (2,4)
        # (2,4)
        #
        # E.g. (2,4) for each 2 for each 4 = 3 * 3 = 9
        assert ans == 9

    def only_threes_test(self):
        l = [3,3,3,3]
        sum = 6

        ans = count_pairs(l, sum)

        # 3 pairs with first 3
        # (l[0],l[1])
        # (l[0],l[2])
        # (l[0],l[3])
        # 2 pairs with second 3
        # (l[1],l[2])
        # (l[1],l[3])
        # 1 pair with third and fourth 3
        # (l[2],l[3])
        # 3 + 2 + 1 = 6 pairs
        assert ans == 6

    def only_ones_should_return_zero_test(self):
        l = [1] * 10
        sum = 6

        ans = count_pairs(l, sum)

        assert ans == 0
    
    # Edge cases
    def empty_list_should_return_zero_test(self):
        ans = count_pairs([], 6)

        assert ans == 0

    def one_item_list_should_return_zero_test(self):
        ans = count_pairs([1], 6)

        assert ans == 0
