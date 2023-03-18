o = 0
p = 0
v = 0
n = 0
d = 0
f = 0
k = 0
a = 0
h = 0
bg = 255
x = 10
l = 1290
r = 240
g = 216
b = 34
m = 0

def setup():
    fullScreen()
    background(255)
def draw():
    global r, g, b, x, l, d, j, f, v, n, k, h
    if h == 0:
        noStroke()
        
        
        img=loadImage("1200x600wa (1)-PhotoRoom.png-PhotoRoom.png")
        image(img,450,0,110,50)
        
        fill(0,0,255)
        rect(0,0,50,50)
        
        fill(255,0,0)
        rect(53,0,50,50)
        
        fill(240,216,34)
        rect(106,0,50,50)
        
        fill(0,255,0)
        rect(159,0,50,50)
        
        fill(75,39,155)
        rect(212,0,50,50)
        
        fill(100,100,255)
        rect(265,0,50,50)
        
        fill(255,255,0)
        rect(318,0,50,50)
        
        fill(0,0,0)
        rect(371,0,50,50)
        
        stroke(0)
        fill(255,255,255)
        rect(424,0,50,50)
        rect(434,10,30,30)
        noStroke()
        
        
        
        fill(0,0,0)
        textSize(30)
        text(x,1250,40)
        text("+",l,38)
        text("-",1230,38)
        
        fill(r,g,b)
        if k == 1:
            if mousePressed and (mouseButton == LEFT):
                for j in range (1,5,5):
                    d = mouseX
                    f = mouseY
                    fill(0,0,0)
                    ellipse(d,f,10,10)
                    
            if mousePressed and (mouseButton == RIGHT):
                fill(255,255,255)
                ellipse(d,f,15,15)
                stroke(0)
                rect(d,f,v,n)
                v = mouseX - d
                n = mouseY - f
                
            if k == 3:
                k = 0
                
        
        
        
        
        
        
        
        
        
        
        
        
        if k == 0:
            if mousePressed and (mouseButton == LEFT): 
                ellipse(mouseX,mouseY,x,x)
        
            if mousePressed and (mouseButton == RIGHT): 
                r = 255
                g = 255
                b = 255
                ellipse(mouseX,mouseY,50,50)
            
        if x >= 100:
            l = 1304
            
        if x <= 9:
            fill(255,255,255)
            rect(1250,10,40,35)
            x = 10
            
    if h == 1:
        img=loadImage("oevsg.-6,omfjedcw43yunf4bw5h,jymec(1).jpg")
        image(img,0,0,1920,1080)
    
def mouseClicked():
    global r, g, b, x, k, m, h
    if h == 0:
        if mouseX > 53 and mouseX < 103 and mouseY > 0 and mouseY < 50:
            k = 0
            r = 255
            g = 0
            b = 0
        
        if mouseX > 0 and mouseX < 50 and mouseY > 0 and mouseY < 50:
            r = 0
            g = 0
            b = 255
            k = 0
        
        if mouseX > 106 and mouseX < 156 and mouseY > 0 and mouseY < 50:
            r = 240
            g = 216
            b = 34
            k = 0
            
        if mouseX > 159 and mouseX < 209 and mouseY > 0 and mouseY < 50:
            r = 0
            g = 255
            b = 0
            k = 0
            
        if mouseX > 212 and mouseX < 262 and mouseY > 0 and mouseY < 50:
            r = 75
            g = 39
            b = 155
            k = 0
            
        if mouseX > 265 and mouseX < 315 and mouseY > 0 and mouseY < 50:
            r = 100
            g = 100
            b = 255
            k = 0
            
        if mouseX > 318 and mouseX < 368 and mouseY > 0 and mouseY < 50:
            r = 255
            g = 255
            b = 0
            k = 0
            
        if mouseX > 371 and mouseX < 421 and mouseY > 0 and mouseY < 50:
            r = 0
            g = 255
            b = 0
            k = 0
            
        if mouseX > 424 and mouseX < 474 and mouseY > 0 and mouseY < 50:
            k = 1
            
        if k == 1:
            for j in range (1,5,5):
                d = mouseX
                f = mouseY
                fill(0,0,0)
                ellipse(d,f,10,10)
    
            if mousePressed and (mouseButton == RIGHT):
                fill(255,255,255)
                ellipse(d,f,15,15)
                stroke(0)
                rect(d,f,v,n)
                v = mouseX - d
                n = mouseY - f
                k = 3
    
        if mouseX > 1290 and mouseX < 1315 and mouseY > 18 and mouseY < 38:
            fill(255,255,255)
            rect(1250,10,40,35)
            x = x + 1
            
        if mouseX > 1230 and mouseX < 1251 and mouseY > 18 and mouseY < 38:
            fill(255,255,255)
            rect(1250,10,40,35)
            x = x - 1
            
        if mouseX > 477 and mouseX < 527 and mouseY > 0 and mouseY < 50:
            img=loadImage("maxresdefault.jpg")
            image(img,0,0,1920,1080)
            img=loadImage("lox-PhotoRoom.png-PhotoRoom.png")
            image(img,100,900,200,200)
            img=loadImage("lox2-PhotoRoom.png-PhotoRoom.png")
            image(img,150,950,200,100)
            m = 1
        
    if m == 1:
        textSize(50)
        fill(255)
        text(u"boss fight",530,50)
        if mouseX > 530 and mouseX < 640 and mouseY > 0 and mouseY < 50:
           h = 1    
