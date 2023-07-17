if __name__ == '__main__':
    start = int(input("Введіть початкове число діапазону: "))
    end = int(input("Введіть кінцеве число діапазону: "))

    def is_prime(number):

        if number < 2:
            return False

        for i in range(2, int(number ** 0.5) + 1):

            if number % i == 0:
                return False

        return True

    def find_primes(start, end):

        primes = []

        for number in range(start, end + 1):

            if is_prime(number):
                primes.append(number)

        return primes
    prime_numbers = find_primes(start, end)

    print("Прості числа у заданому діапазоні:", prime_numbers)