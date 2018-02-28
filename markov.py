n = 0
gamma = 0.9

exercise = [(0.99, 8) , (.01,8), (.2,0), (.8,0)]
relax = [(0.7, 10) , (.3,10), (0,5), (1,5)]

def p(s,a,next_state):
    if next_state == "fit":
        if a == "exercise":
            if s == "fit":
                t = exercise[0]
                return t[0]
            if s == "unfit":
                t = exercise[2]
                return t[0]
        if a == "relax":
            if s == "fit":
                t = relax[0]
                return t[0]
            if s == "unfit":
                t = relax[2]
                return t[0]

    if next_state == "unfit":
        if a == "exercise":
            if s == "fit":
                t = exercise[1]
                return t[0]
            if s == "unfit":
                t = exercise[3]
                return t[0]
        if a == "relax":
            if s == "fit":
                t = relax[1]
                return t[0]
            if s == "unfit":
                t = relax[3]
                return t[0]

def r(s,a,next_state):
    if next_state == "fit":
        if a == "exercise":
            if s == "fit":
                t = exercise[0]
                return t[1]
            if s == "unfit":
                t = exercise[2]
                return t[1]
        if a == "relax":
            if s == "fit":
                t = relax[0]
                return t[1]
            if s == "unfit":
                t = relax[2]
                return t[1]

    if next_state == "unfit":
        if a == "exercise":
            if s == "fit":
                t = exercise[1]
                return t[1]
            if s == "unfit":
                t = exercise[3]
                return t[1]
        if a == "relax":
            if s == "fit":
                t = relax[1]
                return t[1]
            if s == "unfit":
                t = relax[3]
                return t[1]

def q0(s,a):
    ret = p(s,a,"fit") * r(s,a, "fit") + p(s,a,"unfit") * r(s, a, "unfit")
    return ret

def V(s,n):
    if n == 0:
        return max(q0(s,"exercise"), q0(s,"relax"))
    return max(qn(s,"exercise",n), qn(s,"relax",n))

def qn(s,a,n):
    if n == 0:
        return q0(s,a)
    temp = q0(s,a) + gamma * (p(s,a,"fit") * V("fit",n-1) + p(s, a, "unfit") * V("unfit", n-1))
    return temp

#print p("fit", "exercise", "unfit")
#print r("fit", "exercise", "unfit")
#print q0("fit","exercise")
#print qn("fit","exercise",0)

string = 'Fit, Exercise:    '
for i in range(0,3):
    if i == 2:
        string = string + str(qn("fit","exercise",i)) + "\n"
    else:
        string = string + str(qn("fit","exercise",i)) + ', '

string = string + 'Fit, Relax:       '
for i in range(0,3):
    if i == 2:
        string = string + str(qn("fit","relax",i)) + "\n"
    else:
        string = string + str(qn("fit","relax",i)) + ', '

string = string + 'Unfit, Exercise:  '
for i in range(0,3):
    if i == 2:
        string = string + str(qn("unfit","exercise",i)) + "\n"
    else:
        string = string + str(qn("unfit","exercise",i)) + ', '

string = string + 'Unfit, Relax:     ' 
for i in range(0,3):
    if i == 2:
        string = string + str(qn("unfit","relax",i)) + "\n"
    else:
        string = string + str(qn("unfit","relax",i)) + ', '

print string
