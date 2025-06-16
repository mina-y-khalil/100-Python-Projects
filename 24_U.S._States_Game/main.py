from turtle import Turtle, Screen
import pandas


turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    user_input = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What is your guess?").title()
    if user_input == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if user_input in all_states:
        guessed_states.append(user_input)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_input] #getting the row that matches the user input
        t.goto(state_data.x.item() , state_data.y.item() )
        t.write(user_input)

#states_to_learn







screen.exitonclick()