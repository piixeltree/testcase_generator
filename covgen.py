import astor
from ast import *
import sys
import random
import importlib
import os
import math
import numpy as np
cops = [Eq,Lt,Gt,LtE,GtE,NotEq]


def find_mini(func, argc):
    point = [random.randint(1,base_width) for _ in xrange(argc)]
    res = func(*point)
    if res==None:
        return None
    same_counter = 0
    possible_counter = 0
    old_res = None
    while res != 0:
        if possible_counter>100000:
            return None
        gradient = []
        possible_counter+=1
        for i in range(argc):
            next_point = point[:]
            next_point[i] += 1
            gradient.append(func(*next_point) - res)

        #print gradient
        #print point, res
        #raw_input()

        norm = sum(map(lambda x: x**2,gradient))
        alpha = res/(norm+1)

        point = map(lambda x, y: x - alpha*y if y>0 else x - alpha*y, point, gradient)
        res = func(*point)
        if old_res and old_res==res:
            same_counter += 1
            point = map(lambda x, y: x+y,point,[random.randint(-base_width*same_counter,base_width*same_counter+1) for _ in xrange(argc)])
        else:
            if old_res<res:
                alpha = 1
            same_counter = 0
        old_res = res
    return point


def find_mini_avm(func,argc):
    point = [random.randint(1,base_width) for _ in xrange(argc)]
    ori_res = func(*point)
    same_counter = 0
    old_res = None
    while ori_res!=0:
        for i in xrange(argc):
            old_velocity = 0
            velocity = 1
            # determine direction
            point[i]+=1
            if func(*point) < ori_res:
                direction = 1
            else:
                direction = -1
            point[i]-=1
            # go!
            while True:
                point[i] += velocity*direction
                res = func(*point)
                if res>=ori_res:
                    break
                ori_res = res
                velocity, old_velocity = velocity+old_velocity, velocity
            point[i] -= velocity*direction
        if old_res and old_res == ori_res:
            same_counter += 1
            point = map(lambda x, y: x+y, point, [random.randint(-base_width*same_counter,base_width*same_counter+1) for _ in xrange(argc)])
        else:
            same_counter = 0
        old_res = ori_res

    return point



def gen_branch_file(cur, func, depth):
    global cops
    global counter
    global no_func
    if isinstance(cur, If):
        a = cur.test.left
        b = cur.test.comparators[0]
        op = cur.test.ops[0]
        old_body = cur.body
        old_orelse = cur.orelse
        counter += 1
        cur.body = [Return(value=Tuple(elts=[BinOp(left=a, op=Sub(), right=b), Num(n=cops.index(type(op))), Num(n=depth), Str(s='magic\xc0\xff\xeemagic')]))]
        cur.orelse = cur.body
        with open('mutations/%s_%dT.py' % (func.name, counter), 'w') as filei:
            filei.write('depthstrangevariablename = %d\n' % depth + astor.to_source(Module(body=imports+[func])))
        cur.orelse = [Return(value=Tuple(elts=[BinOp(left=a, op=Sub(), right=b), Num(n=5 - cops.index(type(op))), Num(n=depth), Str(s='magic\xc0\xff\xeemagic')]))]
        cur.body = cur.orelse
        with open('mutations/%s_%dF.py' % (func.name, counter), 'w') as filei:
            filei.write('depthstrangevariablename = %d\n' % depth + astor.to_source(Module(body=imports+[func])))
        cur.body = old_body
        cur.orelse = old_orelse
        cur.orelse.insert(0, Return(value=Tuple(elts=[BinOp(left=a, op=Sub(), right=b), Num(n=cops.index(type(op))), Num(n=depth), Str(s='magic\xc0\xff\xeemagic')])))
        for code in cur.body:
            gen_branch_file(code, func, depth + 1)

        cur.orelse.pop(0)
        cur.body.insert(0, Return(value=Tuple(elts=[BinOp(left=a, op=Sub(), right=b), Num(n=5 - cops.index(type(op))), Num(n=depth), Str(s='magic\xc0\xff\xeemagic')])))
        for code in cur.orelse:
            gen_branch_file(code, func, depth + 1)

        cur.body.pop(0)
    else:
        for code in cur.__dict__.get('body',()):
            gen_branch_file(code, func, depth)
        for code in cur.__dict__.get('orelse',()):
            gen_branch_file(code, func, depth)


def func_test_gen(func):

    def gen_check_func(mod):

        def check_func(*args):
            global K
            depth = mod.__dict__['depthstrangevariablename']
            lvl_mini = depth
            bd_mini = np.inf
            x = mod.__dict__[func.name](*args)
            try:
                assert x[-1] == 'magic\xc0\xff\xeemagic'
            except:
                return None

            ap_lvl = depth - x[2]
            if x[1] == 0:
                if x[0] == 0:
                    bd = 0
                else:
                    bd = abs(x[0])
            elif x[1] == 5:
                if x[0] == 0:
                    bd = K
                else:
                    bd = 0
            elif x[1] == 1:
                if x[0] < 0:
                    bd = 0
                else:
                    bd = x[0] + K
            elif x[1] == 3:
                if x[0] <= 0:
                    bd = 0
                else:
                    bd = x[0] + K
            elif x[1] == 2:
                if x[0] > 0:
                    bd = 0
                else:
                    bd = K - x[0]
            elif x[1] == 4:
                if x[0] >= 0:
                    bd = 0
                else:
                    bd = K - x[0]
            #beta = 100
            if lvl_mini > ap_lvl:
                lvl_mini = ap_lvl
                bd_mini = bd
            elif lvl_mini == ap_lvl:
                bd_mini = min(bd_mini,bd)
            fit = bd + (bd_mini*ap_lvl)
            return fit

        return check_func

    argc = len(func.args.args)
    gen_branch_file(func, func, 0)
    sys.path.append('mutations')
    for i in range(1, counter + 1):
        modT = importlib.import_module('%s_%dT' % (func.name, i))
        modF = importlib.import_module('%s_%dF' % (func.name, i))
        check_funcT = gen_check_func(modT)
        check_funcF = gen_check_func(modF)
        Tpoint = find_mini(check_funcT, argc)
        Fpoint = find_mini(check_funcF, argc)
        if Tpoint:
            print '| %dT ' % i + str(Tpoint)[1:-1]
        else:
            print '| %dT -' % i
        if Fpoint:
            print '| %dF ' % i + str(Fpoint)[1:-1]
        else:
            print '| %dF -' % i



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage: python covgen.py target.py'
        exit()
    root = astor.parse_file(sys.argv[1])
    K = 1
    base_width = 10
    imports = filter(lambda x: isinstance(x,Import),root.body)
    for func in root.body:
        if not isinstance(func,FunctionDef):
            continue
        counter = 0
        print 'function : ' + func.name
        func_test_gen(func)
        print
