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
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Use headless to not display the website
options = Options()
options.add_argument("--headless")

PATH= "C:\Program Files (x86)\Webdriver\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=options)


window = tk.Tk()
window.title("Med-Observer")

window.geometry('1080x700')
#frame = tk.Frame(window)
#frame.pack()

# Use ttk.Style to customize widgets
style = ttk.Style()
style.configure('TLabel', font=('arial', 12, 'bold'), borderwidth='4', foreground='green')
style.configure('TButton', font=('arial', 12, 'bold', 'underline'), borderwidth='4', foreground='green')

# students = tk.Label(window, text="Derrick Phung - Kushal Rajam - Sumanth Pallamreddy - Advisor: Katy Kuei")
# students.grid(row=0,column=1)

# open Mission HS image
mission = "C://Users/kevin/Documents/Samsung Solve for Tomorrow/msjhs.JPG"
# img = Image.open(file)
# img.Show()

missionImg = ImageTk.PhotoImage(Image.open(mission))
tk.Label(window, image=missionImg).grid(row=1, column=1)
#panel = tk.Label(window, image=img)
#panel.pack(side="left", fill = "both", expand = "yes", padx=100, pady=0)

# open Samsung Solve for Tomorrow image
samsung = "C://Users/kevin/Documents/Samsung Solve for Tomorrow/samsung.JPG"

samsungImg = ImageTk.PhotoImage(Image.open(samsung))
tk.Label(window, image=samsungImg).grid(row=2, column=1)

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
    # Clear the screen
    text.config(state=tk.NORMAL)
    text.delete('1.0', tk.END)
    
    text.insert(tk.END, "\n" + "...Readying..." + "\n")
    
    state = sMenu.get()
    #print("State: " + state)
    text.insert(tk.END, "State: " + str(state) + "\t")
    county = cMenu.get()
    #print("County: " + county)
    text.insert(tk.END, "\t" + "County: " + str(county) + "\n")

# Use ttk.Style to add a custom style to the widget. Standard tk does not have Style definition
#lbl1 = tk.Label(window, text="Hospital")
stateLabel = ttk.Label(window, text="State", style='TLabel', anchor='w')
stateLabel.grid(row=3,column=0)
#txt1 = tk.Entry(window,width=50) 
#txt1.grid(row=2,column=1)

# State pulldown menu
sMenu = ttk.Combobox(window, value=states)
# sMenu.current(4)
sMenu.SelectedText = "None"
sMenu.grid(row=3,column=1)
sMenu.bind("<<ComboboxSelected>>", sClicked)

#lbl2 = tk.Label(window, text="Search")
countyLabel = ttk.Label(window, text="County", style='TLabel')
countyLabel.grid(row=4,column=0)
#txt2 = tk.Entry(window,width=50)
#txt2.grid(row=3,column=1)

# County pulldown menu
cMenu = ttk.Combobox(window, value=counties)
cMenu.current(0)
cMenu.grid(row=4,column=1)
# cMenu.bind("<<ComboboxSelected>>", cClicked)

def spin():
    # Clear the screen
    #text.config(state=tk.NORMAL)
    #text.delete('1.0', tk.END)
    
    # open spinGlobe
    #spinGlobe = "C://Users/kevin/Documents/Samsung Solve For Tomorrow/loading.gif"
    #spinImg = ImageTk.PhotoImage(Image.open(spinGlobe))
    #tk.Label(text, image=spinImg)
    text.insert(tk.END, "\n" + "...Computing..." + "\n")

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
            #rows = len(rwdata)
            #print("Num of Rows: " + len(rwdata))
            #text.insert(tk.END, str(rows))
            #cols = len(rwdata[0])
            #print("Num of Cols: " + len(rwdata[0]))
            #text.insert(tk.END, str(cols))
            text.insert(tk.END, "\n")
            for r in rwdata:
                data = r.text
                text.insert(tk.END, str(data) + " ")
                #print(data)
                
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

btn = ttk.Button(window, text="Compute", style='TButton', command=lambda:[spin(), clicked()])
#btn = tk.Button(window, text="Compute", command=clicked)
btn.grid(row=6,column=1, padx=100, pady=10)

# lbl3=ttk.Label(window, text="Result", style='TLabel')
# lbl3.grid(row=7,column=1)

scrollbar = tk.Scrollbar(window)
text = tk.Text(window, width=120, height=20, font=('arial', 11), wrap='word')

text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)

text.grid(row=8, column=1, padx=5, pady=5)

# Introduction
text.insert(tk.END, "2021-2022 Samsung Solve for Tomorrow" + "\n")
text.tag_add("header", "1.0", "2.0")
text.tag_config("header", justify="center", font=('arial', 16, 'bold'), background="light blue", foreground="blue")

text.insert(tk.END, "\n" + "The United States and the world has entered into the 3rd year of the COVID-19 pandemic with no end in sight." + "\n")
text.insert(tk.END, "\n" + "As we proceed cautiously into the unknown future with many variants of the virus Delta, Omicron,... that are still spreading wildly among us, no one knows what forms the virus will mutate in the course of time. While there are many unknowns, we stand united across many nations, regardless of races and social statuses in a common goal of getting back our lives together. We all share a desire of finding a solution to defeat the deadly virus." + "\n")
text.insert(tk.END, "\n" + "We may all be affected by the pandemic but that does not mean we are unable to help those that are influenced by the pandemic. Thus, our aim is to inform concerned citizens about their nearest available hospital when an emergency arises." + "\n")
text.insert(tk.END, "\n" + "We, Fremont Med Corp (FMC), present to you Med-Observer!" + "\n")
text.tag_add("welcome", "9.0", "10.0")
text.tag_config("welcome", justify="center", font=('arial', 11, 'italic'))
window.mainloop()
