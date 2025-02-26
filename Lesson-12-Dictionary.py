#        (-----Item-----)
#        (key)     (value)
enemy = {
        'loc_x':  70,
        'loc_y':  50,
        'color':  'green',
        'health':  100,
        'name':    'Retardio',
        'photo':  ['image1.jpg', 'image2.jpg', 'image3.jpg']
}

all_enemies = []

for x in range(0, 10):
    all_enemies.append(enemy.copy())

for single_enemy in all_enemies:
    print(single_enemy)

all_enemies[5]['health'] = 30
all_enemies[8]['name'] = 'Remilio'
all_enemies[2]['loc_x'] += 10
print('----------------------------')
for single_enemy in all_enemies:
    print(single_enemy)