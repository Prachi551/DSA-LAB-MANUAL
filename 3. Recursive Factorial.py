# Experiment 3: Recursive Factorial + Call Stack Trace
# Algorithm
# If n is 0 or 1, return 1.
# Otherwise return n × factorial(n-1).
# Recurrence Relation
# T(n) = T(n-1) + 1
# Time Complexity
# O(n)
# Space Complexity
# O(n)
# (Because n recursive calls are stored in the call stack.)

def factorial(n):
    # Reject negative input
    if n < 0:
        return "Invalid Input! Factorial not defined for negative numbers."
    
    # Base Case
    if n == 0 or n == 1:
        return 1
    
    # Recursive Case
    return n * factorial(n - 1)



# Call Stack Trace Function

def factorial_trace(n):
    if n < 0:
        print("Invalid Input!")
        return
    
    print("Call Stack Trace:")
    
    # Manually showing stack calls
    for i in range(n, 0, -1):
        print(f"factorial({i}) calls factorial({i-1})")
    
    print("factorial(0) returns 1 (Base Case)")
    
    # Showing return values
    result = 1
    for i in range(1, n+1):
        result *= i
        print(f"Returning: {i}! = {result}")



# Main Execution

n = int(input("Enter a number: "))

result = factorial(n)

print("Factorial Result:", result)

factorial_trace(n)

print("Time Complexity: O(n)")
print("Reason: Function calls itself n times")
print("Space Complexity: O(n)")
print("Reason: n recursive calls stored in call stack")