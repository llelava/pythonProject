eggsperbox = 6
eggsperomelette = 4
boxesofeggs = 6

total_eggs = boxesofeggs * eggsperbox

total_omelette = int(total_eggs / eggsperomelette)

message = 'You can make {} omelettes with {} boxes of eggs.'.format(total_omelette, boxesofeggs)

print(format(message))
