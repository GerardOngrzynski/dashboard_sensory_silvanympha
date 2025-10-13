Panel do Wizualizacji Danych
GUIsilvaNympha to aplikacja webowa oparta na frameworku Django, służąca do wizualizacji danych z sensorów. Umożliwia użytkownikom przeglądanie danych pomiarowych na mapie, generowanie wykresów oraz eksportowanie wyników do plików CSV.

Główne Funkcjonalności
Interaktywna mapa: Wyświetlanie obszaru zainteresowania (AOI) oraz lokalizacji sensorów na mapie (przy użyciu Leaflet.js).

Dynamiczne wykresy: Generowanie wykresów liniowych dla wybranych parametrów i zakresów czasowych (przy użyciu Chart.js).

Filtrowanie: Możliwość filtrowania danych według: Parametru sensora, Zakresu dat, Schematu bazy danych (np. daleszyce, gosciecice).

Podgląd danych surowych: Po wybraniu konkretnego sensora, dane wyświetlane są w formie tabelarycznej.

Eksport do CSV: Możliwość pobrania przefiltrowanych danych dla wybranego sensora w formacie .csv.


Użyte Technologie
Backend
Python
Django (+ Django GIS)
PostgreSQL z rozszerzeniem PostGIS (do obsługi danych przestrzennych)
python-dotenv (do zarządzania zmiennymi środowiskowymi)

Frontend
HTML5 / CSS3
JavaScript (ES6+)
Leaflet.js (do obsługi map)
Chart.js (do tworzenia wykresów)
Flatpickr (do wyboru dat)
