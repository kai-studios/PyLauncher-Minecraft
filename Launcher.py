import customtkinter as ctk
from tkinter import messagebox 
import lib.mc as mc

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")


def create_launcher():
    """Создаёт основной интерфейс лаунчера."""

    window = ctk.CTk()
    window.title("Minecraft Launcher (Offline)")
    window.geometry("500x300")

    title_label = ctk.CTkLabel(window, text="Minecraft Launcher", font=("Arial", 20))
    title_label.pack(pady=10)

    username_frame = ctk.CTkFrame(window)
    username_frame.pack(pady=10, padx=20, fill="x")
    username_label = ctk.CTkLabel(username_frame, text="Введите ник:")
    username_label.pack(side="left", padx=10)
    username_entry = ctk.CTkEntry(username_frame, placeholder_text="Ваш ник...")
    username_entry.pack(side="right", fill="x", expand=True, padx=10)

    version_frame = ctk.CTkFrame(window)
    version_frame.pack(pady=10, padx=20, fill="x")
    version_label = ctk.CTkLabel(version_frame, text="Выберите версию:")
    version_label.pack(side="left", padx=10)

    version_combobox = ctk.CTkComboBox(version_frame, values=mc.version_ids())
    version_combobox.pack(side="right", fill="x", expand=True, padx=10)
    if mc.version_ids():
        version_combobox.set(mc.version_ids()[0])  

    def start_game():
        username = username_entry.get()
        version = version_combobox.get()

        if not username.strip():
            messagebox.showerror("Ошибка", "Пожалуйста, введите ник!")
            return

        if not version:
            messagebox.showerror("Ошибка", "Пожалуйста, выберите версию Minecraft!")
            return

        try:
            mc.launch(version, username)
        except Exception as e:
            messagebox.showerror("Ошибка запуска", f"Не удалось запустить Minecraft: {e}")

    start_button = ctk.CTkButton(window, text="Играть", command=start_game)
    start_button.pack(pady=20)

    window.mainloop()

if __name__ == "__main__":
    create_launcher()
