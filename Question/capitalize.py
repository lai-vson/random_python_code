# You are asked to ensure that the first and last names of people begin with a capital letter in their passports

# Complete the solve function below.
def solve(s):
    for x in s.split():
        s = s.replace(x, x.capitalize())
    return s

if __name__ == '__main__':

    s = input()
    result = solve(s)
    print(result)

