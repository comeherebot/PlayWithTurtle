import random
from turtle import * #import everything from turtle module(not recommended to use *)

tim_boy= Turtle()
screen = Screen()
angle= [0,90,180,270]
# pensize(2)
colormode(255)
def random_color():
    r= random.randint(0,255)
    g = random.randint (0, 255)
    b = random.randint (0, 255)
    return r,g,b

'''turtle move and stop'''

# for _ in range(10):
#     forward(5)
#     penup()
#     forward(5)
#     pendown()

'''generate different shape with random color'''

# for i in range(3,11):
#     c= ['midnight blue', 'crimson', 'olive drab', 'dark olive green','maroon']
#     color (random.choice(c))
#     for _ in range(i):
#         pensize(2)
#         forward(60)
#         right(int(360/i))
#     i+=1

'''Loop for random movement with random color'''

# color_list= ['dark red', 'maroon', 'salmon', 'dark salmon', 'light coral', 'orange red', 'burlywood', 'saddle brown', 'sienna', 'rosy brown', 'dark goldenrod', 'khaki', 'dark khaki', 'peach puff', 'moccasin', 'blanched almond', 'midnight blue', 'crimson', 'olive drab', 'dark olive green','maroon']

# for _ in range(500):
#     shape("turtle")
#     color(random.choice(color_list))
#     #left (random.choice (angle)) or right (random.choice (angle)) #or
#     setheading(random.choice(angle))
#     speed("normal")
#     forward(12)

'''loop for random movement and rgb color'''
# for _ in range(500):
#     shape("turtle")
#     color(random_color())
#     #left (random.choice (angle)) or right (random.choice (angle)) #or
#     setheading(random.choice(angle))
#     speed("normal")
#     forward(30)


'''make a spirograph'''

# def draw_a_spirograph(size_of_gap):
#     for i in range(int(360/size_of_gap)):
#         color(random_color())
#         speed(0)
#         circle(100)
#         # left(i) # this one haven't equal gapes between each circle
#         #or
#         setheading(heading()+size_of_gap) #this one looks good and have equal gapes
# draw_a_spirograph(3)