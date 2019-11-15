def series_stumpff(t,k,N=15):
    from math import factorial
    sk=lambda n:t/((2*n+k+1)*(2*n+k+2))*(1-sk(n+1)) if n<N else 0
    return (1-sk(0))/factorial(k)

def error_series_stumpff(t,k,N):
    Pi=lambda N,k:(2*N+k+1)*(2*N+k+2)*Pi(N-1,k) if N>=0 else 1
    from math import factorial
    error=abs(t**N/Pi(N,k)/factorial(k))
    return error

def series_stumpff_analytic(t):
    from math import cos,sin,cosh,sinh
    y=abs(t)**0.5
    c0=cos(y) if t>=0 else cosh(y)
    c1=sin(y)/y if t>=0 else sinh(y)/y
    c2=(1-cos(y))/y**2 if t>=0 else -(1-cosh(y))/y**2
    c3=(y-sin(y))/y**3 if t>=0 else -(y-sinh(y))/y**3
    return c0,c1,c2,c3