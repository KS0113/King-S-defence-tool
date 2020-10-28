# King-S-defence-tool
wavesize = float(input("Enter attacking wave size: "))
attackstrength = float(input("Enter attacking troop's range value (include any comm bonus): "))
commrstrength = 1+(float(input("Enter the range % on the comm (include any HoL bonuses and title effects): "))/100)
shieldwave = float(input("Enter the number of shield waves: "))
noshieldwave = float(input("Enter the number of wall-moat waves: "))
wallcap = float(input("Enter your wall capacity: "))
defm_rstrength = float(input("Enter defensive melee troop's range value: "))
defr_rstrength = float(input("Enter defensive range troop's range value: "))
castmstrength = 1+(float(input("Enter the melee % on the cast (include any HoL bonuses and combat strength %): "))/100)
castrstrength = 1+(float(input("Enter the range % on the cast (include any HoL bonuses and combat strength %): "))/100)
castwprcnt= 1+(float(input("Enter the wall protection % with no tools after comm and HoL reduction is applied (i.e. total wall protection with no tools minus the comm value): "))/100)

totalwavedefshields=0
totalwavedefnoshields=0
totalattackstrength=[]
finallist=[]
finallisttwo=[]
toolcombos = [[0,2.8,0],[0.43,2.1,0],[0,2.1,0.5],[0.43,1.4,0.5],[0.86,1.4,0],[0.86,0.7,0.5],[1.29,0.7,0],[1.72,0,0]]

for a in toolcombos:
    for m in range(1,101):
        m=m/100
        totalwavedefshields=wallcap/((((wallcap*m*defm_rstrength*(castmstrength+a[0])*(castwprcnt+a[2]))/(wavesize*attackstrength*commrstrength))**0.5)*((wallcap*m*defm_rstrength*(castmstrength+a[0])*(castwprcnt+a[2]))/(wavesize*attackstrength*commrstrength)))  
        totalwavedefnoshields=wallcap/(((((wallcap*m*defm_rstrength*(castmstrength+a[0]))+(wallcap*(1-m)*defr_rstrength*(castrstrength+a[1])))/(wavesize*attackstrength*commrstrength))**0.5)*(((wallcap*m*defm_rstrength*(castmstrength+a[0]))+(wallcap*(1-m)*defr_rstrength*(castrstrength+a[1])))/(wavesize*attackstrength*commrstrength)))
        totalattackstrength.append((shieldwave*totalwavedefshields)+(noshieldwave*totalwavedefnoshields))
    finallist.append(min(totalattackstrength))
    finallisttwo.append(totalattackstrength.index(min(totalattackstrength)))
    totalattackstrength=[]

if finallist.index(min(finallist))==0:
    print("Your setup is 4 slits and your melee % is ",finallisttwo[0])
elif finallist.index(min(finallist))==1:
    print("Your setup is 1 quick lime, 3 slits and your melee % is ",finallisttwo[1])
elif finallist.index(min(finallist))==2:
    print("Your setup us  3 slits, 1 murder hole and your melee % is ",finallisttwo[2])
elif finallist.index(min(finallist))==3:
    print("Your setup is 1 quick lime, 2 slits, 1 murder hole and your melee % is ",finallisttwo[3])
elif finallist.index(min(finallist))==4:
    print("Your setup is 2 quick limes, 2 slits and your melee % is ",finallisttwo[4])
elif finallist.index(min(finallist))==5:
    print("Your setup is 2 quick limes, 1 slit, 1 murder hole and your melee % is ",finallisttwo[5])
elif finallist.index(min(finallist))==6:
    print("Your setup is 3 quick limes, 1 slit and your melee % is ",finallisttwo[6])
elif finallist.index(min(finallist))==7:
    print("Your setup us 4 quick limes and your melee % is ", finallisttwo[7])
