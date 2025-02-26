

#        (-----Item-----)
#        (key)     (value)
enemy = {
        'loc_x':  70,
        'loc_y':  50,
        'color':  'green',
        'health':  100,
        'name':    'Retardio',
}

print(enemy)
print("Location x = " + str(enemy['loc_x']))
print("Location y = " + str(enemy['loc_y']))
print("His Name is: " + enemy['name'])

enemy['rank'] = 'Admiral'
print(enemy)

del enemy['rank']
print(enemy)

enemy['loc_x'] = enemy['loc_x'] + 40
enemy['health'] = enemy['health'] - 30
if enemy['health'] < 80:
    enemy['color'] = 'Yellow'

print(enemy)

print(enemy.keys())
print(enemy.values())

