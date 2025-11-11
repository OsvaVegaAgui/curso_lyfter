// Realice el mismo ejercicio anterior, pero con el URL https://reqres.in/api/users/23 para generar un error. 
// Realice el manejo de error adecuado e imprima un mensaje de error indicando que el usuario no se encontró.
async function getUser(userId) {
  try {
        const response = await fetch(`https://reqres.in/api/users/${userId}`, {
            headers: { 'x-api-key': 'reqres-free-v1' }
        });

        if (response.status == 404) {
            console.error(`Usuario ${userId} no encontrado.`);
            return;
        }

        const data = await response.json();  

        console.log("Usuario:", data.data);
    } catch (error) {
        console.log(`Hubo un problema: ${error}`);
    }
}

getUser(23);
