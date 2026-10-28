# Worum es auf dieser Seite geht

DBnomics ist eine freie Bibliothek, die Wirtschaftszeitreihen aus offiziellen Quellen sammelt — dem IWF, der Weltbank, der OECD, Eurostat, den Zentralbanken — und alles hinter eine API legt. Diese Seite nutzt diese Bibliothek, um Wirtschaft zu erklären: ein Thema pro Seite, und jeder Chart ist ein ganz normaler Weblink. Den Link öffnen, und die Zahlen stehen direkt in der URL; in ein beliebiges Dokument eingefügt funktioniert er trotzdem.

Hole dir die Daten selbst aus der Shell (Modul-Hilfe: [x-cmd.com/mod/dbnomics](https://x-cmd.com/mod/dbnomics)):

```sh
x dbnomics data imf.us.gdp.growth
x dbnomics align imf.us.gdp imf.cn.gdp
x dbnomics alias
```

Datenstand: *World Economic Outlook* des IWF (Ausgabe 2025, mit Prognosen) und Leitzinsen des BIS. Jeder Chart nutzt 2025 als letztes Jahr.

**Schnellstart**: Füge die URL eines Charts in ein Dokument ein; oder richte einen KI-Agenten auf den [draw skill](https://raw.githubusercontent.com/x-cmd/draw/main/SKILL.md) aus und bitte ihn, USA gegen China BIP zu charten.
