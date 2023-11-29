let display = document.getElementById("display");
// Inizializza una variabile "currentInput" vuota per tracciare l'input corrente dell'utente
let currentInput = "";

function appendToDisplay(value){
    // Aggiunge il valore del pulsante premuto all'input corrente
    currentInput += value;
    // Aggiorna il valore visualizzato nell'elemento "display" con l'input corrente
    display.value = currentInput;
}

function clearDisplay(){
    // Resetta l'input corrente a una stringa vuota
    currentInput = "";
    // Cancella il contenuto visualizzato nell'elemento "display"
    display.value = "";
}

function calculateResult(){
    try{
        // Utilizza la funzione "eval" per valutare l'espressione matematica contenuta in "currentInput"
        currentInput = eval(currentInput);
        // Aggiorna il valore visualizzato nell'elemento "display" con il risultato
        display.value = currentInput;
    } catch(error){
        display.value = "Errore";
    }
}

// ESERCIZIO EXTRA - NUMERI PARI / DISPARI

const numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const numeriPari = numeri.filter(function (numero){
    return numero % 2 === 0;
});

const numeriDispari = numeri.filter(function (numero){
    return numero % 2 !== 0;
})

console.log("Numeri pari:", numeriPari);
console.log("Numeri dispari:", numeriDispari);