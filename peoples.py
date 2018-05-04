chars = {
    'Thrall':{
        'color': 'Green',
        'age': 500,
        'attack': 1000,
        'defense': 800,
        'class': 'Shaman',
    },

    'Voljin':{
        'color': 'Blue',
        'age': 2000,
        'attack': 900,
        'defense': 1200,
        'class': 'Witch Doctor',
    },

    'Cairne Bloodhoof': {
        'color': 'Yellow',
        'age': 5000,
        'attack': 1900,
        'defense': 1500,
        'class': 'Tauren Chieftain',
    }
}

# percorrer os dicionarios aninhados e mostrar todos os atributos deles
for char_name, char_prop in chars.items():
    Nome = char_name
    Cor = char_prop['color']
    Idade = char_prop['age']
    Ataque = char_prop['attack']
    Defesa = char_prop['defense']
    Classe = char_prop['class']

    print("\nNome: " + Nome)
    print("Cor: " + Cor)
    print("Idade: " + str(Idade))
    print("Ataque: " + str(Ataque))
    print("Defesa: " + str(Defesa))
    print("Classe: " + Classe)


