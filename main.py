import turtle

import pandas

t=turtle.Turtle()


screen=turtle.Screen()
screen.title("us states")

image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
s=0


data=pandas.read_csv("50_states.csv")
while (s<50):
    head = f"{s}/50 states correct"
    answer = screen.textinput(title=head, prompt="enter state name")
    answer_title = answer.title()


    name=data["state"].tolist()
    x_cor=data["x"].tolist()
    y_cor=data["y"].tolist()
    c = 0

    for i in name:
        if(answer_title == i):
            c+=1
            p=data[data.state==i]
            x1=int(p.x)
            y1=int(p.y)

            t.penup()
            t.goto(x1,y1)
            t.write(i)
            t.hideturtle()

            s+=1
            continue




turtle.mainloop()




