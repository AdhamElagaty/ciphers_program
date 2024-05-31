from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import ctypes as ct
import pyperclip
from PIL import Image, ImageTk
from CaesarCipher import CaesarCipher
from PlayfairCipher import PlayfairCipher
from MonoalphabeticCipher import MonoalphabeticCipher
from PolyalphabeticCipher import PolyalphabeticCipher
from VigenereCipher import VigenereCipher
from RailFenceCipher import RailFenceCipher
from RowTranspositionCipher import RowTranspositionCipher
from DECCipher import DECCipher
from AESCipher import AESCipher


class CipherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.get_selection_button = None
        self.decrypt_button = None
        self.radio_var = None
        self.title_label = None
        self.ws = None
        self.hs = None
        self.shift_entry = None
        self.message_Text = None
        self.shift_entry  = None
        self.output_text = None
        self.style = ttk.Style()
        self.title("Ciphers")
        self.can_write_key = True
        self.radio_image = None
        self.setup_ui()
        

    def setup_ui(self):
        self.ws = self.winfo_screenwidth()
        pos_x = round((self.ws - 1400) / 2)
        self.hs = self.winfo_screenheight()
        pos_y = round((self.hs - 750) / 2)
        self.geometry("1400x750+{}+{}".format(pos_x, pos_y))
        self.resizable(False, False)
        self.config(bg="#17171A")
        self.iconbitmap("image/icon/lock_icon.ico")
        self.dark_title_bar()
        self.create_widgets()
        self.radiobutton_click()
        
    def dark_title_bar(self):
        self.update()
        set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
        get_parent = ct.windll.user32.GetParent
        hwnd = get_parent(self.winfo_id())
        value = 2
        value = ct.c_int(value)
        set_window_attribute(hwnd, 20, ct.byref(value),4)
        
        
    def resize_image(self, image):
        image_list = []
        for i in image:
            original_image = Image.open(i)
            resized_image = original_image.resize((30, 30), Image.LANCZOS)
            image_list.append(ImageTk.PhotoImage(resized_image))
        return image_list

    def create_widgets(self):
        title_label = tk.Label(self, text="Ciphers", bg="#17171A", fg="#93959F", font=("arial", 38))
        title_label.place(relx=0.28, rely=0.1, anchor=tk.CENTER)
        self.style = ttk.Style()
        radio_options = ['Caesar', 'Mono Alphabetic', 'Playfair', 'Poly Alphabetic', 'Vigenère', 'Rail Fence',
                         'Row Transposition', 'DES', 'AES']
        self.radio_original_image = ['image/ciphers_logo/Ceasar.png', 'image/ciphers_logo/Mono.png', 'image/ciphers_logo/Playfair.png', 'image/ciphers_logo/Playfair.png', 'image/ciphers_logo/Viginair.png', 'image/ciphers_logo/Rail.png',
                         'image/ciphers_logo/Rail.png', 'image/ciphers_logo/Des.png', 'image/ciphers_logo/Aes.png']
        self.radio_image = self.resize_image(self.radio_original_image)
        self.radio_original_selected_image = ['image/ciphers_logo/Ceasar_slctd.png', 'image/ciphers_logo/Mono_slctd.png', 'image/ciphers_logo/Playfair_slctd.png', 'image/ciphers_logo/Playfair_slctd.png', 'image/ciphers_logo/Viginair_slctd.png', 'image/ciphers_logo/Rail_slctd.png',
                         'image/ciphers_logo/Rail_slctd.png', 'image/ciphers_logo/Des_slctd.png', 'image/ciphers_logo/Aes_slctd.png']
        self.radio_selected_image = self.resize_image(self.radio_original_selected_image)
        self.radio_var = tk.IntVar(value=1)
        for i, option in enumerate(radio_options):
            radiobutton = Radiobutton(self, 
                               text="   "+option, 
                               variable=self.radio_var, 
                               value=i+1, 
                               command=self.radiobutton_click, 
                               cursor="hand2", 
                               indicatoron=0, 
                               height=280,
                               bg="#17171A", 
                               selectcolor="#24263A", 
                               activebackground="#2C3052",
                               borderwidth=0,
                               fg="#7378FF",
                               font=("arial", 12),
                               compound='left',
                               anchor="w",
                               activeforeground="#46474E",
                               justify='left',
                               image = self.radio_image[i],
                               padx=4)
            radiobutton.place(relx=0.1, rely=(i + 1) / (len(radio_options) + 1), anchor=tk.CENTER, relheight= 0.074, relwidth=0.136)
            radiobutton.bind("<Enter>", lambda event, rb=radiobutton: rb.config(bg="#24263A"))
            radiobutton.bind("<Leave>", lambda event, rb=radiobutton: rb.config(bg="#17171A"))

        container_frame = tk.Frame(self, background="#17171A")
        container_frame.place(relx=0.6, rely=0.55, anchor=tk.CENTER, relheight= 0.82, relwidth=0.75)
        key_frame = tk.Frame(container_frame, background="#17171A")
        key_frame.pack(anchor="nw")
        shift_label = tk.Label(key_frame, text="Key", bg="#17171A", fg="#93959F", font=("arial", 16))
        shift_label.grid(row=0, column=0, sticky = W)

        self.shift_entry = tk.Entry(key_frame, bg="#202124", borderwidth=0, font=("arial", 18), fg="white", width=30)
        self.shift_entry.grid(row=1,column=0)
        vcmd = (self.register(self.validate_input), '%S')
        self.shift_entry.config(validate="key", validatecommand=vcmd)
        
        self.copy_key_button = tk.Button(key_frame, text="Copy", bg="#2C3052", fg="#7378FF", borderwidth=0, cursor="hand2", command= self.copy_key_text)
        self.copy_key_button.grid(row=1,column=1, padx=(12, 6))
        self.copy_key_button.bind("<Enter>", lambda event, rb=self.copy_key_button: rb.config(bg="#24263A"))
        self.copy_key_button.bind("<Leave>", lambda event, rb=self.copy_key_button: rb.config(bg="#2C3052"))
        
        self.paste_key_button = tk.Button(key_frame, text="Paste", bg="#2C3052", fg="#7378FF", borderwidth=0, cursor="hand2", command= self.paste_key_button_click)
        self.paste_key_button.grid(row=1,column=2, padx=6)
        self.paste_key_button.bind("<Enter>", lambda event, rb=self.paste_key_button: rb.config(bg="#24263A"))
        self.paste_key_button.bind("<Leave>", lambda event, rb=self.paste_key_button: rb.config(bg="#2C3052"))

        message_frame = tk.Frame(container_frame, background="#17171A")
        message_frame.place(relx=0.35, rely=0.46, anchor=tk.CENTER, relheight= 0.7, relwidth=0.7)
        message_label = tk.Label(message_frame, text="Message", bg="#17171A", fg="#93959F", font=("arial", 16))
        message_label.pack(anchor="nw")

        self.message_Text = tk.Text(message_frame, height=15, bg="#202124", borderwidth=0, font=("arial", 18), fg="white", width=38)
        self.message_Text.pack(anchor="nw")

        
        get_selection_button = tk.Button(container_frame, text="Encrypt".center(25), command=self.encrypt_button_click, bg="#2C3052", fg="#7378FF", cursor="hand2", borderwidth=0, font=("arial", 14), anchor='center', compound='left')
        get_selection_button.place(relx=0, rely=0.85, relwidth=0.12, relheight=0.065)
        
        get_selection_button.bind("<Enter>", lambda event, rb=get_selection_button: rb.config(bg="#24263A" ))
        get_selection_button.bind("<Leave>", lambda event, rb=get_selection_button: rb.config(bg="#2C3052"))

        self.decrypt_button = tk.Button(container_frame, anchor="center", text="Decrypt", command=self.decrypt_button_click, bg="#2C3052", fg="#7378FF", cursor="hand2", borderwidth=0, font=("arial", 14), compound='left')
        self.decrypt_button.place(relx=0.13, rely=0.85, relwidth=0.12, relheight=0.065)
        
        self.decrypt_button.bind("<Enter>", lambda event, rb=self.decrypt_button: rb.config(bg="#24263A" ))
        self.decrypt_button.bind("<Leave>", lambda event, rb=self.decrypt_button: rb.config(bg="#2C3052"))
        
        self.clear_button = tk.Button(container_frame, anchor="center", justify="center", text="Clear".center(30), command=self.clear_text, bg="#583538", fg="#FF7373", cursor="hand2", borderwidth=0, font=("arial", 14))
        self.clear_button.place(relx=0.492, rely=0.85, relwidth=0.12, relheight=0.065)
        
        self.clear_button.bind("<Enter>", lambda event, rb=self.clear_button: rb.config(bg="#331F20" ))
        self.clear_button.bind("<Leave>", lambda event, rb=self.clear_button: rb.config(bg="#583538"))
        
        output_frame = tk.Frame(container_frame, background="#17171A")
        output_frame.place(relx=0.84, rely=0.46, anchor=tk.CENTER, relheight= 0.7, relwidth=0.7)
        output_label_frame = tk.Frame(output_frame, background="#17171A")
        output_label_frame.pack(anchor="nw")
        output_label = tk.Label(output_label_frame, text="Output", bg="#17171A", fg="#93959F", font=("arial", 16))
        output_label.grid(row=0,column=0, padx=(0, 6))
        self.output_text = tk.Text(output_frame,height=15, bg="#202124", borderwidth=0, font=("arial", 18), fg="white", width=38, state="disabled")
        self.output_text.pack(anchor="nw")
        
        self.copy_button = tk.Button(output_label_frame, text="Copy", bg="#2C3052", fg="#7378FF", borderwidth=0, cursor="hand2", command= self.copy_output_text)
        self.copy_button.grid(row=0,column=1, padx=(12, 0))
        self.copy_button.bind("<Enter>", lambda event, rb=self.copy_button: rb.config(bg="#24263A"))
        self.copy_button.bind("<Leave>", lambda event, rb=self.copy_button: rb.config(bg="#2C3052"))

    def update_color(self, event, rb, selected_color, unselected_color):
        if self.radio_var.get() == rb.cget('value'):
            rb.config(fg=selected_color)
        else:
            rb.config(fg=unselected_color)
        
    def radiobutton_click(self):
        selected_value = self.radio_var.get()
        for rb in self.winfo_children():
            if isinstance(rb, Radiobutton):
                if rb.cget("value") == self.radio_var.get():
                    rb.config(bg="#24263A", fg="#7378FF", image=self.radio_selected_image[rb.cget("value")-1])
                else:
                    rb.config(bg="#17171A", fg="#46474E", image=self.radio_image[rb.cget("value")-1])
        self.can_write_key = True
        match selected_value:
            case 2:
                key = MonoalphabeticCipher.generate_key()
                self.shift_entry.delete(0, tk.END)
                self.shift_entry.insert(tk.END, key)
                self.can_write_key = False
            case 1 | 3 | 4 | 5| 6:
                self.shift_entry.delete(0, tk.END)
                self.can_write_key = False
            case 8:
                key = DECCipher.generate_key()
                self.shift_entry.delete(0, tk.END)
                self.shift_entry.insert(tk.END, key.hex())
                self.can_write_key = False
            case 9:
                key = AESCipher.generate_key()
                self.shift_entry.delete(0, tk.END)
                self.shift_entry.insert(tk.END, key.hex())
                self.can_write_key = False
            case _:
                self.shift_entry.delete(0, tk.END)
                self.can_write_key = True
           
    def paste_key_button_click(self):
        selected_value = self.radio_var.get()
        self.can_write_key = True
        self.shift_entry.delete(0, tk.END)
        match selected_value:
            case 2 | 8 | 9:
                self.paste_key_text()
                self.can_write_key = False
            case 1 | 3 | 4 | 5| 6:
                self.can_write_key = False
                self.paste_key_text()
            case _:
                self.paste_key_text()
                self.can_write_key = True             
                
    def validate_input(self, char):
        selected_value = self.radio_var.get()
        match selected_value:
            case 1 | 4 | 6:
                return char.isdigit() or char == "" or self.can_write_key
            case 3 | 5:
                return char.isalpha() or self.can_write_key
            case _:
                return self.can_write_key  
    
    def copy_key_text(self):
        copied_text = self.shift_entry.get()
        pyperclip.copy(copied_text)
        
    def copy_output_text(self):
        copied_text = self.output_text.get("1.0",tk.END).rstrip()
        pyperclip.copy(copied_text)

    def paste_key_text(self):
        try:
            copied_text = pyperclip.paste()
            self.shift_entry.insert(tk.END, copied_text)
        except pyperclip.PyperclipException:
            messagebox.showwarning("Warning", "Clipboard is empty or cannot be accessed.")
            
    def clear_text(self):
        self.message_Text.delete("1.0", tk.END)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)
    
    def encrypt_message(self, message, key):
        selected_value = self.radio_var.get()
        match selected_value:
            case 1:
                return CaesarCipher(int(key)).encrypt(message)
            case 2:
                return MonoalphabeticCipher(key).encrypt(message)
            case 3:
                return PlayfairCipher(key).encrypt(message)
            case 4:
                return PolyalphabeticCipher(int(key)).encrypt(message)
            case 5:
                return VigenereCipher(key).encrypt(message)
            case 6:
                return RailFenceCipher(int(key)).encrypt(message)
            case 7:
                return RowTranspositionCipher(key).encrypt(message)
            case 8:
                return DECCipher(bytes.fromhex(key)).encrypt(message)
            case 9:
                return AESCipher(bytes.fromhex(key)).encrypt(message)
           
    def decrypt_message(self, message, key):
        selected_value = self.radio_var.get()
        match selected_value:
            case 1:
                return CaesarCipher(int(key)).decrypt(message)
            case 2:
                return MonoalphabeticCipher(key).decrypt(message)
            case 3:
                return PlayfairCipher(key).decrypt(message)
            case 4:
                return PolyalphabeticCipher(int(key)).decrypt(message)
            case 5:
                return VigenereCipher(key).decrypt(message)
            case 6:
                return RailFenceCipher(int(key)).decrypt(message)
            case 7:
                return RowTranspositionCipher(key).decrypt(message)
            case 8:
                return DECCipher(bytes.fromhex(key)).decrypt(message)
            case 9:
                return AESCipher(bytes.fromhex(key)).decrypt(message)  
    
    def encrypt_button_click(self):
        try:
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, self.encrypt_message(self.message_Text.get("1.0",tk.END).rstrip(), self.shift_entry.get().rstrip()))
            self.output_text.config(state=tk.DISABLED)
        except ValueError:
            messagebox.showerror("Error", "Please try again.")
 
    def decrypt_button_click(self):
        try:
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, self.decrypt_message(self.message_Text.get("1.0",tk.END).rstrip(), self.shift_entry.get().rstrip()))
            self.output_text.config(state=tk.DISABLED)
        except ValueError:
            messagebox.showerror("Error", "Please try again.")
