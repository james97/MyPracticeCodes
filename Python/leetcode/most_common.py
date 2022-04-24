"""
##### 给定一个List<List<String>>, 找出和每个string同时出现次数最多的其他string或strings
input：[['Casper', 'Purple', 'Wayfair'], ['Purple', 'Wayfair', 'Tradesy'], ['Wayfair', 'Tradesy', 'Peloton']]
output:
* Casper: [Purple, wayfair]
* Purple: [Wayfair]
* Wayfair: [Purple, Tradesy]

"""
from collections import defaultdict
from typing import List


def get_most_occur(str1, strlists: List[List]) -> List:
    occ_count = defaultdict(int)
    for texts in strlists:
        if str1 not in texts:
            continue
        for t in texts:
            if t == str1:
                continue
            occ_count[t] += 1
    max_occ = max(list(occ_count.values()))
    return [k for k, v in occ_count.items() if v == max_occ]


if __name__ == "__main__":
    print(get_most_occur("Purple", [['Casper', 'Purple', 'Wayfair'], ['Purple', 'Wayfair', 'Tradesy'], ['Wayfair', 'Tradesy', 'Peloton']]))