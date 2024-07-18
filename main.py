from tkinter import *
import time
from threading import Thread
blur=["#eae1bb","#eae1dd","#eae1ee"]
root=Tk()
root.title("Disappear Like Poooooffff!!!")
root.geometry("1000x1000")
root.config(background="#F0E3BC")
#Add weight to rows and column
def expand_tk(number):
    for i in range(number):
        root.columnconfigure(i, weight=1)
        root.rowconfigure(i, weight=1)


        

#function to Check the length of letter after five second
def timeout(text_entry):
    text_entry.delete("1.0", "end-1c")
# def timeout(event,words,text_entry):
#     words_fivesec=text_entry.get("1.0", "end-1c")
#     if words_fivesec>words:
#         continue_app(event,text_entry)
#     else:
#         text_entry.delete("1.0", "end-1c")

#Function to get the initial length of letter
def continue_app(event,text_entry):
    text_entry.config(fg="#F7DD72")
    words=text_entry.get("1.0", "end-1c")
    text_entry.after(2000,lambda:blur_text(event,words,text_entry))

def key_pressed(event,text_entry):
    if event.keysym:
            text_entry.config(fg="#F7DD72")
            text_entry.after(1000,lambda:continue_app(event,text_entry))
def change_color(event,text_entry,index=0):
    if index<len(blur):
         text_entry.bind("<Key>",lambda event:key_pressed(event,text_entry))
         text_entry.config(fg=blur[index])
         text_entry.after(1000,lambda:change_color(event,text_entry,index+1))
    
    else:
        timeout(text_entry)


    
def blur_text(event,words,text_entry):
    words_fivesec=text_entry.get("1.0", "end-1c")
    if words_fivesec>words:
        continue_app(event,text_entry)
        
    else:
        
        change_color(event,text_entry)
        
        

    

#Start the Text editor
def start_app():
    expand_tk(3)
    text_entry=Text(root,relief="flat",bg="#14EBAE",fg="#F7DD72",bd=2,font=("Arial",14,"bold"))
    text_entry.grid(column=1,row=1,sticky="nsew")
    text_entry.focus_set()
    text_entry.bind("<Key>",lambda event:continue_app(event,text_entry))
        
        
    # timeout(text_entry)
    # Thread(target=lambda:timeout(text_entry)).start()
    
    
    
    # text_entry.after(5000,timeou,text_entry)
#Destroy button after clicking start
def destroy_start():
    start_button.destroy()
    start_app()
expand_tk(3)
start_button=Button(root,text="START",command=destroy_start)
start_button.grid(column=1,row=1,sticky="ew")


root.mainloop()