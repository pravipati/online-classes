#Using this as a scratch document for various discussion problems

#is_prime: returns True if n is a prime number and False otherwise

def is_prime(n):
    def prime_check(num):
        if num == 1:
            return True
        elif n % num == 0:
            return False
        else:
            return prime_check(num - 1)
    return prime_check(n-1)

#sum_primes_up_to sums up every prime up to and including n. Assume you have an is_prime predicate

def sum_primes_up_to(n):
    if n == 1:
        return 1
    elif is_prime(n):
        return n + sum_primes_up_to(n - 1)
    else:
        return sum_primes_up_to(n - 1)

# count_stair_ways: I can either take 1 or 2 steps each time and I want to go up a flight of stairs that has n steps. How many different ways can I go up this flight of stairs?

def count_stair_ways(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)
