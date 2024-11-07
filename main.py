import subprocess
import time
import datetime

hours = input("Inserisci numero di ore di esecuzione del ping:")
minutes = input("Inserisci numero di minuti di esecuzione del ping:")
seconds = 0

if hours != 0:
    seconds = int(hours) * 3600
if minutes != 0:
    seconds = seconds + (int(minutes) * 60)

print("Avvio test..")
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

input("premi un qualsiasi tasto per chiudere")