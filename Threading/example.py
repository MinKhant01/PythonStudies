from multiprocessing import Pool
import math

def compute_factorial(n):
    return math.factorial(n)

if __name__ == '__main__':
    numbers = [500, 600, 700, 800]
    with Pool() as pool:
        pool.map(compute_factorial, numbers)
    print("Factorials completed.")