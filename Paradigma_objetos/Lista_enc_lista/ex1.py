def nested_sum(t):
    return sum(sum(inner_list) for inner_list in t)

t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))
