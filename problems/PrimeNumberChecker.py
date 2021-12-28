def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("it's a prime number")
    else:
        print("it's not a prime number")


prime_checker(2)
