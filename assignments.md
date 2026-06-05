---
layout: assignments
title: Esercitazioni
permalink: /esercitazioni/
---

Le esercitazioni accompagnano passo passo l'apprendimento della programmazione.
È **fortemente consigliato** lavorarci durante le esercitazioni in aula, da soli o con il proprio gruppo di studio, e sfruttare ricevimenti in caso di dubbi.
Possibili soluzioni disponibili sul [Github del corso](https://github.com/Informatica-per-le-biotecnologie-UniPI/web26/tree/teaching/programmazione/esercitazioni).


---

Per mostrare un risultato, usa `print()`.

# 1
Dato un genoma di lunghezza arbitraria...
1. Estrai il codone (tre caratteri) iniziale
2. Estrai il codone (tre caratteri) finale

# 2
L'espressione
```python
var = 10
f"{var}"
```
viene detta `f-string` (stringa formattata), e valuta a `"10"`: in una stringa preceduta da `f`, le espressioni tra `{ }` vengono valutate, e se son stringhe (o possono essere valutate come tali), inserite nella stringa.

1. Dati i) un codone iniziale, ii) un codone finale, e iii) una sequenza intermedia, crea una f-string che le concateni
2. Dati i) un codone iniziale, ii) un codone finale, e iii) una sequenza intermedia, crea una stringa che le concateni, ma senza usare una f-string
3. Scrivi un'espressione che verifichi che le stringhe date dal punto `1.` e `2.` siano uguali

# 3
4. L'espressione `"ACGT'` contiene un errore?
5. L'espressione `'"ACGT"'` contiene un errore?
6. L'espressione `'"ACGT"'` contiene un errore?
7. L'espressione `'"0" + 1` contiene un errore?
8. L'espressione `'"0" + "1"` contiene un errore?
9. L'espressione `'"0" + "1" == 1` contiene un errore?

# 4
Data una collezione di numeri...
1. Trova i valori massimi
2. Trova i valori minimi
3. Ripeti `1.`, ma se ritrovi lo stesso valore massimo, stampalo ogni volta che lo trovi
4. Ripeti `2.`, ma se ritrovi lo stesso valore minimo, stampalo ogni volta che lo trovi
5. Ripeti `1.`, in questo caso la collezione è una lista: accedi agli elementi usando l'operatore `[]`
6. Verifica che un elemento dato sia nella collezione
7. Verifica che due elementi dati siano entrambi nella collezione
8. Verifica che uno di due elementi dati sia nella collezione, e l'altro no
9. E un'altra collezione di numeri, verifica che tutti gli elementi della seconda siano nella prima
10. E un'altra collezione di numeri della stessa lunghezza, conta il numero di caratteri uguali (posizione per posizione)

# 5
Una *maschera* (mask) è una sequenza booleana che filtra gli elementi di una sequenza. Se l'`i`-esimo elemento della maschera é vero, allora l'elemento viene selezionato, altrimenti viene scartato.

1. Costruisci una maschera di una lunghezza arbitraria
2. Data una sequenza, e.g., una stringa, della stessa lunghezza della maschera, stampa tutti i caratteri selezionati dalla maschera
3. Data una sequenza, e.g., una stringa, della stessa lunghezza della maschera, stampa tutti i caratteri scartati dalla maschera
4. Data una sequenza, e.g., una stringa, di lunghezza inferiore della maschera, stampa tutti i caratteri selezionati dalla maschera. Considera scartati tutti gli elementi in eccesso
5. Data una sequenza, e.g., una stringa, di lunghezza inferiore della maschera, stampa tutti i caratteri scartati dalla maschera. Considera scartati tutti gli elementi in eccesso
6. Data una sequenza, e.g., una stringa, della stessa lunghezza della maschera, somma tutti gli elementi selezionati dalla maschera

# 6
Sono date `n` stringhe (seleziona `n` a piacere) di una data lunghezza `m`.
1. Per ogni posizione `i` in `[0, m - 1]`, stampa tutti i caratteri che appaiono in posizione `i`
2. Per ogni posizione `i` in `[0, m - 1]`, stampa il carattere più frequente in posizione `i`
3. Con `n == 2`, verifica che le due stringhe siano palindrome

---

# Dna to Protein

Scrivere un programma che, data una stringa di DNA, la traduce nella catena di aminoacidi corrispondente. Il programma
1. Traduce il DNA in RNA
2. Traduce l'RNA in una sequenza di aminoacidi

Per semplicità, considera solo un sottoinsieme di aminoacidi. Considera inoltre di dover incorporare alcuni vincoli:

- Il DNA deve avere una lunghezza appropriata
- Esistono un codone iniziale e uno finale che non codificano aminoacidi


---

# Motifs

Data una stringa di DNA, un *motif* rappresenta una sottosequenza frequente, ossia che appare spesso nel DNA. Scrivi un programma che, data una lunghezza, cerca tutti i motif candidati, ne calcola la frequenza, e li restituisce ordinati per frequenza.

---

# Posting lists
Una posting list associa, ad ogni elemento, le posizioni in cui appare in una sequenza. Creare una funzione che crea la posting list di una data stringa.

Esempio.
```
ACGAGGTAC
```
Ha una posting list
```
A: [0, 3, 7]
C: [1, 8]
G: [2, 4, 5]
T: [6]
```


Si crei una funzione per verificare se una stringa `a*b` appare nella sequenza.
`a*b` indica una stringa in cui appare `a`, seguita da un numero arbitrario di caratteri, seguita da `b`.
Si sfrutti la costruzione della posting list.

Esempio.


| `a` | `b` | Appare? |
| --- | --- | ------- |
| `A` | `C` | Si      |
| `A` | `T` | Si      |
| `T` | `C` | Si      |
| `T` | `X` | No      |
| `T` | `G` | No      |


## Posting list 1
Si crei una funzione per verificare se una stringa `a*b*c` appare nella sequenza.

## Posting list 2
Si crei una funzione per verificare se una stringa `(a)+` appare nella sequenza. `(a)+` indica una stringa in cui la stringa `a` appare *almeno* una volta.

## Posting list 3
Si crei una funzione per verificare se una stringa `(a){m,n}` appare nella sequenza. `(a){m,n}` indica una stringa in cui la stringa `a` appare tra `m` e `n` volte. I parametri sono opzionali.

---

# Automata

Un linguaggio regolare implementa un automa, un oggetto matematico che descrive un sistema a stati in cui il sistema è in uno di diversi possibili stati `Si`. Di questi, uno è detto stato iniziale (da cui parte il sistema), e un insieme è detto stato finale (in cui il sistema termina). Il sistema funziona come un *riconoscitore di linguaggi*: elemento per elemento, il sistema consuma una stringa data, e se alla fine si trova in uno stato finale, il sistema *riconosce* il linguaggio, e in caso contrario, no.

Il sistema descrive un insieme di regole di transizione che, partendo dallo stato iniziale, lo fanno passare da uno stato `Si` a uno `Sj`. Ogni passaggio è dato da uno stato di origine, un simbolo, e uno stato di destinazione.

**Esempio.** 

![automaton](https://upload.wikimedia.org/wikipedia/commons/9/9d/DFAexample.svg)

*Un automa con due stati `S1` e `S2`, e le transizioni, definite come archi. Lo stato iniziale viene indicato dalla freccia, e quelli finali da un doppio cerchio.*

Stati del sistema.
```
S = {S1, S2}
```

Transizioni del sistema.

| Sorgente | Simbolo | Destinazione |
| -------- | ------- | ------------ |
| `S1`     | `0`     | `S2`         |
| `S1`     | `1`     | `S1`         |
| `S2`     | `0`     | `S1`         |
| `S2`     | `1`     | `S2`         |

Alcune stringhe accettate (prova partendo da `S1` a seguire gli archi dettati dai simboli: finirai in uno stato finale!)
```
- (stringa vuota)
1
11
111
1111
...
00
0000
000000
010
0110
01110
011110
...
```

**Traccia.** Data una stringa $s$ e un automa $a$, una traccia $T_s^a$ indica la sequenza di stati di $a$ utili a verificare $s$.
E.g., per $s = 0110$ nell'esempio precedente, $T^a_{s} = S_{1}, S_{2}, S_{2}, S_{1}$.

## Automaton 0: Trace

Arricchisci le classi definite nel blocco precedente, aggiungendo un calcolo traccia dove possibile, e.g., nella verifica di una stringa.

## Automaton 1: Non-deterministic automata
Una famiglia di automi è detta *non-deterministica* se nel suo insieme di transizioni esistono due transizioni $S_{i} \xrightarrow{\sigma} S_{j}, S_{i} \xrightarrow{\sigma} S_{k}$ con $S_{j} \neq S_{k}$.
Ossia, se esiste uno stato sorgente in cui possiamo raggiungere due stati destinazione diversi con uno stesso simbolo: un bivio senza indicazioni e che porta a destinazioni diverse.

Implementa la verifica di una stringa su automi non deterministici.
Se ritieni necessario, estendi il tuo sistema di classi.

---

## Modulo 1: organismi
Si definisce una specie `X`, e.g., `Rattus Norvegicus`, i cui membri son definiti da diverse caratteristiche e comportamenti. La specie deve estendere una classe astratta `Species`. L'organismo è definito dal suo genoma, e dal suo meccanismo di riproduzione.

### Genoma
Definito su un alfabeto di basi `{"A", "C", "G", "T"}`, e di una lunghezza fissa $l \geq 30$ e multiplo di tre.

### Meccanismo di riproduzione sessuata
Membri di un sesso si riproducono esclusivamente con membri dell'altro sesso, dando vita a un numero $k$ di organismi figli.

#### Riproduzione
$k$ è dato da
- Un insieme (non vuoto) di fattori ambientali, e.g., concentrazione ossigeno, dati al momento della riproduzione. L'ambiente viene definito nel modulo 2.
- La fertilità combinata degli organismi genitori. Come questa venga combinata, e.g., somma, media, ecc., è di libera scelta.

Come i fattori ambientali determinano $k$ è di libera scelta, e.g.,
- Con bassa concentrazione di ossigeno, $k$ rimane tra $1$ e $3$
- Con media concentrazione di ossigeno, $k$ rimane tra $2$ e $5$
- Con media concentrazione di ossigeno e alta pressione, $k$ rimane tra $1$ e $2$
- ...

#### Genoma nuova generazione
La creazione del genoma per un organismo figlio segue due fasi, una di seguito all'altra:
1. Creazione genoma figlio
2. Mutazioni tratti

La nuova generazione ha, base per base, un genoma randomico che non dipende dai genitori.
Fanno eccezione alcune porzioni contigue del genoma, che codificano dei *tratti* della specie.

**Tratti.** Un *tratto* è caratterizzato da:
- Una posizione e lunghezza (fisse in ogni organismo e generazione!)
- Un insieme di valori, ognuno codificato da (una sequenza di) basi. Per semplicità si può considerare che ogni valore ha una sola sequenza che lo definisce. Qualsiasi altra sequenza che non codifica un valore viene considerata tratto "nullo" o "perso". Puoi usare un "-" come simbolo al di fuori dell'alfabeto per indicarlo.
- Un indice di dominanza dei valori: maggiore è l'indice, maggiore la probabilità che questo valore sia trasmesso di generazione in generazione. Gli indici sono nell'intervallo $[0, 1]$, e sommano a $1$.

Ad esempio, un tratto `Colore occhi` viene trasmesso nella posizione $125$, ha lunghezza $1$, e i seguenti valori e indici di dominanza.

| Valore | Genoma | Indice dominanza |
| ------ | ------ | ---------------- |
| Blu    | `A`    | `0.2`            |
| Verde  | `C`    | `0.4`            |
| Grigio | `G`    | `0.4`            |

*Esempio di indici di dominanza per il tratto colore occhi. Nota che gli indici sommano a 1.*

Nel processo di riproduzione, un valore del tratto dei genitori si trasmette al figlio, con una probabilità proporzionale alla dominanza del tratto.
Ossia, un tratto a dominanza maggiore avrà probabilità maggiore di essere trasmesso.
 
**Mutazioni.** Randomicamente, e a probabilità molto basse, la sequenza che definisce un tratto può mutare.
Questo può anche distruggere il tratto!
Un tratto distrutto ha **sempre** indice di dominanza $0$: viene passato alla generazione successiva *se e solo se* entrambi i genitori hanno il tratto distrutto!
E.g., una mutazione sul colore occhi potrebbe rimuovere totalmente la pigmentazione dell'iride se la mutazione risulta in una sequenza diversa da quelle che lo codificano.
Similmente, un tratto perso per mutazione può essere ripristinato successivamente da un'altra mutazione.

| Valore                | Genoma | Indice dominanza |
| --------------------- | ------ | ---------------- |
| Blu                   | `A`    | `0.2`            |
| Verde                 | `C`    | `0.4`            |
| Grigio                | `G`    | `0.4`            |
| Perdita pigmentazione | `T`    | `0`              |

*Esempio di un tratto `Colore occhi`. Una mutazione del genoma associato al tratto lo può distruggere!*


Si definiscano $2$ tratti con $2+$ possibili valori, indici di dominanza, genomi, posizioni e lunghezze associate. Si definisca una mutazione che, *dopo* la creazione del genoma dell'organismo appena nato, randomicamente e con una data probabilità, modifichi la sequenza associata a un tratto. La mutazione è di libera scelta, con un valore fisso o randomico.


## Modulo 2: ambiente
Si definisce un ambiente che gestisca gli organismi del modulo 1.
L'ambiente è definito da:
- Epoche: unità temporale, e.g., anno, in cui osserviamo l'ambiente e gli organismi in esso
- Organismi: definiti al punto 1
- "Generazione" di ogni organismo che traccia a che generazione appartiene un singolo organismo
- Fattori ambientali che variano a ogni epoca

**Organismi e relazioni.** L'ambiente deve tenere traccia delle varie generazioni e fornire il riconoscimento dell'ordine di generazione, i.e., l'ambiente deve fornire una funzione per poter rispondere alla domanda "L'organismo `A` appartiene a una generazione precedente a organismo `B`?"

**Fattori ambientali.** I fattori ambientali, e.g., pressione atmosferica e concentrazione di ossigeno, variano di epoca in epoca.
I loro valori sono dati da diverse distribuzioni.
Si definiscano $2+$ fattori ambientali, ognuno con distribuzione diversa, e.g., una Gaussiana, una esponenziale, e una Beta.

### Emulazione
L'ambiente fornisce l'emulazione di un numero dato di epoche.
Nell'emulazione di un'epoca avvengono, in ordine:
1. Riproduzione. **Stando ai vincoli sulla riproduzione** definiti nel modulo 1, gli organismi si riproducono, generando figli. La scelta di coppie in riproduzione può essere fatta randomicamente. Vale la monogamia per epoca! In un'epoca, un organismo si riproduce al più con un altro organismo.
2. Mortalità infantile. Fattori ambientali estremi (con valori sotto una certa soglia) possono uccidere alcuni degli organismi nati in questa generazione con una certa probabilità, e.g., se la concentrazione di ossigeno cala sotto il 10% il 3% degli organismi perisce di conseguenza. La scelta di quali fattori, con quali valori e probabilità determinano la morte rimane a scelta libera. Dei fattori definiti sopra, se ne scelga uno con una probabilità di causare morte non nulla.
3. Effetto vecchiaia. Organismi oltre un'età arbitraria muoiono di vecchiaia.

| Fattore                 | Distribuzione                                     | Valore estremo | Probabilità morte |
| ----------------------- | ------------------------------------------------- | -------------- | ----------------- |
| Concentrazione ossigeno | Gaussiana con media a 22, deviazione standard a 2 | 10             | 0.05              |

*Esempio di fattore ambientale estremo: se la concentrazione di ossigeno in una data epoca scende sotto il 10%, allora un organismo muore con probabilità del 5%.*

## Modulo 3: mating strategy
Una mating strategy (strategia di accoppiamento) definisce le preferenze di un organismo in fase di accoppiamento: dato un organismo e una lista di candidati, con quale organismo si accoppierebbe se potesse scegliere? Formalmente, una mating strategy definisce un ranking di preferenze.

Si definiscano 4 mating strategy per gli organismi del modulo $1$ e $2$, che definiscono, per ogni organismo, un ranking di preferenze di accoppiamento con altri organismi. L'organismo dovrà quindi, data una lista di possibili mate, dare un proprio ranking.
Le strategy sono:
- Randomica: un organismo ha un ranking randomico di tutti gli altri organismi
- Per età: maggiore la similarità d'età, minore la posizione nel ranking
- Per tratti desiderati: alla nascita, a ogni organismo sono dati un insieme di valori di tratti desiderati casuali. L'organismo crea un ranking in cui organismi con i tratti desiderati hanno rank minore.
- Bonus: a libera scelta, con strategia definita dal gruppo
