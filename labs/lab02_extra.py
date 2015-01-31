## Boolean Operators ##

# Q4
def gets_discount(x, y):
    """ Returns True if this is a combination of a senior citizen
    and a child, False otherwise.

    >>> gets_discount(65, 12)
    True
    >>> gets_discount(9, 70)
    True
    >>> gets_discount(40, 45)
    False
    >>> gets_discount(40, 75)
    False
    >>> gets_discount(65, 13)
    False
    >>> gets_discount(7, 9)
    False
    >>> gets_discount(73, 77)
    False
    >>> gets_discount(70, 31)
    False
    >>> gets_discount(10, 25)
    False
    """
    "*** YOUR CODE HERE ***"
    return (x <= 12 or y <= 12) and (x >= 65 or y >= 65)
    
# Q5
def is_factor(x, y):
    """ Returns True if x is a factor of y, False otherwise.

    >>> is_factor(3, 6)
    True
    >>> is_factor(4, 10)
    False
    >>> is_factor(0, 5)
    False
    >>> is_factor(0, 0)
    False
    """
    "*** YOUR CODE HERE ***"
    return not(x == 0) and (y % x == 0)


## while Loops ##

# Q10
def factors(n):
    """
    Prints out all of the numbers that divide `n` evenly.

    >>> factors(20)
    20
    10
    5
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    i = n
    while i > 0:
        if (n % i == 0):
            print(i)
        i -= 1

    
## Higher Order Functions ##

# Q13
def cycle(f1, f2, f3):
    """ Returns a function that is itself a higher order function
    >>> def add1(x):
    ...     return x + 1
    ...
    >>> def times2(x):
    ...     return x * 2
    ...
    >>> def add3(x):
    ...     return x + 3
    ...
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
def cycle(f1, f2, f3):
    fn_array = [f1, f2, f3]
    def iterator(n):
        def make_fun(x):
            i = 0
            result = x
            while i < n:
                result = fn_array[i % 3](result)
                i += 1
            return result
        return make_fun
    return iterator

