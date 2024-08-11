def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))
