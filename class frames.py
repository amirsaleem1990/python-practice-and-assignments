first_size = int(input('\nFirst size: '))
second_size = int(input('\nSecond size: '))
frame_size = first_size * second_size / 144
glass_rate = int(input('\nGlass rate: '))
lasani_rate = float(input('\nLasani rate: '))
ps_rate = int(input('\nPs rate: '))
ps_cost = ((first_size + second_size) * 2 * ps_rate* 1.05)/120
glass_cost = frame_size * glass_rate * 1.05
lasani_cost = frame_size * lasani_rate
material_cost = int(input('\nmaterial cost: '))
sideWood_with = int(input('\nSide wood with: '))
sideWood_size = (first_size + second_size) * 2 / 12 * sideWood_with
sideWood_cost = sideWood_size * 1.5
mount_size = float(input('\nmount with: '))
mount_cost = ((first_size + second_size) * 2 / 144) * mount_size * 9.625
p_g_rate = int(input('\nPrinted glass rate: '))
p_g_cost = p_g_rate * 1.05
kareegar = int(input('\nKareegar: '))
total_cost = ps_cost + glass_cost + lasani_cost +material_cost+ sideWood_cost +mount_cost + p_g_cost
print('\n\n\nFrame size:\t', str(first_size)+ '*'+ str(second_size))
print('Glass:\t\t', str(glass_cost))
print('Ps: \t\t', str(ps_cost))
print('Lasani: \t', str(lasani_cost))
print('Matireal:\t', str(material_cost))
print('Side wood:\t', str(sideWood_cost))
print('Mount:\t\t', str(mount_cost))
print('P/g:\t\t', str(p_g_cost))
print('\nTotal cost:\t', str(total_cost))

