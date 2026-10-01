# Yoru — catalogo manga

Sito statico in italiano, pronto per GitHub Pages. Non richiede build né dipendenze: la homepage è `index.html`.

## Pubblicazione su GitHub Pages

1. Crea su GitHub un nuovo repository pubblico, ad esempio `yoru-manga-catalogo`, senza aggiungere file iniziali.
2. Carica in quel repository il contenuto di questa cartella, mantenendo `index.html` nella radice e `.github/workflows/pages.yml`.
3. In **Settings → Pages**, seleziona **GitHub Actions** come sorgente.
4. In **Actions**, controlla il workflow **Pubblica su GitHub Pages**. Al termine, GitHub mostrerà l'indirizzo pubblico nelle impostazioni di Pages.

Il workflow ripubblica automaticamente il sito a ogni push sul branch `main`. I preferiti vengono salvati nel browser del visitatore tramite `localStorage`.
