function cambiaTestoParagrafo(){
    const paragrafoElement = document.getElementById("paragrafo");
    paragrafoElement.textContent = "Il testo è stato cambiato" // Aggiungo il nuovo testo
}

function aggiungiElementoLista(){
    const lista = document.getElementById("lista");
    const nuovoElemento = document.getElementById("nuovoElemento").value; // Ottengo il valore dell'input tramite l'id
    const elementoLista = document.createElement("li"); // Per creare un elemento della lista
    elementoLista.textContent = nuovoElemento; // Va ad aggiungere il testo all'elemento creato
    lista.appendChild(elementoLista); // Aggiunge l'elemento nuovo alla lista
}

function nascondiElemento(){
    const testoNascosto = document.getElementById("hiddenText");
    testoNascosto.style.display = "none";
}

function cambiaColoreTesto(){
    const testoColorato = document.getElementById("testoColorato");
    testoColorato.style.color = "red";
}

function aggiungiAlTitolo(){
    const titolo = document.getElementById("titolo");
    const nuovoTitolo = document.getElementById("nuovoTitolo").value;
    titolo.textContent = nuovoTitolo; // Il titolo precedente viene sostituito con il testo presente nel campo input
}

function removeListElement(){
    const lista = document.getElementById("listElements");
    const elementiSelezionati = lista.querySelectorAll('li');
    // Itera su ciascun elemento <li> all'interno della lista
    elementiSelezionati.forEach(function (elemento){
        lista.removeChild(elemento); // Rimuovi l'elemento dalla lista
    })
}

function calcolaSomma() {
    // Ottieni il valore dell'input con id "numero1" e "numero2" e lo converte in un numero in virgola mobile utilizzando parseFloat
    const numero1 = parseFloat(document.getElementById("numero1").value);
    const numero2 = parseFloat(document.getElementById("numero2").value);
    const somma = numero1 + numero2;
    alert("La somma è: " + somma);
}