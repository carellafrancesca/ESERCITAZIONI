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