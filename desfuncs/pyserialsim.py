
#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import serial
porta = str(input('Digite a porta em que esta conectada sua placa Arduino ')).upper()
ser = serial.Serial(porta)  # Abre uma porta

while True:
    
   
   
    ipo = str(input('Digite sair para feixar a porta ')).upper()

    
    if ipo == '0':
        ser.write(b'\x00')      # desliga r1


    elif ipo == '1':
        ser.write(b'\x01')     # liga r1


    if ipo == '2':
          ser.write(b'\x02')  # 
        


    elif ipo == '3':
        ser.write (b'\x03') 


    if ipo == '4':
        ser.write(b'\x04')  # Escreve 4 (liga o rele 3


    elif ipo == '5':
        ser.write (b'\x05') # Escreve 5 (desliga o rele 3


    if ipo == '6':
        ser.write(b'\x06')  # Escreve 6 Desliga o rele 4


    elif ipo == '7':
        ser.write (b'\x07') # Escreve 7 (liga o rele 4


    
    elif ipo == 'SAIR':
        ser.close()       # Fecha a porta
    
        break


