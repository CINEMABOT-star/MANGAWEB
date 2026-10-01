# Yoru — catalogo manga e libri

## Aggiungere un manga o un libro

Ogni opera ha la sua cartella; ogni capitolo ha una sottocartella. Per mantenere facilmente questa struttura e caricare immagini in blocco, usa **GitHub Desktop**: clona `https://github.com/CINEMABOT-star/MANGAWEB.git`, copia la cartella `_modello` in `manga` oppure `libri`, rinominala con il titolo, poi fai **Commit to main** e **Push origin** da GitHub Desktop.

```text
manga/
  nome-manga/
    info.json
    copertina.jpg                 (facoltativa)
    capitoli/
      001/
        001.jpg
        002.jpg
      002/
        001.jpg

libri/
  nome-libro/
    info.json
    capitoli/
      001/
        capitolo.pdf
      002/
        capitolo.pdf
```

Per un manga usa `manga/nome-manga/`; per un libro usa `libri/nome-libro/`. Aggiorna il `info.json` del modello e copia la cartella `capitoli/001` per ogni nuovo capitolo. Per un manga metti le pagine in immagini numerate (`001.jpg`, `002.jpg` e così via); per un libro metti un PDF dentro la cartella del capitolo. I file `README.md` nei modelli sono solo istruzioni e non vengono mostrati nel catalogo.

### Contenuto di `info.json`

```json
{
  "title": "Il mio manga",
  "author": "Nome autore",
  "genre": "Avventura",
  "year": 2026,
  "description": "Una breve descrizione.",
  "rating": "",
  "volumes": "In corso",
  "cover": "copertina.jpg"
}
```

`title`, `author`, `genre`, `year` e `description` sono obbligatori. `rating`, `volumes` e `cover` sono facoltativi. Se non specifichi la copertina, il sito crea una copertina grafica. Per aggiungere una copertina, aggiungi il suo file (ad esempio `copertina.jpg`) alla cartella del titolo e `"cover": "copertina.jpg"` in `info.json`. Usa nomi di cartella semplici, per esempio `one-piece` o `il-mio-libro`.

## Pubblicazione automatica

Quando hai aggiunto o aggiornato i file, fai **Commit to main** e poi **Push origin** in GitHub Desktop. GitHub Actions trova automaticamente nuove cartelle e capitoli, aggiorna il catalogo e pubblica tutto su [Yoru](https://cinemabot-star.github.io/MANGAWEB/). Non devi modificare `catalogo.json`: viene generato durante la pubblicazione. Puoi controllare lo stato in [Actions](https://github.com/CINEMABOT-star/MANGAWEB/actions/workflows/pages.yml).

I capitoli immagine si leggono direttamente nel sito; PDF ed EPUB si aprono dal relativo capitolo. Carica solo opere e immagini che sei autorizzato a distribuire: il repository e il sito sono pubblici e i file possono essere scaricati da chiunque.

## Link

- [Apri il sito Yoru](https://cinemabot-star.github.io/MANGAWEB/)
- [Repository GitHub](https://github.com/CINEMABOT-star/MANGAWEB)
- [Workflow di pubblicazione](https://github.com/CINEMABOT-star/MANGAWEB/actions/workflows/pages.yml)
