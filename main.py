#script is based off of framework provided by Dr. Angela Yu, 100 Days of Code: The Complete Python Pro Bootcamp for 2023, day 33.
#customized to call to a different API, and to include the author and a different button.
#quotes from https://github.com/tlcheah2/stoic-quote-lambda-public-api

from tkinter import *

import requests

root = Tk()

#list of image file names I want to rotate through, from dall-e prompts, variations, and edits (within platform):
#can streamline this with range later
image_names = ['dall_e_cloud0.png', 'dall_e_cloud1.png', 'dall_e_cloud2.png', 'dall_e_cloud3.png', 'dall_e_cloud4.png', 'dall_e_cloud5.png', 'dall_e_cloud6.png', 'dall_e_cloud7.png', 'dall_e_cloud8.png', 'dall_e_cloud9.png', 'dall_e_cloud10.png', 'dall_e_cloud11.png', 'dall_e_cloud12.png', 'dall_e_cloud13.png', 'dall_e_cloud14.png', 'dall_e_cloud15.png', 'dall_e_cloud16.png', 'dall_e_cloud17.png', 'dall_e_cloud18.png']

#used chatGPT to help here, start
#list of objects
images = [PhotoImage(file=image_name) for image_name in image_names]

# Define a function to change the image on the button
def change_image():
    global current_image
    current_image += 1
    if current_image >= len(images):
        current_image = 0
    button.config(image=images[current_image])
#used chatGPT to help here, end
  
#create the get_quote function, to get the random stoic quote:
def get_quote():
  pass
  quote_response = requests.get(
    url="https://api.themotivate365.com/stoic-quote")
  quote_response.raise_for_status()
  data = quote_response.json()
  who = data["author"]
  quote = data["quote"]
  canvas.itemconfig(quote_text, text=quote)
  canvas.itemconfig(who_text, text=who)

#create a function that runs both quote and image function.
def quote_and_image():
  get_quote()
  change_image()


window = Tk()
window.title('Some Stoicism for the day...')
window.config(padx=25, pady=25)

canvas = Canvas(width=1100, height=210)
background_img = PhotoImage(file="quotebox_3.png")
canvas.create_image(550, 110, image=background_img)
quote_text = canvas.create_text(500,
                                100,
                                text="click the cloud",
                                width=800,
                                font=("Arial", 12, "bold"),
                                fill="white")
who_text = canvas.create_text(550,
                              160,
                              text="",
                              width=250,
                              font=("Arial", 10, "bold"),
                              fill="yellow")
canvas.grid(row=1, column=0)


#used chatGPT to help here, start
# Set the initial image index
current_image = 0

button = Button(image=images[current_image], highlightthickness=0, command=quote_and_image)
button.grid(row=2, column=0)
#used chatGPT to help here, end

root.mainloop()
window.mainloop()
