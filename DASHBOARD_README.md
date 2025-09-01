# Wärmepumpe Wechsel Dashboard

Dieses Dashboard zeigt eine grafische Darstellung der Anzahl der Wechsel von "off" auf "on" der Wärmepumpe über die letzten 7 Tage.

## Funktionen

### 1. Grafische Darstellung (History Graph)
- **X-Achse**: Kalendertage (letzte 7 Tage + heute)
- **Y-Achse**: Anzahl der Wechsel pro Tag
- Zeigt die Wechselanzahl für die letzten 8 Tage in einem Linien-/Balkendiagramm

### 2. Statistik-Karten
- **Wechsel heute**: Aktuelle Anzahl der Wechsel für den heutigen Tag
- **Wechsel gestern**: Anzahl der Wechsel vom gestrigen Tag
- **Durchschnitt**: 7-Tage-Durchschnitt der Wechsel pro Tag

### 3. Detaillierte Tabelle
Zeigt für jeden Tag:
- Exaktes Datum (DD.MM.YYYY)
- Anzahl der Wechsel
- Übersichtliche Darstellung der letzten 7 Tage + heute

### 4. Markdown-Tabelle
- Kompakte tabellarische Darstellung
- Berechnung des 7-Tage-Durchschnitts
- Einfach lesbare Formatierung

## Neue Sensoren

### History Stats Sensoren
- `sensor.warmepumpe_wechsel_tag_minus_2` bis `sensor.warmepumpe_wechsel_tag_minus_7`
- Zählen die Wechsel für jeden der letzten 7 Tage
- Basieren auf `binary_sensor.warmepumpe_ist_aktiv`

### Template Sensor
- `sensor.warmepumpe_wechsel_7_tage_uebersicht`
- Berechnet den 7-Tage-Durchschnitt
- Enthält Attribute mit allen Datumswerten und Wechselzahlen

## Zugriff auf das Dashboard

Das Dashboard ist über die Home Assistant Seitenleiste verfügbar:
- **Name**: "Wärmepumpe"
- **Icon**: Wärmepumpe-Symbol (mdi:heat-pump)
- **Pfad**: `/dashboard-warmepumpe-dashboard/warmepumpe-stats`

## Konfiguration

### Konfigurationsdateien geändert:
1. **configuration.yaml**: 
   - Neue history_stats Sensoren hinzugefügt
   - Lovelace Dashboard-Konfiguration

2. **template.yaml**:
   - Template-Sensor für 7-Tage-Übersicht

3. **dashboard_warmepumpe.yaml** (neu):
   - Dashboard-Layout und Karten-Konfiguration

## Technische Details

- Die Sensoren verwenden `binary_sensor.warmepumpe_ist_aktiv` als Quelle
- Wechsel werden als Übergang von "off" zu "on" gezählt (type: count)
- Zeiträume werden täglich von 00:00 bis 00:00 berechnet
- Alle Sensoren haben eindeutige IDs für die Wiederverwendung
- Das Dashboard aktualisiert sich automatisch alle 60 Sekunden

## Fehlerbehebung

Falls das Dashboard nicht angezeigt wird:
1. Home Assistant neu starten
2. Frontend Cache leeren (Strg+F5)
3. Überprüfen, ob alle Sensoren verfügbar sind
4. Log-Dateien auf Konfigurationsfehler prüfen

## Anpassungen

Das Dashboard kann nach Bedarf angepasst werden:
- Weitere Zeiträume hinzufügen
- Andere Visualisierungstypen verwenden
- Zusätzliche Statistiken einbauen
- Farben und Styling ändern