import turtle
import pandas

correct_guesses = []
game_is_on = True

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
state_t = turtle.Turtle()

data = pandas.read_csv("50_states.csv")

while game_is_on:

    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in data["state"].values:
        if answer_state not in correct_guesses:
            correct_guesses.append(answer_state)
        state_data = data[data["state"] == answer_state]
        x, y = state_data.iloc[0]["x"], state_data.iloc[0]["y"]
        state_t.hideturtle()
        state_t.penup()
        state_t.goto(x, y)
        state_t.write(answer_state, align="center")

    if len(correct_guesses) == 50:
        game_is_on = False
        print("You Win!")

missed_states = [state for state in data["state"].values if state not in correct_guesses]


if missed_states:
    missed_data = pandas.DataFrame(missed_states, columns=["Missed States"])
    missed_data.to_csv("Missed_States.csv", index=False)

