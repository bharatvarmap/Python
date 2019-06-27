def SimpleInterest(p,t,r):
    return (p*t*r)/100

P = int(input("Enter Principal amount: "))
T = int(input("Enter Time period(in years): "))
R = float(input("Enter rate of interest: "))

print("The simple interset to be paid for a ${} loan for a {} year period at R.O.I of {}% is ${}"
      .format(P, T, R, SimpleInterest(P,T,R)))
