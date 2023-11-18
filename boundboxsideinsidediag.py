
import math

from PIL import Image, ImageDraw, ImageFont

path="D:\\Intership\\Renovus\\Camera_python\\PyInt\\Integrate\\Images\\Input_Image_Paint.bmp"
image=Image.open(path)

width,height=image.size
print(width,height)


k=0
l=0
count=0
#left
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
# for j in range(0,height):
#         # color=image.getpixel((k,j))
        
#         newcolor=(255,0,0)
#         image.putpixel((x1,j),newcolor)

#Right
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


#TOP
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

#BOTTOM
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
newcolor=(0,0,0)
# for j in range(0,width):
#         # color=image.getpixel((k,j))
        
#         newcolor=(255,0,0)
#         image.putpixel((j,y4),newcolor)

# sides
# for i in range(x1,x2):
#     newcolor=(255,0,0)
#     image.putpixel((i,y3),newcolor)

# for i in range(x1,x2):
#     newcolor=(255,0,0)
#     image.putpixel((i,y4),newcolor)

# for i in range(y3,y4):
#     newcolor=(255,0,0)
#     image.putpixel((x1,i),newcolor)

# for i in range(y3,y4):
#     newcolor=(255,0,0)
#     image.putpixel((x2,i),newcolor)

# m=(y4-y3)/(x2-x1)
# print(m)

# # diagonal
# d=math.sqrt(((x2-x1)^2)+((y4-y3)^2))
# print(round(d))
# center=(d/2)
# print(round(center))
# count=0
# #left top diagonal center
# exit=False
# side1=0
# for x in range(x1,x2):
#     y=(m*(x-x2))+y4
#     #print(y)
#     color=image.getpixel((x,y))
#     red=color[0]
#     green=color[1]
#     blue=color[2]
#     side1=side1+1
#     if(red!=255 or green!=255 or blue !=255):
#         rx1=x-1
#         ry1=y
#         exit=True
#     if exit==True:
#         print("rx1",rx1)
#         print("ry1",ry1)
#         print(side1)
#         break
#     # count=count+1
#     # image.putpixel((x,round(y)),newcolor)

# #right top digonal center

# m2=(y4-y3)/(x1-x2)

# exit=False
# side2=0
# for x in range(x2,x1,-1):
#     y=(m2*(x-x1))+y4
#     #print(y)
#     color=image.getpixel((x,y))
#     red=color[0]
#     green=color[1]
#     blue=color[2]
#     side2=side2+1
    
#     if(red!=255 or green!=255 or blue !=255):
#         rx2=x+1
#         ry2=y
#         exit=True
#     if exit==True:
#         image.putpixel((rx2,int(ry2)),color)
#         print("rx2",rx2)
#         print("ry2",ry2)
        
#         # print(side1)
#         break

# #bottom  right diagonal center 

# m3=(y4-y3)/(x2-x1)

# exit=False
# side3=0
# for x in range(x2,x1,-1):
#     y=(m3*(x-x2))+y4
#     #print(y)
#     color=image.getpixel((x,y))
#     red=color[0]
#     green=color[1]
#     blue=color[2]
#     side3=side3+1
#     image.putpixel((x,int(y)),color)
#     if(red!=255 or green!=255 or blue !=255):
#         rx3=x
#         ry3=y+1
#         exit=True
#     if exit==True:
        
#         print("rx3",rx3)
#         print("ry3",ry3)
        
#         # print(side1)
#         break

# #bottom left diagonal center

# m4=(y4-y3)/(x1-x2)

# exit=False
# side4=0
# for x in range(x1,x2):
#     y=(m4*(x-x2))+y3
#     #print(y)
#     color=image.getpixel((x,y))
#     red=color[0]
#     green=color[1]
#     blue=color[2]
#     side4=side4+1
#     image.putpixel((x,int(y)),color)
#     if(red!=255 or green!=255 or blue !=255):
#         rx4=x-1
#         ry4=y
#         exit=True
#     if exit==True:
        
#         print("rx4",rx4)
#         print("ry4",ry4)
        
#         # print(side1)
#         break



# #calculate distance

# d1=((rx1-x1)^2)+((round(ry1)-y3)^2)
# d1=math.sqrt(d1)
# print("distance formula",d1)





# draw = ImageDraw.Draw(image)
# text = "Trial"
# font = ImageFont.truetype("arial.ttf", size=100)  # You can specify the font and size you want
# text_color = (255, 0,0)  # RGB color tuple
# position = (0,0)  # (x, y) position where you want the text to appear
# draw.text(position, text, fill=text_color, font=font)



# def calculate_center(x1,x2,y1,y2):
#     p1=int((x1+x2)/2)
#     p2=int((y1+y2)/2)
#     return p1,p2

# def calculate_line(p1,y1,x2,p2):
#     calculate_center()
#     m=(p2-y1)/(x2-p1)
#     print(m)
#     for x in range(p1,x2):
#         y=(m*(x-p1))+y3
#         print(y)
#         image.putpixel((x,round(abs(y))),newcolor)



# # def slope_Line(l):
black=(0,0,0)
# c1=int((x1+x2)/2)
# c2=int((y1+y2)/2)
# image.putpixel((c1,c2),black)

p1=int((x1+x2)/2)
p2=int((y3+y4)/2)
# top=y3-side1-13
# # print(p1)
# # print(p2)

# #calculate slope
m1=(p2-y3)/(x2-p1)
m2=(y4-p2)/(p1-x2)
m3=(p2-y4)/(x1-p1)
m4=(p2-y3)/(x1-p1)

color=(255,0,0)
# print(m)

# for i in range(y3,top,-1):
#     image.putpixel((p1,i),newcolor)

for x in range(p1,x2):

    y=(m1*(x-p1))+y3
    #print(y)
    image.putpixel((x,round(abs(y))),color)

for x in range(p1,x2):
    y=(m2*(x-x2))+p2
    #print(y)
    image.putpixel((x,round(abs(y))),color)

for x in range(x1,p1):
    y=(m3*(x-p1))+y4
    #print(y)
    image.putpixel((x,round(abs(y))),color)

for x in range(x1,p1):
    y=(m4*(x-p1))+y3
    #print(y)
    image.putpixel((x,round(abs(y))),color)

# image.putpixel((c1,c2),newcolor)
# slopeside1=(ry1-top)/(rx1-p1)

# #outside diagonal
# #top left
# for i in range(rx1,p1):
#     y=(slopeside1*(i-p1))+top
#     #print(y)
#     image.putpixel((i,round(abs(y))),color)

# #left
# left = x1-side2-13
# # for i in range(x1,left,-1):
# #     image.putpixel((i,p2),color)

# slopeside2=(rx1-left)/(ry1-p2)
# print("slopeside2",slopeside2)
# #bottom left
# for i in range(int(ry1),p2):
#     # y=(slopeside2*(i-rx1))+ry1
#     # print(y)
#     x=((slopeside2*(i-ry1)))+rx1
#     image.putpixel((round(x),i),color)
#     # x=((i-ry1)/slopeside2)+left
#     # image.putpixel((round(x),i),color)

# #top rightside

# slopeside3=(ry2-top)/(rx2-p1)
# print("slopeside3",slopeside3)

# for i in range(p1,rx2):
#     y=((slopeside3*(i-rx2)))+ry2
#     image.putpixel((i,round(y)),color)

# right=x2+side3+13
# slopeside4=(right-rx2)/(p2-ry2)
# print("slopeside4",slopeside4)

# for i in range(int(ry2),p2):
#     x=((slopeside4*(i-p2)))+right
#     image.putpixel((round(x),i),color)


# #bottom right side

# slopeside5=(rx3-right)/(ry3-p2)
# print("slopeside5",slopeside5)

# for i in range(p2,int(ry3)):
#     x=((slopeside5*(i-ry3)))+rx3
#     image.putpixel((round(x),i),color)

# #p1,y4
# bottom = y4+side4+13

# slopeside6=(bottom-ry3)/(p1-rx3)
# print("slopeside6",slopeside6)

# for i in range(p1,rx3):
#     y=((slopeside6*(i-rx3)))+ry3
#     image.putpixel((i,round(y)),color)

# #bottom left side

# slopeside7=(ry4-bottom)/(rx4-p1)
# print("slopside7",slopeside7)

# for i in range(rx4,p1):
#     y=((slopeside7*(i-p1)))+bottom
#     image.putpixel((i,int(y)),color)

# slopeside8=(rx4-left)/(ry4-p2)
# print("slopeside8",slopeside8)

# for i in range(p2,int(ry4)):
#     x=((slopeside8*(i-ry4)))+rx1
#     image.putpixel((round(x),i),color)

#left side diagonal

#slope
# leftsideslope=(p2-top)/(left-p1)
# for x in range(left,p1):
#     y=(leftsideslope*(x-p1))+top
#     image.putpixel((x,round(abs(y))),color)



image.save("trial1op.bmp")
image.show()


# for i in range(5,0,-1):
#     for j in range(10,0,-1):
        
#         print(i,j)