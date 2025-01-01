import tkinter as tk

# Rule-based logic for the chatbot
data = {
    "who is doraemon": "Doraemon is a Japanese Anime.",
    "who is shizuka": "Shizuka is a character in an Anime named Doraemon. She is the best friend of Nobita.",
    "who is tom": "Tom is Jerry's best friend in the show.",
}

def answer(user_input):
    user_input = user_input.lower().strip()
    return data.get(user_input, "Sorry, I don't know about that character.")

# Function to send a message
def send_message():
    user_message = entry.get()
    if user_message.strip():
        chat_log.insert(tk.END, f"You: {user_message}\n")
        if user_message.lower() == "exit":
            chat_log.insert(tk.END, "Bot: Goodbye!\n")
            entry.delete(0, tk.END)
            window.quit()
        else:
            bot_response = answer(user_message)
            chat_log.insert(tk.END, f"Bot: {bot_response}\n")
        entry.delete(0, tk.END)

# Create the main GUI window
window = tk.Tk()
window.title("Cartoon Talks Chatbot")

# Chat log display
chat_log = tk.Text(window, bg="white", fg="black", wrap=tk.WORD, state=tk.NORMAL, height=20)
chat_log.pack(padx=10, pady=10, fill=tk.BOTH)

# Entry widget for user input
entry = tk.Entry(window, bg="white", fg="black", width=50)
entry.pack(padx=10, pady=10, fill=tk.X)

# Send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(padx=10, pady=10)

# Run the GUI event loop
window.mainloop()
