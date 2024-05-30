# Oppgaver

## Abstraksjon og Innkapsling

### Oppgave 1: Abstraksjon med Abstrakte Klasser

#### Beskrivelse

Lag en abstrakt baseklasse `Employee` med en abstrakt metode `calculate_salary`. Lag deretter to underklasser `FullTimeEmployee` og `PartTimeEmployee` som implementerer `calculate_salary`-metoden for å beregne lønn for henholdsvis heltids- og deltidsansatte.

#### Krav

1. `Employee`-klassen skal være en abstrakt klasse med en abstrakt metode `calculate_salary`.
2. `FullTimeEmployee`-klassen skal arve fra `Employee` og implementere `calculate_salary`-metoden for å returnere en fast månedslønn.
3. `PartTimeEmployee`-klassen skal arve fra `Employee` og implementere `calculate_salary`-metoden for å returnere lønn basert på timebetaling og antall timer arbeidet.

___

### Oppgave 2: Innkapsling med Private Attributter og Gettere/Settere

#### Beskrivelse

Lag en klasse `BankAccount` med private attributter `_balance` og `_account_number`. Implementer metoder for å sette og hente balansen, samt en metode for å hente kontonummeret.

#### Krav

1. `BankAccount`-klassen skal ha private attributter `_balance` og `_account_number`.
2. Klassen skal ha metoder `get_balance`, `set_balance`, og `get_account_number` for å hente og sette verdier.
3. `set_balance`-metoden skal bare tillate positive verdier.

___

### Oppgave 3: Abstraksjon og Innkapsling i Et System

#### Beskrivelse

Lag et enkelt bibliotekssystem. Lag en klasse `Book` med private attributter `_title`, `_author`, og `_isbn`. Implementer en klasse `Library` som håndterer en samling av `Book`-objekter, med metoder for å legge til en bok, fjerne en bok, og søke etter en bok etter tittel.

#### Krav

1. `Book`-klassen skal ha private attributter `_title`, `_author`, og `_isbn`.
2. `Book`-klassen skal ha "gettere" for å hente verdiene til disse attributtene.
3. `Library`-klassen skal håndtere en liste av `Book`-objekter og ha metoder `add_book`, `remove_book`, og `find_book_by_title`.

Disse oppgavene gir praktisk erfaring med abstraksjon og innkapsling, inkludert hvordan man bruker abstrakte klasser, private attributter, og "gettere"/"settere" for å beskytte data og implementere logikk i et system.
