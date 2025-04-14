import math
def can(height,width):
    can=(height*width)/5
    final_can=math.ceil(can)
    print(final_can)


height=int(input("inter height: "))
width=int(input("inter width: "))
can(height, width)