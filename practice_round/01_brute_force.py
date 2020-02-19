"""
Author: Nan <xnone0104@gmail.com>
Date: 17.02.2020

Version: 1.0

Brute Force method for solving example 1
"""
from itertools import combinations

file_names = [
              "a_example.in",
              "b_small.in",
              "c_medium.in",
              "d_quite_big.in",
              "e_also_big.in"
]

def main():
    # read line by line
    with open(file_names[0], 'r') as f:
        content = f.readlines()
    # remove '\n'
    content = [x.strip() for x in content]

    # get M and N
    m, n = [int(x) for x in content[0].split(" ")]
    assert 1 <= m <= 10e9
    assert 1 <= n <= 10e5

    # Get S0, S1, ..., Sn-1
    s_list = [int(x) for x in content[1].split(" ")]

    # list is ascending
    assert sorted(s_list) == s_list

    # last one less or equal than m
    assert s_list[-1] <= m

    # final output file
    line1 = -1
    line2 = []

    # assume at least 2 components
    assert max(s_list) + min(s_list) < m
    
    # check all combinations
    for i in reversed(range(2, n+1)):
        check_list = list(combinations(s_list, i))
        # print(check_list)

    # find max sum under m
    max_sum = 0
    max_list = []

    # check all combinations
    for i in reversed(range(2, n+1)):
        check_list = list(combinations(s_list, i))
        # print(check_list)
        for j in check_list:
            if sum(j) > max_sum and sum(j) < m:
                max_sum = sum(j)
                max_list = j

    # get output lines
    line1 = len(max_list)
    line2 = [s_list.index(x) for x in max_list]

    # write result
    with open('result.txt', 'w') as f:
        f.write(str(line1))
        f.write('\n')
        f.write(' '.join(map(str, line2)))

if __name__ == '__main__':
    main()
