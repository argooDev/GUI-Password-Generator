import tkinter
import tkinter.messagebox


class MainGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Password generator')

        # This code entering a text message
        self.intro = tkinter.Label(
            self.main_window,
            text='Let\'s to generate your password!',
            )
        self.intro.pack(ipadx=20, ipady=20, side='top')

        # This code counting password
        self.count_frame = tkinter.Frame(self.main_window)
        self.pass_count = tkinter.Label(
            self.count_frame,
            text='How many password you want to generate?'
        )
        self.pass_count.pack(side='left')
        self.entry_pass_count = tkinter.Entry(
            self.count_frame,
            width=15
        )
        self.entry_pass_count.pack(side='left')

        # This code load length of password
        self.len_frame = tkinter.Frame(self.main_window)
        self.len_password = tkinter.Label(
            self.len_frame,
            text='Enter length of your password: '
        )
        self.len_password.pack(side='left')
        self.entry_len_pass = tkinter.Entry(
            self.len_frame,
            width=15
        )
        self.entry_len_pass.pack(side='left')

        # Use digits?
        self.digits_frame = tkinter.Frame(self.main_window)

        self.digits = tkinter.Label(
            self.digits_frame,
            text='0123456789'
        )
        self.digits.pack(side='left')

        self.use_digits_value = tkinter.IntVar()
        self.u_digits = tkinter.Checkbutton(
            self.digits_frame,
            text='Add',
            variable=self.use_digits_value
        )
        self.u_digits.pack(side='left')

        # Use string char?
        self.str_char_frame = tkinter.Frame(self.main_window)

        self.str_label = tkinter.Label(
            self.str_char_frame,
            text='abcdefghijklmnopqrstuvwxyz'
        )
        self.str_label.pack(side='left')

        self.str_value = tkinter.IntVar()
        self.u_str = tkinter.Checkbutton(
            self.str_char_frame,
            text='Add',
            variable=self.str_value
        )
        self.u_str.pack(side='left')

        # Use string char upper?
        self.str_char_upper_frame = tkinter.Frame(self.main_window)

        self.str_upper = tkinter.Label(
            self.str_char_upper_frame,
            text='ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        )
        self.str_upper.pack(side='left')

        self.str_upper_value = tkinter.IntVar()
        self.u_str_upper = tkinter.Checkbutton(
            self.str_char_upper_frame,
            text='Add',
            variable=self.str_upper_value
        )
        self.u_str_upper.pack(side='left')

        # Use punctuation?
        self.punctuation_frame = tkinter.Frame(self.main_window)

        self.punc_label = tkinter.Label(
            self.punctuation_frame,
            text='!#$%&*+-=?@^_'
        )
        self.punc_label.pack(side='left')

        self.punc_value = tkinter.IntVar()
        self.use_punc = tkinter.Checkbutton(
            self.punctuation_frame,
            text='Add',
            variable=self.punc_value
        )
        self.use_punc.pack(side='left')

        # This is main buttons
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.generate_btn = tkinter.Button(
            self.bottom_frame,
            text='Generate'
        )
        self.generate_btn.pack(side='left')
        self.exit_btn = tkinter.Button(
            self.bottom_frame,
            text='Exit',
            command=self.main_window.destroy
        )
        self.exit_btn.pack(side='left')

        self.count_frame.pack()
        self.len_frame.pack()
        self.digits_frame.pack()
        self.str_char_frame.pack()
        self.str_char_upper_frame.pack()
        self.punctuation_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


if __name__ == '__main__':
    main_gui = MainGUI()
