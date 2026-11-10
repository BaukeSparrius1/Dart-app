# Darts 301 – camerabeeld met scorebord

Toont twee camerabeelden (één per dartbord) naast elkaar met een 301-scorebord (single out, twee spelers per bord) als overlay. Draait volledig in Chrome, zonder installatie of server.

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

- `index.html` – twee borden tegelijk: twee camera's met elk een scorebord
- `wedstrijd.html` – één wedstrijd tussen twee teams: bordcamera groot in beeld, facecam van de darter als klein venster, instelbare teamnamen en "first to X legs"
- `camera.html` – één camerabeeld, schermvullend

## wedstrijd.html

Beweeg de muis om de instellingen te tonen: teamnamen, aantal legs om te winnen, camera voor het bord en voor de facecam.
Extra sneltoetsen: **P** = facecam naar een andere hoek, **[ ]** = facecam kleiner/groter, **C** = facecam aan/uit.
In de facecam staat de naam van het team dat aan de beurt is.
