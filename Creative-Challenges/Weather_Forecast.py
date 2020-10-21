from tkinter import *
import requests

city = input('Enter city name: ')


url = 'http://api.openweathermap.org/data/2.5/weather?q=London&appid=184f57ba41848e91f08939cf49fada3d'.format(city)

res = requests.get(url)

data = res.json()


print(data)



# Setting up the GUI
root = Tk()
root.geometry('400x200')
root.title('Weather Forecast')
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Hong Kong", fg="purple")
button2 = Button(topFrame, text="UK, London", fg="blue")
button3 = Button(topFrame, text="UK, Exeter", fg='black')
button4 = Button(bottomFrame, text="Quit Application", fg="green")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
root.mainloop()