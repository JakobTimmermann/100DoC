import turtle
import pandas as pd

state_data = pd.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
all_states = state_data.state.to_list()


def compare_answers(user_input, correct_inputs):
    user_input = user_input.strip().title()
    if user_input in all_states and user_input not in correct_inputs:
        x = int(state_data[state_data.state == user_input].x)
        y = int(state_data[state_data.state == user_input].y)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x, y)
        t.write(user_input, align="center")
        correct_inputs.append(user_input)
    return correct_inputs

correct_answers = []
print(len(state_data[~state_data["state"].isin(correct_answers)]))

still_playing = True
while still_playing:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 State Correct", prompt="What's another state's name")
    if answer_state == "exit":
        state_data[~state_data["state"].isin(correct_answers)].to_csv("missing_states.csv")
        break
    correct_answers = compare_answers(answer_state, correct_answers)
