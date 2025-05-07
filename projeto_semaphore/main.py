from round_robin.rr_password_breaker import round_robin
from FCFS_braker.fcfs_password_breaker import fcfs_scheduler_runner

def main():
    print("\nQuebrador de senha com múltiplas estratégias\n")
    print("Escolha o algoritmo:")
    print("1 - Round Robin")
    print("2 - First-Come First-Served")

    choice = input("Opção (1 ou 2): ")
    while choice not in ['1', '2']:
        choice = input("Opção inválida. Escolha 1 ou 2: ")

    password = input("\nDigite a senha de 4 dígitos: ")
    while not password.isdigit() or len(password) != 4:
        password = input("Senha inválida. Digite uma senha de 4 dígitos: ")

    num_threads = int(input("Digite o número de threads: "))

    if choice == '1':
        quantum_size = int(input("Digite o tamanho do quantum: "))
        round_robin(password, num_threads, quantum_size)
    else:
        quantum_size = int(input("Digite o tamanho do quantum: "))
        fcfs_scheduler_runner(password, num_threads, quantum_size)

if __name__ == "__main__":
    main()
