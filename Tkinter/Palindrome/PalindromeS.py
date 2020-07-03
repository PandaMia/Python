from tkinter import *
import sys, os 

def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    else:
        return os.path.join(os.path.abspath("."), relative)

def btn_check():  
    def is_palindrome(text):
        return cleaning(text) == reverse(text)

    def reverse(text):
        text = cleaning(text)
        text = text[::-1]
        return text

    def cleaning(text):
        forbidden = ('.', ',', '?', '!', ' ', '-', ':', '"', '—', '’', '\n')
        for i in forbidden:
            text = text.replace(str(i), '')
        text = text.lower()
        return text

    something = text_input.get('1.0', 'end')
    if something.replace(' ', '').replace('\n', '') == '':
        output['text'] = 'Скажи что-нибудь!'
    else:
        if (is_palindrome(something)):
            output['text'] = 'Да, это палиндром!'
        else:
            output['text'] = 'Нет, это не палиндром!'

root = Tk()
root.title('Palindrome scratch')
root.geometry('960x720')
root.resizable(width = False, height = False)

canvas = Canvas(root, width=960, height=720)
canvas.pack()

photoimage = PhotoImage(file = resource_path('фон.png'))
cat = PhotoImage(file = resource_path('cat.png'))
owl = PhotoImage(file = resource_path('owl.png'))
dialog_cat = PhotoImage(file = resource_path('диалог_кот.png'))
dialog_owl = PhotoImage(file = resource_path('диалог_сова.png'))
canvas.create_image(480, 360, image = photoimage)
canvas.create_image(240, 570, image = cat)
canvas.create_image(630, 425, image = owl)
canvas.create_image(320, 400, image = dialog_cat)
canvas.create_image(700, 270, image = dialog_owl)


output = Label(bg = 'white', font='constantia 16')
output['text'] = 'Скажи слово или фразу, \n а я отвечу \n палиндром это или нет'
output.place(x = 580, y = 200)

text_input = Text(root,
                  height = 3,
                  width = 20,
                  bd = 0,
                  wrap = 'word',
                  font = 'constantia 16')
text_input.place(x = 205, y = 330)

button_check = Button(root,
                      width = 20,
                      height = 2,
                      fg = '#FFD487', 
                      bg = '#1B49BF',
                      activebackground = '#376CD5',
                      font = 'sans 15')
button_check['text'] = 'Проверить'
button_check['command'] = btn_check
button_check.place(x = 630, y = 610)

root.mainloop()
