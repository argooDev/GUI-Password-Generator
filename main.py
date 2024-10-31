import tkinter
import tkinter.messagebox
import random


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

        # For what you generate a password?
        self.for_what_frame = tkinter.Frame(self.main_window)
        self.for_what = tkinter.Label(
            self.for_what_frame,
            text='What service are you generated a password for: '
        )
        self.for_what.pack(side='left')

        self.for_what_entry = tkinter.Entry(
            self.for_what_frame,
            width=15
        )
        self.for_what_entry.pack(side='left')

        # This code show generated password
        self.result_password_frame = tkinter.Frame(self.main_window)
        self.result_password = tkinter.Label(
            self.result_password_frame,
            text='Password: '
        )
        self.result_password.pack(side='left')

        self.password = tkinter.StringVar()
        self.password_label = tkinter.Entry(
            self.result_password_frame,
            textvariable=self.password
        )
        self.password_label.pack(side='left')

        # This is main buttons
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.generate_btn = tkinter.Button(
            self.bottom_frame,
            text='Generate',
            command=self.generate_password
        )
        self.generate_btn.pack(side='left')
        self.exit_btn = tkinter.Button(
            self.bottom_frame,
            text='Exit',
            command=self.main_window.destroy
        )
        self.exit_btn.pack(side='left')

        # This code packs frames
        self.for_what_frame.pack()
        self.len_frame.pack()
        self.result_password_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def generate_password(self):
        self.length_password = int(self.entry_len_pass.get())
        self.digits_val = '0123456789'
        self.punctuation = '!#$%&*+-=?@^_'
        self.l_char = 'abcdefghijklmnopqrstuvwxyz'
        self.h_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        self.password_templates = list(self.digits_val + self.punctuation + self.l_char + self.h_char)
        self.storage = []
        for password in range(self.length_password):
            self.storage.append(random.choice(self.password_templates))

        self.result_password_value = ''.join(self.storage)
        self.password.set(self.result_password_value)

        with open('Password.txt', 'a') as self.file:
            self.file.write(f'{self.for_what_entry.get()} - {self.password_label.get()}\n')


if __name__ == '__main__':
    main_gui = MainGUI()
