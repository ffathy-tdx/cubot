import serial
import time
import kociemba

arduino = serial.Serial('/dev/ttyACM0', 9600)



time.sleep(2)

solution = kociemba.solve('UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB')
print('Solution:', solution)

solution = solution.replace("'", "").lower()

# Send commands to Arduino
for move in solution.split():
    command = move[0]
    count = int(move[1:]) if len(move) > 1 else 1
    print(count)

    for i in range(count):
        print(command)
        command_bytes = str.encode(command)
        arduino.write(command_bytes)
        time.sleep(0.1)


arduino.close()