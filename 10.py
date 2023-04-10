# modules for reuse, get small files
# import module fibo -> variables and functions
#import fibo

## usually we use import onlt for the function we are going to use, otherwise it's cost us in memory

from fibo import fib as first_fib # import specific function call fib, in this way you don't overwrite
from avielfibo import fib as second_fib # import specific function, in this way you don't overwrite
first_fib(100)
second_fib(100)
