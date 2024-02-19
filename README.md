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

- Brugervenlighed og fokus: Applikationen giver en brugervenlig oplevelse ved at holde alt indhold inden for det samme vindue. Dette eliminerer behovet for at jonglere mellem flere åbne vinduer, hvilket reducerer forvirring og holder brugeren fokuseret på den aktuelle opgave.

- Reduceret kompleksitet: Ved at begrænse interaktionen til et enkelt vindue reduceres kompleksiteten i brugergrænsefladen. Dette gør det lettere for brugerne at navigere og forstå systemet uden at skulle bekymre sig om flere åbne vinduer eller skærme.

Ulemper
- Begrænset multitasking: Brugere kan ikke have flere forskellige opgaver åbne eller kørende samtidig inden for samme applikationsvindue. Dette kan være en ulempe for dem, der er vant til at arbejde med flere applikationer eller vinduer samtidig.

- Manglende fleksibilitet: Single Window Application begrænser brugernes mulighed for at tilpasse layoutet eller organisere deres arbejdsområde efter deres præferencer. Dette kan være frustrerende for dem, der foretrækker en mere tilpasset eller fleksibel arbejdsoplevelse.


## Datahåndtering

Applikationen gemmer betalinger i en pickle-fil med navnet `betalinger.pk`. Når applikationen starter, forsøger den at indlæse tidligere gemte data fra filen. Hvis filen ikke findes eller er tom, oprettes en tom dictionary til at holde betalingerne.

## Andre Elementer

- **Pickle**: Python `pickle`-modulet bruges til at gemme og indlæse data fra en fil. Det tillader serialisering og deserialisering af Python-objekter, hvilket gør det let at gemme og genindlæse komplekse datastrukturer som en dictionary i dette tilfælde.


## Disclaimer
Bemærk: Denne README-fil er delvist genereret ved hjælp af AI. Selvom den er udarbejdet med omhu og nøjagtighed, kan visse dele være standardiserede eller automatiserede. Vi opfordrer til at læse og forstå indholdet grundigt og tilpasse det efter behov og specifikke krav til dit projekt.
