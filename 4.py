
def is_palidrome(n):
    n = str(n)

    if n == n[::-1]:
        return True
    else:
        return False

print is_palidrome(100)
print is_palidrome(1001)
print is_palidrome(0)
print is_palidrome(34043)
