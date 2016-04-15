import Tkinter as tkinter


class ChooseGameMenu(object):

    def __init__(self, parent):

        self.parent = parent
        self.sq_size = 100
        self.container = tkinter.Frame(self.parent)
        self.container.pack()
        self.canvas = tkinter.Canvas(self.container,
                                     width=self.sq_size * 3,
                                     height=self.sq_size)
        self.initialize_buttons()
        self.ip_label.grid()
        self.ip.grid()
        self.port_label.grid()
        self.port.grid()
        self.start_button.grid()
        self.stop_button.grid()

    def initialize_buttons(self):

        text_var = tkinter.StringVar()
        self.ip_label = tkinter.Label(self.container, textvariable=text_var)
        text_var.set('IP ADDRESS')

        self.ip = tkinter.Text(
            self.container,
            width=35,
            height=1,
            font=(
                "Arial",
                14))

        text_var = tkinter.StringVar()
        self.port_label = tkinter.Label(self.container, textvariable=text_var)
        text_var.set('PORT')

        self.port = tkinter.Text(
            self.container,
            width=35,
            height=1,
            font=(
                "Arial",
                14))

        self.start_button = tkinter.Button(self.container,
                                           text="START",
                                           width=40,
                                           command=self.start_sending)

        self.stop_button = tkinter.Button(self.container,
                                          text="STOP",
                                          width=40,
                                          command=self.stop_sending)
        self.stop_button.config(state='disabled')

    def start_sending(self):
        self.ip.configure(state='disabled', background="#D3D3D3")
        self.port.configure(state='disabled', background="#D3D3D3")
        self.start_button.config(state='disabled')
        self.stop_button.config(state='normal')
        ip_address = self.ip.get("1.0", tkinter.END)
        port = self.port.get("1.0", tkinter.END)
        print ip_address
        print port
        # object.start_sending(ip_address,port)

    def stop_sending(self):
        self.ip.configure(state='normal', background="#FFFFFF")
        self.port.configure(state='normal', background="#FFFFFF")
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')
        # object.stop_sending()


def main():
    root = tkinter.Tk()
    root.title("Windows Log File Sender")
    ChooseGameMenu(root)
    root.mainloop()

if __name__ == '__main__':
    main()
