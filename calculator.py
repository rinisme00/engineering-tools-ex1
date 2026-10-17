CONTRIBUTORS = ["Minh", "Manh Duc NGUYEN"] # Conflicts generator 1

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a*b

def divide(a, b):
  if b == 0:
    raise ValueError("Cannot divide by zero.")
  return a/b

if __name__ == "__main__":
  print(f"Welcome to the Group Calculator!, written by {CONTRIBUTORS}")
  print(multiply(3, 4))
  print(divide(10, 2))
  print(add(2, 2))
  print(subtract(5, 3)) # Conflicts generator 2
