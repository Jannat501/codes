#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import * 
root = Tk() 
root.title("Chatbot") 
def send(): 
    send = "You ‐> " + e.get() 
    txt.insert(END, "\n" + send) 
    user = e.get().lower() 
    if(user == "hello"): 
        txt.insert(END, "\n" + "Bot ‐> Hi") 
    elif(user == "hi" or user == "hii" or user == "hiiii"): 
        txt.insert(END, "\n" + "Bot ‐> Hello") 
    elif(e.get() == "how are you"): 
        txt.insert(END, "\n" + "Bot ‐> I am fine, what about you?") 
    elif(user == "fine" or user == "i am good" or user == "i am doing good"): 
        txt.insert(END, "\n" + "Bot ‐> Great! how can I help you?") 
    elif(user == "bye" or user == "ok bye" or user == "cya"): 
        txt.insert(END, "\n" + "Bot ‐> Bye, see you soon!!!") 
    else: 
        txt.insert(END, "\n" + "Bot ‐> Sorry! I did not get you, can you please try again") 
    e.delete(0, END) 
txt = Text(root) 
txt.grid(row=0, column=0, columnspan=2) 
e = Entry(root, width=100) 
e.grid(row=1, column=0) 
send = Button(root, text="Send", command=send).grid(row=1, column=1) 
root.mainloop()               


# In[ ]:





# In[9]:


from tkinter import *
root = Tk()
root.title("Chat bot")

def send():
    send = "You->"+e.get()
    txt.insert(END,"\n"+send)
    user = e.get().lower()
    if(user == "hi"):
        txt.insert(END,"\n"+"Bot-> Hello")
    elif(user == "name plz"):
        txt.insert(END,"\n"+"Bot-> ChatBot")
    else:
        txt.insert(END,"\n"+"Bot-> Cant understood")
    e.delete(0,END)    

txt = Text(root)
txt.grid(row = 0,column = 0,columnspan = 2)
e = Entry(root,width = 100)
e.grid(row = 1,column = 0)
send  = Button(root,text = "Send",command = send).grid(row = 1,column =1)
root.mainloop()


# In[ ]:





# In[ ]:





# In[11]:


from tkinter import *

root = Tk()
root.title("Chatbot")



def send():
    send = "You->"+e.get()
    txt.insert(END,"\n"+send)
    user = e.get().lower()
    if(user == "hi"):
        txt.insert(END,"\n"+"Bot-> Hello sir !!!")
    elif(user == "name plz" or user == "what is your name"):
        txt.insert(END,"\n"+"Bot-> I am chat Bot !!!")
    else:
        txt.insert(END,"\n"+"Bot-> Not understand !!!")  
    e.delete(0,END) 
    
    
    
txt = Text(root)
txt.grid(row = 0,column = 0,columnspan=2)
e = Entry(root,width = 100)
e.grid(row = 1,column =0)
send = Button(root,text = "send",command = send).grid(row = 1,column =1)
root.mainloop()



# In[ ]:


https://github.com/pranavawa/LP2


# In[ ]:





# In[ ]:




