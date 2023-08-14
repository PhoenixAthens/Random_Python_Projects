from radon.visitors import ComplexityVisitor
file = open("RadonTestFile.py","r")
v = ComplexityVisitor.from_code(file.read())
file.close()
print(v.functions)

from radon.complexity import cc_rank
print(cc_rank(5), cc_rank(8), cc_rank(13), cc_rank(26), cc_rank(36), cc_rank(45))