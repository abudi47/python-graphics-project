#section  36
#GROUP MEMBERS
# 1 Abduselam Tesfaye -------UGR/25696/14
# 2 Fiker Tibebe-------------UGR/30536/15
# 3 Hermela Alemayehu--------UGR/30671/15
# 4 Sarem Hailu--------------UGR/31198/15
# 5 Rekik Fewashe------------UGR/31134/15
# 6 Abdisa Alemu-------------UGR/30018/15


#pseudo code
''' this incredible graphics work done by section 36 group 1 members
it's ASTU STADIUM'''

from cs1graphics import*
from time import*
import time 

stad=Canvas(1300,900,'darkgreen','ASTU STADIUM',)

tv = Layer()

inch = Rectangle(175,70,Point(120,100))
inch.setFillColor('white')
txt = Text(' 0 : 0 ',22,Point(120,100))
txt.setFontColor("darkblue")
txt.setDepth(10)
txt1 = Text('ETH',22,Point(65,100))
txt1.setFontColor("darkblue")
txt1.setDepth(10)


#  flag
flag1 = Layer()
g = Rectangle(200, 33.3)
y = Rectangle(200, 33.3, Point(0, 33.3))
r = Rectangle(200, 33.3, Point(0, 66.6))

g.setFillColor('green')
y.setFillColor('yellow')
r.setFillColor('red')

c= Circle(20,Point(0, 33.3))
c.setDepth(5)
c.setFillColor('blue')
flag1.add(c)

flag1.add(g)
flag1.add(y)
flag1.add(r)
flag1.scale(0.2)
flag1.setDepth(10)
flag1.moveTo(40,70)


stad.add(flag1)
flag2 = Layer()
g = Rectangle(200, 33.3)
y = Rectangle(200, 33.3, Point(0, 33.3))
r = Rectangle(200, 33.3, Point(0, 66.6))

g.setFillColor('red')
y.setFillColor('white')
r.setFillColor('black')



flag2.add(g)
flag2.add(y)
flag2.add(r)
flag2.scale(0.2)
flag2.setDepth(10)
flag2.moveTo(150,70)

stad.add(flag2)


txt2 = Text('SUD',22,Point(175,100))
txt2.setFontColor("darkblue")
txt2.setDepth(10)
txt3 = Text('ASTU STADIUM' , 55 , Point(700,58))
txt3.setFontColor('red')
txt3.setDepth(10)

sti = Rectangle(20,60,Point(120,165))
sti.setFillColor('black')
tv.add(txt1)
tv.add(txt2)
tv.add(txt3)
tv.add(txt)
tv.add(sti)
tv.add(inch)
tv.move(-30,0)



stad.add(tv)


#car
car2=Layer()
a=Polygon(Point(-250,420),Point(-50,420),Point(-50,390),Point(-100,390),
          Point(-130,350),Point(-250,350))
aa=Polygon(Point(-230,330),Point(-110,330),Point(-130,350),Point(-250,350))
aa.setFillColor("black")
car2.add(aa)
bb=Polygon(Point(-130,350),Point(-100,390),Point(-80,370),Point(-110,330))
car2.add(bb)

cc=Polygon(Point(-50,390),Point(-100,390),Point(-80,370),Point(-30,370))
cc.setFillColor("white")

car2.add(cc)
cd=Polygon(Point(-50,390),Point(-30,370),Point(-30,400),Point(-50,420))
cd.setFillColor("black")
car2.add(cd)
a.setFillColor("white")

a1=Circle(15,Point(-100,420))
a2=Circle(15,Point(-210,420))
a1.setFillColor("black")
a2.setFillColor("black")
a11=Circle(7,Point(-100,420))
a21=Circle(7,Point(-210,420))
a11.setFillColor("white")
a21.setFillColor("white")
car2.add(a)
car2.add(a1)
car2.add(a11)
car2.add(a2)
car2.add(a21)
b=Rectangle(10,15,Point(-160,333))
b.setFillColor("red")
car2.add(b)
up=Ellipse(10,5,Point(-160,325))
up.setFillColor("blue")
nn=Text('AMBULANCE',16,Point(-185,380))
nn.setFontColor("red")

car2.add(nn)
car2.add(up)

car2.moveTo(250,250)


stad.add(car2)



stadium = Layer()


R1=Rectangle(988,500,Point(495,252))
R1.setFillColor('darkgreen')
R1.setBorderColor('darkgreen')


c2=Ellipse(170,170,Point(495,250))
c2.setBorderColor('white')
c2.setBorderWidth(3)


pt1=Rectangle(910,455,Point(495,250))
pt1.setBorderColor('white')
pt1.setBorderWidth(3)

pt2=Rectangle(1,455,Point(495,250))
pt2.setBorderColor('white')
pt2.setBorderWidth(1.5)



cl=Circle(50,Point(180,250))
cl.setBorderColor('white')

cl.setBorderWidth(3)

cf=Rectangle(100,130,Point(138,260))
cf.setFillColor('darkgreen')
cf.setBorderColor('darkgreen')

ptl=Rectangle(95,150,Point(87,250))
ptl.setBorderColor('white')
ptl.setBorderWidth(3)

ptl1=Rectangle(150,230,Point(115,250))
ptl1.setBorderColor('white')
ptl1.setBorderWidth(3)


playing=Layer()
goal = Polygon(Point(188,395),Point(165,380),Point(165,235),Point(165,235),Point(188,250))
goal.setBorderWidth(2)
goal.setBorderColor("white")
playing.add(goal)




goal2 = Polygon(Point(1100,395),Point(1130,380),Point(1130,235),Point(1130,235),Point(1100,250))
goal2.setBorderWidth(2)
goal2.setBorderColor("white")
playing.add(goal2)


stad.add(playing)



def corna(a,b,c):
    col=Circle(a,Point(b,c))
    col.setBorderColor('white')
    col.setBorderWidth(3)
    stadium.add(col)


stadium.add(R1)
stadium.add(c2)

corna(20,40,20)
corna(20,40,482)
corna(20,950,482)

corna(20,950,20)

R2=Rectangle(938,480,Point(495,252))

R2.setBorderColor('darkgreen')
R2.setBorderWidth(25)
stadium.add(R2)







stadium.add(pt1)
stadium.add(pt2)
stadium.add(cl)
stadium.add(cf)
stadium.add(ptl)
stadium.add(ptl1)






cr=Circle(50,Point(680,250))
cr.setBorderColor('white')
cr.setBorderWidth(3)

cr=Circle(50,Point(807,250))
cr.setBorderColor('white')
cr.setBorderWidth(3)

cfr=Rectangle(100,130,Point(849,260))
cfr.setFillColor('darkgreen')
cfr.setBorderColor('darkgreen')

ptr=Rectangle(95,150,Point(902,250))
ptr.setBorderColor('white')
ptr.setBorderWidth(3)

ptr1=Rectangle(150,230,Point(875,250))
ptr1.setBorderColor('white')
ptr1.setBorderWidth(3)


stadium.add(cr)
stadium.add(cfr)
stadium.add(ptr)
stadium.add(ptr1)


def pena(a,b,c):
    pc=Circle(a,Point(b,c))
    pc.setFillColor('white')
    pc.setBorderColor('white')
    stadium.add(pc)

pena(3,160,250)
pena(3,825,250)

fball=Layer()
ball=Circle(8,Point(875,250))

ball.setFillColor('brown')

ball.setBorderColor('black')

ball1=Circle(4,Point(875,250))

ball1.setFillColor('white')

ball1.setBorderColor('black')
fball.add(ball)
fball.add(ball1)

stadium.add(fball)



stadium.moveTo(150,70)
    

stadium.setDepth(200)

stad.add(stadium)
for i in range(1000):
    car2.move(1.05,0)

man=Layer()
men=Ellipse(15,26,Point(460,465))
men.setFillColor("chocolate")
man.add(men)
men2=Rectangle(20,30,Point(460,496))
men2.setFillColor("red")
man.add(men2)
men3=Path(Point(455,515),Point(455,535))
men3.setBorderWidth(5)
man.add(men3)
men4=Path(Point(465,515),Point(465,535))
men4.setBorderWidth(5)
man.add(men4)
men5=Path(Point(445,485),Point(440,495),Point(445,505))
men5.setBorderWidth(3)
man.add(men5)
men6=Path(Point(475,485),Point(480,495),Point(475,505))
men6.setBorderWidth(3)
man.add(men6)
#stad.add(man)

mand=Layer()
men=Ellipse(15,26,Point(460,465))
men.setFillColor("chocolate")
mand.add(men)
men2=Rectangle(20,30,Point(460,496))
men2.setFillColor((0,128,128))
mand.add(men2)
men3=Path(Point(455,515),Point(455,535))
men3.setBorderWidth(5)
mand.add(men3)
men4=Path(Point(465,515),Point(465,535))
men4.setBorderWidth(5)
mand.add(men4)
men5=Path(Point(445,485),Point(440,495),Point(445,505))
men5.setBorderWidth(3)
mand.add(men5)
men6=Path(Point(475,485),Point(480,495),Point(475,505))
men6.setBorderWidth(3)
mand.add(men6)


mane=Layer()
men=Ellipse(15,26,Point(460,465))
men.setFillColor("chocolate")
mane.add(men)
men2=Rectangle(20,30,Point(460,496))
men2.setFillColor((0,255,255))
mane.add(men2)
men3=Path(Point(455,515),Point(455,535))
men3.setBorderWidth(5)
mane.add(men3)
men4=Path(Point(465,515),Point(465,535))
men4.setBorderWidth(5)
mane.add(men4)
men5=Path(Point(445,485),Point(440,495),Point(445,505))
men5.setBorderWidth(3)
mane.add(men5)
men6=Path(Point(475,485),Point(480,495),Point(475,505))
men6.setBorderWidth(3)
mane.add(men6)
###man

players = Layer()
otherman1=mand.clone()
otherman1.scale(0.5)
otherman1.setDepth(32)
otherman1.moveTo(400,-120)
players.add(otherman1)

otherman2=man.clone()
otherman2.scale(0.5)
otherman2.setDepth(32)
otherman2.moveTo(400,-80)
players.add(otherman2)



otherman3=man.clone()
otherman3.scale(0.5)
otherman3.setDepth(32)
otherman3.moveTo(400,-40)
players.add(otherman3)


otherman4=man.clone()
otherman4.scale(0.5)
otherman4.setDepth(32)
otherman4.moveTo(400,00)
players.add(otherman4)


otherman5=man.clone()
otherman5.scale(0.5)
otherman5.setDepth(32)
otherman5.moveTo(400,40)
players.add(otherman5)



otherman6=man.clone()
otherman6.scale(0.5)
otherman6.setDepth(32)
otherman6.moveTo(400,80)
players.add(otherman6)



otherman7=man.clone()
otherman7.scale(0.5)
otherman7.setDepth(32)
otherman7.moveTo(400,120)
players.add(otherman7)





otherman8=man.clone()
otherman8.scale(0.5)
otherman8.setDepth(32)
otherman8.moveTo(400,160)
players.add(otherman8)





otherman9=man.clone()
otherman9.scale(0.5)
otherman9.setDepth(32)
otherman9.moveTo(400,200)
players.add(otherman9)



otherman11=man.clone()
otherman11.scale(0.5)
otherman11.setDepth(32)
otherman11.moveTo(400,240)
players.add(otherman11)


otherman10=man.clone()
otherman10.scale(0.5)
otherman10.setDepth(32)
otherman10.moveTo(400,280)
players.add(otherman10)

players.moveTo(-25,630)
stad.add(players)


manb=Layer()
men=Ellipse(15,26,Point(460,465))
men.setFillColor("chocolate")
manb.add(men)
men2=Rectangle(20,30,Point(460,496))
men2.setFillColor("green")
manb.add(men2)
men3=Path(Point(455,515),Point(455,535))
men3.setBorderWidth(5)
manb.add(men3)
men4=Path(Point(465,515),Point(465,535))
men4.setBorderWidth(5)
manb.add(men4)
men5=Path(Point(445,485),Point(440,495),Point(445,505))
men5.setBorderWidth(3)
manb.add(men5)
men6=Path(Point(475,485),Point(480,495),Point(475,505))
men6.setBorderWidth(3)
manb.add(men6)

###man b

playersb= Layer()
otherman1b=mane.clone()
otherman1b.scale(0.5)
otherman1b.setDepth(32)
otherman1b.moveTo(400,-120)
playersb.add(otherman1b)

otherman2b=manb.clone()
otherman2b.scale(0.5)
otherman2b.setDepth(32)
otherman2b.moveTo(400,-80)
playersb.add(otherman2b)



otherman3b=manb.clone()
otherman3b.scale(0.5)
otherman3b.setDepth(32)
otherman3b.moveTo(400,-40)
playersb.add(otherman3b)


otherman4b=manb.clone()
otherman4b.scale(0.5)
otherman4b.setDepth(32)
otherman4b.moveTo(400,00)
playersb.add(otherman4b)


otherman5b=manb.clone()
otherman5b.scale(0.5)
otherman5b.setDepth(32)
otherman5b.moveTo(400,40)
playersb.add(otherman5b)



otherman6b=manb.clone()
otherman6b.scale(0.5)
otherman6b.setDepth(32)
otherman6b.moveTo(400,80)
playersb.add(otherman6b)



otherman7b=manb.clone()
otherman7b.scale(0.5)
otherman7b.setDepth(32)
otherman7b.moveTo(400,120)
playersb.add(otherman7b)





otherman8b=manb.clone()
otherman8b.scale(0.5)
otherman8b.setDepth(32)
otherman8b.moveTo(400,160)
playersb.add(otherman8b)





otherman9b=manb.clone()
otherman9b.scale(0.5)
otherman9b.setDepth(32)
otherman9b.moveTo(400,200)
playersb.add(otherman9b)



otherman11b=manb.clone()
otherman11b.scale(0.5)
otherman11b.setDepth(32)
otherman11b.moveTo(400,240)
playersb.add(otherman11b)


otherman10b=manb.clone()
otherman10b.scale(0.5)
otherman10b.setDepth(32)
otherman10b.moveTo(400,280)
playersb.add(otherman10b)

playersb.moveTo(50,630)

   


stad.add(playersb)

###manc


manc=Layer()
men=Ellipse(15,26,Point(460,465))
men.setFillColor("chocolate")
manc.add(men)
men2=Rectangle(20,30,Point(460,496))
men2.setFillColor("yellow")
manc.add(men2)
men3=Path(Point(455,515),Point(455,535))
men3.setBorderWidth(5)
manc.add(men3)
men4=Path(Point(465,515),Point(465,535))
men4.setBorderWidth(5)
manc.add(men4)
men5=Path(Point(445,485),Point(440,495),Point(445,505))
men5.setBorderWidth(3)
manc.add(men5)
men6=Path(Point(475,485),Point(480,495),Point(475,505))
men6.setBorderWidth(3)
manc.add(men6)



playersc= Layer()
otherman1c=manc.clone()
otherman1c.scale(0.5)
otherman1c.setDepth(32)
otherman1c.moveTo(420,-80)
playersc.add(otherman1c)

otherman2c=manc.clone()
otherman2c.scale(0.5)
otherman2c.setDepth(32)
otherman2c.moveTo(400,-80)
playersc.add(otherman2c)



otherman3c=manc.clone()
otherman3c.scale(0.5)
otherman3c.setDepth(32)
otherman3c.moveTo(380,-80)
playersc.add(otherman3c)

playersc.moveTo(15,550)
fball.moveTo(-387,390)




stad.add(playersc)
time.sleep(0.1)

for i in range(120):
     fball.move(-0,-4)
     playersc.move(0,-4)
     players.move(0,-4)
     playersb.move(0,-4)
time.sleep(0.1)
for i in range(120):
    otherman2.move(-0.35,-0.32)
    otherman2b.move(0.35,-0.32)
    otherman3.move(-0.70,-0.64)
    otherman3b.move(0.70,-0.64)
    otherman4.move(-1.05,-0.96)
    otherman4b.move(1.05,-0.96)
    otherman5.move(-1.40,-1.28)
    otherman5b.move(1.40,-1.28)
    otherman6.move(-1.75,-1.60)
    otherman6b.move(1.75,-1.60)
    otherman7.move(-1.575,-1.60)
    otherman7b.move(1.575,-1.60)
    otherman8.move(-1.225,-1.92)
    otherman8b.move(1.225,-1.92)
    otherman9.move(-0.875,-2.24)
    otherman9b.move(0.875,-2.24)
    otherman11.move(-0.525,-2.56)
    otherman11b.move(0.525,-2.56)
    otherman10.move(-0.175,-2.88)
    otherman10b.move(0.175,-2.88)
time.sleep(1)
for i in range(120):
    otherman1.move(-3,0.3)
    otherman1b.move(3,0.3)
    otherman2.move(-1.75,-1)
    otherman2b.move(1.75,-1)
    otherman3.move(-1.40,-0)
    otherman3b.move(1.40,-0)
    otherman7.move(-0.5,1)
    otherman7b.move(0.5,1)
    otherman5.move(-0.70,0.5)
    otherman5b.move(0.70,0.5)
    otherman4.move(0.1,-0.75)
    otherman4b.move(-0.1,-0.75)
    otherman6.move(0.8,1.4)
    otherman6b.move(-0.8,1.4)
    otherman9.move(1.0,1.2)
    otherman9b.move(-1.0,1.2)
    otherman10.move(0.3,-1.7)
    otherman11.move(0.19,0)
    otherman11b.move(-0.8,-0.3)
    otherman10b.move(-0.3,-1.7)
    otherman1c.move(-1.9,-1.4)
    otherman3c.move(1.5,2.8)
for i in range(120):
    fball.move(0.1,0.7)

   
    
    
    
    
time.sleep(0.4)
#Thank you
thank=Layer()
tha=Text('THANK YOU',40,Point(-600,300))
tha.setFontColor("black")
thank.add(tha)
fo=Text('FOR',40,Point(600,-250))
fo.setFontColor("yellow")
thank.add(fo)
wat=Text('WATCHING',40,Point(1500,400))
wat.setFontColor("red")
thank.add(wat)
stad.add(thank)
for i in range(300):
     tha.move(3,0)
     wat.move(-2.1,0)
     fo.move(0,2)    
    
time.sleep(0.5)
   
    
#GROUP MEMBERS
group=Layer()
hh=Rectangle(500,300,Point(700,1300))
hh.setFillColor("brown")
hh.setBorderColor("black")
group.add(hh)
gr=Text('SECTION36',16,Point(700,1165))
gr.setFontColor("black")
group.add(gr)
gr2=Text('GROUP MEMBERS',16,Point(700,1185))
gr2.setFontColor("black")
group.add(gr2)
gr3=Text('No    ---- NAME     --------     --------         --------       ID No',15,
         Point(675,1208))
gr3.setFontColor("black")
group.add(gr3)

muk=Text('  1 ABDUSELAM TESFAYE             ugr/25696/14',18,
         Point(680,1225))
muk.setFontColor("black")
group.add(muk)  
mub=Text('2  FIKER  TIBEBE                         ugr/30536/15 ',18,
         Point(685,1245))
mub.setFontColor("black")
group.add(mub)
mud=Text('3   HERMELA  ALEMAYEHU             ugr/30671/15',18,
         Point(695,1265))
mud.setFontColor("black")
group.add(mud)
mul=Text('     4 SAREM HAILU                             ugr/31198/15',18,
         Point(675,1285))
mul.setFontColor("black")
group.add(mul)
mut=Text('        5 REKIK FEWASHE                        ugr/31134/15 ',18,
         Point(675,1305))

mut.setFontColor("black")
group.add(mut)
mul2=Text('      6  ABDISA ALEMU                             ugr/30018/15 ',18,
         Point(680,1325))
mul2.setFontColor("black")
group.add(mul2)
su=Text('SUBMITED TO  Ms. HIWOT',11,Point(800,1365))
su.setFontColor("black")
group.add(su)
date=Text('Submitted date: 06/09/2023.',16,
         Point(780,1395))
date.setFontColor("black")
group.add(date)
group.setDepth(10)
stad.add(group)

for i in range(1000):
    group.move(0,-1)



          















