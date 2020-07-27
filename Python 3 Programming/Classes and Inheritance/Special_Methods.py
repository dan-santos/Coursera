class Fruit():
    # construtor
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # maneira como o objeto é printado (toString do java)
    def __str__(self):
        return self.name

    def sort_priority(self):
        return self.price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
print("-----sorted by price, referencing a class method-----")
for f in sorted(L, key=Fruit.sort_priority):
    print(f)

print("---- one more way to do the same thing-----")
for f in sorted(L, key=lambda x: x.sort_priority()):
    print(f)