class ProductOfNumbers:

    def __init__(self):
        self.products = [1]

    def add(self, num: int) -> None:
        if num == 0: self.products = [1]
        else: self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        if len(self.products) <= k: return 0
        return self.products[-1] // self.products[-k-1]

if __name__ == '__main__':
    problem = ProductOfNumbers()
    print(problem.add(3))
    print(problem.add(0))
    print(problem.add(2))
    print(problem.add(5))
    print(problem.add(4))
    print(problem.getProduct(2))
    print(problem.getProduct(3))
    print(problem.getProduct(4))
    print(problem.add(8))
    print(problem.getProduct(2))