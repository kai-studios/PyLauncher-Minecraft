import customtkinter as ctk
import minecraft_launcher_lib as mll
import subprocess
import os
from tkinter import messagebox 
import uuid 

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")


minecraft_directory = mll.utils.get_minecraft_directory()


def generate_offline_uuid(username):
    """Генерация UUID для оффлайн режима."""
    return str(uuid.uuid3(uuid.NAMESPACE_DNS, username))


def launch_minecraft_offline(version, username):
    """Запуск Minecraft в оффлайн режиме."""
    try:

        options = {
            "username": username,
            "uuid": generate_offline_uuid(username),
            "token": ""
        }

        command = mll.command.get_minecraft_command(version, minecraft_directory, options)

        subprocess.Popen(command, cwd=minecraft_directory)
    except Exception as e:
        messagebox.showerror("Ошибка запуска", f"Не удалось запустить Minecraft: {e}")


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

    versions = mll.utils.get_available_versions(minecraft_directory)
    version_ids = [v["id"] for v in versions]
    version_combobox = ctk.CTkComboBox(version_frame, values=version_ids)
    version_combobox.pack(side="right", fill="x", expand=True, padx=10)
    if version_ids:
        version_combobox.set(version_ids[0])  

    def start_game():
        username = username_entry.get()
        version = version_combobox.get()

        if not username.strip():
            messagebox.showerror("Ошибка", "Пожалуйста, введите ник!")
            return

        if not version:
            messagebox.showerror("Ошибка", "Пожалуйста, выберите версию Minecraft!")
            return

        launch_minecraft_offline(version, username)

    start_button = ctk.CTkButton(window, text="Играть", command=start_game)
    start_button.pack(pady=20)

    window.mainloop()


if __name__ == "__main__":
    create_launcher()
