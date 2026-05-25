# Minesweeper

Klassisk Minesweeper i terminalen, skrevet i Python.

![Skjermbilde](screenshot.png)

## Om prosjektet

Skrevet i 1. klasse på informatikk ved Universitetet i Oslo. Et av de tidlige prosjektene jeg brukte for å øve på objektorientering: cellene, rutenettet og spill-logikken er separate klasser som kommuniserer via metodekall.

## Hva den gjør

- Du velger selv dimensjonene på brettet (x, y)
- Bomber plasseres tilfeldig
- Skriv koordinater for å avdekke en celle, eller `f` for å flagge en celle
- Spillet er vunnet når alle bomber er flagget; tapt om du går på en bombe
- Poengsum vises på slutten

## Kjøring

```bash
python program.py
```

Ingen eksterne avhengigheter — bare standard Python 3.
