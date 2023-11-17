// ESERCIZI SUGLI ARRAY

const numeri = [12, 30, 74];

const numbers = [10, 27, 43, 66, 71, 84, 90, 107, 120];

// 1) Scrivi una funzione che restituisca la somma di tutti gli elementi in un array.

const somma = numeri.reduce(function (acc, totNumeri){
    return acc + totNumeri;
}, 0);

const add = numbers.reduce(function (acc, totaleAdd){
    return acc + totaleAdd;
}, 0);

console.log(somma);
console.log(add);

// 2) Scrivi una funzione che restituisca un nuovo array contenente solo i numeri pari dell'array di input.

const numeriPari = numbers.filter(function (pari){
    return pari % 2 === 0;
})

console.log(numeriPari);

// 3) Scrivi una funzione che restituisca l'elemento più grande in un array.

const numeroMax = Math.max.apply(null, numbers);
console.log(numeroMax);

const numeroMassimo = Math.max.apply(null, numeri);
console.log(numeroMassimo);

/*In questo esempio, Math.max.apply(null, arrayDiNumeri) applica la funzione Math.max() agli elementi dell'array, restituendo l'elemento più grande.*/

// 4) Scrivi una funzione che unisca due array in un unico array. 

const colori = ['Bianco', 'Nero', 'Rosso', 'Grigio'];
const colori2 = ['Blu', 'Verde', 'Giallo', 'Viola'];

const sommaArray = colori.concat(colori2);
console.log(sommaArray);

// 5) Scrivi una funzione che rimuova i duplicati da un array.

const arrayConDuplicati = [20, 45, 118, 34, 55, 20, 61, 103, 34, 79, 85, 55];
const arraySenzaDuplicati = [...new Set(arrayConDuplicati)];

console.log(arraySenzaDuplicati);

//In questo esempio, il costruttore Set viene utilizzato per creare un set, che automaticamente elimina i duplicati. Successivamente, spread syntax ([... ]) viene utilizzato per convertire il set in un array.

// 6) Scrivi una funzione che restituisca il prodotto di tutti gli elementi in un array.

const moltiplicazione = [13, 9, 7];
const risultatoMoltiplicazione = moltiplicazione.reduce(function (acc, result){
    return acc * result;
}, 1);

// Impostando il valore iniziale a 1, stai garantendo che, anche se l'array è vuoto, il risultato della riduzione sarà 1. Questo è spesso utile quando si tratta di operazioni di moltiplicazione, poiché moltiplicare per 1 non cambia il valore.

console.log(risultatoMoltiplicazione);

// 7) Ordina gli elementi di un array in ordine crescente e decrescente.

const numeriCrescenti = numbers.slice().sort(function(a, b){
    return a - b;
})

// In questo caso, la funzione di confronto function(a, b) { return a - b; } confronta gli elementi dell'array in modo che siano ordinati in ordine crescente. Se il risultato è negativo, a viene ordinato prima di b; se è positivo, b viene ordinato prima di a.

console.log("Array in ordine crescente:", numeriCrescenti);
// In questo esempio, stiamo utilizzando slice() per creare una copia dell'array originale in modo che il metodo sort() non modifichi l'array originale. La funzione di confronto (a, b) => a - b ordina gli elementi in ordine crescente.

const numeriDecrescenti = numbers.slice().sort(function (a, b){
    return b - a;
})

// Qui, la funzione di confronto function(a, b) { return b - a; } ordina gli elementi in modo che siano in ordine decrescente. La differenza principale rispetto all'ordinamento crescente è che sottrai b da a anziché a da b.

console.log("Array in ordine decrescente:", numeriDecrescenti);

// 8) Scrivi una funzione che esegua una ricerca lineare per trovare un elemento specifico in un array. 

function ricercaLineare(array, elemento){ 
    // La funzione ricercaLineare accetta due parametri: array: l'array in cui cercare l'elemento. elemento: l'elemento da cercare nell'array.

    const indice = array.indexOf(elemento);

    // Quindi, la condizione if (indice !== -1) si legge come "se l'indice restituito da indexOf() non è -1", il che significa che l'elemento è stato trovato nell'array. Se l'indice è diverso da -1, la condizione è vera, altrimenti è falsa.

    if (indice !== -1){
        console.log(`L'elemento ${elemento} è presente all'indice ${indice}.`);
        return indice; // Puoi restituire l'indice se vuoi
    } else {
        console.log(`L'elemento ${elemento} non è presente nell'array.`);
        return -1; // Se l'elemento non è presente, puoi restituire un valore convenzionale come -1
    }
}

const arrayN = [5, 2, 9, 1, 13, 20];
ricercaLineare(arrayN, 9); // Troverà l'elemento 9
ricercaLineare(arrayN, 7); // Non troverà l'elemento 7


// 9) Scrivi una funzione che conta quante volte un elemento appare in un array. 

function contaOccorrenze(array, element){
    let conteggio = 0; // Il conteggio parte da zero

    for (let i = 0; i < array.length; i++){
        if (array[i] === element){
            // Dentro il ciclo, viene verificato se l'elemento corrente nell'array (array[i]) è uguale all'elemento che stiamo cercando (elemento).
            conteggio++; // Se l'elemento corrente è uguale a quello cercato, incrementiamo il contatore (conteggio) di uno.
        }
    }
    return conteggio;
}

const numeriConteggio = [1, 2, 3, 4, 2, 5, 2];
const occorrenzeDiDue = contaOccorrenze(numeriConteggio, 2);

console.log(`L'elemento 2 appare ${occorrenzeDiDue} volte nell'array.`);