import random
side=["H","T"]
flips_needed=[]
consecutive_flips=3
for _ in range (10):
    consecutive_count=0
    flips=0
    last_outcome=""
    while consecutive_count<consecutive_flips:
        outcome=random.choice(side)
        print(outcome,end=" ")
        if outcome==last_outcome:
            consecutive_count=consecutive_count+1
        else:
            consecutive_count=1
        last_outcome=outcome
        flips=flips+1
    flips_needed.append(flips)
    print("(",flips," flips)",sep="")
flip_average=sum(flips_needed)/len(flips_needed)
print("On average,",flip_average,"flips were needed.")