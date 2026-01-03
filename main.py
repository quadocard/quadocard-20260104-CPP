```python
def factorial(n):
      if n == 0:
                return 1
else:
        return n * factorial(n-1)

def is_prime(num):
      if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                      if num % i == 0:
                                    return False
                            return True

def even_odd_numbers(start, end):
      for i in range(start, end + 1):
                if i % 2 == 0:
                              print(f"{i} is even")
else:
            print(f"{i} is odd")

def main():
      print("Factorial of 5:", factorial(5))
    print("Is 7 prime?", is_prime(7))
    even_odd_numbers(1, 10)

if __name__ == "__main__":
      main()
```
