import pokedex
class Pokemon:
    def __init__(self, name, number, type1, type2, catch_rate):
        self.name = name
        self.number = number
        self.type1 = type1
        self.type2 = type2
        self.catch_rate = catch_rate

pokemon_array = []

pokemon_array.append(Pokemon("Bulbasaur", 1, "Grass", "Poison", 45))
pokemon_array.append(Pokemon("Ivysaur", 2, "Grass", "Poison", 45))
pokemon_array.append(Pokemon("Venusaur", 3, "Grass", "Poison", 45))
pokemon_array.append(Pokemon("Charmander", 4, "Fire", "", 45))
pokemon_array.append(Pokemon("Charmeleon", 5, "Fire", "", 45))
pokemon_array.append(Pokemon("Charizard", 6, "Fire", "Flying", 45))
pokemon_array.append(Pokemon("Squirtle", 7, "Water", "", 45))
pokemon_array.append(Pokemon("Wartortle", 8, "Water", "", 45))
pokemon_array.append(Pokemon("Blastoise", 9, "Water", "", 45))
pokemon_array.append(Pokemon("Caterpie", 10, "Bug", "", 255))
pokemon_array.append(Pokemon("Metapod", 11, "Bug", "", 120))
pokemon_array.append(Pokemon("Butterfree", 12, "Bug", "Poison", 45))
pokemon_array.append(Pokemon("Weedle", 13, "Bug", "Poison", 255))
pokemon_array.append(Pokemon("Kakuna", 14, "Bug", "Poison", 120))
pokemon_array.append(Pokemon("Beedrill", 15, "Bug", "Poison", 45))
pokemon_array.append(Pokemon("Pidgey", 16, "Normal", "Flying", 255))
pokemon_array.append(Pokemon("Pidgeotto", 17, "Normal", "Flying", 120))
pokemon_array.append(Pokemon("Pidgeot", 18, "Normal", "Flying", 45))
pokemon_array.append(Pokemon("Rattata", 19, "Normal", "", 255))
pokemon_array.append(Pokemon("Raticate", 20, "Normal", "", 127))
pokemon_array.append(Pokemon("Spearow", 21, "Normal", "Flying", 255))
pokemon_array.append(Pokemon("Fearow", 22, "Normal", "Flying", 90))
pokemon_array.append(Pokemon("Ekans", 23, "Poison", "", 255))
pokemon_array.append(Pokemon("Arbok", 24, "Poison", "", 90))
pokemon_array.append(Pokemon("Pikachu", 25, "Electric", "", 190))
pokemon_array.append(Pokemon("Raichu", 26, "Electric", "", 75))
pokemon_array.append(Pokemon("Sandshrew", 27, "Ground", "", 255))
pokemon_array.append(Pokemon("Sandslash", 28, "Ground", "", 90))
pokemon_array.append(Pokemon("Nidoran(f)", 29, "Poison", "", 235))
pokemon_array.append(Pokemon("Nidorina", 30, "Poison", "", 120))
pokemon_array.append(Pokemon("Nidoqueen", 31, "Poison", "Ground", 45))
pokemon_array.append(Pokemon("Nidoran(m)", 32, "Poison", "", 235))
pokemon_array.append(Pokemon("Nidorino", 33, "Poison", "", 120))
pokemon_array.append(Pokemon("Nidoking", 34, "Poison", "Ground", 45))
pokemon_array.append(Pokemon("Clefairy", 35, "Normal", "", 150))
pokemon_array.append(Pokemon("Clefable", 36, "Normal", "", 25))
pokemon_array.append(Pokemon("Vulpix", 37, "Fire", "", 190))
pokemon_array.append(Pokemon("Ninetails", 38, "Fire", "", 75))
pokemon_array.append(Pokemon("Jigglypuff", 39, "Normal", "", 170))
pokemon_array.append(Pokemon("Wigglytuff", 40, "Normal", "", 50))
pokemon_array.append(Pokemon("Zubat", 41, "Poison", "Flying", 255))
pokemon_array.append(Pokemon("Golbat", 42, "Poison", "Flying", 90))
pokemon_array.append(Pokemon("Oddish", 43, "Grass", "Poison", 255))
pokemon_array.append(Pokemon("Gloom", 44, "Grass", "Poison", 120))
pokemon_array.append(Pokemon("Vileplume", 45, "Grass", "Poison", 45))
pokemon_array.append(Pokemon("Paras", 46, "Bug", "Grass", 190))
pokemon_array.append(Pokemon("Parasect", 47, "Bug", "Grass", 75))
pokemon_array.append(Pokemon("Venonat", 48, "Bug", "Poison", 190))
pokemon_array.append(Pokemon("Venomoth", 49, "Bug", "Poison", 75))
pokemon_array.append(Pokemon("Diglett", 50, "Ground", "", 255))
pokemon_array.append(Pokemon("Dugtrio", 51, "Ground", "", 50))
pokemon_array.append(Pokemon("Meowth", 52, "Normal", "", 255))
pokemon_array.append(Pokemon("Persian", 53, "Normal", "", 90))
pokemon_array.append(Pokemon("Psyduck", 54, "Water", "", 190))
pokemon_array.append(Pokemon("Golduck", 55, "Water", "", 75))
pokemon_array.append(Pokemon("Mankey", 56, "Fighting", "", 190))
pokemon_array.append(Pokemon("Primeape", 57, "Fighting", "", 75))
pokemon_array.append(Pokemon("Growlithe", 58, "Fire", "", 190))
pokemon_array.append(Pokemon("Arcanine", 59, "Fire", "", 75))
pokemon_array.append(Pokemon("Poliwag", 60, "Water", "", 255))
pokemon_array.append(Pokemon("Poliwhirl", 61, "Water", "", 120))
pokemon_array.append(Pokemon("Poliwrath", 62, "Water", "Fighting", 45))
pokemon_array.append(Pokemon("Abra", 63, "Psychic", "", 200))
pokemon_array.append(Pokemon("Kadabra", 64, "Psychic", "", 100))
pokemon_array.append(Pokemon("Alakazam", 65, "Psychic", "", 50))
pokemon_array.append(Pokemon("Machop", 66, "Fighting", "", 180))
pokemon_array.append(Pokemon("Machoke", 67, "Fighting", "", 90))
pokemon_array.append(Pokemon("Machamp", 68, "Fighting", "", 45))
pokemon_array.append(Pokemon("Bellsprout", 69, "Grass", "Poison", 255))
pokemon_array.append(Pokemon("Weepinbell", 70, "Grass", "Poison", 120))
pokemon_array.append(Pokemon("Victreebel", 71, "Grass", "Poison", 45))
pokemon_array.append(Pokemon("Tentacool", 72, "Water", "Poison", 190))
pokemon_array.append(Pokemon("Tentacruel", 73, "Water", "Poison", 60))
pokemon_array.append(Pokemon("Geodude", 74, "Rock", "Ground", 255))
pokemon_array.append(Pokemon("Graveler", 75, "Rock", "Ground", 120))
pokemon_array.append(Pokemon("Golem", 76, "Rock", "Ground", 45))
pokemon_array.append(Pokemon("Ponyta", 77, "Fire", "", 190))
pokemon_array.append(Pokemon("Rapidash", 78, "Fire", "", 60))
pokemon_array.append(Pokemon("Slowpoke", 79, "Water", "Psychic", 190))
pokemon_array.append(Pokemon("Slowbro", 80, "Water", "Psychic", 75))
pokemon_array.append(Pokemon("Magnemite", 81, "Electric", "", 190))
pokemon_array.append(Pokemon("Magneton", 82, "Electric", "", 60))
pokemon_array.append(Pokemon("Farfetch'd", 83, "Normal", "Flying", 45))
pokemon_array.append(Pokemon("Doduo", 84, "Normal", "Flying", 190))
pokemon_array.append(Pokemon("Dodrio", 85, "Normal", "Flying", 45))
pokemon_array.append(Pokemon("Seel", 86, "Water", "", 190))
pokemon_array.append(Pokemon("Dewgong", 87, "Water", "Ice", 75))
pokemon_array.append(Pokemon("Grimer", 88, "Poison", "", 190))
pokemon_array.append(Pokemon("Muk", 89, "Poison", "", 75))
pokemon_array.append(Pokemon("Shellder", 90, "Water", "", 190))
pokemon_array.append(Pokemon("Cloyster", 91, "Water", "Ice", 60))
pokemon_array.append(Pokemon("Gastly", 92, "Ghost", "Poison", 190))
pokemon_array.append(Pokemon("Haunter", 93, "Ghost", "Poison", 90))
pokemon_array.append(Pokemon("Gengar", 94, "Ghost", "Poison", 45))
pokemon_array.append(Pokemon("Onix", 95, "Rock", "Ground", 45))
pokemon_array.append(Pokemon("Drowzee", 96, "Psychic", "", 190))
pokemon_array.append(Pokemon("Hypno", 97, "Psychic", "", 75))
pokemon_array.append(Pokemon("Krabby", 98, "Water", "", 225))
pokemon_array.append(Pokemon("Kingler", 99, "Water", "", 60))
pokemon_array.append(Pokemon("Voltorb", 100, "Electric", "", 190))
pokemon_array.append(Pokemon("Electrode", 101, "Electric", "", 60))
pokemon_array.append(Pokemon("Exeggcute", 102, "Grass", "Psychic", 90))
pokemon_array.append(Pokemon("Exeggutor", 103, "Grass", "Psychic", 45))
pokemon_array.append(Pokemon("Cubone", 104, "Ground", "", 190))
pokemon_array.append(Pokemon("Marowak", 105, "Ground", "", 75))
pokemon_array.append(Pokemon("Hitmonlee", 106, "Fighting", "", 45))
pokemon_array.append(Pokemon("Hitmonchan", 107, "Fighting", "", 45))
pokemon_array.append(Pokemon("Lickitung", 108, "Normal", "", 45))
pokemon_array.append(Pokemon("Koffing", 109, "Poison", "", 190))
pokemon_array.append(Pokemon("Weezing", 110, "Poison", "", 60))
pokemon_array.append(Pokemon("Rhyhorn", 111, "Ground", "Rock", 120))
pokemon_array.append(Pokemon("Rhydon", 112, "Ground", "Rock", 60))
pokemon_array.append(Pokemon("Chansey", 113, "Normal", "", 30))
pokemon_array.append(Pokemon("Tangela", 114, "Grass", "", 45))
pokemon_array.append(Pokemon("Kangaskhan", 115, "Normal", "", 45))
pokemon_array.append(Pokemon("Horsesa", 116, "Water", "", 225))
pokemon_array.append(Pokemon("Seadra", 117, "Water", "", 75))
pokemon_array.append(Pokemon("Goldeen", 118, "Water", "", 225))
pokemon_array.append(Pokemon("Seaking", 119, "Water", "", 60))
pokemon_array.append(Pokemon("Staryuu", 120, "Water", "", 225))
pokemon_array.append(Pokemon("Starmie", 121, "Water", "Psychic", 60))
pokemon_array.append(Pokemon("Mr. Mime", 122, "Psychic", "Psychic", 45))
pokemon_array.append(Pokemon("Scyther", 123, "Bug", "Flying", 45))
pokemon_array.append(Pokemon("Jynx", 124, "Ice", "Psychic", 45))
pokemon_array.append(Pokemon("Electabuzz", 125, "Electric", "", 45))
pokemon_array.append(Pokemon("Magmar", 126, "Fire", "", 45))
pokemon_array.append(Pokemon("Pinsir", 127, "Bug", "", 45))
pokemon_array.append(Pokemon("Tauros", 128, "Normal", "", 45))
pokemon_array.append(Pokemon("Magikarp", 129, "Water", "", 255))
pokemon_array.append(Pokemon("Gyarados", 130, "Water", "Flying", 45))
pokemon_array.append(Pokemon("Lapras", 131, "Water", "Ice", 45))
pokemon_array.append(Pokemon("Ditto", 132, "Normal", "", 35))
pokemon_array.append(Pokemon("Eevee", 133, "Normal", "", 45))
pokemon_array.append(Pokemon("Vaporeon", 134, "Water", "", 45))
pokemon_array.append(Pokemon("Jolteon", 135, "Electric", "", 45))
pokemon_array.append(Pokemon("Flareon", 136, "Fire", "", 45))
pokemon_array.append(Pokemon("Porygon", 137, "Normal", "", 45))
pokemon_array.append(Pokemon("Omanyte", 138, "Rock", "Water", 45))
pokemon_array.append(Pokemon("Omastar", 139, "Rock", "Water", 45))
pokemon_array.append(Pokemon("Kabuto", 140, "Rock", "Water", 45))
pokemon_array.append(Pokemon("Kabutops", 141, "Rock", "Water", 45))
pokemon_array.append(Pokemon("Aerodactyl", 142, "Rock", "Flying", 45))
pokemon_array.append(Pokemon("Snorlax", 143, "Normal", "", 25))
pokemon_array.append(Pokemon("Articuno", 144, "Ice", "Flying", 3))
pokemon_array.append(Pokemon("Zapdos", 145, "Electric", "Flying", 3))
pokemon_array.append(Pokemon("Moltres", 146, "Fire", "Flying", 3))
pokemon_array.append(Pokemon("Dratini", 147, "Dragon", "", 45))
pokemon_array.append(Pokemon("Dragonair", 148, "Dragon", "", 45))
pokemon_array.append(Pokemon("Dragonite", 149, "Dragon", "Flying", 45))
pokemon_array.append(Pokemon("Mewtwo", 150, "Psychic", "", 3))
pokemon_array.append(Pokemon("Mew", 151, "Psychic", "", 45))
