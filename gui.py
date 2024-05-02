import tkinter as tk
from main import boardBuild

def handler(category, subfield, option = 0):
    """Handles the submit button. Receives the arrays containing the sorted leaderboard, and builds the text of the leaderboard"""
    try:
        resultVal, resultUser = boardBuild(category, subfield, int(option))
        result = ""
        for i in range(min(len(resultVal), 5)):  # Loops 5 times, or less if the array isn't 5 long.
            result += f"{resultUser[i]}: {resultVal[i]}\n"
    except:
        result = "Input invalid or statistic empty. Please try again"


    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

# Create the main application window

root = tk.Tk()
root.title("Minecraft Stats Scraper")

# Create GUI elements
label1 = tk.Label(root, text="Enter the statistic category:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter the statistic name:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Enter player restrictions:\n2 for real players, 1 to include registered bots, 0 to include 'illegal' bots")
label3.pack()

entry3 = tk.Entry(root)
entry3.pack()

button = tk.Button(root, text="Submit", command=lambda:handler(entry1.get(),entry2.get(),entry3.get()))
button.pack()

result_text = tk.Text(root, height=5, width=50)
result_text.pack()

# Start the main event loop
root.mainloop()