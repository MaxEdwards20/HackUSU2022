import random
import turtle
import time

class SnakeCali():

    def __init__(self):
        self.delay = 0.1
        self.score = 0
        self.highScore = 0

        # Create the window screen
        wn = turtle.Screen()
        wn.title("CaliSnake")
        wn.bgcolor("yellow")
        self.wn = wn

        # Setting dimentions of window
        wn.setup(width= 600, height=600)
        wn.tracer(0)

        # Making the snake
        head = turtle.Turtle()
        head.shape("square")
        head.color("green")
        head.penup()
        head.goto(0,0)
        head.direction = "Stop"
        self.head = head


        # the Coins
        coin = turtle.Turtle()
        colors = random.choice(['green','grey','blue'])
        shapes = random.choice(['square','triangle','circle'])
        coin.speed(0)
        coin.shape(shapes)
        coin.color(colors)
        coin.penup()
        coin.goto(0,100)
        self.coin = coin

        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0,250)
        pen.write("Score: 0 High Score : 0", align="center", font=("Arial", 24, "bold"))
        self.pen = pen

        wn = self.wn
        wn.listen()
        wn.onkeypress(self.group, "w")
        wn.onkeypress(self.godown, "s")
        wn.onkeypress(self.goleft, "a")
        wn.onkeypress(self.goright, "d")

        segments = []
        self.segments = segments

    def group(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def godown(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def goright(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def goleft(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def move(self):
        head = self.head
        if head.direction == "up":
            y = self.head.ycor()
            head.sety(y+20)
        if head.direction == "down":
            y = head.ycor()
            head.sety(y-20)
        if head.direction == "left":
            x = head.xcor()
            head.setx(x-20)
        if head.direction == "right":
            x = head.xcor()
            head.setx(x+20)



    def run(self):
        # main logic
        while True:
            head = self.head
            wn = self.wn
            segments = self.segments
            pen = self.pen
            coin = self.coin
            delay = self.delay
            highScore = self.highScore
            score = self.score
            wn.update()
            if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "Stop"
                colors = random.choice(['red','blue','green'])
                shapes = random.choice(['square', 'circle'])
                for segment in segments:
                    segment.goto(1000,1000)
                segments.clear()
                score = 0
                delay = 0.1
                pen.clear()
                pen.write(f"Score : {score} Highscore: {highScore}", align="center",font=("Arial", 24, "bold"))
            if head.distance(coin) <20:
                x = random.randint(-270,270)
                y = random.randint(-270,270)
                coin.goto(x,y)

                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("pink") # tail
                new_segment.penup()
                segments.append(new_segment)
                delay -= 0.001
                score += 10
                if score > highScore:
                    highScore = score
                pen.clear()
                pen.write(f"Score : {score} High Score : {highScore}", align="center",font=("Arial", 24, "bold"))
            for index in range(len(segments) -1,0,-1):
                x = segments[index - 1].xcor()
                y = segments[index-1].ycor()
                segments[index].goto(x,y)
            if len(segments)>0:
                x = head.xcor()
                y = head.ycor()
                segments[0].goto(x,y)
            self.move()
            for segment in segments:
                if segment.distance(head) < 20:
                    time.sleep(1)
                    head.goto(0,0)
                    head.direction = "stop"
                    colors = random.choice(['red','blue','green'])
                    shapes = random.choice(['square','circle'])
                    for segment in segments:
                        segment.goto(1000,1000)
                    segment.clear()
                    score = 0
                    delay = 0.1
                    pen.clear()
                    pen.write(f"Score : {score} High Score : {highScore}", align="center",font=("Arial", 24, "bold"))
            time.sleep(delay)
        wn.mainloop()

if __name__ == "__main__":
    snake = SnakeCali()
    snake.run()