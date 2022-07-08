from tkinter import Toplevel, Label, Button, Tk
from PIL import Image, ImageTk
import json


def update_votes():
    votes = open("votes.txt", "w")
    votes.write("Captains\n")
    votes.write(json.dumps(votes_c))
    votes.write("\nVice Captains\n")
    votes.write(json.dumps(votes_vc))
    votes.close()


def read_captains():
    with open("captains.txt", "r") as f:
        captains = f.read().splitlines()
        return(captains)


def read_vcs():
    with open("vice_captains.txt", "r") as f:
        vcs = f.read().splitlines()
        return(vcs)


def success():
    global success_screen
    success_screen = Toplevel(main_screen)
    success_screen.title("Success")
    success_screen.state('zoomed')
    success_screen.configure(background='black')
    success_message = Label(success_screen, text="Voting successful", bg="black",
                            font=("Copperplate Gothic Bold", 42), fg="white")
    success_message.place(relx=0.5, rely=0.3, anchor="center")
    ty = Label(success_screen, text="Thank You", fg=house_colour,
               font=("Copperplate Gothic Bold", 42), bg="black")
    ty.place(relx=0.5, rely=0.5, anchor="center")
    next_button = Button(success_screen, text="OK", bg=house_colour, font=("Copperplate Gothic Bold", 20),
                         fg="white", height="1", width="7", borderwidth=4, relief="sunken", command=clear_success_screen)
    next_button.place(relx=0.5, rely=0.7, anchor="center")


def clear_success_screen():
    update_votes()
    success_screen.destroy()


def add_captain_vote(index):
    votes_c[captains[index]] += 1


def add_vc_vote(index):
    votes_vc[vcs[index]] += 1


def vc_screen():
    global vote_vice_captain
    vote_vice_captain = Toplevel(main_screen)
    vote_vice_captain.title("Vice Captain")
    vote_vice_captain.state('zoomed')
    vote_vice_captain.configure(background='black')

    heading = Label(vote_vice_captain, text="Vice Captain", bg="black",
                    font=("Copperplate Gothic Bold", 52), fg="white")
    heading.place(relx=0.5, rely=0.15, anchor="center")

    no_of_vcs = len(vcs) + 1

    for (index, vc) in enumerate(vcs):
        def update_vote(i=index):
            add_vc_vote(i)
            vote_vice_captain.destroy()
            success()

        captain_name = Label(vote_vice_captain, text=vc, bg=house_colour,
                             font=("Copperplate Gothic Bold", 28), fg="white")
        captain_name.place(relx=((index+1)*(1/no_of_vcs)),
                           rely=0.4, anchor="center")
        button = Button(vote_vice_captain, text="VOTE", bg=house_colour, font=("Copperplate Gothic Bold", 22),
                        fg="white", borderwidth=4, relief="sunken", command=update_vote)
        button.place(relx=((index+1)*(1/no_of_vcs)),
                     rely=0.8, anchor="center")


def captain_screen():
    global vote_captain
    vote_captain = Toplevel(main_screen)
    vote_captain.title("Captain")
    vote_captain.state('zoomed')
    vote_captain.configure(background='black')

    heading = Label(vote_captain, text="Captain", bg="black",
                    font=("Copperplate Gothic Bold", 52), fg="white")
    heading.place(relx=0.5, rely=0.15, anchor="center")

    no_of_captains = len(captains) + 1

    for (i, captain) in enumerate(captains):
        captain_name = Label(vote_captain, text=captain, bg=house_colour,
                             font=("Copperplate Gothic Bold", 28), fg="white")
        captain_name.place(relx=((i+1)*(1/no_of_captains)),
                           rely=0.4, anchor="center")

    for index in range(len(captains)):
        def update_vote(i=index):
            add_captain_vote(i)
            vote_captain.destroy()
            vc_screen()

        button = Button(vote_captain, text="VOTE", bg=house_colour, font=("Copperplate Gothic Bold", 22),
                        fg="white", borderwidth=4, relief="sunken", command=update_vote)
        button.place(relx=((index+1)*(1/no_of_captains)),
                     rely=0.8, anchor="center")


def account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.state('zoomed')
    main_screen.title("Election")
    main_screen.configure(background='black')

    school = Label(main_screen, text="Navkis Educational Center", font=(
        "Copperplate Gothic Bold", 72), fg="white", bg='black')
    school.place(relx=0.5, rely=0.1, anchor="center")

    election = Label(main_screen, text="2022 Election", bg='black',
                     font=("Copperplate Gothic Bold", 45), fg="white")
    election.place(relx=0.5, rely=0.25, anchor="center")

    image1 = Image.open(house_name.lower() +".jpg")
    image1 = image1.resize((150, 150))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test

    # Position image
    label1.place(relx=0.5, rely=0.45, anchor="center")

    house = Label(main_screen, text=house_name+" House", bg='black',
                  font=("Copperplate Gothic Bold", 60), fg=house_colour)
    house.place(relx=0.5, rely=0.65, anchor="center")

    vote_button = Button(text="Vote", bg=house_colour, font=(
        "Copperplate Gothic Bold", 35), fg="white", borderwidth=6, relief="sunken", command=captain_screen)
    vote_button.place(relx=0.5, rely=0.8, anchor="center")
    main_screen.mainloop()


house_colours = {
    "Raven": "blue",
    "Moven": "#09d402",
    "Pelican": "#fcdb03",
    "Falcon": '#f79328'
}
house_name = "Raven"
house_colour = house_colours[house_name]

captains = read_captains()
vcs = read_vcs()

votes_c = {}
votes_vc = {}

for captain in captains:
    votes_c[captain] = 0

for vc in vcs:
    votes_vc[vc] = 0

account_screen()
