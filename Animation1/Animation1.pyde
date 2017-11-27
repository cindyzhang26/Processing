x = 100
y = 100
speed = 5
def setup():
    size(400, 400)

def draw():
    global x
    global speed
    if x >= 400:
        speed = -speed *0.95
    elif x <= 0:
        speed = -speed*0.95
    x += speed
    background(255)
    noStroke()
    fill(0, 0, 190)
    ellipse(x, y, 40, 40)
