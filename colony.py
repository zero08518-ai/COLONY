
import random
import tkinter as tk


window = tk.Tk()
window.title("COLONY")
window.geometry("900x600")
window.resizable(False, False)

game_map = tk.Canvas(
    window,
    width=900,
    height=550,
    bg="green"
)
game_map.pack()

fl = tk.PhotoImage(file="assets/flower.png")
tree_original = tk.PhotoImage(file="assets/tree.png")
grass = tk.PhotoImage(file="assets/grass.png")

small_tree = tree_original
medium_tree = tree_original.zoom(2, 2)
big_tree = tree_original.zoom(3, 3)

fire_frames = [
    tk.PhotoImage(file="assets/fire1.png"),
    tk.PhotoImage(file="assets/fire2.png"),
    tk.PhotoImage(file="assets/fire3.png")
]

small_fire = fire_frames[0]

fire_frames = [
    frame.zoom(3, 3)
    for frame in fire_frames
]

fire_animation = [
    fire_frames[0],
    fire_frames[1],
    fire_frames[0],
    fire_frames[2]
]

for y in range(18):
    for x in range(29):
        game_map.create_image(
            x * 32, y * 32,
            image=grass,
            anchor="nw"
        )

for i in range(30):
    f = random.randint(0, 868)
    l = random.randint(0, 518)

    game_map.create_image(
        f, l,
        image=fl,
        anchor="nw"
    )

for i in range(14):
    x = random.randint(0, 804)
    y = random.randint(0, 454)

    tree = random.choice([
        small_tree,
        medium_tree,
        big_tree
    ])

    game_map.create_image(
        x, y,
        image=tree,
        anchor="nw"
    )

fire_id = game_map.create_image(
    450, 275,
    image=fire_animation[0]
)


def animate_fire(index=0):
    game_map.itemconfig(
        fire_id,
        image=fire_animation[index]
    )

    next_index = (index + 1) % len(fire_animation)
    window.after(250, animate_fire, next_index)

selected_sprite = fl


sprites = {
    "1": fl,
    "2": small_tree,
    "3": medium_tree,
    "4": big_tree,
    "5": small_fire
}


def select_sprite(event):
    global selected_sprite

    if event.char in sprites:
        selected_sprite = sprites[event.char]


def place_sprite(event):
    game_map.create_image(
        event.x, event.y,
        image=selected_sprite,
        anchor="nw"
    )


window.bind("<Key>", select_sprite)
game_map.bind("<Button-1>", place_sprite)

animate_fire()

window.mainloop()
