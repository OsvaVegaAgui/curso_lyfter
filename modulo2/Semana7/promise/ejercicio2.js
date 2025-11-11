// Realice el mismo ejercicio anterior utilizando la función Promse.any() para mostrar 
// el nombre del primer pokemón que esté contenido en la primera promesa que se resuelva.

function getPokemonName(idPokemon) {
	return new Promise((resolve, reject) => {
		fetch(`https://pokeapi.co/api/v2/pokemon/${idPokemon}`)
		.then(res => {
			if (!res.ok) {
			reject('Error pokemon with id ' + idPokemon);
			}
			return res.json();
		})
		.then(data => {
			const pokemon = data.forms;
			const nombre = pokemon[0].name;
			resolve(nombre);
		})
		.catch(error => {
			reject(error);
		});
	});
}

Promise.any([
	getPokemonName(25888),
	getPokemonName(4),
	getPokemonName(79999)
])
.then((pokemon) => {
  console.log("The first pokemon to respond was:", pokemon);
})
.catch((error) => {
  console.error("All applications failed:", error);
});
