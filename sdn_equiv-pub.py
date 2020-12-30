import timeit
import numpy as np
from z3 import *

# Input size
SIZE = 10
TIME = 0
rec_cnt = 0
rec_limit = 0

def sw1(init):
    global TIME
    # print "this is sw1 start ==========================="
    # print init

    r1 = [ [ Int("r1_%s_%s" % (i+1, j+1)) for j in range(SIZE) ]
          for i in range(SIZE) ]


    sw1_rule = []
    # print "this is sw1_rule"
    # print sw1_rule

    for i in range(SIZE):
        for j in range(SIZE):
            if (j == 1):
                sw1_rule.append(r1[i][j] == (True and init[i][j]))
            else:
                sw1_rule.append(r1[i][j] == False)
    # print "this is sw1_rule"
    # print_matrix(sw1_rule)



    s = Solver()
    s.add(sw1_rule)
 
#    print s.check()

    start_time = timeit.default_timer()
    s.check()
    terminate_time = timeit.default_timer()
    elapsed_time = terminate_time - start_time
#    print "Elapsed time at sw1 is %.2f ms" % (elapsed_time*1000)
    TIME = TIME + elapsed_time
 
    # print("%.8f sec elapsed." % (elapsed_time))
    # print("%.2f ms elapsed." % ((elapsed_time)*1000))
#    print s.statistics()
    m = s.model()
    # print m
    # print "this is sw1 end ==========================="


    t1 = [ [ m.evaluate(r1[i][j]) for j in range(SIZE) ]
    	    	for i in range(SIZE) ]

    # print "this is t1 after sw1_rule remapped to array from model"
    #print t1
    return t1

def sw2(t1):
    global TIME
    # print "this is sw2 start ==========================="
    # print t1

    r2 = [ [ Int("r2_%s_%s" % (i+1, j+1)) for j in range(SIZE) ]
          for i in range(SIZE) ]

    sw2_rule = []
    # print "this is sw2_rule"
    # print sw2_rule

    for i in range(SIZE):
        for j in range(SIZE):
            if(t1[i][j] == 1):
                if (i == 0):
                    sw2_rule.append(r2[i][j] == False)
                elif (j == 1):
                    sw2_rule.append(r2[i][j] == (True and t1[i][j]))
                else:
                    sw2_rule.append(r2[i][j] == False)
            else:
                sw2_rule.append(r2[i][j] == False)
    # print "this is sw2_rule"
    # print_matrix(sw2_rule)

    s = Solver()
    s.add(sw2_rule)

    start_time = timeit.default_timer()
    s.check()
    terminate_time = timeit.default_timer()
    elapsed_time = terminate_time - start_time
#    print "Elapsed time at sw2 is %.2f ms" % (elapsed_time*1000)
    TIME = TIME + elapsed_time
 
    # print("%.8f sec elapsed." % (elapsed_time))
    # print("%.2f ms elapsed." % ((elapsed_time)*1000))

    m = s.model()
    # print m
    # print "this is sw2 end ==========================="


    t2 = [ [ m.evaluate(r2[i][j]) for j in range(SIZE) ]
                for i in range(SIZE) ]
    
    # print "this is t2 after sw2_rule remapped to array from model"
    # print t2
    # exit(1)
    return t2

def sw3(t2):
    global TIME
    # print "this is sw3 start ==========================="
    # print t2

    r3 = [ [ Int("r3_%s_%s" % (i+1, j+1)) for j in range(SIZE) ]
          for i in range(SIZE) ]



    sw3_rule = []
    # print "this is sw3_rule"
    # print sw3_rule

    for i in range(SIZE):
        for j in range(SIZE):
            if(t2[i][j] == 1):
                if (j == 1):
                    sw3_rule.append(r3[i][j] == (True))# and t2[i][j]))
                else:
                    sw3_rule.append(r3[i][j] == False)
            else:
                sw3_rule.append(r3[i][j] == False)
    # print "this is sw3_rule"
    # print_matrix(sw3_rule)
    # exit(1)

    s = Solver()
    s.add(sw3_rule)

    start_time = timeit.default_timer()
    s.check()
    terminate_time = timeit.default_timer()
    elapsed_time = terminate_time - start_time
#    print "Elapsed time at sw3 is %.2f ms" % (elapsed_time*1000)
    TIME = TIME + elapsed_time
 
    # print("%.8f sec elapsed." % (elapsed_time))
    # print("%.2f ms elapsed." % ((elapsed_time)*1000))

    m = s.model()
    # print m
    # print "this is sw3 end ==========================="


    t3 = [ [ m.evaluate(r3[i][j]) for j in range(SIZE) ]
                for i in range(SIZE) ]

    # print "this is t3 after sw3_rule remapped to array from model"
    # print t3
    # exit(1)
    return t3


def sw4(t3):
    global TIME
    # print "this is sw4 start ==========================="
    # print t3

    r4 = [ [ Int("r4_%s_%s" % (i+1, j+1)) for j in range(SIZE) ]
          for i in range(SIZE) ]



    sw4_rule = []
    # print "this is sw4_rule"
    # print sw4_rule

    for i in range(SIZE):
        for j in range(SIZE):
            if(t3[i][j] == 1):
                if (j == 1):
                    sw4_rule.append(r4[i][j] == (True))# and t3[i][j]))
                else:
                    sw4_rule.append(r4[i][j] == False)
            else:
                sw4_rule.append(r4[i][j] == False)
    # print "this is sw4_rule"
    # print_matrix(sw4_rule)
    # exit(1)


    s = Solver()
    s.add(sw4_rule)

    start_time = timeit.default_timer()
    s.check()
    terminate_time = timeit.default_timer()
    elapsed_time = terminate_time - start_time
#    print "Elapsed time at sw4 is %.2f ms" % (elapsed_time*1000)
    TIME = TIME + elapsed_time
 
    # print("%.8f sec elapsed." % (elapsed_time))
    # print("%.2f ms elapsed." % ((elapsed_time)*1000))

    m = s.model()
    # print m
    # print "this is sw4 end ==========================="


    t4 = [ [ m.evaluate(r4[i][j]) for j in range(SIZE) ]
                for i in range(SIZE) ]

    # print "this is t4 after sw4_rule remapped to array from model"
    # print t4
    # exit(1)
    return t4

def sw5(t4):
    global TIME
    global rec_cnt
    global rec_limit
    # print "this is sw4 start ==========================="
    # print t3



    r5 = [ [ Int("r5_%s_%s" % (i+1, j+1)) for j in range(SIZE) ]
          for i in range(SIZE) ]



    sw5_rule = []
    # print "this is sw4_rule"
    # print sw4_rule

    for i in range(SIZE):
        for j in range(SIZE):
            if(t4[i][j] == 1):
                if (j == 1):
                    sw5_rule.append(r5[i][j] == (True))# and t3[i][j]))
                else:
                    sw5_rule.append(r5[i][j] == False)
            else:
                sw5_rule.append(r5[i][j] == False)
    # print "this is sw4_rule"
    # print_matrix(sw4_rule)
    # exit(1)


    s = Solver()
    s.add(sw5_rule)

    start_time = timeit.default_timer()
    s.check()
    terminate_time = timeit.default_timer()
    elapsed_time = terminate_time - start_time
#    print "Elapsed time at sw4 is %.2f ms" % (elapsed_time*1000)
    TIME = TIME + elapsed_time
 
    # print("%.8f sec elapsed." % (elapsed_time))
    # print("%.2f ms elapsed." % ((elapsed_time)*1000))

    m = s.model()
    # print m
    # print "this is sw4 end ==========================="


    t5 = [ [ m.evaluate(r5[i][j]) for j in range(SIZE) ]
                for i in range(SIZE) ]

    # print "this is t4 after sw4_rule remapped to array from model"
    # print t4
    # exit(1)

    if (rec_cnt == rec_limit):
        print "Iterating sw5 %s times takes total %.2f ms, with size %s matrix." % (rec_cnt, ((TIME)*1000), SIZE)
        print "Average is %.2f ms." % (((TIME)*1000)/rec_cnt)
        return



    rec_cnt = rec_cnt + 1
    
    sw5(t5)

    return t5

def checkmyfw():
    global TIME
    global SIZE
    global rec_cnt
    global rec_limit
    init = [ [0 if i==j else 1 for j in range(SIZE)] for i in range(SIZE) ]
#    init = [ [ 1 for j in range(SIZE)] for i in range(SIZE) ]
#    print_matrix(init)
    

    # start_time = timeit.default_timer()
    count = 0
    rule = []
    for i in range(SIZE):
        for j in range(SIZE):
            if (i != j):
                if (i == 0):
                    rule.append(0)
                    count += 1
                elif (j == 1):
                    rule.append(1)
                    count += 1
                else:
                    rule.append(0)
                    count += 1
            else:
                rule.append(0)
                count += 1

    # k1 = ((0,0,0,0,0),
    #       (0,0,0,0,0),
    #       (0,0,1,0,0),
    #       (0,0,0,0,0),
    #       (0,0,0,0,0))

    # k2 = ((1,1,1,1,1),
    #       (1,1,1,1,1),
    #       (1,1,0,1,1),
    #       (1,1,1,1,1),
    #       (1,1,1,1,0))



    TIME = 0
    t124 = sw4(sw2(sw1(init)))
    print("For path 1-2-4, rule check took total %.2f ms, with size %s matrix." % (((TIME)*1000), SIZE))

    TIME = 0
    t134 = sw4(sw3(sw1(init)))
    print("For path 1-3-4, rule check took total %.2f ms, with size %s matrix." % (((TIME)*1000), SIZE))


    temp1 = []
    temp2 = []

    for i in range(SIZE):
        for j in range(SIZE):
            if (t124[i][j] == 0):
                temp1.append(0)
            else:
                temp1.append(1)
    
    for i in range(SIZE):
        for j in range(SIZE):
            if (t134[i][j] == 0):
                temp2.append(0)
            else:
                temp2.append(1)
    


    temp3 = np.logical_or(temp1, temp2)
    temp4 = []
    # Transform (temp1 or temp2) to normal int list

    for i in range(SIZE):
        for j in range(SIZE):
            if (temp3[j+(i*SIZE)] == True):
                temp4.append(1)
            else:
                temp4.append(0)

    print "=========================== Check with rule ==========================="
    print rule == temp4
    
    iter = 10
    TIME = 0
    for i in range(iter):
        sw1(init)
    print "Iterating sw1 %s times takes total %.2f ms, with size %s matrix." % (iter, ((TIME)*1000), SIZE)
    print "Average is %.2f ms." % (((TIME)*1000)/iter)


if __name__ == "__main__":
    checkmyfw()

