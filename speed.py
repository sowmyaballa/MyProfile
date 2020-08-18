import math
def kmph(km):
  x=(0.277778*km)*100
  y=math.floor(x)
  return y
km=input()
print(int(kmph(km)))
