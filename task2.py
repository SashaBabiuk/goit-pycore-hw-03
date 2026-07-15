import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if min < 1:
        print("min must be >= 1")
        return []
    
    if max > 1000:
        print("max must be <= 1000")
        return []
    
    if min >= max:
        print("min must be < max")
        return []
    
    if quantity < 1:
        print("quantity must be >= 1")
        return []
    
    if quantity > (max - min + 1):
        print("quantity exceeds available numbers")
        return []
    
    return sorted(random.sample(range(min, max + 1), quantity))


print("1. Lottery 1-49, 6 numbers:")
print("Your lottery numbers:", get_numbers_ticket(1, 49, 6))
print()

print("2. Lottery 1-100, 10 numbers:")
print("Your lottery numbers:", get_numbers_ticket(1, 100, 10))
print()

print("3. Lottery 1-10, 5 numbers:")
print("Your lottery numbers:", get_numbers_ticket(1, 10, 5))
print()

print("4. Error - min < 1:")
print("Result:", get_numbers_ticket(0, 49, 6))
print()

print("5. Error - max > 1000:")
print("Result:", get_numbers_ticket(1, 1001, 6))
print()

print("6. Error - min >= max:")
print("Result:", get_numbers_ticket(50, 49, 6))
print()

print("7. Error - quantity < 1:")
print("Result:", get_numbers_ticket(1, 49, 0))
print()

print("8. Error - quantity > available numbers:")
print("Result:", get_numbers_ticket(1, 10, 15))
print()

print("9. Lottery 1-1000, 10 numbers:")
print("Your lottery numbers:", get_numbers_ticket(1, 1000, 10))
print()

print("10. Lottery 1-5, all 5 numbers:")
print("Your lottery numbers:", get_numbers_ticket(1, 5, 5))