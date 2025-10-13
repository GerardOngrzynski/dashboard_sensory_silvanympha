import io

file_path = "C:/Users/wikto/PycharmProjects/DjangoProject2/pomiary/models.py"

# Wczytujemy plik binarnie
with open(file_path, "rb") as f:
    data = f.read()

# Usuwamy bajty zerowe
cleaned = data.replace(b"\x00", b"")

# Jeśli coś zostało usunięte, nadpisujemy plik
if cleaned != data:
    with io.open(file_path, "wb") as f:
        f.write(cleaned)
    print(f"[OK] Plik {file_path} został wyczyszczony z bajtów zerowych.")
else:
    print(f"[INFO] W pliku {file_path} nie znaleziono bajtów zerowych.")
