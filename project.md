---
layout: page
title: "Esame e FAQ"
permalink: /esame/
---

<script>
	$(document).ready(function(){ $(".menu .item").tab(); });
</script>

L'esame si compone di due moduli, uno di algoritmica e uno di programmazione. I due possono essere sostenuti in appelli separati, ma all'interno di uno stesso anno accademico. Il modulo di algoritmica prevede un compito scritto, quello di programmazione un progetto da fare in gruppi, seguito da discussione orale (tenuta solo se il progetto risulta sufficiente).

---

# Algoritmica

Esame scritto. Sono disponibili esami degli anni passati per esercitarsi:

- [2023](https://github.com/Informatica-per-le-biotecnologie-UniPI/web26/blob/main/static_files/lectures/algoritmica/verifica%202023.pdf)
- [2022](https://github.com/Informatica-per-le-biotecnologie-UniPI/web26/blob/main/static_files/lectures/algoritmica/verifica%202022.pdf)

---

# Programmazione

In piccoli gruppi, gli studenti devono decidere come modellare i concetti richiesti, definendo classi, interfacce, estensioni, campi, e metodi, operando scelte giustificate. Il progetto **deve** includere:

1. Una documentazione
    1. Generale: un `README.md` che indica brevemente l'obbiettivo del progetto, e la suddivisione in file/funzioni. Includi anche una piccola sezione `Quickstart` in cui mostri le funzioni richieste dal testo. Trovi esempi di `README.md` [qui](https://github.com/Informatica-per-le-biotecnologie-UniPI/postings/blob/master/README.md) e [qui](https://github.com/Informatica-per-le-biotecnologie-UniPI/traits/blob/feb7/README.md). Clicca su `Raw` per vedere il codice.
    2. In codice: documentazione per funzioni e classi, i.e., commenti e tipizzazione funzioni
2. Uno o più file che implementano la consegna.

Progetti che **non seguono la struttura** sopra indicata sono considerati **insufficienti**.

## Gruppi
I gruppi sono formati da 3-4 studenti, e vanno indicati in [questo sheet](https://docs.google.com/spreadsheets/d/1IfKt6NAG3ULoA9gPxBWgUFff2IMi86HDTlrlKxugz0k/edit?usp=sharing).
Indica anche un nome a tema bio/biotech per il tuo gruppo. Il nome più divertente sarà premiato a fine corso.
A ogni gruppo sarà assegnato un progetto durante il corso, pertanto cerca di formare il gruppo appena possibile.
Indica la mail del membro referente: utilizza una mail istituzionale (@studenti.unipi.it).


## Consegna

Per la consegna del progetto, crea un repository privato su [Github](https://github.com/) con il nome del gruppo, e invita user `msetzu` come collaboratore. Il progetto non ha deadline.


## Valutazione progetto

La valutazione del progetto include, in ordine di importanza:

1. Correttezza del codice: il codice rispetta la consegna
2. Documentazione e leggibilità: il codice è scorrevole di facile lettura
3. Modularità, estensibilità: il codice è ben organizzato in moduli/classi/funzioni, e di facile estensione
4. Completezza del codice: il codice tratta anche i casi limite, e.g., un trascrittore di DNA che lancia eccezione quando il DNA dato ha lunghezza zero


## Orale

Alla discussione orale, terrete una breve presentazione (max. 10 minuti) in cui mostrate i risultati ottenuti nel progetto, e le parti del progetto che ritenete più importanti e/o sono state più difficoltose, e come le avete affrontate. Caricate la vostra presentazione in [questa cartella condivisa](https://drive.google.com/drive/folders/17PQz6VxTxfs8e--6oOqQ9ePg4FZpBlqc?usp=sharing). Si consiglia un formato pdf, pptx, o Google Slides.

Viene inoltre richiesto di programmare: viene messa a disposizione una macchina, e una cheat sheet.


## Tips & Tricks

### Nomenclatura, tipizzazione, e commenti
- Usa nomi significativi, ed evita quando possibile sigle e variabili a una lettera, e.g., `x`
- Usa lo *snake case* per variabili e funzioni: separa le parole con `_`, e.g., `starting_codon`
- Usa il *camel case* per le classi: separa le parole con una maiuscola, e.g., `PapillomaVirus`
- Indica i tipi dei parametri delle funzioni, e il loro tipo di ritorno
- Nelle funzioni e nei metodi, indica con un breve commento cosa la funzione implementa, e a cosa servono i vari parametri

### Import
In caso di progetto con diversi file, puoi trattare ogni file come un "modulo" da cui importare funzioni e/o classi. E.g., dato un file `amoeba.py` con contenuto

`amoeba.py`
```python
def foo(a, b):
    ...

class Amoeba:
    ...
```

puoi poi creare, nella stessa cartella, un file con contenuto

```python
from amoeba import Amoeba
from amoeba import foo

x = Amoeba()
y = foo(...)
...
```

**Nota:** L'`import` esegue il file che importa. Se hai del codice esterno alle funzioni/classi, questo viene eseguito ogni volta che fai l'import. Per buona pratica, nei file da cui vuoi importare funzioni/classi non inserire codice ulteriore.

### Documentazione

Quando sei in dubbio, sfrutta la [cheat sheet](https://informatica-per-le-biotecnologie-unipi.github.io/web25//static_files/cheat.pdf) o la documentazione di Python!

- Documentazione [costrutti](https://docs.python.org/3/tutorial/controlflow.html)
- Documentazione [collezioni](https://docs.python.org/3/tutorial/datastructures.html)
- Documentazione [eccezioni](https://docs.python.org/3/tutorial/errors.html)
- Documentazione [funzioni predefinite](https://docs.python.org/3/library/functions.html)

### Scrittura codice
Quando scrivi codice:
1. Identifica che categorie di dati ti servono
2. Identifica che tipo di manipolazioni vuoi farci
3. Traducile in Python con tipi esistenti/nuove classi
4. Struttura, su carta, un piccolo algoritmo per risolvere il problema
	1. Separa quando possibile funzionalità diverse, fino a raggiungere piccoli task relativamente semplici: divide et impera
	2. Identifica relazioni tra i task, e.g., per simulare la trascrizione del DNA devo estrarre triplette, convertire le triplette in aminoacidi, etc.
5. Traduci in Python: decidi cosa implementare come funzione, come metodo, etc.
6. Scrivi un paio di esempi guida per testare il tuo codice, e.g., un paio di piccoli genomi a mano su cui testare se il tuo codice funziona
7. Implementa separatamente tutte le diverse funzioni/algoritmi
8. Testa il tuo codice sugli esempi del punto sopra, partendo dai tuoi task base. Se falliscono, torna indietro, aggiusta, e torna al punto precedente

L'utilizzo di strumenti di AI per la scrittura di codice o documentazione **non è consentito**.


# Testo progetto

TBA