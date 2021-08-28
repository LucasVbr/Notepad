from tkinter import *
from tkinter.filedialog import askopenfilename


class App(Tk):

    def __init__(self, width, height):
        # Variables
        self.width = width
        self.height = height
        self.current_file = ""
        self.file_types = [("TXT file", ".txt"), ("All files", ".*")]
        self.title_text = "NotePad"

        # Create window
        Tk.__init__(self)
        self.geometry(f"{self.width}x{self.height}")
        self.set_title()

        # Window content
        self.create_menu_bar()
        self.textarea = self.create_textarea()

    def set_title(self, name="new"):
        self.title(f"{self.title_text} | {name}")

    def create_menu_bar(self):
        menu_bar = Menu(self)

        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="New", accelerator="CTRL+N",
                              command=self.new_file)
        menu_file.add_command(label="Open", accelerator="CTRL+O",
                              command=self.open_file)
        menu_file.add_command(label="Save", accelerator="CTRL+S",
                              command=self.save_file)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=menu_file)

        # Accelerators
        self.bind_all("<Control-n>", lambda x: self.new_file())
        self.bind_all("<Control-o>", lambda x: self.open_file())
        self.bind_all("<Control-s>", lambda x: self.save_file())

        self.config(menu=menu_bar)

    def create_textarea(self):
        textarea = Text(self, width=self.width, height=self.height)
        textarea.pack()
        return textarea

    def is_file_open(self):
        return self.current_file != ""

    def new_file(self):
        if self.current_file != "" or self.textarea.get(1.0, END) != "\n":
            self.save_file()
            self.current_file = ""

        self.textarea.delete('1.0', END)
        self.set_title()

    def open_file(self):
        file_path = askopenfilename(title="Choose the file to open",
                                    filetypes=self.file_types)

        if file_path != "":
            self.current_file = file_path
            with open(self.current_file, 'r') as file:
                file_content = file.read()

            self.textarea.delete('1.0', END)
            self.textarea.insert(1.0, file_content)
            self.set_title(self.current_file)

    def save_file(self):
        content = self.textarea.get(1.0, END)

        if self.current_file == "":
            current_file = askopenfilename(title="Choose the file to save",
                                           filetypes=self.file_types)
            self.current_file = current_file if current_file != "" \
                else self.current_file

        if self.current_file != "":
            with open(self.current_file, "w") as file:
                file.write(content)
            self.set_title(self.current_file)


if __name__ == "__main__":
    window = App(500, 500)
    window.mainloop()
