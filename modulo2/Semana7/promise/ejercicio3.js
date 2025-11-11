// Cree cuatro promesas, donde cada una resuelve a una de las palabras de la lista ["very", "dogs", "cute", "are"] respectivamente, 
// en el mismo orden. Utilice la combinación de la función setTimeout y Promse.all() para obtener la salida "Dogs are very cute" , 
// sin modificar el orden de la lista manualmente o mediante un sort.


const wordsArray = ["very", "dogs", "cute", "are"];

function getPromise(word, time) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(word);
        }, time);
    });
}

const proUno = getPromise(wordsArray[0], 4000);
const proDos = getPromise(wordsArray[1], 1000);
const proTres= getPromise(wordsArray[2], 3000);
const proCuatro = getPromise(wordsArray[3], 2000);

Promise.all([proUno, proDos, proTres, proCuatro])
.then((words) => {
    const output =words[1]+" "+words[3] +" "+words[0]+" "+ words[2];
    console.log(output);
});
