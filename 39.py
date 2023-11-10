
dBlevel=int(input("dB:"))
if dBlevel == 130:
    print("Jackhammer")
elif dBlevel == 106:
    print('Gas lawnmower')
elif dBlevel ==70:
    print('Alarm clock')
elif dBlevel == 40:
    print ('Quiet room')
elif 40 < dBlevel < 70: 
    print("The sound level is between {40} and {70}")
elif 70 < dBlevel < 106:
    print("The sound level is between {70} and {106}")
elif 106 < dBlevel < 130:
    print ("The sound level is between {106} and {130}")
if dBlevel < 40:
    print('The noise is quieter than a quiet room')
elif dBlevel >130:
    print('The noise is louder than a Jackhammer')