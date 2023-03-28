def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    if number == 1:
       return True
    return False
  # Recursive case: keep dividing number by base.
  return is_power_of(number/base, base)

print(is_power_of(1, 50))
