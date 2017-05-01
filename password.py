import random
from tkinter import *

dict = ('w','e','r','t','y','u','i','o','p','[',']','a','s','d','f','g','h','j','k','l',';','<','>','#','@','$','&','-',
         'z','x','c','v','b','n','m',',','.','/','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L'
        ,'Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','0','=','!','№',';','%',':','?','*','\\','+')

dict_digit = ('1','2','3','4','5','6','7','8','9','0','=','!','№',';','%',':','?','*','\\','+','[',']',
              ';', '<', '>', '#', '@', '$', '&', '-',',','.','/')

dict_latin = ('w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L'
               ,'Z','X','C','V','B','N','M','z','x','c','v','b','n','m')


dict_latin_digit = ('w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L'
                     ,'Z','X','C','V','B','N','M','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0')



root = Tk()
root.title("Generator of passwords")

var=IntVar()

def proverka(event):

    l = entry_input.get()
    metod = var.get()
    try:


        if metod == 1:
            tmp = 0
            pasword = []

            while tmp < int(l):
                choice = random.choice(dict)
                pasword.append(choice)
                tmp += 1

            out = ''.join(pasword)
            Label_output["text"] = out

        if metod == 2:
            tmp = 0
            pasword = []

            while tmp < int(l):
                choice = random.choice(dict_digit)
                pasword.append(choice)
                tmp += 1

            out = ''.join(pasword)
            Label_output["text"] = out

        if metod == 3:
            tmp = 0
            pasword = []

            while tmp < int(l):
                choice = random.choice(dict_latin_digit)
                pasword.append(choice)
                tmp += 1

            out = ''.join(pasword)
            Label_output["text"] = out
    except:
        Label_output["text"] = "укажите длину пароля!"




Label_input = Label(root,text = 'Длина пароля ')
Label_input.grid(column = 0 , row = 0,sticky ='w' )

Label_out = Label(root,text = 'Ваш пароль : ')
Label_out.grid(column = 0 , row = 1,sticky ='w')


entry_input = Entry(root,width = 5)
entry_input.grid(column = 1,row = 0,sticky ='w')

Button_input = Button(root,text = 'Ok')
Button_input.grid(column =2 , row = 0)
Button_input.bind("<Button-1>",proverka)

Frame_output = Frame(root,bg='red',bd=0.5)
Frame_output.grid(column = 1 ,row =1,sticky ='w')
Label_output = Label(Frame_output,width = 20,bg = "white")
Label_output.grid(column = 3, row =1,sticky ='w' )


rbutton1=Radiobutton(root,text='использовать все знаки',variable=var,value=1)
rbutton1.grid(column = 0, row = 2,sticky ='w' )
rbutton2=Radiobutton(root,text='использовать цифры и символы',variable=var,value=2)
rbutton2.grid(column = 0, row = 3,sticky ='w' )
rbutton3=Radiobutton(root,text='использовать буквы и цифры',variable=var,value=3)
rbutton3.grid(column = 0, row = 4,sticky ='w' )




root.mainloop()