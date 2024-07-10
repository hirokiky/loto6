import random


def quick_pick():
    numbers = random.sample(range(31, 44), 4)
    numbers_small = random.sample(range(1, 31), 2)
    return sorted(numbers + numbers_small)


def main():
    for _ in range(5):
        print(" / ".join(str(i) for i in quick_pick()))


if __name__ == "__main__":
    main()

