#Fractional Knapstack Problem

class item:
    def __init__(self,profit,weight):
        self.profit=profit
        self.weight=weight

def frac(w,arr):
    arr.sort(key=lambda x: (x.profit/x.weight), reverse=True)
    finalval=0.0
    for item in arr:
        if(item.weight<=w):
            w-=item.weight
            finalval+=item.profit
        else:
            finalval+=item.profit*w/item.weight
            break
    return finalval
    
w= 50
arr = [item(60, 10), item(100, 20), item(120, 30)]
max_val = frac(w, arr)
print(max_val)
