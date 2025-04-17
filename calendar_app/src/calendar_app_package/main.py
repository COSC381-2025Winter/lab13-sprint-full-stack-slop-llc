from .example import add_one # Relative import
def add_two(number):
    return add_one(number) + 1
if __name__ == "__main__":
    print(add_two(3))