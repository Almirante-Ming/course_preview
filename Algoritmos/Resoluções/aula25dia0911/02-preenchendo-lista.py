N = 5
nums = []

for i in range(N):
    num = int(input(f"Informe o {i + 1}º número: "))
    nums.append(num)

print("Você digitou os seguintes números:")
for i in range(N):
    print(nums[i], end=" ")
