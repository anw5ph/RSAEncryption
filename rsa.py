import math
import random

# Function to check whether or not randomly generated number is prime


def isPrime(num):
    for n in range(2, int(num**0.5)+1):
        if num % n == 0:
            return False
    return True


# Range for prime numbers
minPrime = 0
maxPrime = 10000

# Function to generate list of random primes
primes = [i for i in range(minPrime, maxPrime) if isPrime(i)]

# p and q
p = random.choice(primes)
print("p = " + str(p))
q = random.choice(primes)
print("q = " + str(q))

# n
n = p * q

# Phi(n)
phi_n = (p - 1)*(q - 1)

# e
e = 2
while (e < phi_n):
    if(math.gcd(e, phi_n) == 1):
        break
    else:
        e += 1

print("e = " + str(e))

# d
d = pow(e, -1, phi_n)
print("d = " + str(d))

# Enter message
reply = input("Enter message: ")
message = round(int(reply))

# Encrypted message
enc_message = (message ** e) % n
print("Encrypted message = " + str(enc_message))

# Decrypted message
dec_message = (enc_message ** d) % n
print("Decrypted message = " + str(dec_message))
