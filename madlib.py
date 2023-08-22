#This is the original code for the madlib #
# Prompting a player to enter a name:
#name =  input('What is yoyr name?: ')
# asking for an adjective from a user
#adjective = input('Enter an adjective: ')
#prompting a user for a plural noun
#noun_1 = input('Enter a plural noun: ')

# Prompting a user to enter another name/noun
#noun_2 = input('Enter any other noun: ')



#printing a ryhme
#print("Roses are " + adjective)
#print(noun_1  + "are blue")
#print("I can't start my day without", noun_2)

import tkinter as tk
# This function will generate a madlib for the user to input
def generate_madlib():
    adjective = adjective_entry.get()
    noun_1 = noun1_entry.get()
    noun_2 = noun2_entry.get()

    madlib_result.set("Roses are " + adjective + "\n" +
                     noun_1 + " are blue\n" +
                     "I can't start my day without " + noun_2)

# Creating the main window
root = tk.Tk()
root.title("Mad Libs Game")

# Create and pack labels and entry fields for user input
tk.Label(root, text="Enter an adjective:(any word that talks more about a noun)").pack()
adjective_entry = tk.Entry(root)
adjective_entry.pack()

tk.Label(root, text="Enter a plural noun:").pack()
noun1_entry = tk.Entry(root)
noun1_entry.pack()

tk.Label(root, text="Enter any other noun:").pack()
noun2_entry = tk.Entry(root)
noun2_entry.pack()

# Create a button to generate the Mad Libs result
generate_button = tk.Button(root, text="Generate Mad Lib", command=generate_madlib)
generate_button.pack()

# Create a label to display the result
madlib_result = tk.StringVar()
result_label = tk.Label(root, textvariable=madlib_result)
result_label.pack()

# Start the main event loop
root.mainloop()
