# Objektorientert Programmering

## Abstraksjon og Innkapsling

**Abstraksjon** er en av de grunnleggende prinsippene i OOP. Det handler om å forenkle kompleksiteten ved å skjule de detaljerte implementasjonene og kun eksponere nødvendige deler av objektet. Ved å bruke abstraksjon kan utviklere arbeide med komplekse systemer uten å trenge å forstå alle de interne mekanismene. I kontekst av cyber security, kan abstraksjon hjelpe med å bygge systemer som skjuler sensitive detaljer og eksponerer kun det som er nødvendig for brukere eller andre systemkomponenter.

**Innkapsling** refererer til praksisen med å begrense tilgangen til visse komponenter og beskytte objektets tilstand ved å kontrollere hvordan dataene blir endret. Dette oppnås vanligvis ved å gjøre datafelt private og gi offentlige metoder for tilgang og modifikasjon. I cyber security er innkapsling viktig for å beskytte sensitive data og sikre at de kun kan manipuleres på sikre og kontrollerte måter.

### Praktisk eksempel på bruk av Abstraksjon

___
**ABC-modulen** (Abstract Base Classes) i Python gir et rammeverk for å definere abstrakte basisklasser. Abstrakte basisklasser er klasser som ikke er ment å bli instansiert direkte, men som fungerer som grunnlag for andre klasser. De kan inneholde abstrakte metoder som må implementeres av subklasser, og de kan også inneholde vanlige metoder som gir standard oppførsel.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Instansiering av en abstrakt klasse vil føre til en feil
# animal = Animal()  # Dette vil utløse en TypeError

# Riktig bruk med subklasser
dog = Dog()
cat = Cat()
print(dog.make_sound())  # Output: Bark
print(cat.make_sound())  # Output: Meow
```

### Hvorfor er ABC-modulen nødvendig?

1. **Tvinger Implementasjon**: Ved å bruke abstrakte basisklasser kan du tvinge subklasser til å implementere bestemte metoder. Dette sikrer at alle subklasser følger et felles grensesnitt, noe som gir konsistens i koden.
2. **Forbedrer Kodekvalitet**: ABC-modulen hjelper med å organisere koden bedre ved å tydelig definere hva som forventes av en subklasse. Dette gjør det lettere å vedlikeholde og forstå koden.
3. **Forenkler Testing og Utvidelse**: Ved å bruke abstrakte basisklasser kan du lage testklasser som simulerer ulike scenarier. Det blir også enklere å utvide systemet med nye klasser som implementerer de abstrakte metodene.
4. **Fremmer God Programvarearkitektur**: ABC-modulen støtter prinsipper som SOLID (spesielt Liskov Substitution Principle og Interface Segregation Principle) ved å sikre at klasser har tydelige roller og ansvar.

### Praktisk eksempel på bruk av Innkapsling

#### Eksempel: Bankkonto

Tenk deg at vi skal lage et system for å administrere bankkontoer. Vi vil bruke innkapsling for å beskytte kontoens saldo og sikre at den bare kan endres gjennom kontrollerte metoder.

#### Implementering av Innkapsling

```python
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.__balance = initial_balance  # Privat attributt for saldo

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Innskuddsbeløpet må være positivt")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Uttaksbeløpet må være positivt og ikke overskride saldoen")

    def get_balance(self):
        return self.__balance  # Offentlig metode for å hente saldoen

    def transfer(self, target_account, amount):
        if self.withdraw(amount):
            target_account.deposit(amount)

# Opprette en ny bankkonto
account = BankAccount("123456789", 1000)

# Gjøre innskudd
account.deposit(500)
print(f"Saldo etter innskudd: {account.get_balance()}")

# Gjøre uttak
account.withdraw(200)
print(f"Saldo etter uttak: {account.get_balance()}")

# Forsøke å gjøre et ulovlig uttak
try:
    account.withdraw(2000)
except ValueError as e:
    print(e)

# Prøve å få tilgang til den private saldoen direkte (vil feile)
try:
    print(account.__balance)
except AttributeError as e:
    print(e)
```

#### Forklaring:

1. **Private Attributter**:
   - `self.__balance`: Dette er en privat attributt som kun kan nås direkte innenfor klassen. Ved å bruke to understreker (`__`) foran attributtnavnet, indikerer vi at dette feltet ikke bør endres direkte fra utenfor klassen.

2. **Offentlige Metoder**:
   - `deposit(self, amount)`: Metode for å legge til penger på kontoen. Kontrollerer at beløpet er positivt før det legges til saldoen.
   - `withdraw(self, amount)`: Metode for å ta ut penger fra kontoen. Kontrollerer at beløpet er positivt og ikke overstiger saldoen.
   - `get_balance(self)`: Metode for å hente gjeldende saldo. Gir en kontrollert måte å lese saldoen på.
   - `transfer(self, target_account, amount)`: Metode for å overføre penger til en annen konto ved å bruke de eksisterende innskudd- og uttaksmetodene.

3. **Feilhåndtering**:
   - `ValueError`: Kastes hvis innskudds- eller uttaksbeløpet ikke er gyldig.

4. **Beskyttelse av Data**:
   - Den private attributten `__balance` kan ikke nås direkte fra utenfor klassen. Dette sikrer at saldoen kun kan endres gjennom de definerte metodene, som inneholder nødvendige valideringskontroller.

#### Demonstrasjon av Innkapsling:

- Når vi prøver å gjøre et ulovlig uttak, kaster systemet en feilmelding, noe som forhindrer at saldoen blir negativ.
- Forsøk på å få tilgang til `__balance` direkte fra utsiden av klassen fører til en `AttributeError`, noe som viser at innkapslingen beskytter saldoen fra direkte tilgang og modifikasjon.

### Oppsummering

Innkapsling er et kraftig verktøy i OOP som beskytter objektets tilstand ved å kontrollere hvordan dataene blir endret og aksessert. Dette eksempelet på en bankkonto viser hvordan vi kan bruke private attributter og offentlige metoder for å oppnå sikker og kontrollert tilgang til sensitiv informasjon, som kontosaldoen. Dette er spesielt viktig i kontekster som bank- og finansapplikasjoner, hvor datasikkerhet er kritisk.

### Oppgaver

Oppgaver nedenfor er ment for å gi deg en forståelse av hvordan klasser og objekter fungerer. Disse skal leveres innen neste forelesning. Arbeidskravet vil bestå av å få godkjent minst 2 av oppgavene. Det er ønskelig at dere leverer så mange som mulig, men det er ikke et krav.

Klikk [her](oppgaver/oppgaver.md) for å se oppgaver ([PDF](oppgaver/oppgaver.pdf)).
