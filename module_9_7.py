def is_prime(func):
    def wrapper(*args):
        __sum = func(*args)
        count = 0
        for i in range(2, __sum + 1):
            if __sum % i == 0:
                count += 1
                print('Составное')
            else:
                print('Простое')
            return __sum

    return wrapper


@is_prime
def sum_three(a, b, c, ):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
