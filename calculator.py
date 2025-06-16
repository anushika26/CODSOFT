from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry("400x600")
root.resizable(0,0)
def click():
  s=int()
  a=int(e1.get())
  b=int(e2.get())
  if v.get()=='+':
    c=a+b
    s=s+c
  if v.get()=='-':
    c=a-b
    s=s+c
  if v.get()=='*':
    c=a*b
    s=s+c
  if v.get()=='/':
    if b==0:
      s="Cannot divide by 0."
    else:
      c=a/b
      s=s+c
  lbl4.config(text=s)
lbl1=Label(root,text='Number1',font=('Arial Bold',14),fg='Yellow',bg='Black')
lbl1.grid(row=0,column=0,padx=5,pady=5)
e1=Entry(root,font=('Arial Bold',14))
e1.grid(row=0,column=1,padx=5,pady=5)
lbl2=Label(root,text='Number2',font=('Arial Bold',14),fg='Yellow',bg='Black')
lbl2.grid(row=1,column=0,padx=5,pady=5)
e2=Entry(root,font=('Arial Bold',14))
e2.grid(row=1,column=1,padx=5,pady=5)
lbl3=Label(root,text='Operation',font=('Arial Bold',14))
lbl3.grid(row=2,column=0,padx=5,pady=5)
v=StringVar()
v.set(" ")
chk=Radiobutton(root,text='+',variable=v,value='+',font=('Arial Bold',14))
chk.grid(row=2,column=1)
chk=Radiobutton(root,text='-',variable=v,value='-',font=('Arial Bold',14))
chk.grid(row=2,column=2)
chk=Radiobutton(root,text='*',variable=v,value='*',font=('Arial Bold',14))
chk.grid(row=3,column=1)
chk=Radiobutton(root,text='/',variable=v,value='/',font=('Arial Bold',14))
chk.grid(row=3,column=2)
but=Button(root,text='Press',font=('Arial Bold',14),command=click)
but.grid(row=4,column=0,padx=5,pady=5)
lbl4=Label(root,text='Result',font=('Arial Bold',14))
lbl4.grid(row=4,column=1,padx=5,pady=5)
root.mainloop()
