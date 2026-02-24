import numpy as np
from collections import Counter

# 1. Menyiapkan Data Input (Sama untuk semua versi)
A = np.array([10, 20, 30, 40])
B = np.array([5, 15, 25, 35])

# 2. Mendefinisikan N-Version (Dikembangkan secara terpisah)
def versi_1(a, b):
    # Menggunakan fitur vektorisasi NumPy (SIMD murni)
    return a + b

def versi_2(a, b):
    # Menggunakan pendekatan list comprehension
    return np.array([x + y for x, y in zip(a, b)])

def versi_3(a, b):
    # Simulasi kesalahan (error) pada versi ini untuk menguji fault-tolerance
    return a + b + 1 

# 3. Menjalankan semua versi secara paralel
hasil_1 = versi_1(A, B)
hasil_2 = versi_2(A, B)
hasil_3 = versi_3(A, B)

# 4. Mekanisme Voting (Membandingkan output untuk deteksi error)
semua_hasil = [tuple(hasil_1), tuple(hasil_2), tuple(hasil_3)]
voter = Counter(semua_hasil)

# Mengambil hasil yang paling banyak muncul (majority vote)
hasil_final, jumlah_suara = voter.most_common(1)[0]

# Output Akhir
print(f"Hasil Instruksi C = A + B: {hasil_final}")
print(f"Status: Berhasil dengan {jumlah_suara} dari 3 suara setuju.")