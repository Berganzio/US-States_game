from turtle import Screen, Turtle
import pandas
import time

screen = Screen()
image = 'blank_states_img.gif'
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

timmy = Turtle()
timmy.hideturtle()
timmy.penup()
timmy.speed('fastest')

TOTAL_STATES = 50
guessed_states = 0
already_guessed_states = []

us_data = pandas.read_csv('50_states.csv')
states_names = us_data['state'].to_list()

game_on = True
while game_on:
    answer_state = screen.textinput(title=f'{guessed_states}/{TOTAL_STATES} guessed states',
                                    prompt='Type in the name of a U.S. state:').title()

    if answer_state == 'Exit':
        not_guessed_ones = []
        for state_name in states_names:
            if state_name not in already_guessed_states:
                not_guessed_ones.append(state_name)
        edu_data = pandas.DataFrame(not_guessed_ones)
        edu_data.to_csv('missing_states.txt')
        break

    for name in states_names:
        if answer_state in already_guessed_states:
            pass

        elif answer_state == name:
            guessed_states += 1
            state = us_data[us_data.state == f'{answer_state}']
            state_x = float(state.x)
            state_y = float(state.y)
            timmy.goto(x=state_x, y=state_y)
            timmy.write(arg=f'{name}', align='center', font=('Courier', 6, 'bold'))
            already_guessed_states.append(answer_state)

        if guessed_states == TOTAL_STATES:
            timmy.goto(0, 0)
            timmy.write(arg='CONGRATULATIONS\nYOU GUESSED\nEVERY\nSTATE IN THE\nUSA', align='center', font=('Courier', 50, 'bold'))
            time.sleep(7)
            screen.bye()





