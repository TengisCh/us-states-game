import turtle
import pandas
FONT = ("Times", 8, "normal")


def write_name(name, x, y):
    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.hideturtle()
    new_turtle.goto(x, y)
    new_turtle.write(name, False, "center", FONT)


screen = turtle.Screen()
screen.title("US 50 game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_csv = pandas.read_csv("50_states.csv")
list_state = states_csv.state.tolist()
guessed_states = []

while len(guessed_states) < 50:

    user_answer = screen.textinput("User answer", "Guess the states: ").capitalize()

    if "Exit" == user_answer:
        states_to_learn = [state for state in list_state if state not in guessed_states]
        state_learn_csv = pandas.DataFrame(states_to_learn)
        state_learn_csv.to_csv("state_to_learn.csv")
        break

    if user_answer in list_state:
        state_row = states_csv[states_csv.state == user_answer]
        write_name(user_answer, int(state_row["x"]), int(state_row["y"]))
        guessed_states.append(user_answer)