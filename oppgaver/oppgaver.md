# Oppgaver

## Polymorfisme

### Oppgave 1: Ad Hoc Polymorfisme med Funksjon Overlasting

Definer en klasse `Calculator` som implementerer en metode `add` for å legge sammen to tall. Utvid klassen slik at `add`-metoden kan ta imot to eller tre argumenter (overlasting). Skriv også testkode som viser hvordan `add`-metoden kan brukes med både to og tre argumenter.

#### Beskrivelse

1. **Klasse `Calculator`**:
   - `add`-metoden tar to eller tre argumenter. Hvis tre argumenter gis, returneres summen av alle tre, ellers returneres summen av de to første.

2. **Testkoden**:
   - Oppretter et `Calculator`-objekt.
   - Demonstrerer bruk av `add`-metoden med to og tre argumenter.

___

### Oppgave 2: Ad Hoc Polymorfisme med Operatør Overlasting

Definer en klasse `Product` som representerer et produkt i en butikk. Implementer metode for å overbelaste `+`-operatøren slik at to `Product`-objekter kan legges sammen for å få summen av prisene deres.

#### Beskrivelse

1. **Klasse `Product`**:
   - `__init__`-metoden initialiserer et produkt med navn og pris.
   - `__add__`-metoden overbelaster `+`-operatøren for å kunne legge sammen to `Product`-objekter. Den returnerer et nytt `Product`-objekt med kombinert navn og pris.
   - `__str__`-metoden returnerer en strengrepresentasjon av produktet.

2. **Testkoden**:
   - Oppretter to `Product`-objekter.
   - Bruker `+`-operatøren for å kombinere dem.
   - Skriver ut det kombinerte produktet.

___

### Oppgave 3: Universell Polymorfisme med Subtyping

Definer en baseklasse `Shape` med en metode `area`. Deretter, definer to subklasser `Circle` og `Rectangle` som overstyrer `area`-metoden. Skriv en funksjon `print_area` som tar en `Shape`-instans som argument og skriver ut arealet.

#### Beskrivelse

1. **Klasse `Shape`**:
   - `area`-metoden er en abstrakt metode som skal overstyres i subklassene.

2. **Klasse `Circle`**:
   - `__init__`-metoden initialiserer en sirkel med en radius.
   - `area`-metoden returnerer arealet av sirkelen.

3. **Klasse `Rectangle`**:
   - `__init__`-metoden initialiserer et rektangel med bredde og høyde.
   - `area`-metoden returnerer arealet av rektangelet.

4. **Funksjon `print_area`**:
   - Tar en `Shape`-instans som argument og skriver ut arealet ved å kalle `area`-metoden.

5. **Testkoden**:
   - Oppretter en `Circle`-instans og en `Rectangle`-instans.
   - Bruker `print_area`-funksjonen til å skrive ut arealet av begge figurene.

___

### Oppgave 4: Universell Polymorfisme med Parametrisk Polymorfisme

Implementer en generisk funksjon `maximum` som kan ta inn en liste av elementer og returnere det største elementet. Test funksjonen med både en liste av tall og en liste av strenger.

#### Beskrivelse

1. **Funksjon `maximum`**:
   - Tar en liste av elementer som argument.
   - Returnerer `None` hvis listen er tom.
   - Itererer gjennom listen og finner det største elementet ved å sammenligne hvert element med det nåværende maksimumselementet.

2. **Testkoden**:
   - Tester `maximum`-funksjonen med en liste av tall.
   - Tester `maximum`-funksjonen med en liste av strenger.

___

### Oppgave 5: Polymorfisme i Python med Duck Typing

Lag en klasse `Dog` og en klasse `Cat`, begge med en metode `speak`. Skriv en funksjon `animal_sound` som tar et objekt som argument og kaller `speak`-metoden. Demonstrer duck typing ved å sende instanser av `Dog` og `Cat` til `animal_sound`-funksjonen.

#### Beskrivelse

1. **Klasse `Dog`**:
   - `speak`-metoden returnerer "Woof!".

2. **Klasse `Cat`**:
   - `speak`-metoden returnerer "Meow!".

3. **Funksjon `animal_sound`**:
   - Tar et objekt som argument og kaller `speak`-metoden på dette objektet.
   - Demonstrerer duck typing ved å bruke metoden uten å sjekke objektets klasse.

4. **Testkoden**:
   - Oppretter en `Dog`-instans og en `Cat`-instans.
   - Bruker `animal_sound`-funksjonen til å skrive ut lyden fra begge dyrene.
