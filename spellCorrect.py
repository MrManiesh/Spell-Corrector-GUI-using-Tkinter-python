# import all functions / classes from the tkinter
from tkinter import *
from textblob import TextBlob

# Function to clear both the text entry boxes
def clearAll() :
	
	# whole content of text entry area is deleted
	word1_field.delete(0, END)
	word2_field.delete(0, END)

# Function to get a corrected word
def correction() :

	# get a content from entry box
	input_word = word1_field.get()

	# create a TextBlob object
	blob_obj = TextBlob(input_word)

	# get a corrected word
	corrected_word = str(blob_obj.correct())

	# insert method inserting the
	# value in the text entry box.
	word2_field.insert(10, corrected_word)


# Driver code
if __name__ == "__main__" :

	# Create a GUI window
	root = Tk()

	# Set the background colour of GUI window
	root.configure(background = 'black')
	
	# Set the configuration of GUI window (WidthxHeight)
	root.geometry("400x200")

	# set the name of tkinter GUI window
	root.title("Spell Corrector")
	
	# Create Welcome to Spell Corrector Application: label
	headlabel = Label(root, text = 'Welcome to Spell Corrector Application',
					fg = 'white', bg = 'black',font=('Georgia', 13, 'bold'))
	
	# Create a "Input Word": label
	label1 = Label(root, text = "Input Word",
				fg = 'white', bg = 'black',font=('Georgia', 13, 'bold'))
		
	# Create a "Corrected Word": label
	label2 = Label(root, text = "Corrected Word",
				fg = 'white', bg = 'black',font=('Georgia', 13, 'bold'))
	
	
	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	# padx keyword argument used to set padding along x-axis .
	headlabel.grid(row = 0, column = 0, columnspan=2,pady=10, padx=10)
	label1.grid(row = 1, column = 0)
	label2.grid(row = 3, column = 0)

		
	# Create a text entry box
	# for filling or typing the information.
	word1_field = Entry(root, width=30)
	word2_field = Entry(root, width=30)
		
	# padx keyword argument used to set padding along x-axis .
	# pady keyword argument used to set padding along y-axis .
	word1_field.grid(row = 1, column = 1, pady = 10)
	word2_field.grid(row = 3, column = 1,  pady = 10)

		
	# Create a Correction Button and attached
	# with correction function
	button1 = Button(root, text = "Correction", bg = "brown", fg = "white",
								command = correction,font=('Georgia', 13, 'bold'))
		
	button1.grid(row = 2, column = 1)
	
	# Create a Clear Button and attached
	# with clearAll function
	button2 = Button(root, text = "Clear", bg = "brown",
					fg = "white", command = clearAll,font=('Georgia', 13, 'bold'))
	
	button2.grid(row = 4, column = 1)
	
	# Start the GUI
	root.mainloop()
