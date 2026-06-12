---
layout: page
title: Esame
permalink: /esame/
---

<script>
	$(document).ready(function(){ $(".menu .item").tab(); });
</script>

L'esame si compone di due moduli, uno di algoritmica e uno di programmazione. I due possono essere sostenuti in appelli separati, ma all'interno di uno stesso anno accademico. Il modulo di algoritmica prevede un compito scritto, quello di programmazione un progetto da fare in gruppi da 2-3 studenti, seguito da discussione orale (tenuta solo se il progetto risulta sufficiente).


## FAQ

### Voti
- **Dove vengono pubblicati i voti?** In [questo sheet](https://docs.google.com/spreadsheets/d/1sceV5cGmsFAPHo4SDdtfjNyHVMBFmWezQ56HtSMShAU/edit?usp=sharing).
- **Quando vengono pubblicati i voti?** Per gli scritti di algoritmica, qualche giorno dopo lo scritto. Per il progetto, gli studenti con voto insufficiente sono avvisati via mail entro 3 giorni prima dell'appello: chi ha consegnato il progetto e non ricevuto mail, ha avuto un progetto sufficiente.
- **Come viene calcolato il voto?** Media aritmetica dei voti su due moduli. Entrambi devono essere sufficienti.

### Moduli
- **Posso dare i due moduli separatamente?** Si, ma entro lo stesso anno accademico. Se uno studente non sostiene con profitto entrambi i moduli tra l'appello di ottobre (compreso) e l'appello di settembre dell'anno successivo (compreso), dovrà sostenere nuovamente entrambi i moduli.
- **Per dare un modulo devo aver passato l'altro?** No, i due moduli sono indipendenti. Si consiglia comunque di studiare prima il modulo di algoritmica.

### Ricevimenti e orali
- **Dove trovo il Dipartimento di Informatica?** [Edificio C del Polo Fibonacci](https://maps.app.goo.gl/7KCceYCRTwNGPDMq9), secondo piano.
- **Dove trovo la Sala Riunioni Est/Ovest?** Chiedi nella portineria del dipartimento, o consulta [la mappa online](https://di.unipi.it/mappa-dipartimento/).
- **Quando sono gli orali?** In data d'esame, presso l'ufficio del docente. Per il modulo di programmazione, sono ammessi all'orale solo studenti con progetti sufficienti.

### Progetto
- **Dove trovo la consegna per il progetto?** Qui sotto, pubblicato a dicembre (data TBD).
- **Quando va consegnato il progetto?** Entro 7 giorni dall'appello in cui si desidera dare l'orale. Progetti consegnati oltre **non** vengono considerati.
- **Devo iscrivermi all'appello per consegnare il progetto?** Si. In ogni caso, **indicare nelle note d'iscrizione  che modulo si intende dare**. Per gli appelli straordinari, indicare anche su che programma viene dato il corso.
- **Per l'orale devo portare il computer?** No.
- **Dove si svolge l'orale?** Studio del docente (presso il Dipartimento di Informatica).
- **Come carico il progetto su Github?** Crea un account, e segui le [istruzioni online per creare un repository privato](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository). Dalla pagina del repository seleziona `Upload` (a volte indicato con il tasto `+`) e seleziona i file da caricare.
- **Come invito un collaboratore?** Segui la [documentazione online](https://docs.github.com/articles/inviting-collaborators-to-a-personal-repository).


### Lezioni
- **Sono previsti laboratori aggiuntivi?** No, le lezioni seguono il calendario indicato. Studenti interessati a chiarimenti o approfondimenti possono contattare i docenti e usufruire del ricevimento (riferimenti su Unimap).
- **Devo portare il computer a lezione?** Solo per il modulo di programmazione.
- **Dove trovo i programmi da installare?** Pagina `Materiali`.
- **Dove trovo il gruppo Teams?** Disponibile a inizio corso.

---

# Progetto

## Linee guida


In gruppi di 2-3 persone, gli studenti devono decidere come modellare i concetti richiesti, definendo classi, interfacce, estensioni, campi, e metodi, operando scelte giustificate. Il progetto **deve** includere:

1. Una documentazione
    1. Generale: un `README.md` che indica la struttura del progetto, e.g., che modulo svolge quali funzioni, quali sono le funzioni che offrono quali feature, ecc. Si includa anche una piccola sezione `Quickstart` in cui si dettaglia come eseguire gli esempi di utilizzo richiesti dal testo. Trovi esempi di `README.md` [qui](https://github.com/Informatica-per-le-biotecnologie-UniPI/postings/blob/master/README.md) e [qui](https://github.com/Informatica-per-le-biotecnologie-UniPI/traits/blob/feb7/README.md). Clicca su `Raw` per vedere il codice. Indicare anche i membri del gruppo.
    2. In codice: documentazione per funzioni e classi, i.e., commenti e tipizzazione funzioni
2. Uno o più file che implementano la consegna.

Progetti che non seguono la struttura sopra indicata sono considerati insufficienti.


### Consegna

Per la consegna, creare un repository privato su [Github](https://github.com/), e invitare user `msetzu` come collaboratore.


### Valutazione

La valutazione del progetto include, in ordine di importanza:

1. Correttezza del codice: il codice rispetta la consegna
2. Documentazione e leggibilità: il codice è scorrevole di facile lettura
3. Modularità, estensibilità: il codice è ben organizzato in moduli/classi/funzioni, e di facile estensione
4. Completezza del codice: il codice tratta anche i casi limite, e.g., un trascrittore di DNA che lancia eccezione quando il DNA dato ha lunghezza zero


# Tips & Tricks

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

## Scrittura codice
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

## Testo

<div class="ui placeholder">
    <div class="line"></div>
    <div class="line"></div>
    <div class="line"></div>
    <div class="line"></div>
    <div class="line"></div>
</div>
