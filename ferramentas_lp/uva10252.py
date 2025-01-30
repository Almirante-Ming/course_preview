import sys
input = sys.stdin.read
data = input().splitlines()

for i in range(0, len(data), 2):
    if i + 1 < len(data):
        a = data[i]
        b = data[i+1]
        
        freq_a = [0] * 26
        freq_b = [0] * 26
        
        for char in a:
            freq_a[ord(char) - ord('a')] += 1
        
        for char in b:
            freq_b[ord(char) - ord('a')] += 1
        
        result = []
        for j in range(26):
            common_count = min(freq_a[j], freq_b[j])
            result.extend([chr(j + ord('a'))] * common_count)
        
        print(''.join(result))