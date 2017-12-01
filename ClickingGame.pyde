"""
2-player clicking game

1) drawn an ellipse at a random location on the screen, add to score
2) store the location info in a variable (PVector)
3) using the mousePressed() function. When the user clicks, assign a new location to the
   ball. 
4) Create a score variable. When the user clicks (same function as above_ add +1 to the 
   score. Display score using a text() function
"""
P1x = random(0, 250)
P1y = random(0, 401)
P2x = random(350, 601)
P2y = random(0, 401)
P1Score = 0
P2Score = 0
def setup():
    size(600, 400)
    
def draw():
    background(75, 244, 66)
    fill(255)
    noStroke()
    rect(300, 0, 300, 400)
    ellipse(P1x, P1y , 100, 100)
    text("Score:" + str(P1Score), 25, 25)
    fill(75, 244, 66)
    ellipse(P2x, P2y, 100, 100)
    text("Score:" + str(P2Score), 325, 25)
    if P1Score == 10:
        background(75, 244, 66)
        fill(255)
        noStroke()
        rect(300, 0, 300, 400)
        fill(0)
        textSize(50)
        text("Player 1 Wins", 152, 200)
    elif P2Score == 10:
        background(75, 244, 66)
        fill(255)
        noStroke()
        rect(300, 0, 300, 400)
        fill(0)
        textSize(50)
        text("Player 2 Wins", 158, 200)

        
def mouseClicked():
    global P1Score
    global P2Score
    global P1x
    global P1y
    global P2x
    global P2y
    # if mouseX >= P1x-50 and mouseX <= P1x+50 and mouseY >= P1y-50 and mouseY <= P1y+50:
    #     P1x = random(0, 250)
    #     P1y = random(0, 401)
    #     P1Score += 1
    # elif mouseX >= P2x-50 and mouseX <= P2x+50 and mouseY >= P2y-50 and mouseY <= P2y+50:
    #     P2x = random(350, 601)
    #     P2y = random(0, 401)
    #     P2Score += 1
    
    radius = 100.0 / 2.0
    distance_x = abs(mouseX - P1x)
    distance_y = abs(mouseY - P1y)
    hypotenuse = sqrt(distance_x ** 2 + distance_y ** 2)
    if hypotenuse <= radius:
        P1x = random(0, width/2)
        P1y = random(0, height)
        P1Score += 1
        
    # PLAYER 2
    radius = 100.0 / 2.0
    distance_x = abs(mouseX - P2x)
    distance_y = abs(mouseY - P2y)
    hypotenuse = sqrt(distance_x ** 2 + distance_y ** 2)
    if hypotenuse <= radius:
        P2x = random(width/2, width)
        P2y = random(0, height)
        P2Score += 1