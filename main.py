import tkinter
i = 0
repeater = None

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .25
SHORT_BREAK_MIN = .5
LONG_BREAK_MIN = 20
TIME_LIST = [LONG_BREAK_MIN if x == 8 else WORK_MIN if x % 2 != 0 else SHORT_BREAK_MIN for x in range(1, 9)]


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    global i, repeater
    i = 0
    start_button["state"] = "normal"
    tick_label['text'] = ""
    window.after_cancel(repeater)
    canvas.itemconfig(time_text, text=f"00:00")
    timer_label.config(text="Timer", fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def time_to_seconds():
    return TIME_LIST[i] * 60
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def start_countdown(time_remaining=time_to_seconds()):
    global i, repeater
    timer_label["text"] = ["WORK NOW", "REST NOW"][i % 2]
    timer_label["fg"] = [PINK, GREEN][i % 2]
    if start_button["state"] == 'normal':
        start_button["state"] = 'disabled'
    minutes = int(time_remaining / 60)
    seconds = int(time_remaining % 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(time_text, text=f"{minutes}:{seconds}")
    if int(time_remaining) > 0:
        repeater = window.after(1000, start_countdown, time_remaining - 1)
    else:
        if i < 7:
            i += 1
            if i % 2 != 0:
                tick_label["text"] += "✔"
            window.lift()
            repeater = window.after(1000, start_countdown, time_to_seconds())


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("POMODORO")
window.config(bg=YELLOW, padx=40, pady=30)
window.minsize(500, 400)
picture = tkinter.PhotoImage(file="tomato.png")

timer_label = tkinter.Label(text="TIMER", bg=YELLOW, fg=GREEN, font=("Ariel", 20, "bold"))
timer_label.grid(column=1, row=0, padx=30, pady=10)

canvas = tkinter.Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=picture)
time_text = canvas.create_text(100, 130, text="00:00", fill=YELLOW, font=("Ariel", 20, "bold"))
canvas.grid(column=1, row=1, padx=30, pady=10)

start_button = tkinter.Button(text="Start", bg=YELLOW, command=start_countdown)
start_button.grid(column=0, row=2, padx=30, pady=10)

tick_label = tkinter.Label(text="", bg=YELLOW, fg=GREEN, font=("Ariel", 20, "bold"))
tick_label.grid(column=1, row=2, padx=30, pady=10)

reset_button = tkinter.Button(text="Reset", bg=YELLOW, command=reset_time)
reset_button.grid(column=2, row=2, padx=30, pady=10)

window.mainloop()
