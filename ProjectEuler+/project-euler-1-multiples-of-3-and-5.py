# Project Euler #1: Multiples of 3 and 5
def sum_of_multiples(k, n):
    d =  n // k
    sum = k * (d * (d+1)) // 2
    return sum

def multiples_of_3_and_5(n):
    
    s3 = sum_of_multiples(3, n-1)
    s5 = sum_of_multiples(5, n-1)
    s15 = sum_of_multiples(15, n-1)

    return s3 + s5 - s15

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(multiples_of_3_and_5(n))
