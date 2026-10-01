# Yoru — catalogo manga e libri

## Come aggiungere un titolo da GitHub

1. Apri [`catalogo.json`](./catalogo.json) nel repository GitHub.
2. Premi la matita **Edit this file**.
3. Copia un oggetto già presente, incollalo prima della parentesi quadra finale `]` e cambia i campi. Metti una virgola tra gli oggetti.
4. Per i capitoli, compila la lista `chapters`: ogni capitolo ha un titolo e un link `https://` alla pagina dove si può leggere.
5. Premi **Commit changes** e conferma il commit sul branch `main`. GitHub Actions aggiorna il sito automaticamente.

Il catalogo si aggiorna normalmente in pochi minuti. Non serve modificare `index.html` o il workflow.

## Esempio: aggiungere un libro

Copia questo blocco dentro la lista `[]` di `catalogo.json`. Cambia l'`id` (solo minuscole, numeri e trattini), i dati e il capitolo. Per aggiungere un manga, usa `"type": "manga"` al posto di `"libro"`.

```json
{
  "id": "il-mio-libro",
  "title": "Il mio libro",
  "author": "Nome autore",
  "type": "libro",
  "genre": "Avventura",
  "year": 2026,
  "rating": "",
  "volumes": "In corso",
  "description": "Una breve descrizione.",
  "style": "linear-gradient(145deg,#253945,#bd654a 58%,#e4b36a)",
  "orb": "#edc38c",
  "shape": "#252834",
  "chapters": [
    {
      "title": "Capitolo 1 — L'inizio",
      "url": "https://example.com/il-mio-libro/capitolo-1"
    }
  ]
}
```

Per aggiungere altri capitoli, copia un oggetto dentro `chapters` e separalo dagli altri con una virgola. Puoi lasciare la lista vuota (`"chapters": []`) e completarla in seguito. Puoi copiare i tre campi grafici (`style`, `orb`, `shape`) da un titolo esistente.

Se hai una copertina su un indirizzo pubblico `https://`, aggiungi anche `"cover": "https://esempio.it/copertina.jpg"` prima di `chapters`.

**Nota:** ogni titolo deve avere un `id` diverso. Il JSON usa virgolette doppie e richiede virgole tra i campi e tra gli oggetti, ma non dopo l'ultimo. Il sito controlla il formato e mostra un messaggio se trova un errore.

Inserisci link a capitoli che sei autorizzato a condividere; GitHub Pages pubblica i file del repository e non è un archivio privato.

## Link

- [Apri il sito Yoru](https://cinemabot-star.github.io/MANGAWEB/)
- [Repository GitHub](https://github.com/CINEMABOT-star/MANGAWEB)
- [Modifica il catalogo su GitHub](https://github.com/CINEMABOT-star/MANGAWEB/edit/main/catalogo.json)
- [Workflow di pubblicazione](https://github.com/CINEMABOT-star/MANGAWEB/actions/workflows/pages.yml)

I preferiti vengono conservati localmente nel browser del visitatore tramite `localStorage`.
