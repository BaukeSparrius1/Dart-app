# Darts 301 – camerabeeld met scorebord

Camerabeelden van één of twee dartborden met een scorebord (single out, 201/301/501, best of 1–11) als overlay, plus een klassement voor het hele toernooi. Draait volledig in Chrome, zonder installatie of server.

## Gebruik

1. Verbind de camera's (bijvoorbeeld twee telefoons via Iriun Webcam).
2. Open `index.html` in Chrome en sta cameragebruik toe.
3. Kies per bord de camera in het menu bovenin (beweeg de muis om het te tonen).
4. Toon het op een beeldscherm via HDMI (Win+P → Alleen tweede scherm) of cast het tabblad naar een Chromecast.

## Sneltoetsen

| Toets | Actie |
|---|---|
| Score + Enter | Beurt invoeren |
| Tab | Wisselen tussen bord 1 en 2 |
| U / Ctrl+Z | Laatste beurt ongedaan maken |
| H | TV-modus: bediening en muiscursor verbergen |
| F | Volledig scherm |
| Scrollen / slepen | Zoomen / verschuiven per beeld |
| + / − / pijltjes | Zoomen en verschuiven met het toetsenbord |
| R of dubbelklik | Zoom herstellen |

Stand, spelersnamen, camerakeuze en zoom worden lokaal in de browser bewaard.

## Bestanden

- `index.html` – **alles in één bestand**: 1 bord, 2 borden en klassement. Dit is het bestand om te openen of te downloaden.
- `src/een-bord.html` – één wedstrijd tussen twee teams: bordcamera groot in beeld, facecam als klein venster, instelbare teamnamen en "first to X legs"
- `src/twee-borden.html` – twee borden tegelijk: twee camera's met elk een scorebord
- `src/klassement.html` – totaalstand van alle teams over dartrondes en minigames, met knop om de finale te starten
- `build.py` – voegt de pagina's in `src/` samen tot `index.html`. Draai `python3 build.py` na elke wijziging in `src/`.
- `camera.html` – één camerabeeld, schermvullend

Wisselen tussen de pagina's kan via de knoppen *1 bord*, *2 borden* en *Klassement* (beweeg de muis om ze te tonen). Na het wisselen moet je volledig scherm (F) opnieuw aanzetten.

## 1 bord

Links (of rechts) een paneel met de facecam, het scorebord en de stand van het klassement; daarnaast het bord groot in beeld.
Beweeg de muis om de instellingen te tonen: teams (keuzemenu, namen uit het klassement), best of 1–11, startscore 201/301/501, camera's en indeling.
Extra sneltoetsen: **L** = paneel naar de andere kant, **[ ]** = paneel smaller/breder, **C** = facecam aan/uit, **K** = klassement in het paneel aan/uit.

## Klassement

- Stel het aantal teams in en klik op een team- of kolomnaam om die te wijzigen.
- Voeg kolommen toe met **+ Dartronde** en **+ Minigame**; verwijder ze met het kruisje.
- Typ per team de punten. Optellen in het vakje mag (`3+1`). Enter springt naar het vakje eronder.
- **Finale starten** zet de nummers 1 en 2 als teams op de 1-bordpagina en opent die.
- Onder de tabel staat een tekstvak voor **regels** (bijv. van het drankspel), één regel per lijn. In TV-modus worden ze als lijst getoond.
- Naast de regels staat een vak **Speelschema** voor een afbeelding (kiezen, slepen of plakken met Ctrl+V). Klik erop of druk op **S** om hem schermvullend te tonen.
- **H** = TV-modus (alleen bekijken), **F** = volledig scherm.
