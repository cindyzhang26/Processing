#Create variables for a ball that moves. 
#Requires x-position x-position, x- speed, y-speed.
x = 50
y = 50
xSpeed = 40
ySpeed = 0
def setup():
    global x
    global xSpeed
    size(600, 600)
    ellipse(x, y, 40, 40)
    x += xSpeed
    ellipse(x, y, 40, 40)