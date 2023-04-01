#script is based off of framework provided by Dr. Angela Yu, 100 Days of Code: The Complete Python Pro Bootcamp for 2023, day 33.
#customized to call to a different API, and to include the author and a different button.
#quotes from https://github.com/tlcheah2/stoic-quote-lambda-public-api


from tkinter import *
import requests

def get_quote():
    pass
    quote_response = requests.get(url="https://api.themotivate365.com/stoic-quote")
    quote_response.raise_for_status()
    data = quote_response.json()
    who = data["author"]
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)
    canvas.itemconfig(who_text, text=who)
    
window = Tk()
window.title('Some Stoicism for the day...')
window.config(padx=50, pady=50)

canvas = Canvas(width=1100, height=450)
background_img = PhotoImage(file="quotebox.png")
canvas.create_image(650, 250, image=background_img)
quote_text = canvas.create_text(650, 175, text="click the cloud", width=450, font=("Arial", 16, "bold"), fill="black")
who_text = canvas.create_text(650, 350, text="", width=250, font=("Arial", 16, "bold"), fill="brown")
canvas.grid(row=0, column=0)

who_img = PhotoImage(file="cloud_dalle.png")
who_button = Button(image=who_img, highlightthickness=0, command=get_quote)
who_button.grid(row=1, column=0)



window.mainloop()