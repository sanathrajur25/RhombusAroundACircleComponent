from PIL import Image

#get the image
path="D:\\Intership\\Renovus\\Camera_python\\PyInt\\Integrate\\Images\\Input_Image_Paint.bmp"
image=Image.open(path)


#GET IMAGE WIDTH AND HEIGHT
width,height=image.size

r=(255,0,0)

#LEFT SIDE
ended = False
for i in range(0,width):
    for j in range(0,height):
        color=image.getpixel((i,j))
        red=color[0]
        green=color[1]
        blue=color[2]
        if (red!=255 or blue!=255 or green !=255):
            x1=i
            y1=j
            ended=True
            break
    if ended == True:
        break
print("Coordinate1")
print(x1)
print(y1)

#RIGHT SIDE
ended=False
for i in range(width-1,-1,-1):
    for j in range(0,height):
        color=image.getpixel((i,j))
        red=color[0]
        green=color[1]
        blue=color[2]
        if (red!=255 or blue!=255 or green !=255):
            x2=i
            y2=j
            ended=True
            break
    if ended == True:
        break
print("Coordinate 2")
print(x2)
print(y2)


#TOP SIDE
ended = False
for i in range(0,height-1):
    for j in range(0,width-1):
        color=image.getpixel((j,i))
        red=color[0]
        green=color[1]
        blue=color[2]
        if (red!=255 and blue!=255 and green !=255):
            y3=i
            x3=j
            ended=True
            break
    if ended == True:
        break

print("Coordinate 3")
print(x3)
print(y3)

#BOTTOM SIDE
ended = False
for i in range(height-1,-1,-1):
    for j in range(width-1,-1,-1):
        color=image.getpixel((j,i))
        red=color[0]
        green=color[1]
        blue=color[2]
        if (red!=255 and blue!=255 and green !=255):
            y4=i
            x4=j
            ended=True
            break
    if ended == True:
        break
print("Coordinate 4")
print(x4)
print(y4)

#FIND THE CENTER
p1=((x1+x2)/2)
p2=((y3+y4)/2)
print(p1,p2)
image.putpixel((round(p1),round(p2)),r)

#left top diagonal coordinates
m=(y4-y3)/(x2-x1)
exit=False
side1=0
for x in range(x1,x2):
    y=(m*(x-x2))+y4
    #print(y)
    color=image.getpixel((x,y))
    red=color[0]
    green=color[1]
    blue=color[2]
    side1=side1+1
    if(red!=255 or green!=255 or blue !=255):
        rx1=x
        ry1=y
        image.putpixel((x,int(y)),r)
        exit=True
    if exit==True:
        print("rx1",rx1)
        print("ry1",ry1)
        print(side1)
        break

#right top diagonalcoordinates
m2=(y4-y3)/(x1-x2)

exit=False
side2=0
for x in range(x2,x1,-1):
    y=(m2*(x-x1))+y4
    #print(y)
    color=image.getpixel((x,y))
    red=color[0]
    green=color[1]
    blue=color[2]
    side2=side2+1
    
    if(red!=255 or green!=255 or blue !=255):
        rx2=x
        ry2=y
        image.putpixel((x,int(y)),r)
        exit=True
    if exit==True:
        image.putpixel((rx2,int(ry2)),color)
        print("rx2",rx2)
        print("ry2",ry2)
        
        # print(side1)
        break

#bottom right diagonal
m3=(y4-y3)/(x2-x1)

exit=False
side3=0
for x in range(x2,x1,-1):
    y=(m3*(x-x2))+y4
    #print(y)
    color=image.getpixel((x,y))
    red=color[0]
    green=color[1]
    blue=color[2]
    side3=side3+1
    image.putpixel((x,int(y)),color)
    if(red!=255 or green!=255 or blue !=255):
        rx3=x
        ry3=y
        image.putpixel((x,int(y)),r)
        exit=True
    if exit==True:
        
        print("rx3",rx3)
        print("ry3",ry3)
        
        # print(side1)
        break

#bottom left diagonal
m4=(y4-y3)/(x1-x2)

exit=False
side4=0
for x in range(x1,x2):
    y=(m4*(x-x2))+y3
    #print(y)
    color=image.getpixel((x,y))
    red=color[0]
    green=color[1]
    blue=color[2]
    side4=side4+1
    if(red!=255 or green!=255 or blue !=255):
        rx4=x
        ry4=y
        image.putpixel((x,int(y)),r)
        exit=True
    if exit==True:
        
        print("rx4",rx4)
        print("ry4",ry4)
        
        # print(side1)
        break

#EXTENDED COORDINATES

#x & y value
x=round(p1)-rx1
y=round(p2)-ry1

#xvalue for left side & coordinates for left side (a,p2)
a=int(round(p1)-x-x)
print("a,p2",a,p2)
image.putpixel((a,round(p2)),r)

#yval for top side and coordinates for top side (p1,b)
b=int(round(p2)-y-y)
print("p1,b",p1,b)
image.putpixel((round(p1),b),r)

#xval for right side and coordinates for right side (c,p2)
c=int(round(p1)+x+x)
print("c,p2",c,p2)
image.putpixel((c,round(p2)),r)

#yval for bottom and coordinates for bottom side(p1,d)
d=int(round(p2)+y+y)
print("p1,d",p1,d)
image.putpixel((round(p1),d),r)

#draw diagonal
aTob=(b-p2)/(p1-a)

for i in range(a,round(p1)):
    y=((aTob*(i-round(p1))))+b
    image.putpixel((i,round(y)),r)

bToc=(p2-b)/(c-p1)

for i in range(round(p1),c):
    y=((bToc*(i-c)))+round(p2)
    image.putpixel((i,round(y)),r)

cTod=(d-p2)/(p1-c)

for i in range(c,round(p1),-1):
    y=((cTod*(i-round(p1))))+d
    image.putpixel((i,round(y)),r)

dToa=(p2-d)/(a-p1)

for i in range(a,round(p1)):
    y=((dToa*(i-round(p1)))+d)
    image.putpixel((i,round(y)),r)







#save and show the image
image.save("trial1op.bmp")
image.show()