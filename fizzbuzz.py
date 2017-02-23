start = input("Start value: ")
end = input("End value: ")

def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return str(x)

for x in map(fizzbuzz, range(start,end+1)):
    print "{0:>8s}".format(x)
