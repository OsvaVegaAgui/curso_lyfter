// Repita los ejercicios 1 y 2 de la sección de Async/Await resolviéndolos 
// con las funciones .then(), .catch() y .finally() de ser requerido.


// EJERCCIO #1
function getUser(userId) {
    return fetch(`https://reqres.in/api/users/${userId}`, {
        headers: { 'x-api-key': 'reqres-free-v1' }
    })
    .then(response => response.json())
    .then(data => {
        console.log("Usuario:", data.data);
    });
}

getUser(2);


// EJERCCIO #2
function getUser2(userId) {
    return fetch(`https://reqres.in/api/users/${userId}`, {
        headers: { 'x-api-key': 'reqres-free-v1' }
    })
    .then(response => {
        if (response.status === 404) {
            console.error(`Usuario ${userId} no encontrado.`);
            return;
        }

        return response.json();
    })
    .then(data => {
        if (data) {
            console.log("Usuario:", data.data);
        }
    })
    .catch(error => {
        console.log(`Hubo un problema: ${error}`);
    })
    .finally(() => {
        console.log("Petición finalizada");
    });
}

getUser2(23);
