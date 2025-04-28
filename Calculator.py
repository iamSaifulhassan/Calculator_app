from tkinter import *
import math 
calculator=Tk()
calculator.title('Calculator')
calculator.geometry('370x540')
calculator.resizable(True,True)
#font
font='Calibri',28,'bold'
font2='Times',18,'bold'


def delfun():
    length=len(field.get())
    field.delete(length-1,'end')


def AllClear():
    field.delete(0,END)


def click(event):
    b=event.widget
    text=b['text']
    if text=='⌫':
        ex=field.get
        ex=ex[0:len(ex)-1]
        field.delete(0,END)
        field.insert(0,ex) 
    if text=='C':
        field.insert(END,"")
        return
    if text=='÷':
            field.insert(END,"/")
            return
    if text=='x':
            field.insert(END,"*")
            return
    if text=='=':
        ex=field.get()
        answer=eval(ex)
        field.delete(0,END)
        field.insert(0,answer)
        return
    if text=='sin()':
        ex=float(field.get())
        result=math.sin(ex)
        field.delete(0,END)
        field.insert(0,result)
        return
    if text=='cos()':
        ex=float(field.get())
        result=math.cos(ex)
        field.delete(0,END)
        field.insert(0,result)
        return
    if text=='tan()':
        ex=float(field.get())
        result=math.tan(ex)
        field.delete(0,END)
        field.insert(0,result)
        return
    if text=='√':
        ex=float(field.get())
        result=math.sqrt(ex)
        field.delete(0,END)
        field.insert(0,result)
        return
    if text=='log()':
        ex=float(field.get())
        result=math.log10(ex)
        field.delete(0,END)
        field.insert(0,result)
        return
    if text=='x²':
        ex=int(field.get())
        result=math.pow(ex,2)
        field.delete(0,END)
        field.insert(0,result)
        return
    if text=='x!':
        ex=int(field.get())
        result=math.factorial(ex)
        field.delete(0,END)
        field.insert(0,result)
        return
    if text=='sec()':
        ex=float(field.get())
        result=1/math.cos(ex)
        field.delete(0,END)
        field.insert(0,result)
        return
    if text=='cosec()':
        ex=float(field.get())
        result=result=1/math.sin(ex)
        field.delete(0,END)
        field.insert(0,result)
        return
    if text=='cot()':
        ex=float(field.get())
        result=result=1/math.tan(ex)
        field.delete(0,END)
        field.insert(0,result)
        return
    field.insert(END,text)
    print(text)

#Text field
field=Entry(font=font,bg='White',border=2,borderwidth=2)
field.grid(row=0,column=0,columnspan=3)
field.pack(side=TOP,fill=X)


#frame
buttonframe2=Frame(calculator,background="light blue",height='180',width='360')
buttonframe2.pack(fill=Y)
buttonframe=Frame(calculator,background="Light blue",height='400',width='380')
buttonframe.pack(fill=Y)

sinbutton=Button(buttonframe2,text='sin()',font=font2,bg='black',foreground='white',width=7,relief=GROOVE)
sinbutton.grid(row=0,column=0,padx=2,pady=2)
sinbutton.bind('<Button-1>',click)

cosbutton=Button(buttonframe2,text='cos()',font=font2,bg='black',foreground='white',width=8,relief=GROOVE)
cosbutton.grid(row=0,column=1,padx=2,pady=2)
cosbutton.bind('<Button-1>',click)

tanbutton=Button(buttonframe2,text='tan()',font=font2,bg='black',foreground='white',width=8,relief=GROOVE)
tanbutton.grid(row=0,column=2,padx=2,pady=2)
tanbutton.bind('<Button-1>',click)

cotbutton=Button(buttonframe2,text='cot()',font=font2,bg='black',foreground='white',width=7,relief=GROOVE)
cotbutton.grid(row=1,column=0,padx=2,pady=2)
cotbutton.bind('<Button-1>',click)

cosecbutton=Button(buttonframe2,text='cosec()',font=font2,bg='black',foreground='white',width=8,relief=GROOVE)
cosecbutton.grid(row=1,column=1,padx=2,pady=2)
cosecbutton.bind('<Button-1>',click)

secbutton=Button(buttonframe2,text='sec()',font=font2,bg='black',foreground='white',width=8,relief=GROOVE)
secbutton.grid(row=1,column=2,padx=2,pady=2)
secbutton.bind('<Button-1>',click)

sqrtbutton=Button(buttonframe2,text='√',font=font2,bg='darkOrange3',foreground='White',width=7,relief=GROOVE)
sqrtbutton.grid(row=2,column=0,padx=2,pady=2)
sqrtbutton.bind('<Button-1>',click)

logbutton=Button(buttonframe2,text='log()',font=font2,bg='darkOrange3',foreground='White',width=8,relief=GROOVE)
logbutton.grid(row=2,column=1,padx=2,pady=2)
logbutton.bind('<Button-1>',click)

squarebutton=Button(buttonframe2,text='x²',font=font2,bg='darkOrange3',foreground='White',width=8,relief=GROOVE)
squarebutton.grid(row=2,column=2,padx=2,pady=2)
squarebutton.bind('<Button-1>',click)

#Buttons
#Row 1 buttons
button9=Button(buttonframe,text='9',font=font,bg='Grey',foreground='black',width=3,relief=GROOVE)
button9.grid(row=1,column=2)
button9.bind('<Button-1>',click)

button8=Button(buttonframe,text='8',font=font,bg='Grey',foreground='black',width=3,relief=GROOVE)
button8.grid(row=1,column=1)
button8.bind('<Button-1>',click)

button7=Button(buttonframe,text='7',font=font,bg='Grey',foreground='black',width=3,relief=GROOVE)
button7.grid(row=1,column=0)
button7.bind('<Button-1>',click)
#row 2 buttons
button6=Button(buttonframe,text='6',font=font,bg='Grey',foreground='black',width=3,relief=GROOVE)
button6.grid(row=2,column=2,)
button6.bind('<Button-1>',click)

button5=Button(buttonframe,text='5',font=font,bg='Grey',foreground='black',width=3,relief=GROOVE)
button5.grid(row=2,column=1)
button5.bind('<Button-1>',click)

button4=Button(buttonframe,text='4',font=font,bg='Grey',foreground='black',width=3,relief=GROOVE)
button4.grid(row=2,column=0)
button4.bind('<Button-1>',click)
#row 3 buttons 
button3=Button(buttonframe,text='3',font=font,bg='Grey',foreground='black',width=3,relief=GROOVE)
button3.grid(row=3,column=2)
button3.bind('<Button-1>',click)

button2=Button(buttonframe,text='2',font=font,bg='Grey',foreground='black',width=3,relief=GROOVE)
button2.grid(row=3,column=1)
button2.bind('<Button-1>',click)

button1=Button(buttonframe,text='1',font=font,bg='Grey',foreground='black',width=3,relief=GROOVE)
button1.grid(row=3,column=0)
button1.bind('<Button-1>',click)
#row 4 buttons
zerobutton=Button(buttonframe,text='0',font=font,bg='Grey',foreground='black',width=7,relief=GROOVE)
zerobutton.grid(row=4,column=0,columnspan=2,padx=2)
zerobutton.bind('<Button-1>',click)

dotbutton=Button(buttonframe,text='.',font=font,bg='Grey',foreground='black',width=3,relief=GROOVE)
dotbutton.grid(row=4,column=2)
dotbutton.bind('<Button-1>',click)


#column 3 buttons 

sumbutton=Button(buttonframe,text='+',font=font,bg='blue1',foreground='white',width=3,relief=GROOVE)
sumbutton.grid(row=1,column=3,padx=2,pady=1)
sumbutton.bind('<Button-1>',click)
subtractbutton=Button(buttonframe,text='-',font=font,bg='blue1',foreground='white',width=3,relief=GROOVE)
subtractbutton.grid(row=2,column=3,padx=2,pady=1)
subtractbutton.bind('<Button-1>',click)

multiplybutton=Button(buttonframe,text='x',font=font,bg='blue1',foreground='white',width=3,relief=GROOVE)
multiplybutton.grid(row=3,column=3,padx=2,pady=1)
multiplybutton.bind('<Button-1>',click)

dividebutton=Button(buttonframe,text='÷',font=font,bg='blue1',foreground='white',width=3,relief=GROOVE)
dividebutton.grid(row=4,column=3,padx=2,pady=1)
dividebutton.bind('<Button-1>',click)

#Column 4 buttons
equalbutton=Button(buttonframe,text='=',font=font,bg='darkOrange3',foreground='white',width=3,height=3,relief=GROOVE)
equalbutton.grid(row=3,rowspan=4,column=4,padx=1,pady=2)
equalbutton.bind('<Button-1>',click)

cbutton=Button(buttonframe,text='C',font=font,bg='Black',foreground='white',width=3,relief=GROOVE,command=AllClear)
cbutton.grid(row=2,column=4,padx=2,pady=2)
cbutton.bind('<Button-1>',click)

backbutton=Button(buttonframe,text='⌫',font=font,bg='Black',foreground='white',width=3,relief=GROOVE,command=delfun)
backbutton.grid(row=1,column=4,padx=2,pady=1,ipadx=2,ipady=2)
backbutton.bind('<Button-1>',click)

calculator.mainloop()