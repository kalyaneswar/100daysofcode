# Prime numbers are numbers that can only be cleanly divided by themselves and 1
# NOTE: 2 is a prime number because it's only divisible by 1 and itself, but 1 is not a prime number because it is only divisible by 1.

def is_prime(num):

    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


print(is_prime(11))

