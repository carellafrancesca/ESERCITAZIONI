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
