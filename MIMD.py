import numpy as np
import threading
from collections import Counter

# --- DATA INPUT (Digunakan oleh semua versi) ---
A = np.array([10, 20, 30, 40])
B = np.array([5, 15, 25, 35])

# --- 1. REPRESENTASI SISD (Linear & Sekuensial) ---
def versi_sisd(a, b):
    # Kelebihan: Sederhana & Deterministik. Kekurangan: Bottleneck
    hasil = []
    for i in range(len(a)):
        hasil.append(a[i] + b[i])
    return tuple(hasil)

# --- 2. REPRESENTASI SIMD (Paralel Sinkronus) ---
def versi_simd(a, b):
    # Instruksi tunggal C = A + B dijalankan paralel pada semua data
    hasil = a + b
    return tuple(hasil)

# --- 3. REPRESENTASI MIMD (Asinkronus & Fleksibel) ---
# Menggunakan threading untuk mensimulasikan eksekusi asinkronus
hasil_mimd = []
def versi_mimd(a, b):
    def hitung_parsial(val1, val2):
        hasil_mimd.append(val1 + val2)
    
    threads = []
    for i in range(len(a)):
        t = threading.Thread(target=hitung_parsial, args=(a[i], b[i]))
        threads.append(t)
        t.start()
    
    for t in threads: t.join()
    return tuple(hasil_mimd)

# --- 4. N-VERSION PROGRAMMING & VOTING ---
def jalankan_n_version():
    # Menjalankan N-versi independen secara paralel
    v1 = versi_sisd(A, B)
    v2 = versi_simd(A, B)
    v3 = versi_mimd(A, B)
    
    koleksi_hasil = [v1, v2, v3]
    
    # Mekanisme Voting untuk mendeteksi error
    voter = Counter(koleksi_hasil)
    hasil_final, jumlah_suara = voter.most_common(1)[0]
    
    print("--- HASIL EKSEKUSI ---")
    print(f"Versi SISD: {v1}")
    print(f"Versi SIMD: {v2}")
    print(f"Versi MIMD: {v3}")
    print("-" * 25)
    print(f"Hasil Akhir (Voting): {hasil_final}")
    print(f"Status: Valid dengan {jumlah_suara} dari 3 suara setuju.")

if __name__ == "__main__":
    jalankan_n_version()