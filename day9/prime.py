def prime(no):
    is_prime=True
    for i in range(2,no):
        if(no%i==0):
            is_prime=False
    if(is_prime):
        print("is a prime")
    else:
        print("not a prime")
no = int(input("Enter a no: "))
prime(no)