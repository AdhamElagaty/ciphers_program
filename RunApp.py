from CipherApp import CipherApp


class RunApp(CipherApp):
    def __init__(self):
        super().__init__()


a = RunApp()
a.mainloop()