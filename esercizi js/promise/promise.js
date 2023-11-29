let myPromise = new Promise((resolve, reject) =>{
    setTimeout(() => {
        resolve("Operazione completata con successo!");
    }, 2000);
});

myPromise.then((result) => {
    console.log(result);
}).catch((error) => {
    console.log(error);
});

function eseguiOperazione1(){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Operazione 1 completata");
        }, 5000);
    });
}

function eseguiOperazione2(){
    return new Promise((resolve, reject) =>{
        setTimeout(() => {
            resolve("Operazione 2 completata")
        }, 6500);
    });
}

eseguiOperazione1()
  .then((result1) => {
    console.log(result1);
    return eseguiOperazione2();
  })
  .then((result2) => {
    console.log(result2);
  })
  .catch((error) => {
    console.error(error);
  });

// Array di Promises
let promisesArray = [
    new Promise((resolve) => setTimeout(() => resolve("Prima operazione"), 1000)),
    new Promise((resolve) => setTimeout(() => resolve("Seconda operazione"), 500)),
    new Promise((resolve) => setTimeout(() => resolve("Terza operazione"), 1500)),
  ];
  
// Promise.all per eseguire tutte le Promises contemporaneamente
Promise.all(promisesArray)
    .then((results) => {
      console.log(results); // Array di risultati
    })
    .catch((error) => {
      console.error(error); // Stampiamo l'errore in caso di fallimento di una qualsiasi Promise
    });  