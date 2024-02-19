# FodboldTur Applikation

Dette er en simpel applikation til håndtering af betalinger til en fodboldtur. Applikationen er bygget ved hjælp af Tkinter i Python.

## Funktioner

1. **HomePage**: Forsiden, hvor brugeren kan navigere til andre dele af applikationen.
2. **RegisterPayment**: Her kan brugeren registrere nye betalinger ved at indtaste medlemmets navn og beløb.
3. **ListPayments**: Viser en liste over alle betalinger og det beløb, hver medlem har indbetalt samt det resterende beløb, de mangler at betale.
4. **WorstPayers**: Viser de tre medlemmer, der mangler at betale mest.

## Opsætning og Systemkrav

For at køre denne applikation kræves følgende:

- Python 3 installeret på din computer.
- Tkinter, som er en standard GUI (Grafisk Brugergrænseflade) pakke til Python, er nødvendig. Tkinter følger normalt med Python-installationen, men hvis det ikke er tilfældet, kan det installeres separat.
- Derudover bruges ingen eksterne biblioteker ud over de indbyggede `tkinter` og `pickle`.

## Single Page Application (SPA)-lignende funktionalitet

Applikationen er designet med en lignende struktur som en Single Page Application (SPA), hvor alt indhold præsenteres inden for det samme grafiske brugergrænsefladevindue. Selvom det ikke er en traditionel HTML-baseret SPA, følger det samme principper med hensyn til at præsentere og navigere mellem forskellige dele af applikationen inden for et enkelt vindue. Dette giver en sømløs brugeroplevelse og gør det nemt at organisere og adskille forskellige funktioner i applikationen.

Fordelene ved at bruge en SPA-arkitektur inkluderer:

- Hurtig og mere flydende brugeroplevelse, da kun delvise opdateringer af indholdet er nødvendige.
- Reduceret belastning på serveren, da den kun sender data, ikke hele HTML-sider, til klienten.
- Bedre organisering af kode og adskillelse af ansvar, da hvert "page" er en separat klasse eller modul.

## Datahåndtering

Applikationen gemmer betalinger i en pickle-fil med navnet `betalinger.pk`. Når applikationen starter, forsøger den at indlæse tidligere gemte data fra filen. Hvis filen ikke findes eller er tom, oprettes en tom dictionary til at holde betalingerne.

## Andre Elementer

- **Pickle**: Python `pickle`-modulet bruges til at gemme og indlæse data fra en fil. Det tillader serialisering og deserialisering af Python-objekter, hvilket gør det let at gemme og genindlæse komplekse datastrukturer som en dictionary i dette tilfælde.


## Disclaimer
Bemærk: Denne README-fil er delvist genereret ved hjælp af AI. Selvom den er udarbejdet med omhu og nøjagtighed, kan visse dele være standardiserede eller automatiserede. Vi opfordrer til at læse og forstå indholdet grundigt og tilpasse det efter behov og specifikke krav til dit projekt.
