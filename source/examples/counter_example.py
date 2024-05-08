class Counter:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.count = 0
        return cls._instance

    def increment(self):
        self.count += 1
        return self.count

    def decrement(self):
        self.count -= 1
        return self.count

    # @property
    # def count(self):
    #     return self.count

    def __str__(self):
        return str(self.count)


class Counter2:
    count = 0.0
    count_step = 0.2

    def update(self):
        self.count += self.count_step

    def __repr__(self):
        return f"Counter2({self.count}, {self.count_step})"


c1 = Counter()
c2 = Counter()

c1.increment()

print(c1, c2)

