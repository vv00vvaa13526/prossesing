d = 0
g = 0
f = 0
def setup():
    size(1914,863)
def draw():
    global f, g, d
    img=loadImage("f.jpg")
    rotate(f)
    image(img,g,d)
    g=g - 1
    d=d + 1
    f = f + 0.01
