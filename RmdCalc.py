import tkinter as tk

from MonthDictionary import month_def
from datetime import date

today = date.today()
today_date = today.strftime("%m/%d/%Y")


# creates window
def gui():
    # window setting
    root = tk.Tk()
    root.title("RMD Calculator")
    root.geometry("500x100")

    tk.Label(root, text="Enter Date of Birth").grid(row=0)

    tk.Label(root, text="__/__/____").grid(row=1, column=0)
    e1 = tk.Entry(root)
    e1.grid(row=1, column=1)

    res = tk.Label(root, text="Result")
    res.grid(row=4)

    def input_to_list():
        dob_input = e1.get()
        dates = dob_input.split('/')
        return dates

    def give_age():
        dob_list = input_to_list()
        dob_total_days = month_def.get(dob_list[0]) + int(dob_list[1])
        dob_decimal_days = dob_total_days / 365

        tod_list = today_date.split('/')
        tod_month = tod_list[0]
        tod_day = tod_list[1]
        tod_year = int(tod_list[2])
        tod_total_days = month_def.get(tod_month) + int(tod_day)
        tod_decimal_days = tod_total_days / 365

        age = (tod_year + tod_decimal_days) - ((int(dob_list[2])) + dob_decimal_days)
        age = "{:.2f}".format(age)

        year = int(dob_list[2])
        month = dob_list[0]
        new_first_rmd = 73 + year
        old_first_rmd = 71 + year

        if year > 1949:
            rmd = f"first RMD is due by April 1st, {new_first_rmd}"
        elif year == 1949 and int(month) >= 7:
            rmd = f"first RMD is due by April 1st, {new_first_rmd}"
        elif year == 1949 and int(month) < 7:
            rmd = f"first RMD was due by April 1st, {old_first_rmd}"
        elif year < 1949 and int(month) < 7:
            rmd = f"first RMD was due by April 1st, {old_first_rmd}"
        else:
            rmd = f"first RMD was due by April 1st, {72 + year}"

        statement = f"The age is {age} and the {rmd}"
        return statement

    # input handler to bind to Show button
    def handle_input():
        statement = give_age()
        res.configure(text=str(statement))
        e1.delete(0, tk.END)


    # buttons
    tk.Button(root,
              text='Quit',
              command=root.destroy).grid(row=10,
                                         column=0,
                                         sticky=tk.W,
                                         pady=4)

    tk.Button(root,
              text='Show',
              command=handle_input).grid(row=10,
                                        column=1,
                                        sticky=tk.W,
                                        pady=4)
    root.mainloop()


if __name__ == "__main__":
    gui()