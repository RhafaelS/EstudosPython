chars = {
    'Thrall':{
        'color': 'green',
        'age': 500,
        'attack': 1000,
        'defense': 800,
        'class': 'Shaman',
    },

    'Voljin':{
        'color': 'blue',
        'age': 2000,
        'attack': 900,
        'defense': 1200,
        'class': 'Witch Doctor',
    },

    'Cairne Bloodhoof': {
        'color': 'yellow',
        'age': 5000,
        'attack': 1900,
        'defense': 1500,
        'class': 'Tauren Chieftain',
    }
}

# percorrer os dicionarios aninhados e mostrar todos os atributos deles
for char_name in chars.items():
    print("\nName: " + char_name)
