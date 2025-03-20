def cumsum(t):
    cumulative_sum = []
    current_sum = 0
    
    for num in t:
        current_sum += num
        cumulative_sum.append(current_sum)
    
    return cumulative_sum

t = [1, 2, 3]
print(cumsum(t))
