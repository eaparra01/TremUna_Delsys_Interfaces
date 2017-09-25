
from tkinter import *
from ConnectionDelsys_1_4 import *
from ConnectionDelsys_EMG_1_0 import *
from ConnectionDelsys_ACC_1_0 import *
from PlotDataDelsys import *
import threading


class Delsys_Interface_1_1():

    def __init__(self):
        print('Andres Parra')
        self.Delsys = ConnectionDelsys_1_4()
        self.DelsysACC  = ConnectionDelsys_ACC_1_0()
        self.DelsysEMG = ConnectionDelsys_EMG_1_0()
        self.PlotDelsys = PlotDataDelsys()

        self.sDevice = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.qsensortovarianza = queue.Queue(maxsize=0)

        self.root = Tk()  # Create a object from tkinter class
        self.root.geometry("550x540")
        self.root.title("Interface para la conexión con el Dispositivo DELSYS")
        self.labelframe1 = LabelFrame(self.root)
        self.labelframe2 = LabelFrame(self.root)

        self.button1 = Button(self.root)
        self.button2 = Button(self.root)
        self.button3 = Button(self.root)
        self.button4 = Button(self.root)
        self.button5 = Button(self.root)
        self.button6 = Button(self.root)
        self.button7 = Button(self.root)
        self.button8 = Button(self.root)
        self.button9 = Button(self.root)
        self.button10 = Button(self.root)
        self.button11 = Button(self.root)

        self.entryPatientName = Entry(self.root)
        self.entryMuscle1 = Entry(self.root)
        self.entryMuscle2 = Entry(self.root)
        self.entryMuscle3 = Entry(self.root)
        self.entryMuscle4 = Entry(self.root)
        self.entryMuscle5 = Entry(self.root)
        self.entryMuscle6 = Entry(self.root)
        self.entryMuscle7 = Entry(self.root)
        self.entryMuscle8 = Entry(self.root)

        self.checkbutton1 = Checkbutton(self.root)
        self.checkbutton2 = Checkbutton(self.root)
        self.checkbutton3 = Checkbutton(self.root)
        self.checkbutton4 = Checkbutton(self.root)
        self.checkbutton5 = Checkbutton(self.root)
        self.checkbutton6 = Checkbutton(self.root)
        self.checkbutton7 = Checkbutton(self.root)
        self.checkbutton8 = Checkbutton(self.root)
        self.checkbutton9 = Checkbutton(self.root)

        self.label1 = Label(self.root)
        self.label2 = Label(self.root)
        self.label3 = Label(self.root)
        self.label4 = Label(self.root)
        self.label5 = Label(self.root)
        self.label6 = Label(self.root)
        self.label7 = Label(self.root)
        self.label8 = Label(self.root)
        self.label9 = Label(self.root)

        self.varStringStateDevice = StringVar()

        self.varString1 = StringVar()  # String de Frecuencia
        self.varString2 = StringVar()  # String de Sensores
        self.varString3 = StringVar()  #
        self.varString4 = StringVar()  #
        self.varString5 = StringVar()  #
        self.varString6 = StringVar()  #
        self.varString7 = StringVar()  #
        self.varString8 = StringVar()  #
        self.varString9 = StringVar()  #####
        self.varSaveTypeData = StringVar()

        self.varStringCheck1 = StringVar()  # String de Frecuencia
        self.varStringCheck2 = StringVar()  # String de Frecuencia
        self.varStringCheck3 = StringVar()  # String de Frecuencia
        self.varStringCheck4 = StringVar()  # String de Frecuencia
        self.varStringCheck5 = StringVar()  # String de Frecuencia
        self.varStringCheck6 = StringVar()  # String de Frecuencia
        self.varStringCheck7 = StringVar()  # String de Frecuencia
        self.varStringCheck8 = StringVar()  # String de Frecuencia
        self.varStringCheck9 = StringVar()  # String de Frecuencia

        self.varFlagCheck2 = StringVar()  # Bandera de paridad
        self.varFlagCheck3 = StringVar()  #
        self.varFlagCheck4 = StringVar()  #
        self.varFlagCheck5 = StringVar()  #
        self.varFlagCheck6 = StringVar()  #
        self.varFlagCheck7 = StringVar()  #
        self.varFlagCheck8 = StringVar()  #
        self.varFlagCheck9 = StringVar()  #

        self.varStrMessageLabel1 = StringVar()

        self.varDatosSinEMG = StringVar()
        self.varDatosConEMG = StringVar()
        self.varTerminarDatos = StringVar()

        self.confiGui()

    def confiGui(self):

        self.labelframe1.config(width=530, height=120, text="Conexión con el Dispositivo")
        self.labelframe2.config(width=530, height=385, text="Configuración de Sensores")

        self.labelframe1.place(x=10, y=10)
        self.labelframe2.place(x=10, y=140)

        self.button1.config(text="Conectar", width=11, command=self.connectDevice)
        self.button2.config(text="Desconestar", width=11, command=self.disconnectDevice)
        self.button3.config(text="Salir", width=11, command=quit)
        self.button4.config(text="Datos SIN Estimulación", width=20, command=self.startSample)
        self.button5.config(text="Datos CON Estimulación", width=20, command=self.startSendData)
        self.button6.config(text="Terminar toma de Datos", width=20, command=self.stopSample)
        self.button7.config(text="Mostrar Señales EMG y Varianza", width=25, command =self.plotdataEMGandVar)#self.PlotDelsys.plotEMGVar)
        self.button8.config(text="Mostrar Señales de Varianza", width=25, command=self.plotdataEMGVar)  # self.PlotDelsys.plotEMGVar)
        self.button9.config(text="Mostrar Señales ACC", width=25, command=self.plotdataACC)
        self.button10.config(text="Mostrar Señales de Varianza", width=25, command=self.plotdataACCVar)
        self.button11.config(text="Guardar Datos", width=15, command=self.saveData)

        self.button1.place(x=35, y=75)
        self.button2.place(x=140, y=75)
        self.button3.place(x=250, y=75)
        self.button4.place(x=177, y=240)
        self.button5.place(x=177, y=320)
        self.button6.place(x=177, y=400)
        self.button7.place(x=339, y=240)
        self.button8.place(x=339, y=320)
        self.button9.place(x=339, y=400)
        self.button10.place(x=339, y=480)
        self.button11.place(x=379, y=75)

        self.entryPatientName.config(bd=2, width=29, justify='center')
        self.entryMuscle1.config(bd=2, width=11, justify='center')
        self.entryMuscle2.config(bd=2, width=11, justify='center')
        self.entryMuscle3.config(bd=2, width=11, justify='center')
        self.entryMuscle4.config(bd=2, width=11, justify='center')
        self.entryMuscle5.config(bd=2, width=11, justify='center')
        self.entryMuscle6.config(bd=2, width=11, justify='center')
        self.entryMuscle7.config(bd=2, width=11, justify='center')
        self.entryMuscle8.config(bd=2, width=11, justify='center')

        self.entryPatientName.insert(0,'Ingrese el Nombre del Paciente')
        self.entryMuscle1.insert(0, 'Músculo 1')
        self.entryMuscle2.insert(0, 'Músculo 2')
        self.entryMuscle3.insert(0, 'Músculo 3')
        self.entryMuscle4.insert(0, 'Músculo 4')
        self.entryMuscle5.insert(0, 'Músculo 5')
        self.entryMuscle6.insert(0, 'Músculo 6')
        self.entryMuscle7.insert(0, 'Músculo 7')
        self.entryMuscle8.insert(0, 'Músculo 8')

        self.entryPatientName.place(x=350,y=40)
        self.entryMuscle1.place(x=53, y=223)
        self.entryMuscle2.place(x=53, y=253)
        self.entryMuscle3.place(x=53, y=283)
        self.entryMuscle4.place(x=53, y=313)
        self.entryMuscle5.place(x=53, y=343)
        self.entryMuscle6.place(x=53, y=373)
        self.entryMuscle7.place(x=53, y=403)
        self.entryMuscle8.place(x=53, y=433)

        self.checkbutton1.config(variable=self.varStringCheck1, onvalue=1, offvalue=0, height=0, width=0, command=self.sensorFrequency)
        self.checkbutton2.config(variable=self.varStringCheck2, onvalue=1, offvalue=0, height=0, width=0, command=self.sensorParied)
        self.checkbutton3.config(variable=self.varStringCheck3, onvalue=1, offvalue=0, height=0, width=0, command=self.sensorParied)
        self.checkbutton4.config(variable=self.varStringCheck4, onvalue=1, offvalue=0, height=0, width=0, command=self.sensorParied)
        self.checkbutton5.config(variable=self.varStringCheck5, onvalue=1, offvalue=0, height=0, width=0, command=self.sensorParied)
        self.checkbutton6.config(variable=self.varStringCheck6, onvalue=1, offvalue=0, height=0, width=0, command=self.sensorParied)
        self.checkbutton7.config(variable=self.varStringCheck7, onvalue=1, offvalue=0, height=0, width=0, command=self.sensorParied)
        self.checkbutton8.config(variable=self.varStringCheck8, onvalue=1, offvalue=0, height=0, width=0, command=self.sensorParied)
        self.checkbutton9.config(variable=self.varStringCheck9, onvalue=1, offvalue=0, height=0, width=0, command=self.sensorParied)

        self.checkbutton1.place(x=190, y=170)  # Posición checkbutton Frecuencia

        self.checkbutton2.place(x=130, y=220)  # Posición checkbutton Canal 2
        self.checkbutton3.place(x=130, y=250)  # Posición checkbutton Canal 3
        self.checkbutton4.place(x=130, y=280)  # Posición checkbutton Canal 4
        self.checkbutton5.place(x=130, y=310)  # Posición checkbutton Canal 5
        self.checkbutton6.place(x=130, y=340)  # Posición checkbutton Canal 6
        self.checkbutton7.place(x=130, y=370)  # Posición checkbutton Canal 7
        self.checkbutton8.place(x=130, y=400)  # Posición checkbutton Canal 8
        self.checkbutton9.place(x=130, y=430)  # Posición checkbutton Canal 9

        self.labelStateDevice = Label(self.root, textvariable=self.varStringStateDevice, bg='gray99', relief=GROOVE, width=23)
        self.label1 = Label(self.root, textvariable=self.varString1, relief=FLAT, width=0)
        self.label2 = Label(self.root, textvariable=self.varString2, relief=FLAT, width=0)
        self.label3 = Label(self.root, textvariable=self.varString3, relief=FLAT, width=0)
        self.label4 = Label(self.root, textvariable=self.varString4, relief=FLAT, width=0)
        self.label5 = Label(self.root, textvariable=self.varString5, relief=FLAT, width=0)
        self.label6 = Label(self.root, textvariable=self.varString6, relief=FLAT, width=0)
        self.label7 = Label(self.root, textvariable=self.varString7, relief=FLAT, width=0)
        self.label8 = Label(self.root, textvariable=self.varString8, relief=FLAT, width=0)
        self.label9 = Label(self.root, textvariable=self.varString9, relief=FLAT, width=0)
        self.labelDatosSinEMG = Label(self.root, textvariable=self.varDatosSinEMG, bg='lawn green', relief=GROOVE, width=0)
        self.labelDatosConEMG = Label(self.root, textvariable=self.varDatosConEMG, bg='lawn green', relief=GROOVE, width=0)
        self.labelTerminaDatos = Label(self.root, textvariable=self.varTerminarDatos,  bg='gray99',relief=GROOVE, width=0)

        self.labelStateDevice.place(x=35, y=40)
        self.label1.place(x=35, y=170)
        self.labelTerminaDatos.place(x=177, y=370)

        self.varStringStateDevice.set('Dispositivo Desconectado')
        self.varString1.set("Frecuencia de Muestre 1kHz")
        self.varString2.set("Sensor 1")
        self.varString3.set("Sensor 2")
        self.varString4.set("Sensor 3")
        self.varString5.set("Sensor 4")
        self.varString6.set("Sensor 5")
        self.varString7.set("Sensor 6")
        self.varString8.set("Sensor 7")
        self.varString9.set("Sensor 8")

        self.varStringCheck1.set("1")
        self.varStringCheck2.set("0")
        self.varStringCheck3.set("0")
        self.varStringCheck4.set("0")
        self.varStringCheck5.set("0")
        self.varStringCheck6.set("0")
        self.varStringCheck7.set("0")
        self.varStringCheck8.set("0")
        self.varStringCheck9.set("0")

        self.varFlagCheck2.set("0")
        self.varFlagCheck3.set("0")
        self.varFlagCheck4.set("0")
        self.varFlagCheck5.set("0")
        self.varFlagCheck6.set("0")
        self.varFlagCheck7.set("0")
        self.varFlagCheck8.set("0")
        self.varFlagCheck9.set("0")

        self.varDatosSinEMG.set('¡Tomando Datos Sin Estimulación!')
        self.varDatosConEMG.set('¡Tomando Datos Con Estimulación!')
        self.varTerminarDatos.set('¡Toma de Datos Terminada!')

        self.varStrMessageLabel1.set('Sensor 1')
        self.varSaveTypeData.set('0')

        pass

    # This function connects with the EMG device
    def connectDevice(self):
        try:
            _dataDEVICE = self.Delsys.ConnectDevice()
            #print(_dataDEVICE)
            if _dataDEVICE == b'Delsys Trigno System Digital Protocol Version 2.6 \r\n\r\n':
                self.varStringStateDevice.set('Dispositivo Conectado')
                self.labelStateDevice.config(bg = "lawn green")
                self.button1.config(relief=SUNKEN)
            else:
                self.varStringStateDevice.set('Dispositivo Desconectado')
                self.labelStateDevice.config(bg="gray99")
                self.button1.config(relief=RAISED)
            pass
        except:
            messagebox.showerror('Error de Conexión',
                                 'No se puede establecer conexión con el DELSYS. Verifique que el programa Trigno SDK se está ejecutando y el Delsys están encedidos y conectado al ordenador')

    # This function disconnects with the EMG device
    def disconnectDevice(self):

        self.Delsys.state = False
        self.DelsysACC.state = False
        self.DelsysEMG.state = False

        receiveData = self.Delsys.DisonnectDevice()
        self.varStringStateDevice.set('Dispositivo Desconectado')
        self.labelStateDevice.config(bg="gray99")
        self.button1.config(relief=RAISED)
        print(receiveData)
        pass

    # This function starts the sample EMG signlas
    def startSample(self):
        self.varSaveTypeData.set('0')   # Guarda los datos Sin tomar la información que arroja el TremUna
        self.Delsys.state = True
        self.DelsysEMG.state = True
        self.DelsysACC.state = True

        self.button4.config(relief=SUNKEN)
        self.button5.config(relief=RAISED)
        self.labelDatosSinEMG.place(x=157, y=210)
        self.labelDatosConEMG.place_forget()
        self.labelTerminaDatos.place_forget()

        self.Delsys.StartSample()
        Start1 = threading.Thread(target=self.DelsysEMG.StartEMGSample)#,args=(self.qsensortovarianza,))
        Start2 = threading.Thread(target=self.DelsysEMG.ReadFunction)  # ,args=(self.qsensortovarianza,))
        Start3 = threading.Thread(target=self.DelsysACC.StartACCSample)
        Start4 = threading.Thread(target=self.DelsysACC.ReadFunction)

        Start1.start()
        Start2.start()
        Start3.start()
        Start4.start()
        pass

    # This function starts the sample EMG signals and sends the data to FES interface
    def startSendData(self):
        self.varSaveTypeData.set('1')   # Guarda los datos tomando la información que arroja el TremUna
        self.Delsys.state = True        # Esta variable me activa el ciclo para calcular la varianza y enviar los datos el Tremuna
        self.DelsysEMG.state = True
        self.DelsysACC.state = True

        self.button4.config(relief=RAISED)
        self.button5.config(relief=SUNKEN)
        self.labelDatosConEMG.place(x=157, y=290)
        self.labelTerminaDatos.place_forget()
        self.labelDatosSinEMG.place_forget()

        self.Delsys.StartSample()
        Start1 = threading.Thread(target=self.DelsysEMG.StartEMGSample)
        Start2 = threading.Thread(target=self.DelsysEMG.ReadFunctionSendData)
        Start3 = threading.Thread(target=self.DelsysACC.StartACCSample)
        Start4 = threading.Thread(target=self.DelsysACC.ReadFunctionSendData)

        Start2.start()
        Start3.start()
        Start4.start()
        Start1.start()
        pass

    # This function stops the sample
    def stopSample(self):

        self.Delsys.state = False
        time.sleep(0.01)
        self.DelsysACC.state = False
        self.DelsysEMG.state = False

        self.labelDatosSinEMG.place_forget()
        self.labelTerminaDatos.place(x=177, y=370)
        self.labelDatosConEMG.place_forget()
        self.button4.config(relief=RAISED)
        self.button5.config(relief=RAISED)
        time.sleep(0.01)
        self.Delsys.StopSample()
        pass

    # This function setups the frequency sample, normally it stars in 2000Hz
    def sensorFrequency(self):
        self.Delsys.SensorFrequency(self.varStringCheck1.get())
        pass

    # This function confirms if the sensor are activated
    def sensorParied(self):
        try:
            if (self.varStringCheck2.get() == '1' and self.varFlagCheck2.get() == '0'):
                dataDEVICE = self.Delsys.SensorParied('1')
                if dataDEVICE == b'YES\r\n\r\n':
                    self.varFlagCheck2.set("1")
                else:
                    self.varFlagCheck2.set("0")
                    self.varStringCheck2.set("0")

            if (self.varStringCheck3.get() == '1' and self.varFlagCheck3.get() == '0'):
                dataDEVICE = self.Delsys.SensorParied('2')
                if dataDEVICE == b'YES\r\n\r\n':
                    self.varFlagCheck3.set("1")
                else:
                    self.varFlagCheck3.set("0")
                    self.varStringCheck3.set("0")

            if (self.varStringCheck4.get() == '1' and self.varFlagCheck4.get() == '0'):
                dataDEVICE = self.Delsys.SensorParied('3')
                if dataDEVICE == b'YES\r\n\r\n':
                    self.varFlagCheck4.set("1")
                else:
                    self.varFlagCheck4.set("0")
                    self.varStringCheck4.set("0")

            if (self.varStringCheck5.get() == '1' and self.varFlagCheck5.get() == '0'):
                dataDEVICE = self.Delsys.SensorParied('4')
                if dataDEVICE == b'YES\r\n\r\n':
                    self.varFlagCheck5.set("1")
                else:
                    self.varFlagCheck5.set("0")
                    self.varStringCheck5.set("0")

            if (self.varStringCheck6.get() == '1' and self.varFlagCheck6.get() == '0'):
                dataDEVICE = self.Delsys.SensorParied('5')
                if dataDEVICE == b'YES\r\n\r\n':
                    self.varFlagCheck6.set("1")
                else:
                    self.varFlagCheck6.set("0")
                    self.varStringCheck6.set("0")

            if (self.varStringCheck7.get() == '1' and self.varFlagCheck7.get() == '0'):
                dataDEVICE = self.Delsys.SensorParied('6')
                if dataDEVICE == b'YES\r\n\r\n':
                    self.varFlagCheck7.set("1")
                else:
                    self.varFlagCheck7.set("0")
                    self.varStringCheck7.set("0")

            if (self.varStringCheck8.get() == '1' and self.varFlagCheck8.get() == '0'):
                dataDEVICE = self.Delsys.SensorParied('7')
                if dataDEVICE == b'YES\r\n\r\n':
                    self.varFlagCheck8.set("1")
                else:
                    self.varFlagCheck8.set("0")
                    self.varStringCheck8.set("0")

            if (self.varStringCheck9.get() == '1' and self.varFlagCheck9.get() == '0'):
                dataDEVICE = self.Delsys.SensorParied('8')
                if dataDEVICE == b'YES\r\n\r\n':
                    self.varFlagCheck9.set("1")
                else:
                    self.varFlagCheck9.set("0")
                    self.varStringCheck9.set("0")

            if (self.varStringCheck2.get() == '0'):
                self.varFlagCheck2.set("0")

            if (self.varStringCheck3.get() == '0'):
                self.varFlagCheck3.set("0")

            if (self.varStringCheck4.get() == '0'):
                self.varFlagCheck4.set("0")

            if (self.varStringCheck5.get() == '0'):
                self.varFlagCheck5.set("0")

            if (self.varStringCheck6.get() == '0'):
                self.varFlagCheck6.set("0")

            if (self.varStringCheck7.get() == '0'):
                self.varFlagCheck7.set("0")

            if (self.varStringCheck8.get() == '0'):
                self.varFlagCheck8.set("0")

            if (self.varStringCheck9.get() == '0'):
                self.varFlagCheck9.set("0")

            self.PlotDelsys.flagsensor[0] = self.varFlagCheck2.get()
            self.PlotDelsys.flagsensor[1] = self.varFlagCheck3.get()
            self.PlotDelsys.flagsensor[2] = self.varFlagCheck4.get()
            self.PlotDelsys.flagsensor[3] = self.varFlagCheck5.get()
            self.PlotDelsys.flagsensor[4] = self.varFlagCheck6.get()
            self.PlotDelsys.flagsensor[5] = self.varFlagCheck7.get()
            self.PlotDelsys.flagsensor[6] = self.varFlagCheck8.get()
            self.PlotDelsys.flagsensor[7] = self.varFlagCheck9.get()

        except:
            print('Andres')
            self.varStringCheck2.set('0')
            self.varStringCheck3.set('0')
            self.varStringCheck4.set('0')
            self.varStringCheck5.set('0')
            self.varStringCheck6.set('0')
            self.varStringCheck7.set('0')
            self.varStringCheck8.set('0')
            self.varStringCheck9.set('0')
            messagebox.showwarning('Error de Conexión',
                                 'Primero establesca conexión entre la interfaz y el Dispositivo Delsys.')
            pass

    # This function calls the method
    def plotdataEMGandVar(self):
        self.PlotDelsys.plotEMGandVar()
        pass

    def plotdataEMGVar(self):
        self.PlotDelsys.plotEMGVar()
        pass

    def plotdataACC(self):
        self.PlotDelsys.plotACC()
        pass

    def plotdataACCVar(self):
        self.PlotDelsys.plotACCVar()
        pass

    def savefileName(self,event=None):
        self.Delsys.patientName = self.entryPatientName.get()
        self.Delsys.MeasuredMuscles = [self.entryMuscle1.get(), self.entryMuscle2.get(), self.entryMuscle3.get(), self.entryMuscle4.get(), self.entryMuscle5.get(), self.entryMuscle6.get(), self.entryMuscle7.get(), self.entryMuscle8.get()]
        pass

    def nameMuscle(self, event=None):
        self.PlotDelsys.MeasuredMuscles = [self.entryMuscle1.get(), self.entryMuscle2.get(), self.entryMuscle3.get(), self.entryMuscle4.get(), self.entryMuscle5.get(), self.entryMuscle6.get(), self.entryMuscle7.get(), self.entryMuscle8.get()]
        pass

    def saveData(self):
        self.Delsys.SaveData(self.varSaveTypeData.get())
        pass

if __name__ == '__main__':

    gui = Delsys_Interface_1_1()

    gui.entryPatientName.bind('<Return>',gui.savefileName)
    gui.entryMuscle1.bind('<Return>', gui.nameMuscle)
    gui.entryMuscle2.bind('<Return>', gui.nameMuscle)
    gui.entryMuscle3.bind('<Return>', gui.nameMuscle)
    gui.entryMuscle4.bind('<Return>', gui.nameMuscle)
    gui.entryMuscle5.bind('<Return>', gui.nameMuscle)
    gui.entryMuscle6.bind('<Return>', gui.nameMuscle)
    gui.entryMuscle7.bind('<Return>', gui.nameMuscle)
    gui.entryMuscle8.bind('<Return>', gui.nameMuscle)

    gui.root.mainloop()