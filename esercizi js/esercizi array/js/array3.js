let arrayNumeri = [12, 37, 51, 70, 66, 94, 115];
console.log(arrayNumeri);

// 1) Inverti l'ordine degli elementi in un array.
let reversedArray = [...arrayNumeri].reverse();
//Il metodo reverse() modifica direttamente l'array originale invertendone l'ordine. Se desideri creare una nuova array senza modificare quella originale, puoi fare una copia dell'array e quindi invertirla:
console.log(reversedArray);

// 2) Scrivi una funzione che restituisca un array con la somma cumulativa degli elementi in un array di input.
function sommaCumulativa(arrayNumeri){
    let resultArray = []; // Un array vuoto che verrà utilizzato per memorizzare la somma cumulativa.
    let sum = 0;

    for(let i = 0; i < arrayNumeri.length; i++){
        sum += arrayNumeri[i];
        //Ad ogni iterazione, l'elemento corrente dell'array di numeri (arrayNumeri[i]) viene aggiunto alla variabile sum. In questo modo, sum rappresenta la somma cumulativa degli elementi fino all'indice corrente.
        resultArray.push(sum);
        //La somma cumulativa corrente (sum) viene aggiunta all'array resultArray utilizzando il metodo push(). Quindi, resultArray conterrà la somma cumulativa fino all'indice corrente.
    }

    return resultArray;
}

let risultato = sommaCumulativa(arrayNumeri);
console.log(risultato);

// 3) Scrivi una funzione che filtri gli elementi di un array in base a una determinata condizione (ad esempio, tutti gli elementi pari).

function filterNumbers(array, condizione){
    const arrayFiltrato = array.filter(condizione);
    return arrayFiltrato;
}

const condizionePari = numero => numero % 2 === 0;
const condizioneDispari = numero => numero % 2 !== 0;

const numeriPari = filterNumbers(arrayNumeri, condizionePari);
const numeriDispari = filterNumbers(arrayNumeri, condizioneDispari);

console.log("Numeri Pari:", numeriPari);
console.log("Numeri Dispari:", numeriDispari);

// 4) Concatena due array in un unico array.
function concatenaArray(array1, array2){
    const arrayConcatenato = array1.concat(array2);
    return arrayConcatenato;
}

const array1 = ["uno", "due", "tre"];
const array2 = ["quattro", "cinque", "sei"];

const arrayConcatenato = concatenaArray(array1, array2);
console.log(arrayConcatenato);

// 5) Scrivi una funzione che divida un array in parti più piccole di una dimensione specifica.

function dividiArrayInParti(arrayA, arrayB) {
    const arrayDiviso = [];

    // Verifica se la dimensione specificata è valida e se l'array non è vuoto.
    if (arrayB <= 0 || !Array.isArray(arrayA) || arrayA.length === 0) {
    
    //Utilizza la funzione Array.isArray() per verificare se la variabile arrayA è effettivamente un array. L'operatore ! inverte il risultato, quindi se arrayA non è un array, la condizione restituirà true.    

    // Restituisci l'array vuoto se la dimensione non è valida o se l'array è vuoto.
        return arrayDiviso;
    }

    // Calcola il numero totale di parti necessarie.
    const numeroDiParti = Math.ceil(arrayA.length / arrayB);

    //Math.ceil(...): questa funzione arrotonda il risultato al numero intero più grande non inferiore. Ciò assicura che anche se il risultato della divisione è un numero decimale, il numero di parti sarà arrotondato per eccesso. 

    for (let i = 0; i < arrayB; i++) {
    // Calcola l'indice di inizio per la parte corrente.
    const indiceInizio = i * arrayB;

    // Usa il metodo slice() per estrarre una parte dell'array.
    const parte = arrayA.slice(indiceInizio, indiceInizio + arrayB);

    // Aggiungi la parte estratta all'array risultante.
    arrayDiviso.push(parte);
  }

  // Restituisci l'array contenente le parti divise.
  return arrayDiviso;

}

// Esempio di utilizzo: Suddivide un array di numeri in parti di dimensione 3.
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const arrayDiviso = dividiArrayInParti(numbers, 3);

console.log("Array diviso in parti di dimensione 3:", arrayDiviso);

// 6) Scrivi una funzione che sostituisca tutte le occorrenze di un elemento specifico con un nuovo valore in un array.

function sostituisciElemento(elemento, elementoDaSostituire, nuovoValore){
    for(let i = 0; i < elemento.length; i++){
        if(elemento[i] === elementoDaSostituire){
            elemento[i] = nuovoValore;
        }
    }
    return elemento;
}

const numberElements = [19, 63, 21, 105, 75, 123, 99, 8, 43, 34];
sostituisciElemento(numberElements, 21, 27);
console.log("Array con sostituzioni:", numberElements);

// 7) Calcola la media degli elementi in un array.

function calcolaMedia(arrayMedia){
    if(arrayMedia.length === 0){
        return 0;
    }

    // Utilizza il metodo reduce per sommare tutti gli elementi dell'array.
    const somma = arrayMedia.reduce(function(accumulatore, elementoCorrente){
       return accumulatore + elementoCorrente; 
    }, 0);

    // Calcola la media dividendo la somma per il numero totale di elementi.
    const media = somma / arrayMedia.length;

    return media;
}

const numeriMedia = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];
const mediaTot = calcolaMedia(numeriMedia);

console.log("Media degli elementi:", mediaTot);

// 8) Scrivi una funzione che elimini i duplicati da un array.

function rimuoviDuplicati(array){
    const setUnici = new Set(array);
    // Converte il Set in un array.
    const arraySenzaDuplicati = Array.from(setUnici);

    return arraySenzaDuplicati;
}

const numeriConDuplicati = [12, 64, 85, 109, 77, 3, 52, 52, 47, 99, 99, 117, 1, 33, 61, 61];
const numeriSenzaDuplicati = rimuoviDuplicati(numeriConDuplicati);

console.log("Array con duplicati:", numeriConDuplicati);
console.log("Array senza duplicati:", numeriSenzaDuplicati);

