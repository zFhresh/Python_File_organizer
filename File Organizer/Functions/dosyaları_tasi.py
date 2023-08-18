import os
import shutil
import tkinter.messagebox as messagebox
import LogManager as log
FileData = {}

supported_extensions = {
    "jpg": "Images",
    "jpeg": "Images",
    "png": "png transparent images",
    "gif": "Gif images",
    "spp": "substance painter",
    "fbx": "fbx 3D",
    "obj": "obj 3D",
    "blend": "blender files",


}
Dangerous_extensions = {
    "unity": "Unity files (unity)",
    "cs": "C# files (cs)",
    "js": "JavaScript files (js)",
    "exe": "Executable files (exe)",
    "bat": "Batch files (bat)",
    "py": "Python files (py)",
    "dll": "DLL files (Dynamic Link Library)",
    "jar": "Java files (jar)",
    "sln": "Visual Studio proje dosyaları",
    "csproj": "Visual Studio proje dosyaları",
    "index": "index files",
}

def filetransfer(path):
    Files = os.listdir(path)
    extencions = []

    
    for x in Files:
        file = x.split(".")
        for key in supported_extensions:
            if file[-1] == key:
                print("Dosya türü destekleniyor. " + supported_extensions[key])
                log.write("Dosya türü destekleniyor. " + supported_extensions[key] + "\n")
                break
            else:
                print("Dosya türü desteklenmiyor." + file[-1])
                log.write("Dosya türü desteklenmiyor." + file[-1] + "\n")
                for key in Dangerous_extensions:
                    if file[-1] == key:
                        print("Tehlikeli bir dosya türu bulundu ve işlem yarıda kesildi. + " + Dangerous_extensions[key])
                        log.write("Tehlikeli bir dosya türu bulundu ve işlem yarıda kesildi. + : " + Dangerous_extensions[key])
                        messagebox.showerror("Hata", "Tehlikeli bir dosya türu bulundu ve taşıma işlemi yarıda kesildi. \n  Detaylar için konsolu kontrol edin.")
                        return FileData
                    else:
                        continue





    for x in Files:
        file = x.split(".")
        for key in supported_extensions:
            if file[-1] == key:
                print("Dosya türü destekleniyor. " + supported_extensions[key])
                
                if file[-1] not in extencions:
                    extencions.append(file[-1])
                    FileData[file[-1]] = 0

                break
            else:
                print("Dosya türü desteklenmiyor." + file[-1])
                for key in Dangerous_extensions:
                    if file[-1] == key:
                        print("Tehlikeli bir dosya türu bulundu ve işlem yarıda kesildi. + " + Dangerous_extensions[key])
                        messagebox.showerror("Hata", "Tehlikeli bir dosya türu bulundu ve taşıma işlemi yarıda kesildi. \n  Detaylar için konsolu kontrol edin.")
                        return FileData
                    else:
                        continue
        
        

    for x in extencions:
        if x == "py":
            continue
        try:
            os.mkdir(os.path.join(path, x))  # Hedef dizini belirlemek için os.path.join kullanılıyor
        except:
            pass

    for x in Files:
        file = x.split(".")
        if file[-1] == "py":
            continue

        try:
            source_file = os.path.join(path, x)  # Kaynak dosya yolunu belirlemek için os.path.join kullanılıyor
            target_path = os.path.join(path, file[-1])  # Hedef dizin yolunu belirlemek için os.path.join kullanılıyor
            shutil.move(source_file, target_path)
            FileData[file[-1]] += 1
        except:
            pass
    return FileData
