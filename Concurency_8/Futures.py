import concurrent.futures

def task(n):
    return n * n

# Используем ThreadPoolExecutor для выполнения задач
with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(task, 5)  # Future представляет задачу
    print(future.result())  # Получаем результат, когда задача завершена
