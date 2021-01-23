from tkinter import *
# importing the crawler here
import sele


# defining a function that will work with the functions in the sele.py doc using actions from the GUI
def fill_button():
    sele.fill_supwork_form()
    auto_response.insert(END, 'Getting website......\n')

    sele.access_form()
    auto_response.insert(END, 'accessing form....... \n')
    # The function below carries an argument, refer to line 29 in the sele.py doc, the argument in this case is the
    # input from the GUI
    sele.input_firstname(fn_entry_value.get())
    auto_response.insert(END, 'inputting firstname........ \n')
    # The function below carries an argument, refer to line 34 in the sele.py doc, the argument in this case is the
    # input from the GUI
    sele.input_lastname(ln_entry_value.get())
    auto_response.insert(END, 'inputting lastname............ \n')

    sele.input_email()
    auto_response.insert(END, 'inputting email............ \n')

    sele.select_nationality()
    auto_response.insert(END, 'selecting nationality as Nigeria........... \n')

    sele.input_address()
    auto_response.insert(END, 'inputting address............. \n')

    sele.select_apt_size()
    auto_response.insert(END, 'selecting apt size as 3+1............... \n')

    sele.select_lang()
    auto_response.insert(END, 'selecting language as English.................\n')

    sele.select_prop()
    auto_response.insert(END, 'selecting property as 3+1................. \n')

    sele.input_number()
    auto_response.insert(END, 'inputting phone number.................. \n')

    sele.close_form()
    auto_response.insert(END, 'closing form................... \n')


window = Tk()

window.wm_title("Auto_vobb")

auto_caution = Label(window, text='click button to fill form')
auto_caution.grid(row=0, column=2)

# This is an input space i created on the GUI for the firstname of the user, checkout line 15 above
fn_entry_value = StringVar()
fn_entry = Entry(window, textvariable=fn_entry_value)
fn_entry.grid(row=1, column=1)

# This is an input space i created on the GUI for the lastname of the user, checkout line 19 above
ln_entry_value = StringVar()
ln_entry = Entry(window, textvariable=ln_entry_value)
ln_entry.grid(row=1, column=3)

auto_button = Button(window, text='fill form', command=fill_button)
auto_button.grid(row=2, column=2)

auto_response = Text(window, height=6, width=35)
auto_response.grid(row=3, column=1, rowspan=6, columnspan=3)

window.mainloop()
