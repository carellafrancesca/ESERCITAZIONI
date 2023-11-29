//FORM

document.getElementById("registrationForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Impedisce l'invio predefinito del modulo

    const username = document.getElementById("username").value;
    const surname = document.getElementById("surname").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (username.length < 2) {
        document.getElementById("usernameError").textContent = "Il nome inserito non è valido";
        return;
    } else {
        document.getElementById("usernameError").textContent = "";
    }

    if (surname.length < 2) {
        document.getElementById("surnameError").textContent = "Il cognome inserito non è valido";
        return;
    } else {
        document.getElementById("surnameError").textContent = "";
    }

    if (!email.includes("@") || email.length < 10) {
        document.getElementById("emailError").textContent = "Inserisci un indirizzo email valido";
        return;
    } else {
        document.getElementById("emailError").textContent = "";
    }

    if (password.length < 5) {
        document.getElementById("passwordError").textContent = "La password non è valida.";
        return;
    } else {
        document.getElementById("passwordError").textContent = "";
    }
    
    const userData = {
        nome: username,
        cognome: surname,
        email: email,
        password: password
    };

    console.log(userData);

    // Svuota i campi del modulo
    document.getElementById("username").value = "";
    document.getElementById("surname").value = "";
    document.getElementById("email").value = "";
    document.getElementById("password").value = "";

    // Svuota l'elemento degli errori
    errorMessagesElement.innerHTML = "";


});

// LISTA 
    
    const activities = [];

document.getElementById("activityForm").addEventListener("submit", function (e) {
        e.preventDefault();
    
        const activityInput = document.getElementById("activity");
        const newActivity = activityInput.value.trim(); // Ottiene il valore dell'input senza spazi bianchi iniziali o finali
    
        // Verifica se la nuova attività non è vuota
        if (newActivity !== "") {
            activities.push(newActivity); // Aggiunge la nuova attività all'array activities
            activityInput.value = ""; // Cancella il campo di input

            displayActivities(); // Chiama la funzione per visualizzare le attività aggiornate
        }
});

function displayActivities() {
    const activityList = document.getElementById("activityList");
    activityList.innerHTML = ""; // Cancella il contenuto precedente dell'elenco
    
    // Itera attraverso l'array activities e crea un elemento <li> per ciascuna attività
    for (let i = 0; i < activities.length; i++) {
        const li = document.createElement("li"); // Crea un elemento <li>
        li.textContent = activities[i]; // Imposta il testo dell'elemento <li> con l'attività corrente
        activityList.appendChild(li); // Aggiunge l'elemento <li> all'elenco
    }
}
