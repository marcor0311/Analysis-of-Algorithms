def sumatoria_cubica(n):
    sum=0
    for i in range(1, n+1):
        for j in range(1, i+1):
            for k in range(j, i+j+1):
                sum+=1
    return sum

def sumatoria_constante(n):
    return (n*(n+1)*(n+2))/3
