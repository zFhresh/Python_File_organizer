import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import LogManager as log

import Functions.dosyaları_tasi as dt
import Functions.Dosyaların_yüzdeleri as dy


log.OpenLog()
log.write("Program başlatıldı.")

stats_parcent_Str = ""
stats_count_Str = ""

def startTheProgress(path):
    try:
        log.write("--- İşlemler başlatıldı. ---")
        global stats_str
        global stats_count_Str
        FileData= dt.filetransfer(path)
        stats = dy.count_file_extensions(path)
        print(FileData)
        log.write(FileData)
        stats_str = dict_to_str_yuzdeler(stats)
        stats_count_Str = dict_to_str_sayilar(FileData)
        print (stats_str)
        log.write(stats_count_Str)
        log.write("İşlemler tamamlandı.")
    except Exception as e:
        log.write("Bir hata oluştu. Detaylar: " + str(e))
        messagebox.showerror("Hata", "Bir hata oluştu. Detaylar için konsolu veya log dosyalarını kontrol edin.")
        quit()

#! Yüzdeler hesaplanıyor file data üzerinden dosya sayıları da kullannıcılara gösterilecek 
#! ve Unity dosyalarını düzenlemesini engellemek için bir koruma eklenecek böylece kullanıcılar uyarılacak veya işlem iptal edilecek


def dict_to_str_sayilar(dict):
    text = "Dosa türlerinin sayıları:\n"
    for key in dict:
        text += key + ": " + str(dict[key]) + "\n"
    return text

def dict_to_str_yuzdeler(dict):
    text = "Dosya türlerinin yüzdeleri:\n"
    if len(dict)  > 10:
        return "Dosya sayısı çok fazla. Yüzdeler Console'da gösterilecek."
    for key in dict:
        text += key + ": %" + str(dict[key]) + "\n"
    return text

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        selected_folder_label.config(text="Seçilen Klasör: " + folder_path + " İşlemler başlatıldı")
        startTheProgress(folder_path)
    else:
        selected_folder_label.config(text="Bir klasör seçilmedi.")

root = tk.Tk()
root.title("File organizer")

folder_path = filedialog.askdirectory()

if folder_path:
    selected_folder_label = tk.Label(root, text="Seçilen Klasör: " + folder_path)
    selected_folder_label.grid(row=0, column=1)
    

    startTheProgress(folder_path)
    Stats_label_parcent = tk.Label(root, text=stats_str)
    Stats_label_parcent.grid(row=1, column=0)
    

    Stats_label_Count = tk.Label(root, text=stats_count_Str)
    Stats_label_Count.grid(row=1, column=2)
    log.close()

else:
    selected_folder_label = tk.Label(root, text="Bir klasör seçilmedi.")
    selected_folder_label.grid(row=0, column=0)

# Pencereyi göster
root.mainloop()
