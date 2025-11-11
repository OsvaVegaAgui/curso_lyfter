// 2. Cree dos archivos de texto con el siguiente contenido.
    
//     Lea ambos archivos y compare cuales palabras se repiten en ambos. Muestre el mensaje escondido al final del programa.

const fs = require('fs');
let repeatedWords = [];

function showMessage(arrayMessage){
    let message="";
    arrayMessage.forEach(word => message += word+" ");
    console.log(message)
}

fs.readFile('demo.txt', 'utf8', (err, data) => {
  if (err) throw err;

    fs.readFile('demo1.txt', 'utf8', (err1, data1) => {
        if (err1) throw err1;

        const lines = data.split('\n').map(l => l.trimEnd());
        const lines1 = data1.split('\n').map(l1 => l1.trimEnd());

        for (const line of lines) {
            for (const line1 of lines1) {
                if (line === line1) {
                    repeatedWords.push(line1);
                }
            }
        }

        showMessage(repeatedWords)
    });
});