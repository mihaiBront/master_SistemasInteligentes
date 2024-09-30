Rs = [0,0,0,0,1]
V0 = [0,0,0,0,0]

VnList = []
VnList.append(V0)

Tsas = 1
Gamma = 0.5

n_max = 6
VnList.append([Tsas * Rs[j] + Gamma * VnList[-1][j+1] if (j<(len(Rs)-1)) else Tsas * Rs[j] for j in range(len(Rs))])
i = 1
while VnList[-1] != VnList[-2]:
    v_new = [Tsas * Rs[j] + Gamma * VnList[-1][j+1] if (j<(len(Rs)-1)) else Tsas * Rs[j] for j in range(len(Rs))]
    VnList.append(v_new)
    
print(f"Vstar = {VnList[-1]} (taken {len(VnList) - 2} iterations to complete)")