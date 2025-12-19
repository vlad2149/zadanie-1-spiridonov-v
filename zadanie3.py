#1
"""
count = 0
max_summa = 0
with open('39762.txt', 'r') as file:
    chisla = file.readlines()
    chisla = [int(el) for el in chisla]
for i in range(len(chisla) - 1):
    if (chisla[i] * chisla[i+1]) % 15 == 0 and ((chisla[i] + chisla[i+1]) % 7) == 0:
        count += 1
        if max_summa < (chisla[i] + chisla[i+1]):
            max_summa = (chisla[i] + chisla[i+1])
print(count, max_summa)
"""
#2
"""
with open("68279.txt", "r") as f:
    n = [int(e1) for e1 in f]
    max_e1 = 0

    for e1 in n:
        if str(e1)[-3:] == "562":
            if max_e1 < e1:
                max_e1 = e1
    
    c = 0
    max_sum = 0
    
    for i in range(len(n) - 3):
        lst = [n[i], n[i + 1], n[i + 2], n[i + 3]]
        lst5 = [e for e in lst if len(str(e)) == 5]
        lst_not5 = [e for e in lst if len(str(e)) != 5]
        lst_crat3 = [e for e in lst if e % 3 == 0]
        lst_crat7 = [e for e in lst if e % 7 == 0]
        
        if len(lst5) >= 1 and len(lst_not5) >= 2:
            if len(lst_crat3) < len(lst_crat7):
                if max_e1 < sum(lst) < 2 * max_e1:
                    c += 1
                    if max_sum < sum(l):
                        max_sum = sum(l)
    
    print(c, max_sum)
"""


