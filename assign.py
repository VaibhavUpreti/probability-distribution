# import matplotlib as mtt
import matplotlib.pyplot as mt
numEvents = int(input("Enter number of times bulb is drawn: "))
p = 0.2
time = 500
Event = {}
# LOGIC
# nCr * p ^k  * (1-p)^n-k
def nCr(n, r):
    return (factorial(n) / (factorial(r) * factorial(n - r)))
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result
n = numEvents
r = 0
for k in range(numEvents+1):
    " Graph --- prob of success at kth trial vs trials"
    # z = (1-p)**(k)
    print(int(nCr(n, r)))
    ans = (int(nCr(n, r))) * p**(k) * (1-p)**(n-k)
    r = r + 1
    Event[k] = ans

x_axis = list(Event.keys())
y_axis = list(Event.values())
print(x_axis)
print(y_axis)
mt.bar(x_axis, y_axis)
# mt.plot(x_axis, y_axis)
mt.title("k success")
mt.xlabel("Number of Trials")
mt.ylabel("Probability")
mt.show()