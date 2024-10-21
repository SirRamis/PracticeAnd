import concurrent.futures

def create_file(index):
    filename = f"file_{index}.txt"
    with open(filename, 'w') as f:
        f.write(f"This is file number {index}")
    print(f"Created: {filename}")

if __name__ == "__main__":
    # Используем пул потоков для параллельного создания файлов
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Создаем 10 файлов параллельно
        executor.map(create_file, range(1,11))
