import os
import shutil
import tkinter as tk
from tkinter import messagebox
import psutil

def delete_temp_files():
    temp_folder = os.environ.get('TEMP')  # Ottiene il percorso della cartella temporanea
    if temp_folder:
        try:
            for root, dirs, files in os.walk(temp_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    if os.path.exists(file_path):  # Verifica se il file esiste
                        try:
                            if not is_file_open(file_path):  # Controlla se il file è aperto
                                os.remove(file_path)  # Elimina il file
                                print(f"File eliminato: {file_path}")
                            else:
                                print(f"File {file_path} in uso, ignorato.")
                        except Exception as e:
                            print(f"Errore durante l'eliminazione del file {file_path}: {e}")
                    else:
                        print(f"Il file {file_path} non esiste.")

            # Elimina le cartelle vuote all'interno della cartella TEMP
            for root, dirs, files in os.walk(temp_folder, topdown=False):
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    try:
                        os.rmdir(dir_path)
                        print(f"Cartella eliminata: {dir_path}")
                    except Exception as e:
                        print(f"Errore durante l'eliminazione della cartella {dir_path}: {e}")

            messagebox.showinfo("Operazione completata", "I file temporanei sono stati eliminati con successo.")
        except Exception as e:
            messagebox.showerror("Errore", f"Si è verificato un errore durante l'eliminazione dei file: {e}")
    else:
        messagebox.showwarning("Avviso", "La variabile d'ambiente TEMP non è stata definita.")

def is_file_open(file_path):
    # Controlla se il file è aperto in background
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if file_path in proc.open_files():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, FileNotFoundError):
            pass
    return False

# Creazione della finestra principale
root = tk.Tk()
root.title("Eliminazione File Temporanei")

# Creazione del pulsante per eliminare i file temporanei
delete_button = tk.Button(root, text="Elimina File Temporanei", command=delete_temp_files)
delete_button.pack(pady=20)

# Esecuzione del loop principale della GUI
root.mainloop()
