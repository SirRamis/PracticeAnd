import multiprocessing
import time

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

def process_number(n):
    divisors = get_divisors(n)
    return divisors

if __name__ == "__main__":
    start_range = 1000
    end_range = 2000

    # Замеряем время выполнения
    start_time = time.time()

    # Используем пул процессов для параллельного выполнения
    with multiprocessing.Pool() as pool:
        results = pool.map(process_number, range(start_range, end_range + 1))

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")
