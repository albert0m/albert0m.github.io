# Concorsi Smart — TWA Site

Sito statico per GitHub Pages che serve `/.well-known/assetlinks.json` per la verifica TWA.

## Setup GitHub Pages

1. Crea un repo pubblico su GitHub (es. `concorsi-twa-site`)
2. Pusha il contenuto di questa cartella:
   ```bash
   cd test_twa
   git init
   git remote add origin git@github.com:<TUO_USER>/concorsi-twa-site.git
   git add .
   git commit -m "Initial TWA site"
   git push -u origin main
   ```
3. Vai su **Settings → Pages** del repo
4. Source: **Deploy from a branch** → branch `main`, folder `/ (root)`
5. Salva. Dopo ~1 minuto il sito sarà su `https://<TUO_USER>.github.io/concorsi-twa-site/`

## Verifica

Controlla che l'assetlinks sia raggiungibile:
```
https://<TUO_USER>.github.io/concorsi-twa-site/.well-known/assetlinks.json
```

## Aggiornare la TWA nell'app

Nel `TwaLauncherActivity`, aggiorna l'URL:
```java
Uri.parse("https://<TUO_USER>.github.io/concorsi-twa-site/")
```

## Test locale

```bash
python3 serve.py
# Apri http://localhost:8080
```
