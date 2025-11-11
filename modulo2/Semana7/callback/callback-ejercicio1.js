// 1. Cree una función que reciba tres parámetros: un número y dos funciones de callback.
//     1. Si el número es par, se debe ejecutar el primer callback.
//         1. Este debe mostrar “The number is even!”.
//     2. Si el número es impar, se debe ejecutar el segundo.
//         1. Este debe mostrar “The number is odd!”.


function getNumber(number, callbackEven, callbackOdd){
    if(number%2 === 0){
        callbackEven(number)
    }else{
        callbackOdd(number)
    }
}

getNumber(
    35, 
    (num) => {
    console.log("The number is even!");
    }, (num) => {
    console.log("The number is odd!");
    }
);