import subprocess
import time
import datetime

print("Welcome to PING_PAN, a network diagnostic tool by Francesco Pannozzo")


hours = 0
minutes = 0
seconds = 0

CORRECT_CHOOSE = False
while not CORRECT_CHOOSE:
    hours = input("Enter the test duration hours (integer):")
    minutes = input("Enter the test duration minutes (integer):")
    seconds = 0
    try:
        if hours != 0:
            seconds = int(hours) * 3600
        if minutes != 0:
            seconds = seconds + (int(minutes) * 60)
        CORRECT_CHOOSE = True
    except ValueError:
        print("WARNING, the provided values (or one of them) are not integers, please retry")

print("Test starting..")
start_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
# Avvia il comando in background
process = subprocess.Popen(['ping', '-n', str(seconds), '8.8.8.8'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


cont = 0
output_lines = ""
while cont <= seconds+1:
    # Leggi una riga dall'output del comando
    line = process.stdout.readline()
    
    
    if line:
        # Aggiungi timestamp alla riga
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        formatted_line = f"[{timestamp}] {line.strip()}\n"
        print(f"[{timestamp}] {line.strip()}")  # Stampa l'output con data e ora
        output_lines = output_lines + formatted_line
        cont = cont + 1
            

# Attendi che il processo termini e cattura l'output
stdout, stderr = process.communicate()

# Mostra l'output
print(stdout)
print(stderr)

# Scrivi l'output in un file
with open(f'ping_output_{start_time}.txt', 'w') as file:
    file.write(output_lines)
    file.write(stdout)

input("Press any key to continue..")