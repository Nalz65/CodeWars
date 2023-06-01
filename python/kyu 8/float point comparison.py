'''
a, b, c = 1e-9, 1e-9, 3.33e7
print(c)
print((a + b) + c)
print(a + (b + c))
print((a + b) + c == a + (b + c))
'''

def approx_equals(a, b, rel_tol=1e-03, abs_tol=0.0):
    #a = round(a, 3)
    #b = round(b, 3)
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
    #return abs(a) == abs(b)
print(approx_equals(0.1+0.2,0.3))

#Reference
# https://davidamos.dev/the-right-way-to-compare-floats-in-python/
# https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python