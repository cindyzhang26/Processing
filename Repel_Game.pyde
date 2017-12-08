x1_loc = random(100, 700)
y1_loc = random(100, 550)
x2_loc = random(50, 750)
y2_loc = random(50, 600)
player_ball_size = 100
ball_1_size = 100
ball_2_size = 50
boundary = 100
score = 0
ball_1_speed = PVector(100, 100)
ball_2_speed = PVector(100, 100)
ball_1_loc = PVector(x1_loc, y1_loc)
ball_2_loc = PVector(x2_loc, y2_loc)
player_loc = PVector(100, 100)

def setup():
    size(800, 650)

def draw():  
    global player_loc, score, x1_loc, y1_loc, x2_loc,y2_loc, ball_1_speed, ball_2_speed, ball_1_loc, ball_2_loc
    player_speed = PVector(mouseX - pmouseX, mouseY - pmouseY)
    player_loc.x = mouseX
    player_loc.y = mouseY
    
    background(255)
    # ball_1_loc.add(ball_1_speed)
    # ball_2_loc.add(ball_2_speed)
    fill(0)
    textSize(40)
    text("Score: " + str(score), 600, 50)
    fill(255, 0, 0)
    ellipse(ball_1_loc.x + ball_1_speed.x, ball_1_loc.y + ball_1_speed.y, ball_1_size, ball_1_size)
    ellipse(ball_2_loc.x + ball_2_speed.x, ball_2_loc.y + ball_2_speed.y, ball_2_size, ball_2_size)
    fill(0)
    ellipse(mouseX, mouseY, player_ball_size, player_ball_size)

    player_loc = PVector(mouseX, mouseY)
    fill(255, 0, 0)
    ellipse(player_loc.x, player_loc.y, player_ball_size, player_ball_size)
    #player_loc = PVector(mouseX, mouseY)
    player_speed = PVector(mouseX - pmouseX, mouseY - pmouseY)
    radius_ball_1 = ball_1_size /2
    radius_ball_2 = ball_2_size/2
    boundary_ball_1 = ball_1_size/2 + boundary
    boundary_ball_2 = ball_2_size/2 + boundary
    radius_player = player_ball_size/2
    a = ball_1_loc.x - player_loc.x
    b = ball_1_loc.y - player_loc.y
    c = ball_2_loc.x - player_loc.x
    d = ball_2_loc.y - player_loc.y
    distance1 = sqrt(a**2 + b**2)
    distance2 = sqrt(c**2 + d**2)
    distance3 = distance1 - 20

    
    if distance1 <= boundary_ball_1 + radius_player:
        import math
        vector_sub = PVector.sub(player_loc, ball_1_loc)
        angle = vector_sub.heading()
        fromangle = PVector.fromAngle(angle)
        ball_1_speed += player_speed.mult((angle*(180/math.pi))/180)
        ball_1_speed.sub(fromangle)
    if distance2 <= boundary_ball_2 + radius_player:
        import math
        vector_sub = PVector.sub(player_loc, ball_2_loc)
        angle = vector_sub.heading()
        fromangle = PVector.fromAngle(angle)
        ball_2_speed += player_speed.mult((angle * (180/math.pi))/180)
        ball_2_speed.sub(fromangle) 
    # if ball_1_loc.x == 700 or ball_1_loc.x == 100 or ball_1_loc.y == 550 or ball_1_loc == 100:
    #     ball_1_speed * -1
    