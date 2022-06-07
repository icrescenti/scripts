from math import log

print("BEWARE that rb and Tb are set from a compression generated using bzip2 on the following hardware")
print("----------------------")

alpha = 1.0
r = float(input("Compression ratio: ")) #1.0031931878658862
T = float(input("Compression time: ")) #0.03873023986816406
rb = 1.005687584836085
Tb = 0.013791036605834962
# 1.3143446969047792

w = alpha * r/rb * log(Tb)/log(T)

print(w)