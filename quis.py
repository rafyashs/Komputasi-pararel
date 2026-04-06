import multiprocessing
import time

def square_numbers(data_chunk, process_id, result_dict):
    print(f"[Process {process_id}] Mengerjakan data: {data_chunk}")
    results = []
    for num in data_chunk:
        time.sleep(0.3)
        results.append(num ** 2)
    result_dict[process_id] = results
    print(f"[Process {process_id}] Selesai -> Hasil: {results}")  # ganti -> bukan panah unicode


if __name__ == "__main__":
    full_data = list(range(1, 17))
    num_processes = 4

    chunk_size = len(full_data) // num_processes
    chunks = [full_data[i * chunk_size:(i + 1) * chunk_size]
              for i in range(num_processes)]

    print("=" * 55)
    print("       DATA PARALLELISM - Rafyasha Hafizh Hakeem")
    print("=" * 55)
    print(f"Data lengkap  : {full_data}")
    print(f"Jumlah proses : {num_processes}")
    for i, chunk in enumerate(chunks):
        print(f"  Proses {i}     : {chunk}")
    print("-" * 55)

    manager = multiprocessing.Manager()
    result_dict = manager.dict()

    processes = []
    start_time = time.time()

    for i, chunk in enumerate(chunks):
        p = multiprocessing.Process(
            target=square_numbers,
            args=(chunk, i, result_dict)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    elapsed = time.time() - start_time

    final_result = []
    for i in range(num_processes):
        final_result.extend(result_dict[i])

    print("-" * 55)
    print(f"Input awal    : {full_data}")
    print(f"Hasil kuadrat : {final_result}")
    print(f"Waktu paralel : {elapsed:.2f} detik")
    print("=" * 55)