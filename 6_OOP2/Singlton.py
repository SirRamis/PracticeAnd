class Singleton:
    _instance = None  # Это будет хранить единственный экземпляр

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            Singleton.do_s(Singleton._instance)
        return cls._instance
    def do_s(self):
        print('I done something')
        self.data = 101

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    Singleton.data = 102
    print(s1 is s2)  # True, оба объекта ссылаются на один и тот же экземпляр
    print(Singleton.data)


