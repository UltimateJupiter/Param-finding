import numpy as np

def ret_parse():
    fl = open("./testing_params.txt")
    
    queue = list()
    ls = [n for n in fl]
    assert len(ls) == 15, len(ls)

    for line in ls:

        tmp = line.split("|")
        ret = float(tmp[1])/100
        queue.append(ret)
    
    arr = np.asarray(queue) 
    # arr = arr/100
    return arr
