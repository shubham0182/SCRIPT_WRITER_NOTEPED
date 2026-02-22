import pyautogui as s
import time

s.press('win')
time.sleep(1)

s.write('notepad',interval=0.2)
s.press('enter')

time.sleep(1)

s.write("“Hello and welcome! I’m Thakor Shubham, a passionate data science student on a journey to uncover insights from data and solve real-world problems. Here, you’ll find my projects, learning experiences, and explorations into Python, machine learning, and analytics.Let’s explore the fascinating world of data together!”",interval=0.2)
s.press("enter")

s.write("shubham sir",interval=0.2)
s.press("enter")