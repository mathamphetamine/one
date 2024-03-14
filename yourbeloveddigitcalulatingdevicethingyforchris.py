import math
import cmath
def maxpow(x):#amogus
    x=math.floor(maxnum*math.log(10,x))#noa
    return x#cool math stuf
maxnum=4300
func=input("Insert a calculation of ** ")
func=func.strip(" ")
func=func.split("**")
if maxpow(int(func[0]))>int(func[1]):
    print(int(func[0])**int(func[1]))
else:
    print("ERROR: Integer Value Exceeds Limit")
print(maxpow(8937597592749824))