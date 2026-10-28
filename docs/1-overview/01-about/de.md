# Ökonomie, die man sehen kann

Jedes Diagramm auf dieser Seite ist ein Link. Klickt man ihn, erscheint das Bild; liest man den Link, bekommt man die Zahlen dahinter — die Daten stecken in der URL, also kann sie ein KI-Agent ebenfalls lesen. Thematisch geht es um das, was deine Woche bestimmt: Arbeit, Preise, Wachstum, Schulden und darum, was die größten Volkswirtschaften der Welt tatsächlich tun.

Die Seite gliedert sich in sechs Abschnitte, die man in einer Richtung liest: **was man anschaut → welche Regel es bindet → wie eine Volkswirtschaft aus der Nähe aussieht**. Indikatoren (BIP, Wachstum, Inflation, Arbeitslosenquote, Schulden, Leistungsbilanz, Leitzinsen, Bevölkerung und Sparen) · Makroökonomie (fünf Gesetze: Phillips, Okun, Wagner, Beveridge, Laffer) · und drei Fallstudien — Europa, die USA, China.

Unsicher, wo du anfangen sollst? Diese sechs Seiten sind die, über die gestritten wird — und jede beantwortet eine Frage, die du dir ohnehin schon stellst.

**Drei Volkswirtschaften, drei Argumente.** USA, Eurozone und China auf denselben Skalen: Wer hat den engsten Arbeitsmarkt, wer die ruhigsten Preise, wer wächst noch, wer leiht am meisten. Jeder hat eine Meinung; hier sind die Daten — und die Stellen, an denen die Daten die Sache nicht entscheiden.

**Deine Arbeit und dein Einkaufswagen liegen auf derselben Wippe.** Die Phillips-Kurve ist die älteste Regel der Makroökonomie: Steigen die Preise, werden Arbeitsplätze knapper, also müssen die Regierungen wählen, wovon sie mehr wollen. Amerika hat gerade die glatteste Variante seit vierzig Jahren durchlaufen.

**Wie kann eine Stadt Jobs haben, die niemand will, und Menschen, die einen brauchen?** Die Beveridge-Kurve trägt offene Stellen gegen die Arbeitslosigkeit ab. Sie fällt normalerweise ab; die Pandemie hat sie nach außen gebogen, und ganz gerade geworden ist sie seither nicht mehr.

**Der einzige Indikator, der jede amerikanische Rezession seit sechzig Jahren angekündigt hat.** Fällt die Rendite der 10-jährigen Treasury unter die 3-monatige, wetet der Markt darauf, dass die Notenbank senkt — und meist folgt eine Rezession. In 2022 und 2023 invertierte sie; 2025 steilte sie sich wieder auf.

**Fünfzig Volkswirtschaften, eine Kreditkarte.** Washington betreibt für Staaten, die sich eine Währung und sonst fast nichts teilen, eine einzige Fiskalpolitik, eine einzige Fed-Karte und ein einziges Insolvenzgericht. New York und Mississippi liegen um den Faktor 2,2 auseinander, und 24 Jahre „Konvergenz“ haben das nicht geschlossen.

**Ein Land, zwei Volkswirtschaften.** An Chinas Küste kann eine Fabrikstadt mehr verdienen als eine ganze Provinz im Norden. Der Abstand verringerte sich von 11,7 auf das 4,3-Fache — doch die Menschen gingen in die andere Richtung: Guangdong hat 55 Millionen Einwohner mehr als 2000.

Wie man ein Diagramm hier liest: anklicken. Die URL *ist* das Diagramm, und die Zahlen stehen sichtbar darin. Die Daten sind eine Eingabe entfernt (Modul-Hilfe: [x-cmd.com/mod/dbnomics](https://x-cmd.com/mod/dbnomics)):

```sh
x dbnomics data imf.us.gdp.growth
x dbnomics align imf.us.gdp imf.cn.gdp
x dbnomics alias
```

Datenstand: das *World Economic Outlook* des IWF (Ausgabe 2025, mit Prognosen) und die Leitzinsen des BIS; die Seiten zu Bundesstaaten und Provinzen nutzen die Regionaldatenbank der OECD. Jedes Diagramm nutzt 2025 als jüngstes Jahr. **Schnellstart**: Füge die URL eines beliebigen Diagramms in ein Dokument ein oder richte einen KI-Agenten auf den [draw skill](https://raw.githubusercontent.com/x-cmd/draw/main/SKILL.md) und bitte ihn, das BIP der USA mit dem Chinas zu vergleichen.
