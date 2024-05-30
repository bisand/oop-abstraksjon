# Objektorientert Programmering

## Polymorfisme

Polymorfisme er et grunnleggende konsept i objektorientert programmering som refererer til evnen til en funksjon eller en metode til å behandle objekter av mange forskjellige klasser på en uniform måte. Ordet "polymorfisme" kommer fra gresk og betyr "mange former". Det finnes hovedsakelig to typer polymorfisme i programmering:

- ad hoc polymorfisme
- universell polymorfisme.

### Praktisk eksempel på bruk av polymorfisme

___
La oss opprette en klasse som demonstrerer alle aspekter av universell polymorfisme: Parametrisk Polymorfisme og Inklusjonspolymorfisme (Subtyping). Vi kan opprette en klasse som representerer et bibliotekssystem, der vi kan legge til forskjellige typer medier (bøker, DVD-er, tidsskrifter) og utføre ulike operasjoner på dem.

```python
class Media:
    def __init__(self, title):
        self.title = title

    def display_info(self):
        return f"Title: {self.title}"

class Book(Media):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}"

class DVD(Media):
    def __init__(self, title, director):
        super().__init__(title)
        self.director = director

    def display_info(self):
        return f"Title: {self.title}, Director: {self.director}"

class Magazine(Media):
    def __init__(self, title, issue_number):
        super().__init__(title)
        self.issue_number = issue_number

    def display_info(self):
        return f"Title: {self.title}, Issue Number: {self.issue_number}"

# Generisk funksjon for å vise informasjon om et media
def display_media_info(media):
    print(media.display_info())

# Oppretter instanser av forskjellige medier
book = Book("The Great Gatsby", "F. Scott Fitzgerald")
dvd = DVD("Inception", "Christopher Nolan")
magazine = Magazine("National Geographic", "January 2024")

# Viser informasjon om hvert medium
display_media_info(book)      # Output: Title: The Great Gatsby, Author: F. Scott Fitzgerald
display_media_info(dvd)       # Output: Title: Inception, Director: Christopher Nolan
display_media_info(magazine)  # Output: Title: National Geographic, Issue Number: January 2024
```

### Forklaring

1. **`Media`-klassen**: Dette er en grunnleggende klasse som representerer et medium med et tittelattributt.

2. **Underklassene (`Book`, `DVD`, `Magazine`)**: Disse klassene arver fra `Media` og legger til ytterligere attributter (f.eks. forfatter, regissør, utgivelsesnummer) og implementerer `display_info`-metoden for å vise informasjon om det spesifikke medietypen.

3. **Generisk funksjon `display_media_info`**: Dette er en generisk funksjon som kan vise informasjon om ethvert medium, uavhengig av dets spesifikke type. Den kaller `display_info`-metoden på det gitte mediaobjektet.

4. **Instanser av `Book`, `DVD`, `Magazine`**: Vi oppretter instanser av hver mediatype og viser informasjonen ved hjelp av den generiske funksjonen `display_media_info`.

Dette eksempelet demonstrerer parametrisk polymorfisme gjennom generisk funksjon og inklusjonspolymorfisme gjennom arv og metodetilpasning (overriding) i underklassene. Klassen `Media` fungerer som en felles grensesnitt for alle mediatypene, og underklassene bruker denne felles grensesnittet mens de legger til sine egne unike egenskaper og metoder.

### Oppgaver

Oppgaver nedenfor er ment for å gi deg en forståelse av hvordan klasser og objekter fungerer. Disse skal leveres innen neste forelesning. Arbeidskravet vil bestå av å få godkjent minst 2 av oppgavene. Det er ønskelig at dere leverer så mange som mulig, men det er ikke et krav.

Klikk [her](oppgaver/oppgaver.md) for å se oppgaver ([PDF](oppgaver/oppgaver.pdf)).
