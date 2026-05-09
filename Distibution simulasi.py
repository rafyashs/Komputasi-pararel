# ============================================
#  STATIC UNEVEN DISTRIBUTION — NRP 152020042
#  NRP Genap → Static (tidak berubah saat runtime)
# ============================================

import numpy as np
import time

# Bobot statis tidak merata berdasarkan digit NRP
# NRP: 1-5-2-0-2-0-0-4-2  →  digit unik: [0,1,2,4,5]
NRP        = "152020042"
N_WORKERS  = 4           # jumlah worker/prosesor
TOTAL_TASK = 1000        # total task yang didistribusikan
TOLERANCE  = 0.05        # toleransi 5% dari distribusi ideal

# Bobot STATIS — ditentukan di awal, tidak berubah
STATIC_WEIGHTS = [0.40, 0.30, 0.20, 0.10]

def compute_ideal_distribution(total, n_workers):
    """Distribusi ideal = pembagian merata"""
    ideal = total / n_workers
    return [ideal] * n_workers

def static_distribute(total, weights):
    """Distribusikan task dengan bobot statis tidak merata"""
    tasks = [int(total * w) for w in weights]
    tasks[-1] += total - sum(tasks)   # sisa ke worker terakhir
    return tasks

def check_ideal_reached(distribution, ideal, tolerance):
    """Cek apakah distribusi sudah mendekati ideal"""
    for actual, exp in zip(distribution, ideal):
        deviation = abs(actual - exp) / exp
        if deviation > tolerance:
            return False
    return True

def simulate_convergence(total_tasks, weights, ideal, tol):
    """Simulasi iterasi hingga mencapai distribusi ideal
    dengan menyesuaikan bobot secara bertahap"""
    w = weights.copy()
    ideal_per = 1.0 / len(w)
    iteration = 0
    
    while True:
        dist = static_distribute(total_tasks, w)
        iteration += 1
        
        if check_ideal_reached(dist, ideal, tol):
            print(f"✅ Distribusi ideal tercapai pada iterasi {iteration}!")
            break
        
        # Geser bobot 5% mendekati ideal per iterasi
        w = [wi + 0.05 * (ideal_per - wi) for wi in w]
        w = [max(0.01, wi) for wi in w]   # min weight
        total_w = sum(w)
        w = [wi / total_w for wi in w]  # normalisasi
    
    return iteration, dist, w

# ── MAIN ──────────────────────────────────
ideal = compute_ideal_distribution(TOTAL_TASK, N_WORKERS)
dist  = static_distribute(TOTAL_TASK, STATIC_WEIGHTS)

print(f"NRP: {NRP}  →  Tipe: STATIC UNEVEN")
print(f"Distribusi awal : {dist}")
print(f"Distribusi ideal: {ideal}")

iter_done, final_dist, final_w = simulate_convergence(
    TOTAL_TASK, STATIC_WEIGHTS, ideal, TOLERANCE
)
print(f"Bobot akhir: {[round(w,4) for w in final_w]}")
print(f"Distribusi akhir: {final_dist}")