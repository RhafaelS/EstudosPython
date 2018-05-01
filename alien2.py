aliens = []
cont = 0

for alien_number in range(40):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    cont = cont + 1

for alien in aliens[:5]:
    print(alien)

print("Foram adicionados " + str(cont) + " alienigenas!")