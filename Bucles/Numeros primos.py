
def num_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(1, 51):
    if num_primo(num):
        print(num, end=", " if num < 50 else "")
