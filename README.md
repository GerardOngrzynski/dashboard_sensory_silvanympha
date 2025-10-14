Panel do Wizualizacji Danych
GUIsilvaNympha to aplikacja webowa oparta na frameworku Django, służąca do wizualizacji danych z sensorów. Umożliwia użytkownikom przeglądanie danych pomiarowych na mapie, generowanie wykresów oraz eksportowanie wyników do plików CSV.

Główne Funkcjonalności
Interaktywna mapa: Wyświetlanie obszaru zainteresowania (AOI) oraz lokalizacji sensorów na mapie (przy użyciu Leaflet.js).

Dynamiczne wykresy: Generowanie wykresów liniowych dla wybranych parametrów i zakresów czasowych (przy użyciu Chart.js).

Filtrowanie: Możliwość filtrowania danych według: Parametru sensora, Zakresu dat, Schematu bazy danych (np. daleszyce, gosciecice).

Podgląd danych surowych: Po wybraniu konkretnego sensora, dane wyświetlane są w formie tabelarycznej.

Eksport do CSV: Możliwość pobrania przefiltrowanych danych dla wybranego sensora w formacie .csv.


Użyte Technologie
Backend:
Python,
Django (+ Django GIS),
PostgreSQL z rozszerzeniem PostGIS (do obsługi danych przestrzennych),
python-dotenv (do zarządzania zmiennymi środowiskowymi)

Frontend:
HTML5 / CSS3,
JavaScript (ES6+),
Leaflet.js (do obsługi map),
Chart.js (do tworzenia wykresów),
Flatpickr (do wyboru dat)


Wymagania systemowe
Przed instalacją zależności Pythona, upewnij się, że masz zainstalowaną w systemie bibliotekę GDAL. Jest ona niezbędna do obsługi danych geograficznych przez GeoDjango.
plik settings.py zawiera miejsce na ścieżkę do biblioteki

Windows: przez OSGeo4W.
macOS: brew install gdal.
Linux (Ubuntu/Debian): sudo apt-get install gdal-bin libgdal-dev

Instalacja i uruchomienie

git clone <URL>
cd


Stworzenie i aktywacja środowiska wirtualnego:
# Dla Windows
python -m venv .venv
.\.venv\Scripts\activate

# Dla macOS/Linux
python3 -m venv .venv
source .venv/bin/activate


Instalacja pakietów:
pip install django psycopg2-binary python-dotenv
pip freeze > requirements.txt

Utworzenie pliku .env w głównym folderze projektu

Połączenie z baza danych

Uruchomienie: python manage.py runserver
