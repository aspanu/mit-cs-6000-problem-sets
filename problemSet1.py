import math

def problem_1_solution():
    # Compute the 1000th prime number, most likely with a 'generate-and-test' method

    # Plan:
    # 1. Generate new odd numbers starting from 21
    # 2. 2, 3, 5, 7, 11, 13, 17, 19 are the previous prime numbers, so we will start at 8
    # 3. Generate a new number, check if it is prime, if it is, increase the "number of primes found" counter
    # 4. Stop when the counter gets to 1000

    number = 21
    numberOfPrimes = 8
    numberOfPrimesToStopAt = 1000

    while(numberOfPrimes <= numberOfPrimesToStopAt):
        number += 2
        if (isPrime(number)):
            # print(f"Number {number} is a prime!!!")
            numberOfPrimes += 1
 
    return number

def isPrime(number):
    # Check every integer up to sqrt(number) and see if it is perfectly divisible
    numberUpTo = math.sqrt(number)

    for i in range(2, math.floor(numberUpTo) + 1):
        if (number % i == 0):
            return False
    
    return True


print(problem_1_solution())

def problem_2_solution(endingNumber):
    # Compute sum of logarithms for primes from 2 to a number n


    currentNumber = 2
    sumOfPrimeLogs = math.log(2)

    while (currentNumber < endingNumber):
        if (currentNumber == 2): 
            currentNumber += 1 
        else:
            currentNumber += 2

        if (isPrime(currentNumber)):
            sumOfPrimeLogs += math.log(currentNumber)
    
    print(f"Sum of Logs: {sumOfPrimeLogs}, N: {endingNumber}, Ratio: {endingNumber/sumOfPrimeLogs}")

problem_2_solution(10)
problem_2_solution(100)
problem_2_solution(1000)
# problem_2_solution(10000)
# problem_2_solution(100000)
# problem_2_solution(1000000)
# problem_2_solution(10000000)
