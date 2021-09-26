def count_memo(string1, string2, p1, p2, cache):
    if p1 >= len(string1):
        return len(string2) - p2
    if p2 >= len(string2):
        return len(string1) - p1

    if cache[p1][p2] is not None:
        return cache[p1][p2]

    if string1[p1] == string2[p2]:
        # copy
        cache[p1][p2] = count_memo(string1, string2, p1 + 1, p2 + 1, cache)
    else:
        # replace
        replace = count_memo(string1, string2, p1 + 1, p2 + 1, cache) + 1

        # delete
        delete = count_memo(string1, string2, p1, p2 + 1, cache) + 1

        # insert
        insert = count_memo(string1, string2, p1 + 1, p2, cache) + 1

        cache[p1][p2] = min(insert, delete, replace)

    return cache[p1][p2]


def count_table(string1, string2):
    # create a table
    length1 = len(string1)
    length2 = len(string2)

    table = [[0 for _ in range(length2 + 1)] for _ in range(length1 + 1)]
    # fill up first row and first column
    for i in range(length1 + 1):
        table[i][0] = i
    for j in range(length2 + 1):
        table[0][j] = j

    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            if string1[i - 1] == string2[j - 1]:
                table[i][j] = min(table[i][j - 1] + 1, table[i - 1][j] + 1, table[i - 1][j - 1])
            else:
                table[i][j] = min(table[i][j - 1] + 1, table[i - 1][j] + 1, table[i - 1][j - 1] + 1)

    return table[length1][length2]


def edit_memo(string1, string2):
    if len(string1) == 0:
        return len(string2)
    if len(string2) == 0:
        return len(string1)
    # construct the table
    cache = [[None for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]
    return count_memo(string1, string2, 0, 0, cache)


def edit_table(string1, string2):
    if len(string1) == 0:
        return len(string2)
    if len(string2) == 0:
        return len(string1)
    return count_table(string1, string2)


def count_brute_force(string1, string2, p1, p2):
    if p1 >= len(string1):
        return len(string2) - p2
    if p2 >= len(string2):
        return len(string1) - p1

    if string1[p1] == string2[p2]:
        # copy
        return count_brute_force(string1, string2, p1 + 1, p2 + 1)
    else:
        # replace
        replace = count_brute_force(string1, string2, p1 + 1, p2 + 1) + 1

        # delete
        delete = count_brute_force(string1, string2, p1, p2 + 1) + 1

        # insert
        insert = count_brute_force(string1, string2, p1 + 1, p2) + 1

        return min(insert, delete, replace)


def edit_brute_force(string1, string2):
    if len(string1) == 0:
        return len(string2)
    if len(string2) == 0:
        return len(string1)
    return count_brute_force(string1, string2, 0, 0)


print(f"edit_brute_force: {edit_brute_force('paris', 'arid')}")
print(f"edit_memo: {edit_memo('paris', 'arid')}")
print(f"edit_table: {edit_table('paris', 'arid')}")
