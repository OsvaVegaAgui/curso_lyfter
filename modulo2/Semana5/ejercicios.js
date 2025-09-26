// #### PRIMER EJERCICIO #####
// Realiza un programa que recorra una lista e imprima todos sus elementos


const arraySports = ["Pickleball", "Padel", "Tennis", "Volleyball", "Jiu-jitsu"];

for (const sport of arraySports){
    console.log(sport)
}


// #### SEGUNDO EJERCICIO #####
// 2. Realiza un programa que recorra una lista de números y almacene todos los pares en otra lista
    // 1. Para este ejercicio intenta hacer una solución con un `for` y otra utilizando la función `filter`

const arrayNumbers = [12, 80, 58, 23, 34, 47, 20, 61, 75, 15];

const arrayEvenNumbers = [];
arrayNumbers.forEach((number)=>{
    if(number%2 === 0){
        arrayEvenNumbers.push(number);
    }
});

const arrayEvenNumbersFilters = arrayNumbers.filter(number => number%2 === 0);
console.log(arrayEvenNumbersFilters)


// #### TERCER EJERCICIO #####
// Toma una lista de temperaturas en grados celsius y conviertala a farenheit utilizando la función map



const arrayCelcius = [25, 18, 30, 10, 5, 22, 14, 28];

const arrayFarenheit = arrayCelcius.map(temperature=> (temperature*1.8)+32)

console.log(arrayFarenheit)


// #### CUARTO EJERCICIO #####
// Toma un string y conviertelo en una lista de palabras, separandolas por espacios en blanco. No puedes usar la función split.


const example = "This is a string!";
const arrayWords =[];
let word = "";

for (const lettter of example) {
    if(lettter === " "){
        arrayWords.push(word);
        word = "";
    }else{
        word += lettter;
    }
}
arrayWords.push(word);


// #### QUINTO EJERCICIO #####
// Realiza un programa que reciba el siguiente objeto, e imprima otro objeto con los siguientes datos:Realiza un programa que reciba el siguiente objeto, e imprima otro objeto con los siguientes datos:


function printStudentData(student) {

    let sumNotes = 0;

    let highestGrade = { name: "", grade: -1 };
    let lowestGrade = { name: "", grade: 101 };


    for (const score of student.grades) {

        sumNotes += score.grade;

        if (score.grade > highestGrade.grade) {
            highestGrade = score;
        }

        if (score.grade < lowestGrade.grade) {
            lowestGrade = score;
        }
    }

    const gradeAvg = sumNotes / student.grades.length;

    const result = {
        name: student.name,
        gradeAvg:gradeAvg,
        highestGrade: highestGrade.name,
        lowestGrade: lowestGrade.name
    };

    console.log(result);
}


const student = {
    name: "John Doe",
    grades: [
        { name: "math", grade: 80 },
        { name: "science", grade: 100 },
        { name: "history", grade: 60 },
        { name: "PE", grade: 90 },
        { name: "music", grade: 98 }
    ]
};


printStudentData(student);