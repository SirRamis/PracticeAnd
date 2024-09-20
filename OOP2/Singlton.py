class Singleton:
    _instance = None  # Это будет хранить единственный экземпляр

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Использование
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # True, оба объекта ссылаются на один и тот же экземпляр
