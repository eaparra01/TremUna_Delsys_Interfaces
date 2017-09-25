# Simple Gui
# Create window

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from ConnectionTremuna_1_2 import *
from PIL import ImageTk, Image
import threading
import queue

# Main layout
root = Tk()
root.geometry ("1250x500")
root.title ("Interface para la conexión con el dispositivo TREMUNA")

menubar = Menu(root)
filemenu = Menu(menubar)
submenu = Menu(menubar)

topFrame = Frame (root)
bottomFrame = Frame (root)
topFrame.pack (side=TOP)
bottomFrame.pack (side=BOTTOM)
#
Tremuna = ConnectionTremuna_1_2()    # Crea el objeto Tremuna de la clase ConnectionTremina
portsUSB = Tremuna.scanDevice()  # Busca los puertos que están conectados y de vuelve una lista con los puertos

img1 = ImageTk.PhotoImage(Image.open("CSIC_resize.jpg"))
img2 = ImageTk.PhotoImage(Image.open("upm_logo_resize.png"))
img3 = ImageTk.PhotoImage(Image.open("CAR.jpg"))

## Variables

Therapytype1 = BooleanVar()
Therapytype2 = BooleanVar()
Therapytype3 = BooleanVar()

qState = queue.Queue()

Therapytype1.set(True)
Therapytype2.set(False)
Therapytype3.set(False)

RunStep = StringVar()
RunStep.set('0')

varString1 = StringVar ()

varString2 = StringVar ()  # Variable del ButtonRadio

varString3 = StringVar ()
varString4 = StringVar ()
varString5 = StringVar ()
varString6 = StringVar ()
varString7 = StringVar ()
varString8 = StringVar ()
varString9 = StringVar ()

varString10 = StringVar ()
varString11 = StringVar ()
varString12 = StringVar ()
varString13 = StringVar ()
varString14 = StringVar ()
varString15 = StringVar ()
varString16 = StringVar ()

varStringTitle = StringVar ()  # Nombre variable PN 8

varStringNameMuscle = StringVar ()
varStringStateDevice = StringVar ()
varStringOnDevice = StringVar ()
varStringOffDevice = StringVar ()
varStringTherapy = StringVar ()

varString17 = StringVar ()  # Variable de CheckBox1
varString18 = StringVar ()  # Variable de CheckBox2
varString19 = StringVar ()  # Variable de CheckBox3
varString20 = StringVar ()  # Variable de CheckBox4
varString21 = StringVar ()  # Variable de CheckBox5
varString22 = StringVar ()  # Variable de CheckBox6
varString23 = StringVar ()  # Variable de CheckBox7
varString24 = StringVar ()  # Variable de CheckBox8

varString25 = StringVar ()  # Nombre Canal 1
varString26 = StringVar ()  # Nombre Canal 2
varString27 = StringVar ()  # Nombre Canal 3
varString28 = StringVar ()  # Nombre Canal 4
varString29 = StringVar ()  # Nombre Canal 5
varString30 = StringVar ()  # Nombre Canal 6
varString31 = StringVar ()  # Nombre Canal 7
varString32 = StringVar ()  # Nombre Canal 8

varStringCurrent1 = StringVar ()  # Nombre variable corriente 1
varStringCurrent2 = StringVar ()  # Nombre variable corriente 2
varStringCurrent3 = StringVar ()  # Nombre variable corriente 3
varStringCurrent4 = StringVar ()  # Nombre variable corriente 4
varStringCurrent5 = StringVar ()  # Nombre variable corriente 5
varStringCurrent6 = StringVar ()  # Nombre variable corriente 6
varStringCurrent7 = StringVar ()  # Nombre variable corriente 7
varStringCurrent8 = StringVar ()  # Nombre variable corriente 8

varStringFrequency1 = StringVar ()  # Nombre variable Frecuencia 1
varStringFrequency2 = StringVar ()  # Nombre variable Frecuencia 2
varStringFrequency3 = StringVar ()  # Nombre variable Frecuencia 3
varStringFrequency4 = StringVar ()  # Nombre variable Frecuencia 4
varStringFrequency5 = StringVar ()  # Nombre variable Frecuencia 5
varStringFrequency6 = StringVar ()  # Nombre variable Frecuencia 6
varStringFrequency7 = StringVar ()  # Nombre variable Frecuencia 7
varStringFrequency8 = StringVar ()  # Nombre variable Frecuencia 8

varStringPW1 = StringVar ()  # Nombre variable PW 1
varStringPW2 = StringVar ()  # Nombre variable PW 2
varStringPW3 = StringVar ()  # Nombre variable PW 3
varStringPW4 = StringVar ()  # Nombre variable PW 4
varStringPW5 = StringVar ()  # Nombre variable PW 5
varStringPW6 = StringVar ()  # Nombre variable PW 6
varStringPW7 = StringVar ()  # Nombre variable PW 7
varStringPW8 = StringVar ()  # Nombre variable PW 8

varStringDT1 = StringVar ()  # Nombre variable DT 1
varStringDT2 = StringVar ()  # Nombre variable DT 2
varStringDT3 = StringVar ()  # Nombre variable DT 3
varStringDT4 = StringVar ()  # Nombre variable DT 4
varStringDT5 = StringVar ()  # Nombre variable DT 5
varStringDT6 = StringVar ()  # Nombre variable DT 6
varStringDT7 = StringVar ()  # Nombre variable DT 7
varStringDT8 = StringVar ()  # Nombre variable DT 8

varStringPN1 = StringVar ()  # Nombre variable PN 1
varStringPN2 = StringVar ()  # Nombre variable PN 2
varStringPN3 = StringVar ()  # Nombre variable PN 3
varStringPN4 = StringVar ()  # Nombre variable PN 4
varStringPN5 = StringVar ()  # Nombre variable PN 5
varStringPN6 = StringVar ()  # Nombre variable PN 6
varStringPN7 = StringVar ()  # Nombre variable PN 7
varStringPN8 = StringVar ()  # Nombre variable PN 8

varStringEMG1 = StringVar ()  # Nombre variable EMG 1
varStringEMG2 = StringVar ()  # Nombre variable EMG 2
varStringEMG3 = StringVar ()  # Nombre variable EMG 3
varStringEMG4 = StringVar ()  # Nombre variable EMG 4
varStringEMG5 = StringVar ()  # Nombre variable EMG 5
varStringEMG6 = StringVar ()  # Nombre variable EMG 6
varStringEMG7 = StringVar ()  # Nombre variable EMG 7
varStringEMG8 = StringVar ()  # Nombre variable EMG 8

varStringACC1 = StringVar ()  # Nombre variable EMG 8

varString1.set ("Puerto de Conexión")
varString2.set ("0")         # Variable de ButtonRadio que dice para configurar un canal o varios
varString3.set ("Seleccione el Canal a Configurar")

varString4.set ("Conf. Mascara")
varString5.set ("Conf. Corriente")
varString6.set ("Conf. Frecuencia [Hz]")
varString7.set ("Conf. PW [us]")
varString8.set ("DT [ms]")
varString9.set ("PN")

varStringTitle.set('Ingrese Nombre del Archivo')

varString10.set ("Habilitar")
varString11.set ("Canal")
varString12.set ("Corriente [mA]")
varString13.set ("Frecu. [Hz]")
varString14.set ("PW [us]")
varString15.set ("DT [ms]")
varString16.set ("PN")

varStringNameMuscle.set ("Nombre del Músculo")
varStringStateDevice.set('Dispositivo Desconectado')
varStringOnDevice.set('¡Dispositivo Encendido!')
varStringOffDevice.set('¡Dispositivo Apagado!')
varStringTherapy.set("Control desde el dispositivo EMG Directo")


varString17.set ("0")  # Valores iniciales de del Check Box Canal 1
varString18.set ("0")  # Valores iniciales de del Check Box Canal 2
varString19.set ("0")  # Valores iniciales de del Check Box Canal 3
varString20.set ("0")  # Valores iniciales de del Check Box Canal 4
varString21.set ("0")  # Valores iniciales de del Check Box Canal 5
varString22.set ("0")  # Valores iniciales de del Check Box Canal 6
varString23.set ("0")  # Valores iniciales de del Check Box Canal 7
varString24.set ("0")  # Valores iniciales de del Check Box Canal 8

varString25.set ("Canal 1")
varString26.set ("Canal 2")
varString27.set ("Canal 3")
varString28.set ("Canal 4")
varString29.set ("Canal 5")
varString30.set ("Canal 6")
varString31.set ("Canal 7")
varString32.set ("Canal 8")

varStringCurrent1.set ("0")  # Valores iniciales de Corriente Canal 1
varStringCurrent2.set ("0")  # Valores iniciales de Corriente Canal 2
varStringCurrent3.set ("0")  # Valores iniciales de Corriente Canal 3
varStringCurrent4.set ("0")  # Valores iniciales de Corriente Canal 4
varStringCurrent5.set ("0")  # Valores iniciales de Corriente Canal 5
varStringCurrent6.set ("0")  # Valores iniciales de Corriente Canal 6
varStringCurrent7.set ("0")  # Valores iniciales de Corriente Canal 7
varStringCurrent8.set ("0")  # Valores iniciales de Corriente Canal 8

varStringFrequency1.set ("0")  # Valores iniciales de Frecuenca Canal 1
varStringFrequency2.set ("0")  # Valores iniciales de Frecuenca Canal 1
varStringFrequency3.set ("0")  # Valores iniciales de Frecuenca Canal 1
varStringFrequency4.set ("0")  # Valores iniciales de Frecuenca Canal 1
varStringFrequency5.set ("0")  # Valores iniciales de Frecuenca Canal 1
varStringFrequency6.set ("0")  # Valores iniciales de Frecuenca Canal 1
varStringFrequency7.set ("0")  # Valores iniciales de Frecuenca Canal 1
varStringFrequency8.set ("0")  # Valores iniciales de Frecuenca Canal 1

varStringPW1.set ("0")  # Valores inicial de PW Canal 1
varStringPW2.set ("0")  # Valores inicial de PW Canal 2
varStringPW3.set ("0")  # Valores inicial de PW Canal 3
varStringPW4.set ("0")  # Valores inicial de PW Canal 4
varStringPW5.set ("0")  # Valores inicial de PW Canal 5
varStringPW6.set ("0")  # Valores inicial de PW Canal 6
varStringPW7.set ("0")  # Valores inicial de PW Canal 7
varStringPW8.set ("0")  # Valores inicial de PW Canal 8

varStringDT1.set ("0")  # Valores inicial de DT Canal 1
varStringDT2.set ("0")  # Valores inicial de DT Canal 2
varStringDT3.set ("0")  # Valores inicial de DT Canal 3
varStringDT4.set ("0")  # Valores inicial de DT Canal 4
varStringDT5.set ("0")  # Valores inicial de DT Canal 5
varStringDT6.set ("0")  # Valores inicial de DT Canal 6
varStringDT7.set ("0")  # Valores inicial de DT Canal 7
varStringDT8.set ("0")  # Valores inicial de DT Canal 8

varStringPN1.set ("0")  # Valores inicial de PN Canal 1
varStringPN2.set ("0")  # Valores inicial de PN Canal 1
varStringPN3.set ("0")  # Valores inicial de PN Canal 1
varStringPN4.set ("0")  # Valores inicial de PN Canal 1
varStringPN5.set ("0")  # Valores inicial de PN Canal 1
varStringPN6.set ("0")  # Valores inicial de PN Canal 1
varStringPN7.set ("0")  # Valores inicial de PN Canal 1
varStringPN8.set ("0")  # Valores inicial de PN Canal 1

varStringEMG1.set('0') # Valores iniciales de EMG 1
varStringEMG2.set('0') # Valores iniciales de EMG 2
varStringEMG3.set('0') # Valores iniciales de EMG 3
varStringEMG4.set('0') # Valores iniciales de EMG 4
varStringEMG5.set('0') # Valores iniciales de EMG 5
varStringEMG6.set('0') # Valores iniciales de EMG 6
varStringEMG7.set('0') # Valores iniciales de EMG 7
varStringEMG8.set('0') # Valores iniciales de EMG 8

varStringACC1.set('0')

# Functiones

# Se conecta con el dispositivo
def connectDevice():
    Tremuna.portNumber = listbox1.get(ACTIVE)
    print ('Se conectará al puerto %s' % Tremuna.portNumber)
    print (listbox1.get(ACTIVE))
    connect=Tremuna.ConnectDevice()
    if connect == '>OK<':
        button1.config(relief=SUNKEN)
        varStringStateDevice.set('Dispositivo Conectado')
        labelStateDevice.config(bg='lawn green')
    else:
        button1.config(relief=RAISED)
        varStringStateDevice.set('Dispositivo Desconectado')
        labelStateDevice.config(bg='gray99')
        messagebox.showwarning('Fallo en conexión con el computador',
                           'No se puede establer conexión con el TREMUNA y el computador. Busque el puerto en la casilla de Puerto de Conexión. Sino se conecta cierre y vuelva abrir el programa, cerciorandose que con anterioridad está el dipositivo conectado y encendido')

    #conectionPort = Tremuna.ConnectDevice
    #return conectionPort
    pass
    # Se desconecta con el dispositivo

def disconnectDevice():
    button1.config(relief=RAISED)
    varStringStateDevice.set('Dispositivo Desconectado')
    labelStateDevice.config(bg='gray99')
    labelOnDevice.place_forget()
    turnOFF()
    Tremuna.portNumber = listbox1.get (ACTIVE)
    print ('Se desconectará al puerto %s' % Tremuna.portNumber)
    print (listbox1.get (ACTIVE))
    Tremuna.DisonnectDevice()
    Tremuna.sINTERAPPS_EMG.close()
    Tremuna.sINTERAPPS_ACC.close()
    pass

def activateChannels(): # Por ahora no modifica ningún dato de Configuración al enviar el sendData

    rButtonChannel = int (varString2.get())
    #Tremuna.maskReceived = maskEntry
    #Tremuna.currentReceived = currentEntry
    #Tremuna.frequencyReceived = frequencyEntry
    #Tremuna.pwReceived = (pwEntry).to_bytes (2, byteorder='big')    #(pwEntry).to_bytes (2, byteorder='big')
    #Tremuna.dtReceived = (dtEntry).to_bytes (2, byteorder='big')    #(dtEntry).to_bytes (2, byteorder='big')
    #Tremuna.pnReceived = (pnEntry).to_bytes (2, byteorder='big')    #(pnEntry).to_bytes (2, byteorder='big')
    #Tremuna.pnReceived = numpy.uint16(pnEntry)
    if rButtonChannel == 1:
        spinBoxChannel = int(spinbox1.get ())
        Tremuna.canalInt = int(spinbox1.get())
        print ("Se escogio el canal %d" %Tremuna.canalInt)
        canalsArrayBits = {1: ['0', '0', '0', '0', '0', '0', '0', '1'],
                           2: ['0', '0', '0', '0', '0', '0', '1', '0'],
                           3: ['0', '0', '0', '0', '0', '1', '0', '0'],
                           4: ['0', '0', '0', '0', '1', '0', '0', '0'],
                           5: ['0', '0', '0', '1', '0', '0', '0', '0'],
                           6: ['0', '0', '1', '0', '0', '0', '0', '0'],
                           7: ['0', '1', '0', '0', '0', '0', '0', '0'],
                           8: ['1', '0', '0', '0', '0', '0', '0', '0']}
        #print(canalsArrayBits[spinBoxChannel])
        Tremuna.canalsArrayBits = canalsArrayBits[spinBoxChannel]

        #print(spinBoxChannel)
        #print (Tremuna.canalsArrayBits)
        Tremuna.MaskData()

        for i in range(0,8):
            if i==spinBoxChannel-1:
                labelActive[i].config(bg='lawn green')
            else:
                labelActive[i].config(bg='gray95')
        # print("Optición por canal Escogido")

    elif rButtonChannel == 2 or rButtonChannel == 3:
        print (varString2.get ())
        canalsArrayBits = [varString24.get (), varString23.get (), varString22.get (), varString21.get (),
                           varString20.get (), varString19.get (), varString18.get (), varString17.get ()]
        Tremuna.canalsArrayBits = canalsArrayBits
        Tremuna.MaskData()
        print(canalsArrayBits)

        for i in range(0,8):
            if canalsArrayBits[i]=='1':
                labelActive[7-i].config(bg='lawn green')
            else:
                labelActive[7-i].config(bg='gray95')

    else:
        print ("Seleccione una opción para la configuración de los Canales")
        Tremuna.DisonnectDevice()

    pass

def turnON():
    OnOff = Tremuna.TurnOnDevice()
    if OnOff == '>OK<':
        button5.config(relief=SUNKEN)
        labelOnDevice.place(x=260, y=275)
        labelOffDevice.place_forget()
    else:
        button5.config(relief=RAISED)
        labelOnDevice.place_forget()
        labelOffDevice.place(x=260, y=372)
    pass

def turnOFF():
    Tremuna.flag=False
    button5.config(relief=RAISED)
    buttonConnectionDelsys.config(relief=RAISED)
    labelOnDevice.place_forget()
    labelOffDevice.place(x=260, y=342)
    Tremuna.TurnOffDevice()
    print(RunStep.get())
    if RunStep.get() == '3':
        ConfigurationOption2()
        varString2.set('2')
    pass

# Función que modifica la corriente, primero modifica la variable de la interfaz y luego se lo envía a la variable del
# de la clase Tremuna se utiliza por ahora con el widget 1
def currentModified():
    print("Se modificó sólo la corriente ")
#    if varString2.get()=='1':
#        currentEntry = int (currentSpinbox.get ())
#    elif varString2.get()=='2':
#        currentEntry = int(entry2.get())
    currentEntry = int(currentSpinbox.get())
    Tremuna.canalInt = int(spinbox1.get())
    #Tremuna.currentReceived = currentEntry
    if spinbox1.get () =='1':
        varStringCurrent1.set(str(currentEntry))
        Tremuna.currentReceived = int(varStringCurrent1.get())
    elif spinbox1.get () =='2':
        varStringCurrent2.set (str (currentEntry))
        Tremuna.currentReceived = int (varStringCurrent2.get ())
    elif spinbox1.get () == '3':
        varStringCurrent3.set (str (currentEntry))
        Tremuna.currentReceived = int (varStringCurrent3.get ())
    elif spinbox1.get () == '4':
        varStringCurrent4.set (str (currentEntry))
        Tremuna.currentReceived = int (varStringCurrent4.get ())
    elif spinbox1.get () == '5':
        varStringCurrent5.set (str (currentEntry))
        Tremuna.currentReceived = int (varStringCurrent5.get ())
    elif spinbox1.get () == '6':
        varStringCurrent6.set (str (currentEntry))
        Tremuna.currentReceived = int (varStringCurrent6.get ())
    elif spinbox1.get () == '7':
        varStringCurrent7.set (str (currentEntry))
        Tremuna.currentReceived = int (varStringCurrent7.get ())
    elif spinbox1.get () == '8':
        varStringCurrent8.set (str (currentEntry))
        Tremuna.currentReceived = int (varStringCurrent8.get ())

    Tremuna.CurrentData()
    pass

#def spinboxCurrentValues():
#    Tremuna.canalInt = int(spinbox1.get ())
#    currentEntry = int (currentSpinbox.get ())
#    Tremuna.currentReceived = currentEntry
#    current = Tremuna.CurrentData ()
#    print (current)
#    if spinbox1.get () == '1':
#        varStringCurrent1.set (str (currentEntry))
#    elif spinbox1.get () == '2':
#        varStringCurrent2.set (str (currentEntry))
#    elif spinbox1.get () == '3':
#        varStringCurrent3.set (str (currentEntry))
#    elif spinbox1.get () == '4':
#        varStringCurrent4.set (str (currentEntry))
#    elif spinbox1.get () == '5':
#        varStringCurrent5.set (str (currentEntry))
#    elif spinbox1.get () == '6':
#        varStringCurrent6.set (str (currentEntry))
#    elif spinbox1.get () == '7':
#        varStringCurrent7.set (str (currentEntry))
#    elif spinbox1.get () == '8':
#        varStringCurrent8.set (str (currentEntry))
#    pass

#   pass

def frequencyModified():
    print("Se modificó sólo la frecuencia")
    frequencyEntry = int(frequencySpinbox.get())
#    frequencyEntry = int (entry3.get ())
#    Tremuna.frequencyReceived = frequencyEntry
    Tremuna.canalInt = int (spinbox1.get ())

    if spinbox1.get () =='1':
        varStringFrequency1.set(str(frequencyEntry))
        Tremuna.frequencyReceived = int(varStringFrequency1.get())
    elif spinbox1.get () =='2':
        varStringFrequency2.set (str (frequencyEntry))
        Tremuna.frequencyReceived = int (varStringFrequency2.get ())
    elif spinbox1.get () == '3':
        varStringFrequency3.set (str (frequencyEntry))
        Tremuna.frequencyReceived = int (varStringFrequency3.get ())
    elif spinbox1.get () == '4':
        varStringFrequency4.set (str (frequencyEntry))
        Tremuna.frequencyReceived = int (varStringFrequency4.get ())
    elif spinbox1.get () == '5':
        varStringFrequency5.set (str (frequencyEntry))
        Tremuna.frequencyReceived = int (varStringFrequency5.get ())
    elif spinbox1.get () == '6':
        varStringFrequency6.set (str (frequencyEntry))
        Tremuna.frequencyReceived = int (varStringFrequency6.get ())
    elif spinbox1.get () == '7':
        varStringFrequency7.set (str (frequencyEntry))
        Tremuna.frequencyReceived = int (varStringFrequency7.get ())
    elif spinbox1.get () == '8':
        varStringFrequency8.set (str (frequencyEntry))
        Tremuna.frequencyReceived = int (varStringFrequency8.get ())
    frequency = Tremuna.FrequencyData ()
    print (frequency)
    pass

def pwModified():
    print("Se modificó sólo el PW")
    pwEntry = int(pwSpinbox.get())
#    pwEntry = int (entry4.get ())
    Tremuna.canalInt = int (spinbox1.get())
    #Tremuna.pwReceived = (pwEntry).to_bytes (2, byteorder='big')

    if spinbox1.get () =='1':
        varStringPW1.set(str(pwEntry))
        Tremuna.pwReceived = (int(varStringPW1.get())).to_bytes (2, byteorder='big')
    elif spinbox1.get () =='2':
        varStringPW2.set (str (pwEntry))
        Tremuna.pwReceived = (int (varStringPW2.get())).to_bytes (2, byteorder='big')
    elif spinbox1.get () == '3':
        varStringPW3.set (str (pwEntry))
        Tremuna.pwReceived = (int (varStringPW3.get())).to_bytes (2, byteorder='big')
    elif spinbox1.get () == '4':
        varStringPW4.set (str (pwEntry))
        Tremuna.pwReceived = (int (varStringPW4.get())).to_bytes (2, byteorder='big')
    elif spinbox1.get () == '5':
        varStringPW5.set (str (pwEntry))
        Tremuna.pwReceived = (int (varStringPW5.get())).to_bytes (2, byteorder='big')
    elif spinbox1.get () == '6':
        varStringPW6.set (str (pwEntry))
        Tremuna.pwReceived = (int (varStringPW6.get())).to_bytes (2, byteorder='big')
    elif spinbox1.get () == '7':
        varStringPW7.set (str (pwEntry))
        Tremuna.pwReceived = (int (varStringPW7.get())).to_bytes (2, byteorder='big')
    elif spinbox1.get () == '8':
        varStringPW8.set (str (pwEntry))
        Tremuna.pwReceived = (int (varStringPW8.get())).to_bytes (2, byteorder='big')
    pw = Tremuna.PWData ()
    print(pw)
    pass

def dtModified():
    print("Se modificó sólo el DT")
    dtEntry = int (dtSpinbox.get())
#    dtEntry = int (entry5.get())
#    Tremuna.dtReceived = (dtEntry).to_bytes(2, byteorder='big')
    Tremuna.canalInt = int(spinbox1.get())

    if spinbox1.get () =='1':
        varStringDT1.set(str(dtEntry))
        Tremuna.dtReceived = (int(varStringDT1.get())).to_bytes (2, byteorder='big')
    elif spinbox1.get () =='2':
        varStringDT2.set (str (dtEntry))
        Tremuna.dtReceived = (int (varStringDT2.get ())).to_bytes (2, byteorder='big')
    elif spinbox1.get () == '3':
        varStringDT3.set (str (dtEntry))
        Tremuna.dtReceived = (int (varStringDT3.get ())).to_bytes (2, byteorder='big')
    elif spinbox1.get () == '4':
        varStringDT4.set (str (dtEntry))
        Tremuna.dtReceived = (int (varStringDT4.get ())).to_bytes (2, byteorder='big')
    elif spinbox1.get () == '5':
        varStringDT5.set (str (dtEntry))
        Tremuna.dtReceived = (int (varStringDT5.get ())).to_bytes (2, byteorder='big')
    elif spinbox1.get () == '6':
        varStringDT6.set (str (dtEntry))
        Tremuna.dtReceived = (int (varStringDT6.get ())).to_bytes (2, byteorder='big')
    elif spinbox1.get () == '7':
        varStringDT7.set (str (dtEntry))
        Tremuna.dtReceived = (int (varStringDT7.get ())).to_bytes (2, byteorder='big')
    elif spinbox1.get () == '8':
        varStringDT8.set (str (dtEntry))
        Tremuna.dtReceived = (int (varStringDT8.get ())).to_bytes (2, byteorder='big')
    dt = Tremuna.DTData()
    print(dt)
    pass

def pnModified():
    print("Se modificó sólo el PN")
    pnEntry = int(pnSpinbox.get())
    #pnEntry = int (entry6.get())
    Tremuna.canalInt = int(spinbox1.get())
#    Tremuna.pnReceived = (pnEntry).to_bytes(2, byteorder='big')

#    canalsArrayBits = {1: ['0', '0', '0', '0', '0', '0', '0', '1'],
#                       2: ['0', '0', '0', '0', '0', '0', '1', '0'],
#                       3: ['0', '0', '0', '0', '0', '1', '0', '0'],
#                       4: ['0', '0', '0', '0', '1', '0', '0', '0'],
#                       5: ['0', '0', '0', '1', '0', '0', '0', '0'],
#                       6: ['0', '0', '1', '0', '0', '0', '0', '0'],
#                       7: ['0', '1', '0', '0', '0', '0', '0', '0'],
#                       8: ['1', '0', '0', '0', '0', '0', '0', '0']}
#    Tremuna.canalsArrayBits = canalsArrayBits[Tremuna.canalInt]
#    mask = Tremuna.MaskData()
 #   print (mask)
    if spinbox1.get () =='1':
        varStringPN1.set(str(pnEntry))
        Tremuna.pnReceived = (int(varStringPN1.get())).to_bytes(2, byteorder='big')
    elif spinbox1.get () =='2':
        varStringPN2.set (str (pnEntry))
        Tremuna.pnReceived = (int (varStringPN2.get())).to_bytes (2, byteorder='big')
    elif spinbox1.get () == '3':
        varStringPN3.set (str (pnEntry))
        Tremuna.pnReceived = (int (varStringPN3.get())).to_bytes (2, byteorder='big')
    elif spinbox1.get () == '4':
        varStringPN4.set (str (pnEntry))
        Tremuna.pnReceived = (int (varStringPN4.get())).to_bytes (2, byteorder='big')
    elif spinbox1.get () == '5':
        varStringPN5.set (str (pnEntry))
        Tremuna.pnReceived = (int (varStringPN5.get())).to_bytes (2, byteorder='big')
    elif spinbox1.get () == '6':
        varStringPN6.set (str (pnEntry))
        Tremuna.pnReceived = (int (varStringPN6.get())).to_bytes (2, byteorder='big')
    elif spinbox1.get () == '7':
        varStringPN7.set (str (pnEntry))
        Tremuna.pnReceived = (int (varStringPN7.get())).to_bytes (2, byteorder='big')
    elif spinbox1.get () == '8':
        varStringPN8.set (str (pnEntry))
        Tremuna.pnReceived = (int (varStringPN8.get())).to_bytes (2, byteorder='big')
    pn = Tremuna.PNData ()
    print (pn)
    pass

def spinboxCanalValues():       # Toma el valor de las variables de cada canal y los refresca en el spinbox y entries
    if spinbox1.get()=='1':
        varString17.set('1')
        varString18.set('0')
        varString19.set('0')
        varString20.set('0')
        varString21.set('0')
        varString22.set('0')
        varString23.set('0')
        varString24.set('0')
        entry2.delete(0,5)
        entry2.insert(0, varStringCurrent1.get())
        currentSpinbox.delete(0,END)
        currentSpinbox.insert(0,varStringCurrent1.get())
        entry3.delete(0,5)
        entry3.insert(0,varStringFrequency1.get())
        frequencySpinbox.delete(0,END)
        frequencySpinbox.insert(0,varStringFrequency1.get())
        entry4.delete(0,5)
        entry4.insert(0,varStringPW1.get())
        pwSpinbox.delete(0,END)
        pwSpinbox.insert(0,varStringPW1.get())
        entry5.delete(0,5)
        entry5.insert(0,varStringDT1.get())
        dtSpinbox.delete(0,END)
        dtSpinbox.insert(0,varStringDT1.get())
        entry6.delete(0,5)
        entry6.insert(0,varStringPN1.get())
        pnSpinbox.delete(0,END)
        pnSpinbox.insert(0,varStringPN1.get())
    elif spinbox1.get()=='2':
        varString17.set('0')
        varString18.set('1')
        varString19.set('0')
        varString20.set('0')
        varString21.set('0')
        varString22.set('0')
        varString23.set('0')
        varString24.set('0')
        entry2.delete(0,6)
        entry2.insert(0,varStringCurrent2.get())
        currentSpinbox.delete(0,END)
        currentSpinbox.insert(0,varStringCurrent2.get())
        entry3.delete (0,6)
        entry3.insert(0,varStringFrequency2.get())
        frequencySpinbox.delete (0,END)
        frequencySpinbox.insert (0,varStringFrequency2.get())
        entry4.delete (0,6)
        entry4.insert(0,varStringPW2.get())
        pwSpinbox.delete(0,END)
        pwSpinbox.insert(0,varStringPW2.get ())
        entry5.delete (0,6)
        entry5.insert(0,varStringDT2.get())
        dtSpinbox.delete (0,END)
        dtSpinbox.insert (0,varStringDT2.get())
        entry6.delete (0,6)
        entry6.insert(0,varStringPN2.get())
        pnSpinbox.delete (0, END)
        pnSpinbox.insert (0, varStringPN2.get ())
    elif spinbox1.get()=='3':
        varString17.set('0')
        varString18.set('0')
        varString19.set('1')
        varString20.set('0')
        varString21.set('0')
        varString22.set('0')
        varString23.set('0')
        varString24.set('0')
        entry2.delete(0,6)
        entry2.insert(0,varStringCurrent3.get())
        currentSpinbox.delete (0, END)
        currentSpinbox.insert (0, varStringCurrent3.get ())
        entry3.delete (0,6)
        entry3.insert(0,varStringFrequency3.get())
        frequencySpinbox.delete(0,END)
        frequencySpinbox.insert(0,varStringFrequency3.get())
        entry4.delete (0,6)
        entry4.insert(0,varStringPW3.get())
        pwSpinbox.delete(0,END)
        pwSpinbox.insert(0,varStringPW3.get())
        entry5.delete (0,6)
        entry5.insert(0,varStringDT3.get())
        dtSpinbox.delete (0, END)
        dtSpinbox.insert (0, varStringDT3.get ())
        entry6.delete (0,6)
        entry6.insert(0,varStringPN3.get())
        pnSpinbox.delete (0, END)
        pnSpinbox.insert (0, varStringPN3.get ())
    elif spinbox1.get()=='4':
        varString17.set('0')
        varString18.set('0')
        varString19.set('0')
        varString20.set('1')
        varString21.set('0')
        varString22.set('0')
        varString23.set('0')
        varString24.set('0')
        entry2.delete(0,6)
        entry2.insert(0,varStringCurrent4.get())
        entry3.delete (0,6)
        entry3.insert(0,varStringFrequency4.get())
        entry4.delete (0,6)
        entry4.insert(0,varStringPW4.get())
        entry5.delete (0,6)
        entry5.insert(0,varStringDT4.get())
        entry6.delete (0,6)
        entry6.insert(0,varStringPN4.get())
        currentSpinbox.delete (0, END)
        currentSpinbox.insert (0, varStringCurrent4.get ())
        frequencySpinbox.delete (0, END)
        frequencySpinbox.insert (0, varStringFrequency4.get ())
        pwSpinbox.delete (0, END)
        pwSpinbox.insert (0, varStringPW4.get ())
        dtSpinbox.delete (0, END)
        dtSpinbox.insert (0, varStringDT4.get ())
        pnSpinbox.delete (0, END)
        pnSpinbox.insert (0, varStringPN4.get ())
    elif spinbox1.get()=='5':
        varString17.set('0')
        varString18.set('0')
        varString19.set('0')
        varString20.set('0')
        varString21.set('1')
        varString22.set('0')
        varString23.set('0')
        varString24.set('0')
        entry2.delete(0,6)
        entry2.insert(0,varStringCurrent5.get())
        entry3.delete (0,6)
        entry3.insert(0,varStringFrequency5.get())
        entry4.delete (0,6)
        entry4.insert(0,varStringPW5.get())
        entry5.delete (0,6)
        entry5.insert(0,varStringDT5.get())
        entry6.delete (0,6)
        entry6.insert(0,varStringPN5.get())
        currentSpinbox.delete (0, END)
        currentSpinbox.insert (0, varStringCurrent5.get ())
        frequencySpinbox.delete (0, END)
        frequencySpinbox.insert (0, varStringFrequency5.get ())
        pwSpinbox.delete (0, END)
        pwSpinbox.insert (0, varStringPW5.get ())
        dtSpinbox.delete (0, END)
        dtSpinbox.insert (0, varStringDT5.get ())
        pnSpinbox.delete (0, END)
        pnSpinbox.insert (0, varStringPN5.get ())
    elif spinbox1.get()=='6':
        varString17.set('0')
        varString18.set('0')
        varString19.set('0')
        varString20.set('0')
        varString21.set('0')
        varString22.set('1')
        varString23.set('0')
        varString24.set('0')
        entry2.delete(0,6)
        entry2.insert(0,varStringCurrent6.get())
        entry3.delete (0,6)
        entry3.insert(0,varStringFrequency6.get())
        entry4.delete (0,6)
        entry4.insert(0,varStringPW6.get())
        entry5.delete (0,6)
        entry5.insert(0,varStringDT6.get())
        entry6.delete (0,6)
        entry6.insert(0,varStringPN6.get())
        currentSpinbox.delete (0, END)
        currentSpinbox.insert (0, varStringCurrent6.get ())
        frequencySpinbox.delete (0, END)
        frequencySpinbox.insert (0, varStringFrequency6.get ())
        pwSpinbox.delete (0, END)
        pwSpinbox.insert (0, varStringPW6.get ())
        dtSpinbox.delete (0, END)
        dtSpinbox.insert (0, varStringDT6.get ())
        pnSpinbox.delete (0, END)
        pnSpinbox.insert (0, varStringPN6.get ())
    elif spinbox1.get()=='7':
        varString17.set('0')
        varString18.set('0')
        varString19.set('0')
        varString20.set('0')
        varString21.set('0')
        varString22.set('0')
        varString23.set('1')
        varString24.set('0')
        entry2.delete(0,6)
        entry2.insert(0,varStringCurrent7.get())
        entry3.delete (0,6)
        entry3.insert(0,varStringFrequency7.get())
        entry4.delete (0,6)
        entry4.insert(0,varStringPW7.get())
        entry5.delete (0,6)
        entry5.insert(0,varStringDT7.get())
        entry6.delete (0,6)
        entry6.insert(0,varStringPN7.get())
        currentSpinbox.delete (0, END)
        currentSpinbox.insert (0, varStringCurrent7.get ())
        frequencySpinbox.delete (0, END)
        frequencySpinbox.insert (0, varStringFrequency7.get ())
        pwSpinbox.delete (0, END)
        pwSpinbox.insert (0, varStringPW7.get ())
        dtSpinbox.delete (0, END)
        dtSpinbox.insert (0, varStringDT7.get ())
        pnSpinbox.delete (0, END)
        pnSpinbox.insert (0, varStringPN7.get ())
    elif spinbox1.get () == '8':
        varString17.set('0')
        varString18.set('0')
        varString19.set('0')
        varString20.set('0')
        varString21.set('0')
        varString22.set('0')
        varString23.set('0')
        varString24.set('1')
        entry2.delete (0, 6)
        entry2.insert (0, varStringCurrent8.get ())
        entry3.delete (0, 6)
        entry3.insert (0, varStringFrequency8.get ())
        entry4.delete (0, 6)
        entry4.insert (0, varStringPW8.get ())
        entry5.delete (0, 6)
        entry5.insert (0, varStringDT8.get ())
        entry6.delete (0, 6)
        entry6.insert (0, varStringPN8.get ())
        currentSpinbox.delete (0, END)
        currentSpinbox.insert (0, varStringCurrent8.get ())
        frequencySpinbox.delete (0, END)
        frequencySpinbox.insert (0, varStringFrequency8.get ())
        pwSpinbox.delete (0, END)
        pwSpinbox.insert (0, varStringPW8.get ())
        dtSpinbox.delete (0, END)
        dtSpinbox.insert (0, varStringDT8.get ())
        pnSpinbox.delete (0, END)
        pnSpinbox.insert (0, varStringPN8.get ())
    pass

def spinbox1Event(event=None):
    spinboxCanalValues()
    print('Esta en evento')
    pass

def currentEvent(event=None):
    currentModified()
    pass

def frequencyEvent(event=None):
    frequencyModified()
    pass

def pwEvent(event=None):
    pwModified()
    pass

def dtEvent(event=None):
    dtModified()
    pass

def pnEvent(event=None):
    pnModified()
    pass

def entryCurrentEvent(event=None):
    varStringCurrent1.set(entry2.get())
    varStringCurrent2.set(entry2.get())
    varStringCurrent3.set(entry2.get())
    varStringCurrent4.set(entry2.get())
    varStringCurrent5.set(entry2.get())
    varStringCurrent6.set(entry2.get())
    varStringCurrent7.set(entry2.get())
    varStringCurrent8.set(entry2.get())
    ensembleConfiguration()
    pass

def entryFrequencyEvent(event=None):
    varStringFrequency1.set(entry3.get())
    varStringFrequency2.set(entry3.get())
    varStringFrequency3.set(entry3.get())
    varStringFrequency4.set(entry3.get())
    varStringFrequency5.set(entry3.get())
    varStringFrequency6.set(entry3.get())
    varStringFrequency7.set(entry3.get())
    varStringFrequency8.set(entry3.get())
    ensembleConfiguration()
    pass

def entryPWEvent(event=None):
    varStringPW1.set(entry4.get())
    varStringPW2.set(entry4.get())
    varStringPW3.set(entry4.get())
    varStringPW4.set(entry4.get())
    varStringPW5.set(entry4.get())
    varStringPW6.set(entry4.get())
    varStringPW7.set(entry4.get())
    varStringPW8.set(entry4.get())
    ensembleConfiguration()
    pass

def entryDTEvent(event=None):
    varStringDT1.set(entry5.get())
    varStringDT2.set(entry5.get())
    varStringDT3.set(entry5.get())
    varStringDT4.set(entry5.get())
    varStringDT5.set(entry5.get())
    varStringDT6.set(entry5.get())
    varStringDT7.set(entry5.get())
    varStringDT8.set(entry5.get())
    ensembleConfiguration()
    pass

def entryPNEvent(event=None):
    varStringPN1.set(entry6.get())
    varStringPN2.set(entry6.get())
    varStringPN3.set(entry6.get())
    varStringPN4.set(entry6.get())
    varStringPN5.set(entry6.get())
    varStringPN6.set(entry6.get())
    varStringPN7.set(entry6.get())
    varStringPN8.set(entry6.get())
    ensembleConfiguration()
    pass

def ensembleConfiguration():
    maskEntry = int(entry1.get())
    currentEntry = int(varStringCurrent1.get())  # int (entry2.get ())
    frequencyEntry = int(varStringFrequency1.get())  # int (entry3.get ())

    Tremuna.Frequency = frequencyEntry
    Tremuna.PW = int(varStringPW2.get())
    Tremuna.DT = int(varStringDT2.get())
    Tremuna.PN = int(varStringPN2.get())

    pwEntry = (int(varStringPW2.get())).to_bytes(2, byteorder='big')  # (pwEntry).to_bytes (2, byteorder='big')
    dtEntry = (int(varStringDT2.get())).to_bytes(2, byteorder='big')  # (dtEntry).to_bytes (2, byteorder='big')
    pnEntry = (int(varStringPN2.get())).to_bytes(2, byteorder='big')  # (pnEntry).to_bytes (2, byteorder='big')
    print('Andres')
    for i in range(0, 8):
        Tremuna.ensembleCurrent[i] = currentEntry
        Tremuna.ensembleFrequency[i] = frequencyEntry
        Tremuna.ensemblePW_0[i] = pwEntry[0]
        Tremuna.ensemblePW_1[i] = pwEntry[1]
        Tremuna.ensembleDT_0[i] = dtEntry[0]
        Tremuna.ensembleDT_1[i] = dtEntry[1]
        Tremuna.ensemblePN_0[i] = pnEntry[0]
        Tremuna.ensemblePN_1[i] = pnEntry[1]

    Tremuna.EnsembleConfiguration()

    print(maskEntry)
    print(currentEntry)
    print(frequencyEntry)
    print(pwEntry)
    print(dtEntry)
    print(pnEntry)
    print("Optición por canales Escogidos")
    pass

def ConfigurationOption1():     # Activa los spinbox de configuración
    RunStep.set('1')
    print("Se activa los widget 1")
    buttonConnectionDelsys.config(relief=RAISED)
    Tremuna.flag = False
    Tremuna.sINTERAPPS_EMG.close()
    Tremuna.sINTERAPPS_ACC.close()
    currentSpinbox.place(x=170, y=240) # Estaba en posicion 190
    frequencySpinbox.place(x=170, y=275)
    pwSpinbox.place (x=170, y=310)
    dtSpinbox.place (x=170, y=345)
    pnSpinbox.place (x=170, y=380)
    entry2.place_forget()
    entry3.place_forget()
    entry4.place_forget()
    entry5.place_forget()
    entry6.place_forget()
    checkbutton1.config(state='disabled')
    checkbutton2.config(state='disabled')
    checkbutton3.config(state='disabled')
    checkbutton4.config(state='disabled')
    checkbutton5.config(state='disabled')
    checkbutton6.config(state='disabled')
    checkbutton7.config(state='disabled')
    checkbutton8.config(state='disabled')

    label2.config(state='normal')
    spinbox1.config(state='normal')

    pass

def ConfigurationOption2():     # Activa los entries de configuración
    RunStep.set('2')
    print("Se activa los widget 2")
    buttonConnectionDelsys.config(relief=RAISED)
    Tremuna.flag = False
    Tremuna.sINTERAPPS_EMG.close()
    Tremuna.sINTERAPPS_ACC.close()
    currentSpinbox.place_forget()
    frequencySpinbox.place_forget()
    pwSpinbox.place_forget()
    dtSpinbox.place_forget()
    pnSpinbox.place_forget()
    entry2.place (x=170, y=240) # Estaba en posicion x 190  # Posición para el Valor de Entrada Conf. Corriente
    entry3.place (x=170, y=275)  # Posición para el Valor de Entrada Conf. Frecuencia
    entry4.place (x=170, y=310)  # Posición para el Valor de Entrada Conf. PW
    entry5.place (x=170, y=345)  # Posición para el Valor de Entrada Conf. DT
    entry6.place (x=170, y=380)  # Posición para el Valor de Entrada Conf. PN

    checkbutton1.config(state='normal')
    checkbutton2.config(state='normal')
    checkbutton3.config(state='normal')
    checkbutton4.config(state='normal')
    checkbutton5.config(state='normal')
    checkbutton6.config(state='normal')
    checkbutton7.config(state='normal')
    checkbutton8.config(state='normal')

    label2.config(state = 'disabled')
    spinbox1.config(state = 'disabled')

    pass

def ConnectionWithDelsys():

    #RunStep.set('3')
    #print("Se activa los widget 3")
    buttonConnectionDelsys.config(relief=SUNKEN)
    Tremuna.flag = True
    label2.config(state='disabled')
    spinbox1.config(state='disabled')
    Tremuna.sensorNumber = 1
    therapy = varStringTherapy.get()

    if(therapy=="Control desde el dispositivo EMG Agarre Fuerte"):
        #print('Terapia Fuerte')
        tConnectionEMG = threading.Thread(target = Tremuna.EMGConnection)
        tConnectionACC = threading.Thread(target = Tremuna.ACCConnection)
        tCanalsControl = threading.Thread(target=Tremuna.PowerGraspControl,args=(qState,))
        tProcessState = threading.Thread(target=ProcessState)

        tConnectionEMG.start()
        tConnectionACC.start()
        tCanalsControl.start()
        tProcessState.start()

    elif (therapy == "Control desde el dispositivo EMG Pinza"):
        #print('Terapia Pinza')
        tConnectionEMG = threading.Thread(target=Tremuna.EMGConnection)
        tConnectionACC = threading.Thread(target=Tremuna.ACCConnection)
        tCanalsControl = threading.Thread(target=Tremuna.PinchControl, args=(qState,))
        tProcessState = threading.Thread(target=ProcessState)

        tConnectionEMG.start()
        tConnectionACC.start()
        tCanalsControl.start()
        tProcessState.start()
    #print('Fin de Terapia Talogo')
    pass

def DirectOption():
    Therapytype1.set(True)
    Therapytype2.set(False)
    Therapytype3.set(False)
    varStringTherapy.set("Control desde el dispositivo EMG Directo")
    buttonConnectionDelsys.config(text=varStringTherapy.get())
    pass

def PowerGrasp():

    Therapytype1.set(False)
    Therapytype2.set(True)
    Therapytype3.set(False)
    varStringTherapy.set("Control desde el dispositivo EMG Agarre Fuerte")
    buttonConnectionDelsys.config(text=varStringTherapy.get())#,arg=(qState,))
    value1, value2, value3, value4, value5, value6, value7, value8, value9 = EMGACCValuesWindow()

    varStringEMG1.set(value1.get())
    varStringEMG2.set(value2.get())
    varStringEMG3.set(value3.get())
    varStringEMG4.set(value4.get())
    varStringEMG5.set(value5.get())
    varStringEMG6.set(value6.get())
    varStringEMG7.set(value7.get())
    varStringEMG8.set(value8.get())
    varStringACC1.set(value9.get())

    Tremuna.EMG1 = float(varStringEMG1.get())
    Tremuna.EMG2 = float(varStringEMG2.get())
    Tremuna.EMG3 = float(varStringEMG1.get())
    Tremuna.EMG4 = float(varStringEMG2.get())
    Tremuna.EMG5 = float(varStringEMG5.get())
    Tremuna.EMG6 = float(varStringEMG6.get())
    Tremuna.EMG7 = float(varStringEMG1.get())
    Tremuna.EMG8 = float(varStringEMG2.get())
    Tremuna.ACC1 = float(varStringACC1.get())
    #print(value1.get(), value2.get(), value3.get(), value4.get(), value5, value6, value7, value8, value9)
    pass

def Pinch():
    Therapytype1.set(False)
    Therapytype2.set(False)
    Therapytype3.set(True)
    varStringTherapy.set("Control desde el dispositivo EMG Pinza")
    buttonConnectionDelsys.config(text=varStringTherapy.get())

    value1, value2, value3, value4, value5, value6, value7, value8, value9 = EMGACCValuesWindow()
    print(value1.get())
    print(value2.get())
    print(value3.get())
    print(value4.get())
    print(value5.get())
    print(value6.get())
    print(value7.get())
    print(value8.get())
    print(value9.get())

    varStringEMG1.set(value1.get())
    varStringEMG2.set(value2.get())
    varStringEMG3.set(value3.get())
    varStringEMG4.set(value4.get())
    varStringEMG5.set(value5.get())
    varStringEMG6.set(value6.get())
    varStringEMG7.set(value7.get())
    varStringEMG8.set(value8.get())
    varStringACC1.set(value9.get())

    Tremuna.EMG1 = float(varStringEMG1.get())
    Tremuna.EMG2 = float(varStringEMG2.get())
    Tremuna.EMG3 = float(varStringEMG3.get())
    Tremuna.EMG4 = float(varStringEMG2.get())
    Tremuna.EMG5 = float(varStringEMG5.get())
    Tremuna.EMG6 = float(varStringEMG6.get())
    Tremuna.EMG7 = float(varStringEMG7.get())
    Tremuna.EMG8 = float(varStringEMG1.get())
    Tremuna.ACC1 = float(varStringACC1.get())
    pass

# Esta funcion crea una ventana donde se ingresan los valores de varianza de EMGs y ACC1 y luego devuelve los valores
def EMGACCValuesWindow():

    top = tk.Toplevel()
    top.title('Valores de Terapia')
    top.geometry('270x295')

    labelState1 = Label(top, text='Primeros Valores', relief=FLAT, width=17)
    label1 = Label(top, text='Músculo Deltoides', relief=FLAT, width=17)
    label2 = Label(top, text='Músculo Bíceps', relief=FLAT, width=17)
    label3 = Label(top, text='Músculo Tríceps', relief=FLAT, width=17)

    labelState2 = Label(top, text='Segundos Valores', relief=FLAT, width=17)
    label5 = Label(top, text='Músculo Deltoides', relief=FLAT, width=17)
    label6 = Label(top, text='Músculo Bíceps', relief=FLAT, width=17)
    label7 = Label(top, text='Músculo Tríceps', relief=FLAT, width=17)
    #label8 = Label(top, text='Valor EMG8', relief=FLAT, width=17)
    #label9 = Label(top, text='Aceleración', relief=FLAT, width=17)

    entryEMG1 = tk.Entry(top, bd=2, width=15, justify='center',textvariable=varStringEMG1)
    entryEMG2 = tk.Entry(top, bd=2, width=15, justify='center',textvariable=varStringEMG2)

    #entryEMG4 = tk.Entry(top, bd=2, width=15, justify='center',textvariable=varStringEMG4)
    entryEMG5 = tk.Entry(top, bd=2, width=15, justify='center',textvariable=varStringEMG5)
    entryEMG6 = tk.Entry(top, bd=2, width=15, justify='center',textvariable=varStringEMG6)

    #entryEMG8 = tk.Entry(top, bd=2, width=15, justify='center',textvariable=varStringEMG8)
    #entryACC1 = tk.Entry(top, bd=2, width=15, justify='center', textvariable=varStringACC1)

    button1 =tk.Button(top, text ="Aceptar", width=12, command = top.destroy)

    labelState1.place(x=80, y=15)
    label1.place(x=7, y=45)
    label2.place(x=7, y=72)

    labelState2.place(x=80, y=135)
    label5.place(x=7, y=163)
    label6.place(x=7, y=190)

    #label8.place(x=7, y=169)
    #label9.place(x=7, y=221)

    entryEMG1.place(x=150,y=45)
    entryEMG2.place(x=150, y=72)

    #entryEMG4.place(x=110, y=98)
    entryEMG5.place(x=150, y=163)
    entryEMG6.place(x=150, y=190)

    #entryEMG8.place(x=110, y=169)
    #entryACC1.place(x=150, y=213)

    if(Therapytype3.get()==True):
        label3.place(x=7, y=99)
        entryEMG3 = tk.Entry(top, bd=2, width=15, justify='center', textvariable=varStringEMG3)
        entryEMG3.place(x=150, y=99)
        label7.place(x=7, y=217)
        entryEMG7 = tk.Entry(top, bd=2, width=15, justify='center', textvariable=varStringEMG7)
        entryEMG7.place(x=150, y=217)


    button1.place(x=100,y=255)
    top.wait_window()
    return (varStringEMG1,varStringEMG2,varStringEMG3,varStringEMG4,varStringEMG5,varStringEMG6,varStringEMG7,varStringEMG8, varStringACC1)

    pass

def nameMuscle(event=None):
    #Tremuna.FileName = entryFileName.get()
    Tremuna.MusclesName = [entryNameMuscle1.get(), entryNameMuscle2.get(), entryNameMuscle3.get(), entryNameMuscle4.get(),
                           entryNameMuscle5.get(), entryNameMuscle6.get(), entryNameMuscle7.get(), entryNameMuscle8.get()]
    pass

# Esta funcion indica en que parte de la terapia se enuentra el paciente
def ProcessState():
    labelState.config(text='Comienzo de la Terapia',background='DarkOliveGreen1')# background='light blue')
    #print('Comienza proceso')
    while(Tremuna.flag==True):
        state = qState.get()
        if state==1:
            labelState.config(text='Estado '+str(state)+' Levantar el Brazo')# background='DarkOliveGreen1')
        elif state ==2:
            labelState.config(text='Estado '+str(state)+' Llevar Brazo Hacie el Vaso')
        elif state == 3:
            labelState.config(text='Estado ' + str(state) + ' Tiempo de reposo')
        elif state == 4:
            labelState.config(text='Estado ' + str(state) + ' Cerrar y Tomar el Vaso')
        elif state == 5:
            labelState.config(text='Estado ' + str(state) + ' Levantar el Brazo y Beber')
        elif state == 6:
            labelState.config(text='Estado ' + str(state) + ' Colocar el Vaso en la Mesa')
        elif state == 7:
            labelState.config(text='Estado ' + str(state) + ' Suelta el Vaso')
        elif state == 8:
            labelState.config(text='Estado ' + str(state) + ' Levantar Brazo')
        elif state == 9:
            labelState.config(text='Estado ' + str(state) + ' Brazo en Reposo a un Costado de Cuerpo')
        elif state == 0:
            labelState.config(text='Fina de la Terapia')
    labelState.config(text='Fin de la Terapia', background='light blue')
    qState.queue.clear()
    pass


## Widgets

submenu.add_checkbutton(label=" Directo ",variable=Therapytype1,command=DirectOption)
submenu.add_checkbutton(label=" Agarre Fuerte ",variable=Therapytype2, command=PowerGrasp)
submenu.add_checkbutton(label=" Pinza ",variable=Therapytype3, command=Pinch)

filemenu.add_cascade(label="Tipos de Terapia", menu=submenu, underline=0)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=filemenu, underline=0)

labelframe1 = LabelFrame (root, width=440, height=113, text="Configuración del Dispositivo")

label1 = Label (root, textvariable=varString1, relief=FLAT, width=15)
listbox1 = Listbox (root, height=1, width=15, selectmode='browse', justify='center')  # Selección del puesto USB

button1 = Button (root, text="Conectar", width=11, command=connectDevice)
button2 = Button (root, text="Desconestar", width=11, command=disconnectDevice)
button3 = Button (root, text="Salir", width=11, command=quit)


# Botones de configuración individual
labelframe2 = LabelFrame (root, width=440, height=345, text="Configuración de la Estimulación")

radiobutton1 = Radiobutton (root, text="Configurar un Canal", value=1, variable=varString2, command=ConfigurationOption1)
radiobutton2 = Radiobutton (root, text="Configuración de todos los Canales", value=2, variable=varString2, command=ConfigurationOption2)
#radiobutton3 = Radiobutton (root, text=varStringTherapy.get(), value=3, variable=varString2, command=ConfigurationOption3)
buttonConnectionDelsys = Button(root, text = varStringTherapy.get(), width=35,command=ConnectionWithDelsys)
labelState = Label (root, text='Comienzo de Rutina', relief=SUNKEN, width=35,background='light blue')

label2 = Label (root, textvariable=varString3, relief=FLAT, width=26)

spinbox1 = Spinbox (root, from_=1, to=8, bd=2, width=8, justify='center',command=spinboxCanalValues)
spinbox1.bind('<Return>', spinbox1Event)        # Evento de cuando se presiones Enter cambia el valor

currentSpinbox = Spinbox (root, from_=0, to=20, bd=2, width=8, justify='center',validate=ALL,command=currentModified)
currentSpinbox.bind('<Return>', currentEvent)   # Evento de cuando se presiones Enter cambia el valor
frequencySpinbox = Spinbox (root, from_=0, to=1000, bd=2, width=8, justify='center',command=frequencyModified)
frequencySpinbox.bind('<Return>', frequencyEvent)
pwSpinbox = Spinbox (root, from_=0, to=1000, bd=2, width=8, justify='center',command=pwModified)
pwSpinbox.bind('<Return>', pwEvent)             # Evento de cuando se presiones Enter cambia el valor
dtSpinbox = Spinbox (root, from_=0, to=1000, bd=2, width=8, justify='center',command=dtModified)
dtSpinbox.bind('<Return>', dtEvent)             # Evento de cuando se presiones Enter cambia el valor
pnSpinbox = Spinbox (root, from_=0, to=1000, bd=2, width=8, justify='center',command=pnModified)
pnSpinbox.bind('<Return>', pnEvent)             # Evento de cuando se presiones Enter cambia el valor
#currentButton = Button(root, text=varString5.get(), width=17, command=currentModified)
#frequencyButton = Button(root, text=varString6.get(), width=17, command=frequencyModified)
#pwButton = Button(root, text=varString7.get(), width=17, command=pwModified)
#dtButton = Button(root, text=varString8.get(), width=17, command=dtModified)
#pnButton = Button(root, text=varString9.get(), width=17, command=pnModified)
#label3 = Label (root, textvariable=varString4, relief=FLAT, width=17)
label4 = Label (root, textvariable=varString5, relief=FLAT, width=17)
label5 = Label (root, textvariable=varString6, relief=FLAT, width=17)
label6 = Label (root, textvariable=varString7, relief=FLAT, width=17)
label7 = Label (root, textvariable=varString8, relief=FLAT, width=17)
label8 = Label (root, textvariable=varString9, relief=FLAT, width=17)

entry1 = Entry (root, bd=2, width=8, justify='center')

entry2 = Entry (root, bd=2, width=8, justify='center')#,validatecommand=currentModified)
entry2.bind('<Return>', entryCurrentEvent)
entry3 = Entry (root, bd=2, width=8, justify='center')
entry3.bind('<Return>', entryFrequencyEvent)
entry4 = Entry (root, bd=2, width=8, justify='center')
entry4.bind('<Return>', entryPWEvent)
entry5 = Entry (root, bd=2, width=8, justify='center')
entry5.bind('<Return>', entryDTEvent)
entry6 = Entry (root, bd=2, width=8, justify='center')
entry6.bind('<Return>', entryPNEvent)

entry1.insert (0, "0")
entry2.insert (0, "3")
entry3.insert (0, "50")
entry4.insert (0, "250")
entry5.insert (0, "0")
entry6.insert (0, "0")

andres = 'Andres'

button4 = Button (root, text="ACTIVAR CANALES", width=20, command=activateChannels)
button5 = Button (root, text="FES ON", width=20, command=turnON)
button6 = Button (root, text="FES OFF", width=20,command=turnOFF)

labelframe3 = LabelFrame (root, width=770, height=400, text="Canales de Conexión")

labelTitle = Label(root, textvariable=varStringTitle, width=21)

labelActive = [Label(root, bg='gray95', relief=GROOVE, width=3),Label(root, bg='gray95', relief=GROOVE, width=3),Label(root, bg='gray95', relief=GROOVE, width=3),Label(root, bg='gray95', relief=GROOVE, width=3),
               Label(root, bg='gray95', relief=GROOVE, width=3),Label(root, bg='gray95', relief=GROOVE, width=3),Label(root, bg='gray95', relief=GROOVE, width=3),Label(root, bg='gray95', relief=GROOVE, width=3)]

label9 = Label (root, textvariable=varString10, relief=RAISED, width=12)
label10 = Label (root, textvariable=varString11, relief=RAISED, width=12)
label11 = Label (root, textvariable=varString12, relief=RAISED, width=12)
label12 = Label (root, textvariable=varString13, relief=RAISED, width=12)
label13 = Label (root, textvariable=varString14, relief=RAISED, width=12)
label14 = Label (root, textvariable=varString15, relief=RAISED, width=12)
label15 = Label (root, textvariable=varString16, relief=RAISED, width=12)

labelNameMuscle = Label (root, textvariable=varStringNameMuscle, relief=RAISED, width=16)
labelStateDevice = Label (root, textvariable=varStringStateDevice, bg = "gray99", relief=GROOVE,width=23)
labelOnDevice = Label (root, textvariable=varStringOnDevice,bg = "lawn green", relief=GROOVE, width=23)
labelOffDevice = Label (root, textvariable=varStringOffDevice,bg = "gray99", relief=GROOVE, width=23)

checkbutton1 = Checkbutton (root, variable=varString17, onvalue=1, offvalue=0, height=0, width=0)
checkbutton2 = Checkbutton (root, variable=varString18, onvalue=1, offvalue=0, height=0, width=0)
checkbutton3 = Checkbutton (root, variable=varString19, onvalue=1, offvalue=0, height=0, width=0)
checkbutton4 = Checkbutton (root, variable=varString20, onvalue=1, offvalue=0, height=0, width=0)
checkbutton5 = Checkbutton (root, variable=varString21, onvalue=1, offvalue=0, height=0, width=0)
checkbutton6 = Checkbutton (root, variable=varString22, onvalue=1, offvalue=0, height=0, width=0)
checkbutton7 = Checkbutton (root, variable=varString23, onvalue=1, offvalue=0, height=0, width=0)
checkbutton8 = Checkbutton (root, variable=varString24, onvalue=1, offvalue=0, height=0, width=0)

label25 = Label (root, textvariable=varString25, relief=RAISED, width=12)
label26 = Label (root, textvariable=varString26, relief=RAISED, width=12)
label27 = Label (root, textvariable=varString27, relief=RAISED, width=12)
label28 = Label (root, textvariable=varString28, relief=RAISED, width=12)
label29 = Label (root, textvariable=varString29, relief=RAISED, width=12)
label30 = Label (root, textvariable=varString30, relief=RAISED, width=12)
label31 = Label (root, textvariable=varString31, relief=RAISED, width=12)
label32 = Label (root, textvariable=varString32, relief=RAISED, width=12)

labelCurrent1 = Label (root, textvariable=varStringCurrent1, relief=SUNKEN, background='white', width=12,
                       justify=CENTER)
labelCurrent2 = Label (root, textvariable=varStringCurrent2, relief=SUNKEN, background='white', width=12,
                       justify=CENTER)
labelCurrent3 = Label (root, textvariable=varStringCurrent3, relief=SUNKEN, background='white', width=12,
                       justify=CENTER)
labelCurrent4 = Label (root, textvariable=varStringCurrent4, relief=SUNKEN, background='white', width=12,
                       justify=CENTER)
labelCurrent5 = Label (root, textvariable=varStringCurrent5, relief=SUNKEN, background='white', width=12,
                       justify=CENTER)
labelCurrent6 = Label (root, textvariable=varStringCurrent6, relief=SUNKEN, background='white', width=12,
                       justify=CENTER)
labelCurrent7 = Label (root, textvariable=varStringCurrent7, relief=SUNKEN, background='white', width=12,
                       justify=CENTER)
labelCurrent8 = Label (root, textvariable=varStringCurrent8, relief=SUNKEN, background='white', width=12,
                       justify=CENTER)

labelFrequency1 = Label (root, textvariable=varStringFrequency1, relief=SUNKEN, background='white', width=12,
                         justify=CENTER)
labelFrequency2 = Label (root, textvariable=varStringFrequency2, relief=SUNKEN, background='white', width=12,
                         justify=CENTER)
labelFrequency3 = Label (root, textvariable=varStringFrequency3, relief=SUNKEN, background='white', width=12,
                         justify=CENTER)
labelFrequency4 = Label (root, textvariable=varStringFrequency4, relief=SUNKEN, background='white', width=12,
                         justify=CENTER)
labelFrequency5 = Label (root, textvariable=varStringFrequency5, relief=SUNKEN, background='white', width=12,
                         justify=CENTER)
labelFrequency6 = Label (root, textvariable=varStringFrequency6, relief=SUNKEN, background='white', width=12,
                         justify=CENTER)
labelFrequency7 = Label (root, textvariable=varStringFrequency7, relief=SUNKEN, background='white', width=12,
                         justify=CENTER)
labelFrequency8 = Label (root, textvariable=varStringFrequency8, relief=SUNKEN, background='white', width=12,
                         justify=CENTER)

labelPW1 = Label (root, textvariable=varStringPW1, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelPW2 = Label (root, textvariable=varStringPW2, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelPW3 = Label (root, textvariable=varStringPW3, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelPW4 = Label (root, textvariable=varStringPW4, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelPW5 = Label (root, textvariable=varStringPW5, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelPW6 = Label (root, textvariable=varStringPW6, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelPW7 = Label (root, textvariable=varStringPW7, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelPW8 = Label (root, textvariable=varStringPW8, relief=SUNKEN, background='white', width=12, justify=CENTER)

labelDT1 = Label (root, textvariable=varStringDT1, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelDT2 = Label (root, textvariable=varStringDT2, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelDT3 = Label (root, textvariable=varStringDT3, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelDT4 = Label (root, textvariable=varStringDT4, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelDT5 = Label (root, textvariable=varStringDT5, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelDT6 = Label (root, textvariable=varStringDT6, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelDT7 = Label (root, textvariable=varStringDT7, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelDT8 = Label (root, textvariable=varStringDT8, relief=SUNKEN, background='white', width=12, justify=CENTER)

labelPN1 = Label (root, textvariable=varStringPN1, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelPN2 = Label (root, textvariable=varStringPN2, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelPN3 = Label (root, textvariable=varStringPN3, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelPN4 = Label (root, textvariable=varStringPN4, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelPN5 = Label (root, textvariable=varStringPN5, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelPN6 = Label (root, textvariable=varStringPN6, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelPN7 = Label (root, textvariable=varStringPN7, relief=SUNKEN, background='white', width=12, justify=CENTER)
labelPN8 = Label (root, textvariable=varStringPN8, relief=SUNKEN, background='white', width=12, justify=CENTER)

#entryFileName = Entry (root, bd=2, width=29, justify='center')
#entryFileName.bind('<Return>', nameMuscle)

entryNameMuscle1 = Entry (root, bd=2, width=19, justify='center')
entryNameMuscle1.bind('<Return>', nameMuscle)
entryNameMuscle2 = Entry (root, bd=2, width=19, justify='center')
entryNameMuscle2.bind('<Return>', nameMuscle)
entryNameMuscle3 = Entry (root, bd=2, width=19, justify='center')
entryNameMuscle3.bind('<Return>', nameMuscle)
entryNameMuscle4 = Entry (root, bd=2, width=19, justify='center')
entryNameMuscle4.bind('<Return>', nameMuscle)
entryNameMuscle5 = Entry (root, bd=2, width=19, justify='center')
entryNameMuscle5.bind('<Return>', nameMuscle)
entryNameMuscle6 = Entry (root, bd=2, width=19, justify='center')
entryNameMuscle6.bind('<Return>', nameMuscle)
entryNameMuscle7 = Entry (root, bd=2, width=19, justify='center')
entryNameMuscle7.bind('<Return>', nameMuscle)
entryNameMuscle8 = Entry (root, bd=2, width=19, justify='center')
entryNameMuscle8.bind('<Return>', nameMuscle)

#entryFileName.insert(0,'TituloVacio')

entryNameMuscle1.insert(0,'Vacio1')
entryNameMuscle2.insert(0,'Vacio2')
entryNameMuscle3.insert(0,'Vacio3')
entryNameMuscle4.insert(0,'Vacio4')
entryNameMuscle5.insert(0,'Vacio5')
entryNameMuscle6.insert(0,'Vacio6')
entryNameMuscle7.insert(0,'Vacio7')
entryNameMuscle8.insert(0,'Vacio8')


image1 = Label(root, image = img1)
image2 = Label(root, image = img2)
image3 = Label(root, image = img3)

## Position
labelframe1.place (x=10, y=10)

label1.place (x=35, y=40)
listbox1.place (x=150, y=40)

button1.place (x=35, y=70)
button2.place (x=140, y=70)
button3.place (x=250, y=70)

labelframe2.place (x=10, y=140)

radiobutton1.place (x=30, y=170)
radiobutton2.place (x=30, y=190)
buttonConnectionDelsys.place (x=90, y=443)
labelState.place(x=93,y=417)

label2.place (x=250, y=170)
spinbox1.place (x=320, y=195)

#label3.place (x=65, y=235)
label4.place (x=40, y=240) #Estaba en x 270
label5.place (x=40, y=275)
label6.place (x=40, y=310)
label7.place (x=40, y=345)
label8.place (x=40, y=380)

#currentButton.place(x=61, y=267)
#frequencyButton.place(x=61, y=302)
#pwButton.place(x=61, y=337)
#dtButton.place(x=61, y=372)
#pnButton.place(x=61, y=407)

button4.place (x=270, y=240) # y 270
button5.place (x=270, y=305)
button6.place (x=270, y=370)

labelframe3.place (x=470, y=10) # Tenía x 500

labelTitle.place(x=770,y=25)

labelActive[0].place(x=483,y=92)
labelActive[1].place(x=483,y=131)
labelActive[2].place(x=483,y=171)
labelActive[3].place(x=483,y=212)
labelActive[4].place(x=483,y=250)
labelActive[5].place(x=483,y=291)
labelActive[6].place(x=483,y=330)
labelActive[7].place(x=483,y=369)

label9.place (x=480, y=55)              # Posición del titulo de Habilitar
label10.place (x=570, y=55)             # Posición del titulo de Canal
label11.place (x=660, y=55)             # Posición del titulo de Corriente
label12.place (x=750, y=55)             # Posición del titulo de Frecuencia
label13.place (x=840, y=55)             # Posición del titulo de PW
label14.place (x=930, y=55)             # Posición del titulo de DT
label15.place (x=1020, y=55)            # Posición del titulo de PN
labelNameMuscle.place (x=1110, y=55)    # Posición del titulo de Nombre del Músculo
labelStateDevice.place(x=260,y=40)

#labelOnDevice.place(x=260,y=305)
labelOffDevice.place(x=260,y=342)

checkbutton1.place (x=515, y=90)   # Posición checkbutton Canal 1
checkbutton2.place (x=515, y=130)  # Posición checkbutton Canal 2
checkbutton3.place (x=515, y=170)  # Posición checkbutton Canal 3
checkbutton4.place (x=515, y=210)  # Posición checkbutton Canal 4
checkbutton5.place (x=515, y=250)  # Posición checkbutton Canal 5
checkbutton6.place (x=515, y=290)  # Posición checkbutton Canal 6
checkbutton7.place (x=515, y=330)  # Posición checkbutton Canal 7
checkbutton8.place (x=515, y=370)  # Posición checkbutton Canal 8

label25.place (x=570, y=90)   # Posición del Canal 1
label26.place (x=570, y=130)  # Posición del Canal 2
label27.place (x=570, y=170)  # Posición del Canal 3
label28.place (x=570, y=210)  # Posición del Canal 4
label29.place (x=570, y=250)  # Posición del Canal 5
label30.place (x=570, y=290)  # Posición del Canal 6
label31.place (x=570, y=330)  # Posición del Canal 7
label32.place (x=570, y=370)  # Posición del Canal 8

labelCurrent1.place (x=660, y=90)   # Posición del Valor Corriente 1
labelCurrent2.place (x=660, y=130)  # Posición del Valor Corriente 2
labelCurrent3.place (x=660, y=170)  # Posición del Valor Corriente 3
labelCurrent4.place (x=660, y=210)  # Posición del Valor Corriente 4
labelCurrent5.place (x=660, y=250)  # Posición del Valor Corriente 5
labelCurrent6.place (x=660, y=290)  # Posición del Valor Corriente 6
labelCurrent7.place (x=660, y=330)  # Posición del Valor Corriente 7
labelCurrent8.place (x=660, y=370)  # Posición del Valor Corriente 8

labelFrequency1.place (x=750, y=90)   # Posición del Valor Frecuencia 1
labelFrequency2.place (x=750, y=130)  # Posición del Valor Frecuencia 2
labelFrequency3.place (x=750, y=170)  # Posición del Valor Frecuencia 3
labelFrequency4.place (x=750, y=210)  # Posición del Valor Frecuencia 4
labelFrequency5.place (x=750, y=250)  # Posición del Valor Frecuencia 5
labelFrequency6.place (x=750, y=290)  # Posición del Valor Frecuencia 6
labelFrequency7.place (x=750, y=330)  # Posición del Valor Frecuencia 7
labelFrequency8.place (x=750, y=370)  # Posición del Valor Frecuencia 8

labelPW1.place (x=840, y=90)   # Posición del Valor PW 1
labelPW2.place (x=840, y=130)  # Posición del Valor PW 2
labelPW3.place (x=840, y=170)  # Posición del Valor PW 3
labelPW4.place (x=840, y=210)  # Posición del Valor PW 4
labelPW5.place (x=840, y=250)  # Posición del Valor PW 5
labelPW6.place (x=840, y=290)  # Posición del Valor PW 6
labelPW7.place (x=840, y=330)  # Posición del Valor PW 7
labelPW8.place (x=840, y=370)  # Posición del Valor PW 8

labelDT1.place (x=930, y=90)   # Posición del Valor DT 1
labelDT2.place (x=930, y=130)  # Posición del Valor DT 2
labelDT3.place (x=930, y=170)  # Posición del Valor DT 3
labelDT4.place (x=930, y=210)  # Posición del Valor DT 4
labelDT5.place (x=930, y=250)  # Posición del Valor DT 5
labelDT6.place (x=930, y=290)  # Posición del Valor DT 6
labelDT7.place (x=930, y=330)  # Posición del Valor DT 7
labelDT8.place (x=930, y=370)  # Posición del Valor DT 8

labelPN1.place (x=1020, y=90)   # Posición del Valor DT 1
labelPN2.place (x=1020, y=130)  # Posición del Valor DT 2
labelPN3.place (x=1020, y=170)  # Posición del Valor DT 3
labelPN4.place (x=1020, y=210)  # Posición del Valor DT 4
labelPN5.place (x=1020, y=250)  # Posición del Valor DT 5
labelPN6.place (x=1020, y=290)  # Posición del Valor DT 6
labelPN7.place (x=1020, y=330)  # Posición del Valor DT 7
labelPN8.place (x=1020, y=370)  # Posición del Valor DT 8

#entryFileName.place(x=930,y=25)

entryNameMuscle1.place(x=1110,y=90)
entryNameMuscle2.place(x=1110,y=130)
entryNameMuscle3.place(x=1110,y=170)
entryNameMuscle4.place(x=1110,y=210)
entryNameMuscle5.place(x=1110,y=250)
entryNameMuscle6.place(x=1110,y=290)
entryNameMuscle7.place(x=1110,y=330)
entryNameMuscle8.place(x=1110,y=370)

## Some attributes
# Muestra de lista de puertos USBs en listBox
portsNumber = len (portsUSB)
for i in range (0, portsNumber):
    listbox1.insert (i, portsUSB[i])
#listbox1.insert (2, portsUSB[2])

# theLabel = Label(root, text="Frst interface")
# theLabel.pack()

image1.place(x=550,y=410)
image2.place(x=815,y=410)
image3.place(x=950,y=410)
root.config(menu=menubar)
root.mainloop ()

#print ('Cierra la ventana.')
