# GUIsilvaNympha - Panel do Wizualizacji Danych 📊

`GUIsilvaNympha` to aplikacja webowa oparta na frameworku Django, służąca do interaktywnej wizualizacji danych z sensorów. Umożliwia użytkownikom przeglądanie danych pomiarowych na mapie, generowanie dynamicznych wykresów oraz eksportowanie wyników do plików CSV.

---

## Główne Funkcjonalności 🚀

* **Interaktywna mapa:** Wyświetlanie obszaru zainteresowania (AOI) oraz lokalizacji sensorów na mapie (przy użyciu `Leaflet.js`).
* **Dynamiczne wykresy:** Generowanie wykresów liniowych dla wybranych parametrów i zakresów czasowych (przy użyciu `Chart.js`).
* **Zaawansowane filtrowanie:** Możliwość filtrowania danych według:
    * Parametru sensora
    * Zakresu dat
    * Schematu bazy danych (np. `daleszyce`, `gosciecice`).
* **Podgląd danych surowych:** Po wybraniu konkretnego sensora, dane wyświetlane są w formie tabelarycznej.
* **Eksport do CSV:** Możliwość pobrania przefiltrowanych danych dla wybranego sensora w formacie `.csv`.






https://github.com/user-attachments/assets/91b250f3-e047-4a1d-9426-021653492e2b




---

## Użyte Technologie 💻

### Backend
* **Python**
* **Django** (+ Django GIS)
* **PostgreSQL** z rozszerzeniem **PostGIS**
* **`python-dotenv`** (do zarządzania zmiennymi środowiskowymi)

### Frontend
* **HTML5 / CSS3**
* **JavaScript (ES6+)**
* **`Leaflet.js`** (mapy)
* **`Chart.js`** (wykresy)
* **`Flatpickr`** (wybór dat)

---

## Instalacja i Uruchomienie ⚙️

### 1. Wymagania Systemowe (GDAL)

> ⚠️ **Ważne:** Przed instalacją zależności Pythona, upewnij się, że masz zainstalowaną w systemie bibliotekę **GDAL**. Jest ona niezbędna do obsługi danych geograficznych przez GeoDjango.

* **Windows:** Zalecana instalacja przez [OSGeo4W](https://trac.osgeo.org/osgeo4w/).
* **macOS:** `brew install gdal`
* **Linux (Ubuntu/Debian):** `sudo apt-get install gdal-bin libgdal-dev`

*Plik `settings.py` zawiera miejsce na ręczne ustawienie ścieżki `GDAL_LIBRARY_PATH`, jeśli Django nie wykryje jej automatycznie.*

### 2. Klonowanie i Środowisko Wirtualne

1.  Sklonuj repozytorium:
    ```bash
    git clone <URL_REPOZYTORIUM>
    cd <NAZWA_FOLDERU_REPO>
    ```

2.  Stwórz i aktywuj środowisko wirtualne:
    ```bash
    # Windows
    python -m venv .venv
    .\.venv\Scripts\activate
    
    # macOS / Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

### 3. Instalacja Zależności

1.  Zainstaluj wymagane pakiety (najlepiej z pliku `requirements.txt`, jeśli istnieje):
    ```bash
    pip install -r requirements.txt
    ```
    
2.  Jeśli nie masz pliku `requirements.txt`, zainstaluj pakiety ręcznie i stwórz plik:
    ```bash
    pip install django psycopg2-binary python-dotenv
    pip freeze > requirements.txt
    ```

### 4. Konfiguracja

1.  **Utwórz plik `.env`** w głównym folderze projektu. Będzie on zawierał Twoje poufne dane:
    ```env
    SECRET_KEY='tutaj_wklej_swoj_tajny_klucz_django'
    DB_PASSWORD='haslo_do_twojej_bazy_danych'
    ```

2.  **Połączenie z bazą danych:**
    > ⚠️ Ten projekt **nie tworzy** bazy danych. Musisz mieć dostęp do **istniejącej bazy PostGIS**, która zawiera już wszystkie tabele i schematy. Modele w `models.py` używają `managed = False`.
    
    Upewnij się, że dane w `settings.py` (HOST, PORT, NAME, USER)  wskazują na BD.

### 5. Uruchomienie

Gdy baza danych jest dostępna i skonfigurowana, uruchom serwer:
```bash
python manage.py runserver
