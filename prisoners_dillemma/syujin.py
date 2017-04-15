#-*- coding:utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm 

confession_2=7       #二人とも自白した時の量刑
silent_2=2           #二人とも黙秘した場合
confession_silent=5  #自分は自白するが相手は黙秘
silent_confession=10 #自分は黙秘するが相手は自白
raw=0.01

N=10000 #試行回数
X_border=0.5 #この閾値を超えたら自白
Y_border=0.5
ims=[]
fig=plt.figure()
X_plot=[]
Y_plot=[]
Count_00=0 #共に自白の回数
Count_01=0 #Yが自白
Count_10=0 #Xが自白
Count_11=0 #共に黙秘

for i in range(N):
    rnd_x=random.random()
    rnd_y=random.random()
    if rnd_x>X_border:
        X=1
    else:
        X=0
    if rnd_y>Y_border:
        Y=1
    else:
        Y=0
   
    if X==1 and Y==1:
        X_sentence=confession_2
        Y_sentence=confession_2
	Count_11+=1
    elif X==1 and Y==0:
        X_sentence=confession_silent
        Y_sentence=silent_confession
	Count_10+=1
    elif X==0 and Y==1:
        X_sentence=silent_confession
        Y_sentence=confession_silent
	Count_01+=1
    elif X==0 and Y==0:
        X_sentence=silent_2
        Y_sentence=silent_2
	Count_00+=1
    if X==0:
        X_border+=raw*X_sentence
    elif X==1:
        X_border-=raw*X_sentence
    if Y==0:
        Y_border+=raw*Y_sentence
    elif Y==1:
        Y_border-=raw*Y_sentence

    if X_border>0.95:
	X_border=0.95
    elif X_border<0.05:
	X_border=0.05
    if Y_border>0.95:
	Y_border=0.95
    elif Y_border<0.05:
	Y_border=0.05

    print X,Y,X_border,Y_border,rnd_x,rnd_y
    X_plot.append([X])
    Y_plot.append([Y])
    im=plt.scatter(X,Y,s=10000,color=cm.hsv(float(i)/N))
    ims.append([im])
    
print Count_00,Count_01,Count_10,Count_11

#選択の推移をアニメーション（散布図）で表す
plt.xlabel("Player X")
plt.ylabel("Player Y")
plt.hlines([0.5],-0.2,1.2,linestyles="dashed")
plt.vlines([0.5],-0.2,1.2,linestyles="dashed")
ani=animation.ArtistAnimation(fig,ims,interval=50,repeat_delay=1000)
ani.save("graph/sanpu.gif")
plt.show()

#グラフで表示
fig=plt.figure()
plt.xlabel("times")
plt.title("(X,Y) : (0,0)=%d, (0,1)=%d, (1,0)=%d, (1,1)=%d"% (Count_00,Count_01,Count_10,Count_11))
plt.ylim(-0.1,1.1)
plt.plot(X_plot)
plt.plot(Y_plot)
plt.savefig("graph/data.png")
plt.show()
