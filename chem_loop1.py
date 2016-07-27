element1 = ['Li', 'Na', 'K', 'Rb', 'Cs']
element2 = ['F', 'Cl', 'Br', 'I', 'At']
element3 = ['Mg', 'Ca', 'Sr', 'Ba', 'Ra']
element4 = ['Al', 'Ga', 'In', 'Tl','As']
number = ['2','3','4']
i = 0
j = 0
k = 0
print "List of compounds in database:"
while i<4 :
 
    compound = element1[i] + element2[i] 
    
    print compound
    i = i + 1
 
    compound = element3[j] + element2[j] + number[0]

    print compound
    j = j + 1

    compound = element4[k] + element2[k] + number[1]

    print compound
    k = k + 1

    print '----------------------'
print 'Equations to study:'
m = 0
while m<4:

    compound1 = element1[m] + element2[m+1]
    compound2 = element1[m+1] + element2[m]
    compound3 = element1[m+1] + element2[m+1]
    compound4 = element1[m] + element2[m]
    print compound1 ,'+', compound2 , '------>', compound3 ,'+', compound4 ,
    print ' '
    compound11 = element3[m] + element4[m+1]
    compound21 = element3[m+1] + element4[m]
    compound31 = element3[m+1] + element4[m+1]
    compound41 = element3[m] + element4[m]
    print compound11 ,'+', compound21 , '------>', compound31 ,'+', compound41 ,
    print ' '
    m = m + 1

print ' *********************************'
print 'Molecular Weight Calculations:'
'Lets use the following atomic weights for practice.'
print 'sodium = 23'
print 'chlorine = 35'
print "Now find the molecular weight of the compound sodium chloride which has the formula, NaCl."


x = float(raw_input('>'))
if x == 58:
    print 'correct.'
else:
    print 'sorry, incorrect.'
print '**********************'
print 'sulfur = 32'
print 'oxygen = 16'
print "Now find the molecular weight of the compound sulfur trioxide which has the formula, SO3."
y = float(raw_input('>'))
if y == 80 and x != 58:

    print 'correct.'
if x == 58 and y == 80:
    print 'Congrats, you got both correct!'


if x != 58 and y != 80:
    print "Sorry, you got both wrong."
print '*******************************'
print 'Temperature conversions.'
print 'Input the Celsius value.' 
temp_C = float(raw_input('>'))
temp_F = 1.8*temp_C + 32
print 'Temp.(F) =', temp_F
print '*******************************'
print 'Mass to moles conversion.'
print 'Input the mass (g) of sulfur trioxide to obtain the number of moles.'
mass = float(raw_input('>'))
no_moles = mass/80
print 'Number of moles = ', no_moles 
print '*******************************'
print 'Stoichiometry'
print 'In the following reaction, how many moles of oxygen is needed to react completely with 2 moles of SO2?'
print 'SO2 + O2 ------> SO3'

a = float(raw_input('>'))

if a == 1.0:
    print "Correct!"
else:
    print "sorry, incorrect."
print '*******************************'