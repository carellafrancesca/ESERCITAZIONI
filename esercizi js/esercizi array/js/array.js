const pokemons = [
    {
      nome: "Pikachu",
      tipo: "Elettrico",
      livello: 25,
      mossa: "Scarica",
      simili: [
        { nome: "Raichu", tipo: "Elettrico", livello: 45 },
        { nome: "Pichu", tipo: "Elettrico", livello: 5 },
      ],
      dettagli: { altezza: "0.4m", peso: "6kg" },
    },
    {
      nome: "Bulbasaur",
      tipo: "Erba/Veleno",
      livello: 20,
      mossa: "Erbopolvere",
      simili: [
        { nome: "Ivysaur", tipo: "Erba/Veleno", livello: 40 },
        { nome: "Venusaur", tipo: "Erba/Veleno", livello: 60 },
      ],
      dettagli: { altezza: "0.7m", peso: "6.9kg" },
    },
    {
      nome: "Charmander",
      tipo: "Fuoco",
      livello: 18,
      mossa: "Braciere",
      simili: [
        { nome: "Charmeleon", tipo: "Fuoco", livello: 36 },
        { nome: "Charizard", tipo: "Fuoco/Volo", livello: 56 },
      ],
      dettagli: { altezza: "0.6m", peso: "8.5kg" },
    },
    {
      nome: "Raikou",
      tipo: "Elettrico",
      livello: 40,
      abilità: "Assorbivolt",
      simili: [
        { nome: "Zapdos", tipo: "Elettrico/Volante", livello: 50 },
        { nome: "Jolteon", tipo: "Elettrico", livello: 35 },
      ],
      dettagli: {
        altezza: "1.9m",
        peso: "178kg",
        descrizione:
          "Raikou è uno dei leggendari cani elettrici. Si dice che porti con sé tempeste e fulmini.",
      },
    },
];

// Crea un nuovo array contenente solo i nomi dei Pokémon
const nomiPokemon = pokemons.map(function (pokemons){
    return pokemons.nome;
});
console.log("Nomi dei Pokemons:");
console.log(nomiPokemon);

// Crea un nuovo array contenente solo i Pokémon con il tipo "Elettrico."
const tipoElettrico = pokemons.filter(function (pokemons){
    return pokemons.tipo === 'Elettrico';
})
console.log("Tutti i Pokemons di tipo Elettrico:");
console.log(tipoElettrico);

// Modifica l'abilità di "Pikachu" in "Fulmine."
const pikachu = pokemons.find(function (pokemons){ 
    return pokemons.nome === 'Pikachu';
});

if(pikachu){
    pikachu.mossa = "Fulmine";
    console.log("Mossa di Pikachu modificata in:", pikachu.mossa);
} else {
    console.log("Pokemon non trovato");
}

// Calcola il peso totale di tutti i Pokemon dell'array
const pesoTotale = pokemons.reduce (function (acc, pokemons){ //Il metodo reduce accetta una funzione di callback e un valore iniziale per l'accumulatore (acc).
    // Estrai il peso del Pokémon e convertilo in un numero
    const pesoNumerico = parseFloat(pokemons.dettagli.peso); // parseFloat per convertire in numero
    return acc + pesoNumerico;
}, 0); // L'accumulatore inizia da 0

console.log("La somma del peso di tutti i Pokémon è:", pesoTotale);

// Trova il Pokémon con il tipo "Erba/Veleno."
const tipoErbaVeleno = pokemons.find(function (pokemons){
    return pokemons.tipo === 'Erba/Veleno';
})
console.log("Pokemon di tipo Erba/Veleno:");
console.log(tipoErbaVeleno);

// Verifica se tutti i Pokémon nell'array hanno un livello inferiore a 30
const livelloSotto30 = pokemons.every(function (pokemons){
    return pokemons.livello < 30;
});

console.log("Tutti i Pokemon hanno Livello < 30?", livelloSotto30);

// Calcola la somma dei livelli di tutti i Pokemon
const livelliTotali = pokemons.reduce(function (acc, pokemons){
    return acc + pokemons.livello; // A differenza di prima dove il peso era sotto forma di Stringa, quindi andava convertito con il ParseFloat, qui i livelli sono già definiti come number quindi non servirà convertirli
}, 0);

console.log("Somma di tutti i livelli dei Pokemons:", livelliTotali);

// Crea un nuovo array contenente i nomi dei Pokémon che hanno un livello superiore a 20
const livello20 = pokemons 
    .filter(function (pokemons){
    return pokemons.livello > 20;
    })
    .map(function (pokemons){
    return pokemons.nome;
    });
    // Il metodo filter per ottenere un nuovo array contenente solo i Pokémon con livello maggiore di 20 e quindi utilizzare il metodo map per estrarre i nomi da questo array
console.log("I Pokemon con livello superiore a 20:", livello20);

// Modifica il livello di "Charmander" a 25.
const charmander = pokemons.find(function (pokemons){ 
    return pokemons.nome === 'Charmander';
});

if(charmander){
    charmander.livello = 25;
    console.log("Livello di Charmander modificato:", charmander.livello);
} else {
    console.log("Pokemon non trovato");
}