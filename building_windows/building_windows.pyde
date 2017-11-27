def setup():
    size(400,400)
    
def draw():
    background(245)
    fill(0)
    rect(100, 50, 200, 500)
    for y in range(67, 401, 48):
        for x in range (114, 286, 48):
            fill(160)
            rect(x, y, 30, 30)