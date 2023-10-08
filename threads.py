import threading
import time

# Funkcja, która będzie wykonywana w wątku
def print_numbers():
    for i in range(5):
        print(f'Wątek "print_numbers": {i}')
        time.sleep(1)

# Utworzenie wątku
thread1 = threading.Thread(target=print_numbers)

# Uruchomienie wątku
thread1.start()

# Główny kod będzie kontynuowany niezależnie od wątku
for letter in 'abcde':
    print(f'Główny wątek: {letter}')
    time.sleep(1)

# Poczekaj na zakończenie wątku
thread1.join()

print('Koniec programu')
