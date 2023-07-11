def make_readable(seconds):
    try:
        seconds = float(seconds)
        HH = 0
        MM = 0
        SS = 0
        if seconds > 3599:
            while seconds > 3599:
                seconds -= 3600
                HH += 1
        else:
            HH = "00"
        if seconds > 59:
            while seconds > 59:
                seconds -= 60
                MM += 1
        else:
            MM = "00"
        if seconds > 59:
            seconds = 0
        else:
            SS = int(seconds)
        HH = str(HH)
        MM = str(MM)
        SS = str(SS)

        result = HH.zfill(2) + ':' + MM.zfill(2) + ':' + SS.zfill(2)
    except:
        result = "Nothing to make readable"
    return result

print(make_readable(93982))

'''
Testing solutions because of a troll in the comments calling the top solution bad code:

import sys, timeit

def make_readable1(s):
    return f'{s // 3600:02}:{s // 60 % 60:02}:{s % 60:02}'
def make_readable2(s):
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return f'{h:02}:{m:02}:{s:02}'
print(sys.version_info)
t = timeit.timeit(lambda: make_readable1(93982), number=100000)
print(f"Time taken: {t:.6f} seconds")
t = timeit.timeit(lambda: make_readable2(93982), number=100000)
print(f"Time taken: {t:.6f} seconds")
'''
