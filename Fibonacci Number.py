class Solution:
def fib(self, n: int) -> int:

    if n == 0:
        return 0
    if n == 1:
        return 1
    if(n > 1):
        return self.fib(n - 1) + self.fib(n - 2)

    
    
nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
   
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)

       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
