

from tkinter import messagebox

import numpy
import decimal
import socket
import time
import queue
import scipy.io

import psutil, os
p = psutil.Process(os.getpid())
p.nice(psutil.HIGH_PRIORITY_CLASS)

class ConnectionDelsys_1_4():

    # Puerto de comunicación con el Delsys para el control de datos EMG y ACC
    TCP_IP = 'localhost'#"192.168.42.240"
    DEVICE_PORT = 50040
    EMG_PORT = 50041
    #ACC_PORT = 50042
    CLIENTE_PORT = 5005

    BUFFER_SIZE_DEVICE = 64
    BUFFER_SIZE_INTERAPPS = 16
    QUERY_BUFFER_SIZE_INTERAPPS = 2

    # Puerto de comunicación con el Delsys para el control de datos EMG y ACC
    sDEVICE = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Establish a TCP/IP socket with the main device
    MeasuredMuscles = ['Músculo 1', 'Músculo 2', 'Músculo 3', 'Músculo 4', 'Músculo 5', 'Músculo 6', 'Músculo 7','Músculo 8']
    patientName = 'Nombre del Paciente'

    def __init__(self):
        self.powFraction=numpy.array([[5.00000000e-01],[2.50000000e-01],[1.25000000e-01],[ 6.25000000e-02],[3.12500000e-02],[1.56250000e-02],[7.81250000e-03],[3.90625000e-03],[1.95312500e-03],[9.76562500e-04],[4.88281250e-04],[2.44140625e-04],[1.22070312e-04],[6.10351562e-05],[3.05175781e-05],[1.52587891e-05],[7.62939453e-06],[3.81469727e-06],[1.90734863e-06],[ 9.53674316e-07],[4.76837158e-07],[2.38418579e-07],[1.19209290e-07]],dtype=numpy.float32)
        pass

    # Ésta función realiza la decodificación de los datos que viene del EMG Delsys por el metodo IEEE float
    def DecodificationEMGData(self,dataDevice):
        dataBinary = numpy.unpackbits(numpy.fromstring(dataDevice, dtype=numpy.uint8))
        return numpy.prod([ numpy.power((-1),int(numpy.array(dataBinary[0]))),numpy.add(1,numpy.dot(dataBinary[9:33],self.powFraction)) ,numpy.power(2,int(numpy.packbits(dataBinary[1:9])) - 127,dtype=float)])
        pass

    # Ésta función realiza el conexionado con el dispositivo Delsys y realiza la conficuración inicial
    def ConnectDevice(self):

        self.sDEVICE = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # Establish a TCP/IP socket with the main device
        self.sDEVICE.connect((self.TCP_IP, self.DEVICE_PORT))
        
        _dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
        print(_dataDEVICE)

        self.sDEVICE.send(b'MASTER\r\n\r\n')
        dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
        print('Se tomó el como NEW MASTER: %s' % dataDEVICE)

        self.sDEVICE.send(b'TRIGGER?\r\n\r\n')
        dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
        print('El TRIGGER se encuentra en esatdo: %s ' % dataDEVICE)

        self.sDEVICE.send(b'TRIGGER STOP OFF\r\n\r\n')
        dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
        print('El TRIGGER ahora se encuentra en STOP: %s ' % dataDEVICE)

        self.sDEVICE.send(b'UPSAMPLING?\r\n\r\n')
        dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
        print('El UPSAMPLIG está en modo: %s ' % dataDEVICE)

        self.sDEVICE.send(b'UPSAMPLE ON\r\n\r\n')
        dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
        print('Frecuencia de muestre de 2kHz ON es: %s ' % dataDEVICE)

        #self.sDEVICE.send(b'SENSOR 1 TYPE?\r\n\r\n')
        #dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
        #print('El SENSOR 1 está en tipo: %s ' % dataDEVICE)

        #self.sDEVICE.send(b'SENSOR 1 SERIAL?\r\n\r\n')
        #dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
        #print('El SENSOR 1 SERIAL está en: %s ' % dataDEVICE)

        self.sDEVICE.send(b'SENSOR 1 FIRMWARE?\r\n\r\n')
        dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
        print('El SENSOR 1 FIRMWARE es: %s ' % dataDEVICE)

        self.sDEVICE.send(b'SENSOR 1 PAIRED?\r\n\r\n')
        dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
        print('La paridad del SENSOR 1 es: %s ' % dataDEVICE)

        #self.sDEVICE.send(b'SENSOR 1 CHANNEL 1 GAIN?\r\n\r\n')
        #dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
        #print('El canal del SENSOR 1 es: %s ' % dataDEVICE)

        #self.sDEVICE.send(b'SENSOR 1 CHANNEL 2 UNITS?\r\n\r\n')
        #dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
        #print('La unidad del SENSOR 1 es: %s ' % dataDEVICE)

        self.sDEVICE.send(b'ENDIAN BIG\r\n\r\n')
        dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
        print('ENDIAN BIG de los SENSORES es: %s ' % dataDEVICE)

        self.sDEVICE.send(b'ENDIANNESS?\r\n\r\n')
        dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
        print('ENDIAN BIG de los SENSORES es: %s ' % dataDEVICE)

        return _dataDEVICE

    # Ésta función realiza la desconexión con el dispositivo Delsys y cierra los puertos de conexión
    def DisonnectDevice(self):

        self.sDEVICE.send(b'STOP\r\n\r\n')
        dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
        #self.sEMG.close()
        #self.sACC.close()
        self.sDEVICE.close()
        #self.sEMG.close()
        print('La toma de datos de se finalizado: %s' % dataDEVICE)
        return dataDEVICE

    # Ésta función revisa si los sensores están conectados con el dispositivo Delsys
    def SensorParied(self, nsensor):
        print(type(nsensor))
        ns = bytes(nsensor, 'utf-8')
        print(type(ns))
        ns = b"".join([b'SENSOR ',ns,b' PAIRED?\r\n\r\n'])
        print(ns)
        self.sDEVICE.send(ns)
        dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
        print('La paridad del SENSOR '+nsensor+' es: %s ' % dataDEVICE)
        return dataDEVICE
        pass

    # Ésta función configura la frecuencia de muestreo de los sensores
    def SensorFrequency(self,switch):

        if(switch == '1'):
            self.sDEVICE.send(b'UPSAMPLE ON\r\n\r\n')
            dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
            print('Frecuencia de muestre de 2kHz ON es: %s ' % dataDEVICE)
        else:
            self.sDEVICE.send(b'UPSAMPLE OFF\r\n\r\n')
            dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
            print('Frecuencia de muestre de 2kHz OFF es: %s ' % dataDEVICE)
        pass

    # Ésta función detiene la muestreo
    def StopSample(self):

        self.sDEVICE.send(b'STOP\r\n\r\n')
        dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
        print('El muestre de los datos a terminado: %s ' % dataDEVICE)
        #self.sEMG.close()
        pass
    
    # Ésta función comienza la lectura EMG de los sensores y realiza la decodificación las muestas guardando los datos en un queue
    # y en una tabla de texto .txt
    def StartSample(self):

        self.sDEVICE.send(b'START\r\n\r\n')
        dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)

        print('Comienza la lectura EMG de los Sensores: %s ' % dataDEVICE)
        print('Comienzo de la lectura de los Sensor')

        pass

    def SaveData(self,type):

        if type =='0':

            ### Datos de EMG
            data_EMG = open('dataEMG.txt', 'r')
            variance_EMG = open('varianceEMG.txt', 'r')

            length = 410000  # 303998 portatil y 359338 escritorio muestran en aprox 5 mins
            value_EMG = numpy.zeros((length, 9))#,dtype=numpy.dtype(decimal.Decimal))  # se tiene 9 datos uno para tiempo y los demás para sensores
            line = '0'
            t_EMG = 0
            while len(line) > 0:
                line = numpy.array(data_EMG.readline().split()).astype(float)
                if len(line) > 0:
                    value_EMG[t_EMG, :] = line[0:9]     # Matriz donde se guarda la inf de dataEMG
                    t_EMG = t_EMG + 1
            data_EMG.close()

            length = 20000  # 6076 portatil 10883 escritorio muestras en aprox 5 mins
            var_EMG = numpy.zeros((length, 9))#, dtype=numpy.float)  ## matriz de calculo de valores
            line = '0'
            t_varEMG = 0
            while len(line) > 0:
                line = numpy.array(variance_EMG.readline().split()).astype(float)
                if len(line) > 0:
                    var_EMG[t_varEMG, :] = line[0:9]     # Matriz donde se guarda la inf de varianceEMG
                    t_varEMG = t_varEMG + 1
            variance_EMG.close()

            ### Datos de ACC
            data_ACC = open('dataACC.txt', 'r')
            variance_ACC = open('varianceACC.txt', 'r')

            length = 60000  # 44993 muestras en aprox 5 mins
            value_ACC = numpy.zeros((length, 25))#, dtype=numpy.dtype(decimal.Decimal))  # se tiene 9 datos uno para tiempo y los demás para sensores

            line = '0'
            t_ACC = 0
            while len(line) > 0:
                line = numpy.array(data_ACC.readline().split()).astype(float)
                if len(line) > 0:
                    value_ACC[t_ACC, :] = line[0:25]         #Matriz donde se guarda los la inf de dataACC
                    t_ACC = t_ACC + 1
            data_ACC.close()

            length = 25000  # 6076 portatil 10883 escritorio muestras en aprox 5 mins
            var_ACC = numpy.zeros((length, 25))#, dtype=numpy.float)  ## matriz de calculo de valores
            line = '0'
            t_varACC = 0
            while len(line) > 0:
                line = numpy.array(variance_ACC.readline().split()).astype(float)
                if len(line) > 0:
                    var_ACC[t_varACC, :] = line[0:25]
                    t_varACC = t_varACC + 1
            variance_ACC.close()


            EMG = {'measuredMuscle': self.MeasuredMuscles, 'dataEMG': value_EMG[1:t_EMG,:], 'varianceEMG': var_EMG[1:t_varEMG,:]}
            ACC = {'dataACC': value_ACC[1:t_ACC,:], 'VarianceACC': var_ACC[1:t_varACC,:]}
            dataList = {'DataEMG': EMG, 'DataACC': ACC, 'PatientName': self.patientName}

            fileName = self.patientName + '_' +'Sin Terapia'+'_'+str(time.localtime().tm_year)+str(time.localtime().tm_mon)+str(time.localtime().tm_mday)+'_'+str(time.localtime().tm_hour)+str(time.localtime().tm_min)+str(time.localtime().tm_sec)+'.mat'

        else:

            ### Datos de EMG
            data_EMG = open('dataEMG.txt', 'r')
            variance_EMG = open('varianceEMG.txt', 'r')

            length = 410000  # 303998 portatil y 359338 escritorio muestran en aprox 5 mins
            value_EMG = numpy.zeros((length,
                                     9))  # ,dtype=numpy.dtype(decimal.Decimal))  # se tiene 9 datos uno para tiempo y los demás para sensores
            line = '0'
            t_EMG = 0
            while len(line) > 0:
                line = numpy.array(data_EMG.readline().split()).astype(float)
                if len(line) > 0:
                    value_EMG[t_EMG, :] = line[0:9]  # Matriz donde se guarda la inf de dataEMG
                    t_EMG = t_EMG + 1
            data_EMG.close()

            length = 20000  # 6076 portatil 10883 escritorio muestras en aprox 5 mins
            var_EMG = numpy.zeros((length, 9))  # , dtype=numpy.float)  ## matriz de calculo de valores
            line = '0'
            t_varEMG = 0
            while len(line) > 0:
                line = numpy.array(variance_EMG.readline().split()).astype(float)
                if len(line) > 0:
                    var_EMG[t_varEMG, :] = line[0:9]  # Matriz donde se guarda la inf de varianceEMG
                    t_varEMG = t_varEMG + 1
            variance_EMG.close()

            ### Datos de ACC
            data_ACC = open('dataACC.txt', 'r')
            variance_ACC = open('varianceACC.txt', 'r')

            length = 60000  # 44993 muestras en aprox 5 mins
            value_ACC = numpy.zeros((length,
                                     25))  # , dtype=numpy.dtype(decimal.Decimal))  # se tiene 9 datos uno para tiempo y los demás para sensores

            line = '0'
            t_ACC = 0
            while len(line) > 0:
                line = numpy.array(data_ACC.readline().split()).astype(float)
                if len(line) > 0:
                    value_ACC[t_ACC, :] = line[0:25]  # Matriz donde se guarda los la inf de dataACC
                    t_ACC = t_ACC + 1
            data_ACC.close()

            length = 25000  # 6076 portatil 10883 escritorio muestras en aprox 5 mins
            var_ACC = numpy.zeros((length, 25))  # , dtype=numpy.float)  ## matriz de calculo de valores
            line = '0'
            t_varACC = 0
            while len(line) > 0:
                line = numpy.array(variance_ACC.readline().split()).astype(float)
                if len(line) > 0:
                    var_ACC[t_varACC, :] = line[0:25]
                    t_varACC = t_varACC + 1
            variance_ACC.close()

            ### Datos de Estimulación
            data_stimulation = open('stimulation.txt', 'r')
            length = 60000  # 44993 muestras en aprox 5 mins
            value_stimulation = numpy.zeros((length,9))  # , dtype=numpy.dtype(decimal.Decimal))  # se tiene 9 datos uno para tiempo y los demás para sensores

            line = '0'
            t_stimulation = 0

            while len(line) > 0:
                line = numpy.array(data_stimulation.readline().split()).astype(float)
                if len(line) > 0:
                    value_stimulation[t_stimulation, :] = line[0:9]  # Matriz donde se guarda los la inf de dataACC
                    t_stimulation = t_stimulation + 1
            data_stimulation.close()

            infTherapy = open('infTherapy.txt', 'r')
            line = numpy.array(infTherapy.readline().split())
            inf_Therapy = {'Therapy':line[0],'Frequency':numpy.float(line[1]),'PW':numpy.float(line[2]),'DT':numpy.float(line[3]),'PN':numpy.float(line[4])}
            line = numpy.array(infTherapy.readline().split())
            Sti_Muscle = line[0:9]
            infTherapy.close()

            EMG = {'measuredMuscle': self.MeasuredMuscles, 'dataEMG': value_EMG[0:t_EMG, :],'varianceEMG': var_EMG[0:t_varEMG, :]}
            ACC = {'dataACC': value_ACC[0:t_ACC, :], 'VarianceACC': var_ACC[0:t_varACC, :]}
            STIMULATION ={'InformationTherapy':inf_Therapy,'StimulatedMuscle':Sti_Muscle,'dataStimulacion':value_stimulation[0:t_stimulation,:]}

            dataList = {'DataEMG': EMG, 'DataACC': ACC,'DataStimulation':STIMULATION ,'PatientName': self.patientName}

            fileName = self.patientName + '_' +inf_Therapy['Therapy']+'_'+str(time.localtime().tm_year)+str(time.localtime().tm_mon)+str(time.localtime().tm_mday)+'_'+str(time.localtime().tm_hour)+str(time.localtime().tm_min)+str(time.localtime().tm_sec)+'.mat'

        scipy.io.savemat(fileName,{'DataPatient'+dataList['PatientName']:dataList})

        pass



