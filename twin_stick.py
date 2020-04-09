# Game code is gonna go here!!!!!!

WIDTH = 860
HEIGHT = 540

player = {}

player["sprites"] = {}
player["turret"] = Actor("turret.png", center=(WIDTH//2, HEIGHT//2), anchor=('center', 'center'))
player["treads"] = Actor("treads.png", center=(WIDTH//2, HEIGHT//2), anchor=('center', 'center'))
player["movement"] = [0, 0]

def update():
    if keyboard[keys.RIGHT]:
        player["movement"][0] = 1
    elif keyboard[keys.LEFT]:
        player["movement"][0] = -1
    else:
        player["movement"][0] = 0
    if keyboard[keys.UP]:
        player["movement"][1] = 1
    elif keyboard[keys.DOWN]:
        player["movement"][1] = -1
    else:
        player["movement"][1] = 0

    player


def draw():
    screen.blit("arena.png", (0, 0))
    player["treads"].draw()
    player["turret"].draw()