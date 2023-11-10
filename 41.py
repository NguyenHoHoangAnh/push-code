note=input("Enter a note: ")
octave_str=note[1]
octave=int(octave_str)
letter=note[0]
C4=261.63
D4=293.66
E4=329.63
F4=349.23
G4=392.00
A4=440.00
B4=493.88
if letter=="C":
    print("Frequency:",C4/2**(4-octave),"Hz")
elif letter=="D":
    print("Frequency:",D4/2**(4-octave),"Hz")
elif letter=="E":
    print("Frequency:",E4/2**(4-octave),"Hz")
elif letter=="F":
    print("Frequency:",F4/2**(4-octave),"Hz")
elif letter=="G":
    print("Frequency:",G4/2**(4-octave),"Hz")
elif letter=="A":
    print("Frequency:",A4/2**(4-octave),"Hz")
elif letter=="B":
    print("Frequency:",B4/2**(4-octave),"Hz")