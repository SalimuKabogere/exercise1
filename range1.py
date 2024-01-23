# Write a Python program to test whether a number is within 100 of 1000 or 2000.

def diff(n):
    nearAthousand=((n-1000))<=100 or ((n-2000))<=100
    return nearAthousand
print(diff(300)) 
print(diff(50900))
print(diff(7000))
print(diff(700))