# HCL_testing
```
Write a program which can compute the factorial of a given numbers.Theresults should be printed in a comma-separated sequence on a singleline.Suppose the following input is supplied to the program:8 
Then, the output should be:40320
```

```
n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
```

```
Write a Python program that accepts a sentence and calculate the number of letters and digits.Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
```

```
s=input()
letters=0
digits=0
for i in s:
    if i.isalpha():
        letters+=1
    elif i.isdigit():
        digits+=1
print("LETTERS",letters)
print("DIGITS",digits)
```


```
Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated
sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
```
```
s=input().split(",")
result = []
for i in s:
    n=int(i,2)
    if(n%5==0):
        result.append(i)
print(",".join(result))
```


#OUTPUT:
<img width="1915" height="1021" alt="image" src="https://github.com/user-attachments/assets/290d7cb8-080e-4106-8771-a70e7ab8843a" />


