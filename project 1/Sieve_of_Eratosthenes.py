from math import isqrt

def primer(n: int) -> list[int]:
    if n <= 2:
        return []

    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, isqrt(n) + 1):
        if is_prime[i]:
            print(f"\nStarting sieve {i}:")
            eliminated = []
            for x in range(i * i, n, i):
                if is_prime[x]:
                    eliminated.append(x)
                is_prime[x] = False
            print(f"Eliminated{i}: {eliminated}")

    print("\nFinal:")
    return [i for i in range(n) if is_prime[i]]

if __name__ == "__main__":
    data = input("Enter a Maximum number using the Sieve of Eratosthenes: ")
    data=int(data)
    print(primer(data))
