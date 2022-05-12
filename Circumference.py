class solution:
    def initial(self, sets):
        return self.final(sets)

    def final(self, sets):
        return list(map(lambda x: ((x ** 3) % 2 == 0, x ** 3), sets))


print(solution().initial([4, 5, 6]))