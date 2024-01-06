import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
count = 0
data = pandas.read_csv("50_states.csv")
data_states = list(data["state"])  # lista com letras maiusculas

data_cor_x = data["x"].to_list()
data_cor_y = data["y"].to_list()
correct_guesses = []
while count < 50:
    answer_state = screen.textinput(title=f"Guess The State {count}/50", prompt="What`s another state`s name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in data_states:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")


        break
    if answer_state in data_states:

        if answer_state in correct_guesses:
            pass
        else:
            correct_guesses.append(answer_state)
            index = data_states.index(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(data_cor_x[index], data_cor_y[index])
            t.write(f"{data_states[index]}")
            count += 1

screen.exitonclick()
