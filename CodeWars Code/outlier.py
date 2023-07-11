def find_outlier(integers):
    odds = [x for x in integers if x%2!=0]
    return odds[0] if len(odds)==1 else next(x for x in integers if x%2==0)

a = 2, 4, 6, 8, 10, 3
print(find_outlier(a))
