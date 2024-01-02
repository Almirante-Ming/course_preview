def calculate_sum_of_factorials(argument1, argument2):
    factorial1 = calculate_factorial(argument1)
    factorial2 = calculate_factorial(argument2)
    result = calculate_sum(factorial1, factorial2)
    return result


def calculate_factorial(argument):
    factorial_result = 1
    for i in range(1, argument + 1):
        factorial_result *= i
    return factorial_result


def calculate_sum(argument1, argument2):
    return argument1 + argument2


a = 5
b = 10
sum_of_factorials = calculate_sum_of_factorials(a, b)
print("The sum of factorials of the entered integers is", sum_of_factorials)
