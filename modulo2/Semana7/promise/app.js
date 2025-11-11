function getPokemonName(idPokemon) {
  return new Promise(resolve => {
    fetch(`https://pokeapi.co/api/v2/pokemon/${idPokemon}`)
      .then(res => res.json())
      .then(data => {
        const pokemon = data.forms;
        resolve(pokemon[0].name)
      })
  })
}

getPokemonName(7)
.then(pokemonName => {
    console.log("El nombre del Pokémon es:", pokemonName);
});