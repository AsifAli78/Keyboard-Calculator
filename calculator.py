import tkinter as tk

# Define the color scheme
bg_color = "black"
text_color = "white"
button_color = "gray"

def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Keyboard Calculator")
root.configure(bg=bg_color)

entry = tk.Entry(root, width=80, bg=bg_color, fg=text_color)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/',
]

row_val = 1
col_val = 0

for button in buttons:
    button_frame = tk.Button(root, text=button, width=5, height=2, bg=button_color, fg=text_color)
    button_frame.grid(row=row_val, column=col_val)
    button_frame.bind("<Button-1>", on_button_click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
