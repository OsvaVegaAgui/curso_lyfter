// Utilice el API https://pokeapi.co/api/v2/pokemon/:ID para solicitar 3 distintos pokemónes. 
// Utilice la función Promise.all() para mostrar en pantalla el nombre de los tres pokemónes 
// al mismo tiempo, hasta que todas las promesas se resuelvan.

function getPokemonName(idPokemon) {
  return new Promise((resolve, reject) => {
    fetch(`https://pokeapi.co/api/v2/pokemon/${idPokemon}`)
      .then(res => res.json())
      .then(data => {
            const pokemon = data.forms;
            const nombre = pokemon[0].name;
            resolve(nombre);
      })
  });
}

Promise.all([
    getPokemonName(25),
    getPokemonName(4),
    getPokemonName(7)
])
.then((nombres) => {
    console.log("The 3 pokemon are:", nombres[0], nombres[1], nombres[2]);
})
