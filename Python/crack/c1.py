#########################################################################
# File Name: c1.py
# Author: Jun M
# mail: warrior97@gmail.com
# Created Time: Tue 15 Dec 11:05:05 2015
#########################################################################
# !/usr/bin/env python
import os
import sys
import math
import random


def is_unique(s):
    # 1-1
    if not s:
        return True
    else:
        exist_chars = {}
        for char in list(s):
            if char.lower() in exist_chars.keys():
                return False
            else:
                exist_chars[char.lower()] = 1

        return True


def check_permutation(s1, s2):
    # 1-2
    if not s1 or not s2:
        return False
    else:
        tmp_s1 = str(sorted(list(s1)))
        tmp_s2 = str(sorted(list(s2)))
        if tmp_s1 == tmp_s2:
            return True
        else:
            return False


def urlify(url, length):
    # 1-3
    if not url:
        return
    else:
        outputUrl = url.replace("_", "")
        if len(outputUrl.strip()) > length:
            raise IOError("wrong length input\n")
        else:
            remain_blank = length - len(outputUrl.strip())
            outputUrl = outputUrl.strip().replace(" ", "%20")
            for i in xrange(remain_blank):
                outputUrl += "%20"

        return outputUrl


def palindrome(s):
    # 1-4
    if not s:
        return False
    else:
        tmp_s = s.replace("\w+", "").lower()
        length = len(tmp_s)
        for _ in xrange(len(tmp_s) / 2):
            if tmp_s[_] != tmp_s[length - 1 - _]:
                return False

        return True


def one_away(s1, s2):
    # 1-5
    if not s1 or not s2:
        return False
    else:
        difference = math.fabs(len(s1) - len(s2))
        if difference >= 2:
            return False
        elif difference == 0:
            diff_char_counter = 0
            for _ in xrange(len(s1)):
                if s1[_] != s2[_]:
                    diff_char_counter += 1

            return not (diff_char_counter > 1)
        else:
            # make sure s1 is longer, remember this way to assign values
            (s1, s2) = (s1, s2) if (len(s1) > len(s2)) else (s2, s1)
            if s1.find(s2) != -1:
                return True
            for _ in xrange(len(s2)):
                if s1[_] != s2[_]:
                    s1 = s1[:_] + s1[_ + 1:]
                    break

            return (s1 == s2)


def string_compression(s):
    # 1-6
    if not s:
        return False

    prev = s[0]
    counter = 0
    output = ""
    for char in s:
        if char != prev:
            output += prev + str(counter)
            counter = 1
            prev = char
        else:
            counter += 1

    output += char + str(counter)
    output = output if (len(output) < len(s)) else s
    return output


def rotate_matrix_brute(mat):
    # 1-7 brute force
    if not mat:
        return

    n = len(mat)
    output_matrix = [[0 for i in range(n)] for j in range(n)]

    for i in xrange(n):
        for j in xrange(n):
            output_matrix[j][n - 1 - i] = mat[i][j]

    return output_matrix


def rotate_matrix(mat):
    # 1-7 in space
    if not mat:
        return

    n = len(mat)
    for i in range((n + 1) / 2):
        for j in range(n / 2):
            _ = mat[n - j - 1][i]
            mat[n - j - 1][i] = mat[n - i - 1][n - j - 1]
            mat[n - i - 1][n - j - 1] = mat[j][n - i - 1]
            mat[j][n - i - 1] = mat[i][j]
            mat[i][j] = _

    return mat


def zero_matrix(mat):
    # 1-8
    if len(mat) == 0:
        return

    zero_rows = {}
    zero_cols = {}
    for x in xrange(len(mat)):
        for y in xrange(len(mat[0])):
            if mat[x][y] == 0:
                if x not in zero_rows.keys():
                    zero_rows[x] = 1
                if y not in zero_cols.keys():
                    zero_cols[y] = 1

    for _ in zero_cols.keys():
        for x in xrange(len(mat)):
            mat[x][_] = 0

    for _ in zero_rows.keys():
        for x in xrange(len(mat[0])):
            mat[_][x] = 0

    return mat


if __name__ == "__main__":
    # Test for 1-1
    # print is_unique("")
    # print is_unique("Happy")
    # print is_unique("have")

    # Test for 1-2
    # print check_permutation("catty", "datty")
    # print check_permutation("catty", "ycatt")

    # Test for 1-3
    # print urlify("Mr John Smith     ", 14)

    # Test for 1-4
    #    print palindrome("Tact coa")
    #    print palindrome("civic")
    #    print palindrome("ci v ic")

    # Test for 1-5
    # print one_away("pale", "ple")
    # print one_away("pales", "pale")
    # print one_away("pale", "bale")
    # print one_away("hihihi", "hohoho")

    # Test for 1-6
    # print string_compression("aabcccccaaa")
    # print string_compression("abcdefg")

    rows = 4
    columns = 4
    random_matrix = [[random.randint(-10, 10) for j in range(columns)]
                     for i in
                     range(rows)]
    for i in range(rows):
        print random_matrix[i]
    print "********************************"
    # Test for 1-7
    rotate_mat = rotate_matrix_brute(random_matrix)
    for i in range(rows):
        print rotate_mat[i]
    print "********************************"
    rotate_mat = rotate_matrix(random_matrix)
    for i in range(rows):
        print rotate_mat[i]

    # Test for 1-8, remember this way to generate a random matrix

    # zeroMat = zero_matrix(random_matrix)
    # for i in range(rows):
    #    print zeroMat[i]
