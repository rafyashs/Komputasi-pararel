import sys

# --- BAGIAN MOCK MPI (Hanya untuk simulasi tanpa instalasi) ---
class MockComm:
    def __init__(self, size=4):
        self.size = size
        self.rank = 0
        self.storage = {}

    def Get_rank(self): return self.rank
    def Get_size(self): return self.size
    
    def send(self, obj, dest, tag=0):
        print(f"[Simulasi] Rank {self.rank} mengirim ke Rank {dest}: {obj}")
        self.storage[dest] = obj

    def recv(self, source, tag=0):
        data = self.storage.get(self.rank, None)
        print(f"[Simulasi] Rank {self.rank} menerima data: {data}")
        return data

class MockMPI:
    COMM_WORLD = MockComm()

# Mencoba import asli, jika gagal gunakan Mock
try:
    from mpi4py import MPI
except ImportError:
    MPI = MockMPI
# -----------------------------------------------------------

# KODE UTAMA ANDA DIMULAI DI SINI
def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    print(f"Halo dari Rank {rank} dari total {size} proses.")

    if rank == 0:
        data = {'pesan': 'Halo dari pusat!'}
        # Simulasi kirim ke rank 1
        comm.send(data, dest=1)
    else:
        # Untuk simulasi sederhana, kita paksa rank 1 menerima
        comm.rank = 1 
        data = comm.recv(source=0)

if __name__ == "__main__":
    main()