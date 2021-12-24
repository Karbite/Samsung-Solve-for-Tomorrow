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
from selenium.webdriver.support.ui import Select

# Use headless to not display the website
# options = Options()
# options.add_argument("--headless")
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

driver.get("https://data.rgj.com/covid-19-hospital-capacity/")

# State Dropdown menu options
states = []
select = Select(WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "state"))))
options = select.options
for option in options:
    states.append(option.text)

counties = [
    "All"
    ]

def sClicked(e):
    state = sMenu.get()
    print("State: " + state)
    searchState = Select(driver.find_element_by_id("state"))
    searchState.select_by_visible_text(state)
    
    print("Search County: " + "\n")
    counties.clear()
    # County Dropdown menu options
    select = Select(WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "location"))))
    options = select.options
    for option in options:
        print(option.text)
        counties.append(option.text)
    
    cMenu.config(value=counties)
    
def cClicked(e):
    state = sMenu.get()
    print("State: " + state)
    county = cMenu.get()
    print("County: " + county)

# Use ttk.Style to add a custom style to the widget. Standard tk does not have Style definition
#lbl1 = tk.Label(window, text="Hospital")
stateLabel = ttk.Label(window, text="State", style='TLabel')
stateLabel.grid(row=2,column=0)
#txt1 = tk.Entry(window,width=50) 
#txt1.grid(row=2,column=1)

# State pulldown menu
sMenu = ttk.Combobox(window, value=states)
sMenu.current(4)
sMenu.grid(row=2,column=1)
sMenu.bind("<<ComboboxSelected>>", sClicked)

#lbl2 = tk.Label(window, text="Search")
countyLabel = ttk.Label(window, text="County", style='TLabel')
countyLabel.grid(row=3,column=0)
#txt2 = tk.Entry(window,width=50)
#txt2.grid(row=3,column=1)

# County pulldown menu
cMenu = ttk.Combobox(window, value=counties)
cMenu.current(0)
cMenu.grid(row=3,column=1)
cMenu.bind("<<ComboboxSelected>>", cClicked)

def clicked():
#    res = txt1.get() + " " + txt2.get()
    state = sMenu.get()
    county = cMenu.get()

    driver.get("https://data.rgj.com/covid-19-hospital-capacity/")
    #print(driver.title)
    
    searchState = Select(driver.find_element_by_id("state"))
    searchState.select_by_visible_text(state)
    #searchState.select_by_value(state)
    
    #searchCounty = Select(driver.find_element_by_id("carea"))
    searchCounty = Select(WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "location"))))
    #time.sleep(5)
    searchCounty.select_by_value(county)
  
    submit = driver.find_element_by_id("submit")
    submit.click()
    
    title = driver.title
    
    #searchState = driver.find_element_by_id("state")
    #searchState.send_keys(state)
    #searchCounty = driver.find_element_by_id("carea")
    #searchCounty.send_keys(county)
    
    #print(driver.page_source)
    
    try:
        cnty = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "cnty")))
        print(title)
        
        # Clear the screen
        text.config(state=tk.NORMAL)
        text.delete('1.0', tk.END)
        
        text.insert(tk.END, str(title) + "\n")
        # text.insert(tk.END, "Search results:" + "\n")
        # print("Search results:")
        
        header = driver.find_element_by_class_name("panel-title")
        data = header.text
        print(data)
        text.insert(tk.END, str(data) + "\n")
        
        print("Individual search:")
        cntys = driver.find_elements_by_id("cnty")
        # traverse list
        for cnty in cntys:
            
            td = cnty.find_element_by_class_name("ac")
            data = td.text
            print(data)
            text.insert(tk.END, str(data) + "\t")
            
            ac = cnty.find_element_by_class_name("ac.bg1")
            td = ac.find_element_by_class_name("qt")
            # td = cnty.find_element_by_class_name("qt")
            data = td.text
            print(data)
            text.insert(tk.END, str(data) + "\t")
            
            ac = cnty.find_element_by_class_name("ac.bg2")
            td = ac.find_element_by_class_name("qt")
            # td = cnty.find_element_by_class_name("qt")
            data = td.text
            print(data)
            text.insert(tk.END, str(data) + "\t")
            
            td = cnty.find_element_by_class_name("ac.bg3")
            data = td.text
            print(data)
            text.insert(tk.END, str(data) + "\n")
            
            # identifying the rows having <td> tag
            rwdata = cnty.find_elements_by_xpath("//table/tbody/tr/td")
            # len method is used to get the size of that list
            print(len(rwdata))
            for r in rwdata:
                print(r.text)
                
            #header = cnty.find_element_by_tags_name("h3")
            #header = cnty.find_element_by_class_name("panel-title")
            # get_attribute() to get all h3 class
            #header = cnty.get_attribute("class")
            #print(header)
            #text.insert(tk.END, str(header) + "\n")
            
            #data = cnty.text          
            #print(data)
            #text.insert(tk.END, str(data) + "\n")

    except:
#    finally:
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
