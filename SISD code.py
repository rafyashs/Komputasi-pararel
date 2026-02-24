import numpy as np
from collections import Counter

# --- DATA INPUT (Sama untuk semua versi) ---
A = np.array([10, 20, 30, 40])
B = np.array([5, 15, 25, 35])

# --- 1. REPRESENTASI SISD (Single Instruction, Single Data) ---
# Diproses secara linear/sekuensial (satu unit data per waktu)
def proses_sisd(a, b):
    hasil = []
    for i in range(len(a)):
        hasil.append(a[i] + b[i]) # Satu per satu
    return np.array(hasil)

# --- 2. REPRESENTASI SIMD (Single Instruction, Multiple Data) ---
# Instruksi C = A + B dieksekusi secara paralel pada semua elemen
def proses_simd(a, b):
    return a + b  # Operasi vektor (semua A1..A4 diproses sekaligus)

# --- 3. N-VERSION PROGRAMMING (Fault-Tolerance) ---
# Mengembangkan versi independen secara terpisah
def versi_1(a, b): return proses_simd(a, b) # Menggunakan SIMD yang efisien
def versi_2(a, b): return proses_sisd(a, b) # Menggunakan SISD yang sederhana
def versi_3(a, b): return a + b + 0         # Versi lain (asumsi benar)

# Eksekusi paralel dari N-versi
output_v1 = versi_1(A, B)
output_v2 = versi_2(A, B)
output_v3 = versi_3(A, B)

# --- 4. VOTING SYSTEM (Deteksi Error) ---
hasil_kolektif = [tuple(output_v1), tuple(output_v2), tuple(output_v3)]
voter = Counter(hasil_kolektif)
hasil_final, suara = voter.most_common(1)[0]

# --- OUTPUT ---
print("=== Hasil Representasi Program ===")
print(f"Input A      : {A}")
print(f"Input B      : {B}")
print(f"Instruksi    : C = A + B")
print("-" * 35)
print(f"Hasil Akhir  : {list(hasil_final)}")
print(f"Status Voting: {suara} dari 3 versi setuju")