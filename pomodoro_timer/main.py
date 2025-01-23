from tkinter import *
import time
#colors
yellow='#E7D283'
green='#77B254'
pink='#FFAAAA'
red='#FB4141'
color=green
work=30
rest=5
long_break=20
compute_time=0
timer1=None
timer2=None

#---------------------Functionality--------------------#
def compute_timer(start,color):
    global timer1
    if start<0:
        return
    a=start//60
    b=start%60
    if len(str(a))<2:
        a=str('0')+str(a)
    if len(str(b))<2:
        b=str('0')+str(b)
    
    canvas.itemconfig(canvas_text,text=f'{str(a)+':'+str(b)}')
    timer1=window.after(1000,compute_timer,start-1,color)

def timer(i):
    global timer2
    global compute_time
    global color
    if i>8:
        btn1["state"] = NORMAL
        return
    if i&1!=0:
        print('work')
        label.config(text='Work',fg=color)
        color=green
        compute_time=work*60
    elif i==8:
        print('long break')
        color=red
        label.config(text='Long Break',fg=color)
        compute_time=long_break*60
    else:
        print('break')
        color=pink
        label.config(text='Short Break',fg=color)
        compute_time=rest*60
        
    if compute_time!=120:
            txt=tick.cget("text")
            txt+=(' ✔ ')
            tick.config(text=txt)
    compute_timer(compute_time,color)
    
    timer2=window.after(compute_time*1000,timer,i+1)

def start_timer():
    btn1["state"] = DISABLED
    timer(1)

def reset():
    window.after_cancel(timer1)
    window.after_cancel(timer2)
    canvas.itemconfig(canvas_text,text=f'00:00')
    tick.config(text='')
    label.config(text='Timer',fg=green)
    btn1["state"] = NORMAL
    
#---------------------UI Design----------------------------#

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100,bg=yellow)
canvas=Canvas(width=300,height=300,bg=yellow,highlightthickness=0)
image=PhotoImage(file='image.png')
canvas.create_image(150,150,image=image)
canvas_text=canvas.create_text(150,175,text="00:00",fill='white',font=('Arial',35,"bold"))
canvas.grid(row=1,column=1)

label=Label(text='Timer',fg=green,bg=yellow,font=('Arial',30))
label.grid(row=0,column=1)

btn1=Button(text="Start",command=start_timer)
btn1.grid(row=2,column=0)

btn2=Button(text="Reset",command=reset)
btn2.grid(row=2,column=2)

tick=Label(text='',fg=green,bg=yellow,font=('Arial',20,'bold'))
tick.grid(row=2,column=1)

window.mainloop()