n1 = float(input("\033[1;30;45mStudent's first grade:\033[m "))
n2 = float(input("\033[1;30;45mStudent's second grade:\033[m "))
c = {'clean': '\033[m',
     'blackandblue': '\033[1;30;46m',
     'blackandred': '\033[1;30;41m'}
print("{}The student's average is{} {}{:.1f}{}".format(c['blackandblue'], c['clean'], c['blackandred'], (n1+n2) / 2, c['clean']))
