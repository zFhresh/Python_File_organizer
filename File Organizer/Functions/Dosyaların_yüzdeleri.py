import os

def count_file_extensions(directory):
    print("Dosyalar sayılıyor...")
    extensions = {
        "TOTAL": 0
    }
    percents = {}

    for root, dirs, files in os.walk(directory):
        for x in files:
            file = x.split(".")
            if len(file) < 2 or file[-1] == "py":
                continue
            extension = file[-1]
            if not extension in extensions:
                extensions[extension] = 0
            extensions[extension] += 1
            extensions["TOTAL"] += 1

    for extension in extensions:
        if extension == "py" or extension == "TOTAL":
            continue
        percents[extension] = round((extensions[extension] / extensions["TOTAL"]) * 100)
    return percents

