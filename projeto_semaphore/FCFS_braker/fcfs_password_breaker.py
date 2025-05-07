import threading
import time
from queue import Queue

password_found = False
semaphores = []
ready_queue = Queue()
lock = threading.Lock()
current_thread = None


class PasswordBreakerFCFS(threading.Thread):
    def __init__(self, password, start_range, end_range, thread_id, quantum):
        super().__init__()
        self.password = password
        self.start_range = start_range
        self.end_range = end_range
        self.thread_id = thread_id
        self.quantum = quantum
        self.semaphore = threading.Semaphore(0)
        semaphores.append(self.semaphore)

    def run(self):
        global password_found, current_thread
        i = self.start_range

        while i < self.end_range and not password_found:
            self.semaphore.acquire()
            if password_found:
                return

            with lock:
                current_thread = self.thread_id

            for _ in range(self.quantum):
                if i >= self.end_range or password_found:
                    break

                attempt = f"{i:04}"
                print(f"Thread-{self.thread_id} tentando: {attempt}")
                time.sleep(0.001)

                if attempt == self.password:
                    with lock:
                        password_found = True
                    print(f"Senha encontrada: {attempt} por Thread-{self.thread_id}")
                    break

                i += 1

            with lock:
                current_thread = None
                if i < self.end_range and not password_found:
                    ready_queue.put(self.thread_id)


def fcfs_scheduler():
    global password_found
    while not password_found:
        if not ready_queue.empty():
            thread_id = ready_queue.get()
            semaphores[thread_id].release()
        time.sleep(0.001)
        
    for sem in semaphores:
        sem.release()


def fcfs_scheduler_runner(password, num_threads, quantum=5):
    global password_found, semaphores, current_thread
    password_found = False
    semaphores = []
    current_thread = None

    start_time = time.time()

    interval_size = 10000 // num_threads
    thread_ranges = [(i * interval_size, (i + 1) * interval_size) for i in range(num_threads)]

    threads = []
    for i in range(num_threads):
        start_range, end_range = thread_ranges[i]
        t = PasswordBreakerFCFS(password, start_range, end_range, i, quantum)
        threads.append(t)
        ready_queue.put(i)

    for t in threads:
        t.start()

    sched_thread = threading.Thread(target=fcfs_scheduler)
    sched_thread.start()

    for t in threads:
        t.join()
    sched_thread.join()

    end_time = time.time()
    print(f"\nTempo total (FCFS com Semáforo): {end_time - start_time:.2f} segundos\n")
