from tkinter import *
import random

generated_password = ""

window = Tk()
window.title("Password Generator V.0.1")
window.configure(width=500, height=700)
window.configure(bg='white')

def validate_lenght_pw():
  global generated_password
  generated_password = ""
  if(val_check_button1 or val_check_button2 or val_check_button3 or val_check_button4):
    try:
      tmp = int(pw_lenght_input.get())
      if(tmp > 100):
        password_output.config(text="I dont think you need such a long password ._. insert a lower number please.")
      else:
        tmp = generate_password(tmp)
        pass_list_to_string(tmp)
        password_output.config(text=generated_password)
    except ValueError:
        password_output.config(text="This is not a Number!")
  else:
    password_output.config(text="You have to tick something. Cant generate a password from nothing :)")
  
def pass_list_to_string(tmp):
  for i in tmp:
    global generated_password
    generated_password += i


def generate_password(lenght_of_password):
  tmp_pw = []
  for i in range(lenght_of_password):
    if(val_check_button1.get() and val_check_button2.get() and val_check_button3.get() and val_check_button4.get()):
      x = random.randint(0, 3)
      y = 0
      if(x == 0):
        y = random.randint(0, 24)
      elif(x == 1):
        y = random.randint(0,9)
      elif(x == 2):
        y = random.randint(0,25)
      elif(x == 3):
        y = random.randint(0,25)
      tmp_pw.append(get_random_char(x,y))

    if(val_check_button1.get() == 0 and val_check_button2.get() and val_check_button3.get() and val_check_button4.get()):
      x = random.randint(1, 3)
      y = 0
      if(x == 0):
        y = random.randint(0, 24)
      elif(x == 1):
        y = random.randint(0,9)
      elif(x == 2):
        y = random.randint(0,25)
      elif(x == 3):
        y = random.randint(0,25)
      tmp_pw.append(get_random_char(x,y))

    if(val_check_button1.get() and val_check_button2.get() == 0 and val_check_button3.get() and val_check_button4.get()):
      x = 1
      while(x == 1):
        x = random.randint(0, 3)
      y = 0
      if(x == 0):
        y = random.randint(0, 24)
      elif(x == 1):
        y = random.randint(0,9)
      elif(x == 2):
        y = random.randint(0,25)
      elif(x == 3):
        y = random.randint(0,25)
      tmp_pw.append(get_random_char(x,y))

    if(val_check_button1.get() and val_check_button2.get() and val_check_button3.get() == 0 and val_check_button4.get()):
      x = 2
      while(x == 2):
        x = random.randint(0, 3)
      y = 0
      if(x == 0):
        y = random.randint(0, 24)
      elif(x == 1):
        y = random.randint(0,9)
      elif(x == 3):
        y = random.randint(0,25)
      tmp_pw.append(get_random_char(x,y))

    if(val_check_button1.get() and val_check_button2.get() and val_check_button3.get() and val_check_button4.get() == 0):
      x = random.randint(0, 2)
      y = 0
      if(x == 0):
        y = random.randint(0, 24)
      elif(x == 1):
        y = random.randint(0,9)
      elif(x == 2):
        y = random.randint(0,25)
      tmp_pw.append(get_random_char(x,y))

    if(val_check_button1.get() == 0 and val_check_button2.get() == 0 and val_check_button3.get() and val_check_button4.get() == 0):
      x = 2
      y = 0
      if(x == 2):
        y = random.randint(0,25)
      tmp_pw.append(get_random_char(x,y))
    if(val_check_button1.get() and val_check_button2.get() == 0 and val_check_button3.get() and val_check_button4.get() == 0):
      x = 1
      while(x == 1 or x == 3):
        x = random.randint(0,3)
      y = 0
      if(x == 2):
        y = random.randint(0,25)
      tmp_pw.append(get_random_char(x,y))
    if(val_check_button1.get() and val_check_button2.get() and val_check_button3.get() == 0 and val_check_button4.get() == 0):
      x = random.randint(0,1)
      y = 0
      if(x == 0):
        y = random.randint(0, 24)
      elif(x == 1):
        y = random.randint(0,9)
      tmp_pw.append(get_random_char(x,y))
    if(val_check_button1.get() == 0 and val_check_button2.get() and val_check_button3.get() and val_check_button4.get() == 0):
      x = 0
      while(x == 0 or x == 3):
        x = random.randint(1,2)
      y = 0
      if(x == 1):
        y = random.randint(0,9)
      elif(x == 2):
        y = random.randint(0,25)
      tmp_pw.append(get_random_char(x,y))
    if(val_check_button1.get() and val_check_button2.get() == 0 and val_check_button3.get() == 0 and val_check_button4.get()):
      x = 1
      while(x == 1 or x == 2):
        x = random.randint(0,3)
      y = 0
      if(x == 0):
        y = random.randint(0, 24)
      elif(x == 3):
        y = random.randint(0,25)
      tmp_pw.append(get_random_char(x,y))
    if(val_check_button1.get() == 0 and val_check_button2.get() and val_check_button3.get() == 0 and val_check_button4.get()):
      x = 0
      while(x == 0 or x == 2):
        x = random.randint(1,3)
      y = 0
      if(x == 1):
        y = random.randint(0,9)
      elif(x == 3):
        y = random.randint(0,25)
      tmp_pw.append(get_random_char(x,y))
    if(val_check_button1.get() == 0 and val_check_button2.get() == 0 and val_check_button3.get() and val_check_button4.get()):
      x = 0
      while(x == 0 or x == 1):
        x = random.randint(2,3)
      y = 0
      if(x == 2):
        y = random.randint(0,25)
      elif(x == 3):
        y = random.randint(0,25)
      tmp_pw.append(get_random_char(x,y))
  return tmp_pw

def get_random_char(x,y):
  return list_of_all_characters[x][y]

def copy_to_clipboard():
  window.clipboard_clear()
  window.clipboard_append(generated_password)



val_check_button1 = IntVar()
val_check_button2 = IntVar()
val_check_button3 = IntVar()
val_check_button4 = IntVar()

check_button1 = Checkbutton(window, text="Symbols? --> (!?²³$%&/*", variable=val_check_button1, onvalue=1, offvalue=0, height=2, width=25, bg='white')
check_button2 = Checkbutton(window, text="Numbers? --> 1234567890", variable=val_check_button2, onvalue=1, offvalue=0, height=2, width=25, bg='white')
check_button3 = Checkbutton(window, text="Lowercase Letters? --> abc...", variable=val_check_button3, onvalue=1, offvalue=0, height=2, width=25, bg='white')
check_button4 = Checkbutton(window, text="Uppercase Letters? --> ABC...", variable=val_check_button4, onvalue=1, offvalue=0, height=2, width=25, bg='white')
ask_lenght_of_pw = Label(window, text="How long should the password be?", bg='white')
password_output = Label(window, text='')
pw_lenght_input = Entry(window, bd=1)
generate_button = Button(window, text="Generate it!", command=validate_lenght_pw)
clipboard_button = Button(window, text="Copy to clipboard", command=copy_to_clipboard)


symbols = ['!', '"', '§', '$', '%', '&', '/', '(', ')', '=', '?', '|', '<', '>', '²', '³', '@', '_', '-', ',', '.', ':', ';', '*', '~']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_of_all_characters = [symbols, numbers, lowercase_letters, uppercase_letters]
print(str(len(symbols)), str(len(numbers)), str(len(lowercase_letters)), str(len(uppercase_letters)))


check_button1.pack(side= TOP)
check_button2.pack()
check_button3.pack()
check_button4.pack()
ask_lenght_of_pw.pack(side= LEFT)
pw_lenght_input.pack()
generate_button.pack()
password_output.pack()
clipboard_button.pack(pady=20)


window.mainloop()