#!/usr/bin/python2
# -*- coding: utf-8 -*-

from math import *
from fractions import *
from itertools import *
from bisect import *

def cached(func):
    pool = {}
    def wrapper(*arg):
        if arg not in pool:
            pool[arg] = func(*arg)
        return pool[arg]
    return wrapper

@cached
def fib(n):
    return fib(n-1)+fib(n-2) if n >= 2 else 1

def isqrt(n):
    return int(sqrt(n))

def first_factor(n):
    assert n > 1
    if n == 2: return n
    if n % 2 == 0: return 2
    for i in xrange(3, isqrt(n)+1, 2):
        if n % i == 0: return i
    return n

def is_prime(n):
    return first_factor(n) == n if n >= 2 else False

def prime():
    yield 2
    yield 3
    primes = [5]
    yield primes[0]
    last = 5
    six_flag = True
    while True:
        last += 2 if six_flag else 4
        six_flag = not six_flag
        up_limit = int(sqrt(last))
        flag = False
        for p in primes:
            if last % p == 0:
                break
            if p >= up_limit:
                flag = True
                break
        if flag:
            primes.append(last)
            yield last

def pow_mod(n, m, p):
    if m == 1: return n % p
    if m == 0: return 1
    k = pow_mod(n, m/2, p)
    k = k*k % p
    if m % 2 == 0:
        return k
    return k*n % p

def sieve(n):
    marked = [i % 2 for i in xrange(n)]
    marked[1] = 0
    marked[2] = 1
    for value in xrange(3, n, 2):
        if marked[value] == 1:
            for i in xrange(value*3, n, value*2):
                marked[i] = 0
    return marked

def gcd(m, n):
    if m < n: m, n = n, m
    if m == n: return m
    if n == 0: return m
    return gcd(n, m % n)

def is_quad(n):
    return isqrt(n)**2 == n

def palindrome(x):
    s = str(x)
    return s == s[::-1]

def palindrome_0(x):
    return x == int(str(x)[::-1])

def get_primes_by_sieve(m, odd_only=False):
    sieves = sieve(m)
    if odd_only:
        primes = [i for i, f in enumerate(sieves) if f and i != 2]
    else:
        primes = [i for i, f in enumerate(sieves) if f]
    return primes, sieves

def factorization(n):
    if n % 2 == 0:
        k = 0
        while n % 2 == 0:
            n /= 2
            k += 1
        ret = [(2, k)]
    else:
        ret = []
    p = 3
    isqrtn = isqrt(n)
    while n > 1 and p <= isqrtn:
        while n % p != 0: p += 2
        k = 0
        while n % p == 0:
            n /= p
            k += 1
        ret.append((p, k))
    if n > 1: ret.append((n, 1))
    return ret

def phi(n):
    for p, k in factorization(n):
        n = n/p*(p-1)
    return n

#============================
# Deprecated
#============================

class Primes(list):
    _primes = [2, 3]
    _size = 2
    def __getitem__(self, n):
        #prime = self._primes
        if self._size > n: return self._primes[n]
        last = self._primes[-1]
        while True:
            last += 2
            up_limit = isqrt(last)
            flag = True
            for p in self._primes:
                if last % p == 0:
                    flag = False
                    break
                if p >= up_limit: break
            if flag:
                self._primes.append(last)
                self._size += 1
                if self._size > n: 
                    self._primes[n] = last
                    return last

def get_prime(index_=None, max=None):
    assert any((index_, max))
    if index_ is not None:
        cnt = index_ - 1
        for i, p in enumerate(prime()):
            if i == cnt:
                return p
    if max is not None:
        ps = []
        for p in prime():
            if p < max:
                ps.append(p)
        return ps

def test_prime(n):
    ret = []
    for p in prime():
        if p > n:
            break
        ret.append(p)
    return ret

def test_fib(n):
    return [fib(i) for i in xrange(n)]
