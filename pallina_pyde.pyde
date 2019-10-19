x=50
y=80
verY=1
verX=1
xrect1=400
yrect1=575
xrect2=400
yrect2=0

def setup():
    size(900,600)
    
def draw():
    global x,y,verY,verX
    
    background(255,255,255)
    ellipse(x,y,20,20)
    rect(xrect1,yrect1,100,25)
    rect(xrect2,yrect2,100,25)
    x=x+2*verX
    y=y+2*verY
    #fa rimbalzare la pallina sul muro (4 if)
    if (y+10>height):
        verY=-1
    if (x+10>width):
        verX=-1
    if (y<10):
         verY=1
    if (x<10):
        verX=1
    #fa rimbalzare la pallina sulla racchetta  
    if (y+10>height-25 and x+10>xrect1 and x-10<xrect1+100):
        verY=-1
    if(y-10<25 and x+10>xrect2 and x-10<xrect2+100):
        verY=1 
        
def keyPressed():
    global xrect1,xrect2 #dichiarare globale solo se deve essere modificato il valore
    #fa muovere la racchetta
    if keyCode==LEFT:
        xrect1=xrect1-7
    if keyCode==RIGHT:
        xrect1=xrect1+7
    if key=='a':
        xrect2=xrect2-7
    if key=='d':
        xrect2=xrect2+7
        
    
     
        
        
