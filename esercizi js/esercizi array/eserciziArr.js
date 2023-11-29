// ESERCIZI SUI CICLI PER ARRAY

// 1) Utilizza un ciclo for per stampare ogni elemento di un array.

const cicloArray = ['Mario', 'Giuseppe', 'Sara', 'Francesca', 'Mattia'];

for( let i = 0; i < cicloArray.length; i++){
    console.log(cicloArray[i]);
}

for (const elemento of cicloArray){
    console.log(elemento);
}

// 2) Scrivi una funzione che restituisca un array con la somma cumulativa degli elementi.

function sommaCumulativa(arr){
    let totaleCumulativo = 0; // Questa variabile tiene traccia della somma cumulativa mentre attraversiamo gli elementi dell'array. Viene inizializzata a 0 all'inizio.

    // Utilizziamo il metodo map per generare un nuovo array con la somma cumulativa
    const arraySomma = arr.map(function (element){
        totaleCumulativo += element;
        return totaleCumulativo;
    });

    // Per ogni elemento nell'array, aggiorniamo totaleCumulativo aggiungendo l'elemento corrente. Quindi, restituiamo il valore corrente di totaleCumulativo per inserirlo nel nuovo array.

    return arraySomma;

    // Infine, restituiamo l'array risultante che contiene la somma cumulativa di ogni elemento dell'array di input.    
}

const arrayDiNumeri = [1, 2, 3, 4, 5];
const risultato = sommaCumulativa(arrayDiNumeri);

console.log(risultato);

// METODI PER LE STRINGHE

// 1) Scrivi una funzione che inverta una stringa.

function invertiStringa (string){
    // Converte la stringa in un array di caratteri, lo inverte e lo riunisce in una stringa
    return string.split('').reverse().join('');
}

const stringaOg = 'Buongiorno a tutti';
const stringaInvertita = invertiStringa(stringaOg);
console.log(stringaInvertita);

// 2) Scrivi una funzione che verifichi se una stringa è un palindromo.

function verificaPalindromo(stringa) {
    const stringaInvertita = stringa.split('').reverse().join('');
    return stringa.toLowerCase() === stringaInvertita.toLowerCase();
}
  
// Esempio di utilizzo:
const stringaPalindroma = "Anna";
const isPalindromo = verificaPalindromo(stringaPalindroma);
console.log(isPalindromo); // Output: true  

// 3) Scrivi una funzione che converte una stringa in maiuscolo.

function convertiInMaiuscolo(stringa) {
    return stringa.toUpperCase();
}
  
// Esempio di utilizzo:
const stringaMinuscola = "hello, world!";
const stringaMaiuscola = convertiInMaiuscolo(stringaMinuscola);
console.log(stringaMaiuscola); // Output: "HELLO, WORLD!"
  