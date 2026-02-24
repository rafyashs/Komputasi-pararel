import numpy as np

# Membuat array besar
data = np.array([1, 2, 3, 4, 5])

# Operasi SIMD: Satu perintah (* 2) untuk semua elemen
hasil = data * 2

print(hasil) # Output: [ 2  4  6  8 10]