#Centered polygonal numbers

def centPoly(n,m): #n=number of sides, m=number of terms
    print([((n*(x**2) + n*x + 2)/2) for x in range(m)])

