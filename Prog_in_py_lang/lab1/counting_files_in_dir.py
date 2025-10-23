import os 


file_count = 0
for item in os.listdir("/Program Files"):
    full_path = os.path.join("/Program Files", item)
    if os.path.isfile(full_path):
        file_count += 1

print(f"Liczba plików w katalogu Program Files: {file_count}")

dir_count = 0
for item in os.listdir("/Program Files"):
    full_path = os.path.join("/Program Files", item)
    if os.path.isdir(full_path):
        dir_count += 1

print(f"Liczba folderów w katalogu Program Files: {dir_count}")


