import matplotlib.pyplot as plt

data= {}

f_name  = "090_energies.txt"
nf_name = "norm_" + f_name

#-----------------------------------------------------------
ptrn = "sum of band energies :"

f  = open(f_name , 'r')
nf = open(nf_name, 'w')

lines = f.readlines()
for i in range(len(lines)):
    if i%2 == 0:
        theta = lines[i].strip()[-3:]
        energy = lines[i+1].replace(ptrn, "").strip()
        
        print("\nTHETA :", theta)
        print("ENERGY:" , energy)
        
        data[float(theta)] = float(energy)
        
        nf.write(f"THETA : {theta} \nENERGY: {energy}\n\n")

f.close()
nf.close()
#-----------------------------------------------------------

print(20*"-")
print('0 = 360:', data[0] == data[360])


coords = sorted(data.items())
xs, ys = zip(*coords)

plt.title("Magnetic Anisotropy w/ THETA = 090")
plt.xlabel("PHI angle " + "$^o$")
plt.ylabel("Sum of band Energies " + "[Ry]")
plt.plot(xs, ys)

title = "090_energies"
plt.savefig(title + '.svg', format='svg', dpi=1200, bbox_inches='tight')
plt.show()

a = list(ys)
a.sort()
print("\nLowest Energy : ", a[0], "\nHighest Energy: ", a[-1])

nf = open(nf_name, 'a')
nf.write(50*'-' + "\n\n")
nf.write(f"Lowest Energy : {a[0]} \nHighest Energy: {a[-1]}")
nf.close()