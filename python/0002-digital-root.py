def digital_root(n):
    sn = str(n)
    size = len(sn)
    
    if size > 1:
        while size > 1:
            total = 0
            for i in range(size):
                total += int(sn[i])

            sn = str(total)
            size = len(sn)

        return(total)
    else:
        return(n)

n = 493193
print(digital_root(n))