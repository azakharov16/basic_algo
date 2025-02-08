from itertools import chain, repeat
### Itertools tricks ###
# Chain of chains
c = chain('ABC', chain('DEF', [1, 2, 3]), chain('GH', (4, 5)))
print([*c])


def repeat_expand(ls, n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Argument n must be a positive integer")
    res = []
    for elem in sorted(ls):
        res += [*repeat(elem, n)]
    return res


def cycle_expand(ls, n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Argument n must be a positive integer")
    res = []
    for elem in sorted(ls):
        res += [elem for _ in range(n)]
    return res


### Basic algorithms ###
def binary_search(ls, elem):
    if ls != sorted(ls):
        raise ValueError("The array must be sorted")
    elif elem > max(ls) or elem < min(ls):
        return -1
    mid = len(ls) // 2
    if ls[mid] > elem:
        pos = binary_search(ls[:mid], elem)
    elif ls[mid] < elem:
        pos = mid + binary_search(ls[mid:], elem)
    elif ls[mid] == elem:
        pos = mid
    else:
        pos = -1
    return pos


def rep(val, n):
    return [val for _ in range(n)]


def expand(ls, n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Argument n must be a positive integer")
    if n == 1:
        res = ls
    else:
        res = [*ls, *expand(ls, n - 1)]
    return sorted(res)


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


a = [5, 1, 3, 6, 4, 2]
insertion_sort(a)


