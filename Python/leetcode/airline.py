from collections import defaultdict


class Solution:
    """
    @param N: the number of rows
    @param S: a list of reserved seats
    @return: An integer
    """

    def solution(self, N: int, S: str) -> int:
        # Write your code here.
        # for each row, can accomodate at most 2 4-person families, potential chances are
        # xB xC xD xE/xF xG xH xJ/xD xE/xF/xG, so just check which ones are taken
        potential_2_sol = [{'B', 'C', 'D', 'E'}, {'F', 'G', 'H', 'I'}]
        alternative_sol = {'D', 'E', 'F', 'G'}

        total_count = 0
        if not S:
            return 2 * N

        taken_seats = defaultdict(set)
        for seat in S.split():
            taken_seats[seat[:-1]].add(seat[-1])

        for i in range(1, N + 1):
            print(i)
            taken_seats_in_i = taken_seats.get(str(i), set())
            print(taken_seats_in_i)
            if not taken_seats_in_i:
                total_count += 2
                continue
            row_count = 0
            for sol in potential_2_sol:
                if not sol.intersection(taken_seats_in_i):
                    row_count += 1
                    print(sol)
            if row_count:
                total_count += row_count
                continue
            else:
                if not alternative_sol.intersection(taken_seats_in_i):
                    total_count += 1
                    print(sol)
                    continue

        return total_count


if __name__ == "__main__":
    S="1H 1E 2J 2C 3B 3F 4E 4I 5C 5D 6F 6G 7I 7A 8D 8H 9G 9J 10A 10B 11H 11E 12J 12C 13B 13F 14E 14I 15C 15D 16F 16G 17I 17A"
    N=17
    sol = Solution()
    print(sol.solution(N, S))