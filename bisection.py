def bisection(f, xmin, xmax, threshold=1e-4):
    xmid = .5*(xmin + xmax)
    if abs(xmax - xmid) < abs(threshold):
        return (xmid, f(xmid))
    else:
        if slope(f, xmid) < 0:
            return bisection(f, xmid, xmax, threshold)
        else:
            return bisection(f, xmin, xmid, threshold)

def slope(f, x):
    dx = 0.0001
    return (f(x + dx) - f(x - dx))/(2*dx)

ans = bisection(lambda x: (x-2)**2, -10, 10, 1e-6)
