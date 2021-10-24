# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:10:27 2021
@author: derrickp, sumanthp, kushalr
https://sites.google.com/a/chromium.org/chromedriver/downloads
https://sites.google.com/chromium.org/driver/
"""
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH="C:\Program Files (x86)\Webdriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

window = tk.Tk()
window.title("Mission San Jose High School - Chemistry Class - Ms Kuei")

window.geometry('1000x600')
#frame = tk.Frame(window)
#frame.pack()

# Use ttk.Style to customize widgets
style = ttk.Style()
style.configure('TLabel', font=('arial', 12, 'bold'), borderwidth='4', foreground='green')
style.configure('TButton', font=('arial', 12, 'bold', 'underline'), borderwidth='4', foreground='green')

students = tk.Label(window, text="Derrick Phung - Kushal Rajam - Sumanth Pallamreddy")
students.grid(row=0,column=1)

# open image
file = "C://Users/kevin/Documents/Samsung Solve for Tomorrow/msjhs.JPG"
# img = Image.open(file)
# img.Show()

img = ImageTk.PhotoImage(Image.open(file))
tk.Label(window, image=img).grid(row=1, column=1)
#panel = tk.Label(window, image=img)
#panel.pack(side="left", fill = "both", expand = "yes", padx=100, pady=0)

# Use ttk.Style to add a custom style to the widget. Standard tk does not have Style definition
#lbl1 = tk.Label(window, text="Hospital")
lbl1 = ttk.Label(window, text="Hospital", style='TLabel')
lbl1.grid(row=2,column=0)
txt1 = tk.Entry(window,width=50) 
txt1.grid(row=2,column=1)

#lbl2 = tk.Label(window, text="Search")
lbl2 = ttk.Label(window, text="Search", style='TLabel')
lbl2.grid(row=3,column=0)
txt2 = tk.Entry(window,width=50)
txt2.grid(row=3,column=1)

def clicked():
    res = txt1.get() + " " + txt2.get()
    driver.get("https://bing.com")
    print(driver.title)
    search = driver.find_element_by_id("sb_form_q")
    search.send_keys(res)
    search.send_keys(Keys.RETURN)
    #print(driver.page_source)
    
    try:
        # b_algo = WebDriverWait(driver, 10).until(
        #    EC.presence_of_element_located((By.CLASS_NAME, "b_algo")))
        b_results = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "b_results")))
        print("Search results:")
        print(b_results.text)
        
        print("Individual search:")
        links = b_results.find_elements_by_tag_name("a")
        # traverse list
        for link in links:
            # get_attribute() to get all href
            href = link.get_attribute("href")
            print(href)
            text.insert(tk.END, str(href) + "\n")

#    except:
    finally:
        driver.quit()
        
    # element = b_results.find_elements_by_partial_link_text("https")
    # element = b_results.find_element_by_tags_name("h2")
    # print(element.text)
    # lbl_sum.configure(text=element.text).grid(column=1)

btn = ttk.Button(window, text="Compute", style='TButton', command=clicked)
#btn = tk.Button(window, text="Compute", command=clicked)
btn.grid(row=5,column=1, padx=100, pady=10)

lbl3=ttk.Label(window, text="Result", style='TLabel')
lbl3.grid(row=6,column=1)

scrollbar = tk.Scrollbar(window)
text = tk.Text(window, width=100, height=20)

text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)

text.grid(row=7, column=1, padx=5, pady=5)

window.mainloop()

