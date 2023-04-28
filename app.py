import tkinter as tk
import csv
from  exponentialTree import *
import time
from tkinter import ttk

# Create a Tkinter window object
root = tk.Tk()
root.title("KBC Scores")
root.geometry("500x500")

# Create a label and entry field for the user's name
name_label = tk.Label(root, text="Enter your name:", font=("Arial", 14))
name_label.pack(pady=10)
name_entry = tk.Entry(root) #it allow to enter text
name_entry.pack(pady=10) #padding

# Create a list of questions and answers
questions = [
    {"text": "What is the capital of France?", "options": ["A. Paris", "B. Rome", "C. Madrid", "D. Berlin"], "answer": "A"},
    {"text": "What is the tallest mountain in the world?", "options": ["A. Mount Everest", "B. Mount Kilimanjaro", "C. Mount Fuji", "D. Mount McKinley"], "answer": "A"},
    {"text": "Which planet in our solar system is known as the 'Red Planet'?", "options": ["A. Jupiter", "B. Saturn", "C. Mars", "D. Neptune"], "answer": "C"}, 
    {"text": "What is the largest country in the world by land area?", "options": ["A. Russia", "B. China", "C. India", "D. Canada"], "answer": "A"},
    {"text": "Who is the current Prime Minister of Canada?", "options": ["A. Justin Trudeau", "B. Stephen Harper", "C. Jean Chrétien", "D. Brian Mulroney"], "answer": "A"},
    
]

# Create a label to display questions and options
question_label = tk.Label(root, text=questions[0]["text"], font=("Arial", 14))
question_label.pack(pady=10)

# Create an IntVar to hold the value of the selected option
selected_option = tk.IntVar()

# Create radio buttons for each option and associate them with the selected_option variable
option1 = tk.Radiobutton(root, text=questions[0]["options"][0], variable=selected_option, value=1)
option1.pack()
option2 = tk.Radiobutton(root, text=questions[0]["options"][1], variable=selected_option, value=2)
option2.pack()
option3 = tk.Radiobutton(root, text=questions[0]["options"][2], variable=selected_option, value=3)
option3.pack()
option4 = tk.Radiobutton(root, text=questions[0]["options"][3], variable=selected_option, value=4)
option4.pack()

current_question = 0
total_score = 0

def check_answer():
    global current_question
    global total_score
    # Get the correct answer for the current question
    correct_answer = questions[current_question]["answer"]
    # Get the index of the correct answer in the options list
    correct_index = ord(correct_answer) - 65
    # Get the index of the user's answer
    user_index = selected_option.get() - 1
    # Check if the user's answer is correct
    if user_index == correct_index:
        score = 20
    else:
        score = 0
    total_score += score
    
    # Move on to the next question
    current_question += 1
    
    if current_question < len(questions):
        # Update the question and options labels
        question_label.config(text=questions[current_question]["text"])
        option1.config(text=questions[current_question]["options"][0], value=1)
        option2.config(text=questions[current_question]["options"][1], value=2)
        option3.config(text=questions[current_question]["options"][2], value=3)
        option4.config(text=questions[current_question]["options"][3], value=4)
        # Clear the selected_option variable
        selected_option.set(0)
    else:
        # Show the final score with the user's name
        name = name_entry.get()
        score_label.config(text=f"{name}, your final score is: {total_score}")
        # Disable the radio buttons and submit button
        option1.config(state="disabled")
        option2.config(state="disabled")
        option3.config(state="disabled")
        option4.config(state="disabled")
        submit_button.config(state="disabled")
# Save the score to a CSV file
    with open("scores.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, total_score])

def view_leaderboard():
    # read data from scores.csv file
    with open("scores.csv", "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    branching_factor = 3
    tree = ExponentialTree(b=branching_factor)
    for name, score in data:
        tree.insert(name, int(score))
    print(f"With branching factor {branching_factor}: " , tree.write_sorted())

    data = tree.write_sorted()
    # data = [('Charlie', 100), ('Hank', 100), ('Rohini', 100), ('Roshan', 100), ('Quinn', 100), ('megha', 80), ('Emma', 80), ('Larry', 80), ('Amit', 80), ('Bob', 80), ('rohan', 80), ('Peter', 80), ('Isabel', 80), ('Suhana', 60), ('Alice', 60), ('Karen', 60), ('Tom', 60), ('Anmol', 60), ('Veer', 60), ('Olivia', 60), ('Gina', 60), ('Ragini', 60), ('Shalin', 40), ('Jack', 40), ('Sarah', 40), ('Amir', 40), ('', 40), ('hira', 40), ('ragi', 40), ('Daya', 40), ('Rajat', 40), ('Nick', 40), ('David', 40), ('Frank', 20), ('Rachel', 20), ('inam', 20), ('Amna', 20), ('', 20), ('Alisha', 20), ('Meer', 20), ('', 20), ('himachal', 20), ('Raju', 20), ('hania', 20), ('alia', 20), ('Amrat', 20), ('hope', 20), ('amir', 20), ('Faaz', 20), ('mirra', 20), ('Ashi', 20), ('piya', 20), ('Mohan', 20), ('Megan', 20), ('ayush', 0), ('maya', 0)]

    root = tk.Tk()
    root.title("Leader Board")
    
    # Create a treeview with columns 'Rank', 'Name', and 'Score'
    tree = ttk.Treeview(root, columns=('Rank', 'Name', 'Score'))

    # Define column headings
    tree.heading('Rank', text='Rank')
    tree.heading('Name', text='Name')
    tree.heading('Score', text='Score')

    # Pack the treeview into the window and expand to fill both directions
    tree.pack(fill=tk.BOTH, expand=True)

    # Set the minimum size of the window
    root.minsize(800, 600)

    # Insert data rows
    for i, (name, score) in enumerate(data, start=1):
        tree.insert('', tk.END, values=(i, name, score))

    # Pack the treeview into the window
    tree.pack()
    root.geometry("800x600")

    root.mainloop()

# Create a submit button to check the user's answer
submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack(pady=10)

# Create a board button to check the user's answer
leaderBoard_button = tk.Button(root, text="View leader board", command=view_leaderboard)
leaderBoard_button.pack(pady=10)

# Create a label to display the score
score_label = tk.Label(root, text="", font=("Arial", 14))
score_label.pack(pady=10)

# Start the main loop
root.mainloop()

