import sys
import socket
import time
import serial
import winsound
import string
import numpy
import queue
import numba
import scipy.io as sio

import psutil, os

p = psutil.Process(os.getpid())
p.nice(psutil.HIGH_PRIORITY_CLASS)


class ConnectionTremuna_1_2():

    TCP_IP = 'localhost'
    SERVER_PORT_EMG = 5005
    SERVER_PORT_ACC = 5007
    num_ports = 226
    verbose = True
    portNumber = 'COM9'  # ser = serial.Serial()
    x_byte = b''
    x_string = ' '
    CheckOn = 0
    CheckConnection = False
    FileName = 'TituloVacio'
    ser = serial.Serial()

    sINTERAPPS_EMG = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sINTERAPPS_ACC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ensembleCurrent = [0, 0, 0, 0, 0, 0, 0, 0]
    ensembleFrequency = [0, 0, 0, 0, 0, 0, 0, 0]
    ensemblePW_0 = bytearray([0, 0, 0, 0, 0, 0, 0, 0])
    ensemblePW_1 = bytearray([0, 0, 0, 0, 0, 0, 0, 0])
    ensembleDT_0 = bytearray([0, 0, 0, 0, 0, 0, 0, 0])
    ensembleDT_1 = bytearray([0, 0, 0, 0, 0, 0, 0, 0])
    ensemblePN_0 = bytearray([0, 0, 0, 0, 0, 0, 0, 0])
    ensemblePN_1 = bytearray([0, 0, 0, 0, 0, 0, 0, 0])

    EMG1 = 0    # Deltoids
    EMG2 = 0    # Biceps
    EMG3 = 0    # Triceps
    EMG4 = 0
    EMG5 = 0    # Deltoids
    EMG6 = 0    # Biceps
    EMG7 = 0    # Triceps
    EMG8 = 0
    ACC1 = 0.2

    qsensorsEMG = queue.Queue()            # queue.Queue(maxsize=0)
    qsensorsACC = queue.Queue()             # queue.Queue(maxsize=0)
    qcurrents = queue.Queue()           # queue.Queue(maxsize=0)

    stimulatedMuscles = ['Vacio1','Vacio2','Vacio3','Vacio4','Vacio5','Vacio6','Vacio7','Vacio8']
    Frequency = 0
    PW = 0
    DT = 0
    PN = 0

    BUFFER_SIZE = 16  # Normally 1024, but we want fast response
    QUERY_DIGIT_SIZE = 1
    QUERY_BUFFER_SIZE = 2

    maskReceived = 0
    currentReceived = 0
    currentDataReceived = numpy.array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=numpy.float)
    frequencyReceived = 0
    pwReceived = []
    dtReceived = []
    pnReceived = []
    currents = [0, 0, 0, 0, 0, 0, 0, 0]
    frequencies = [0, 0, 0, 0, 0, 0, 0, 0]

    canalsArrayBits = []  # Arreglo de bites para realizar la mascara
    canalInt = 0  # El número en entero para las demás funciones de configuración

    flag = False

    # Función que realiza una busqueda de los puertos que está utilizando el computador
    def scanDevice(self):
        #  def scan(num_ports=226, verbose=True):
        # -- Lista de los dispositivos serie. Inicialmente vacia
        dispositivos_serie = []
        if self.verbose:
            print("Escanenado %d puertos serie:" % self.num_ports)
            # -- Escanear num_port posibles puertos serie
        for i in range(self.num_ports):
            if self.verbose:
                sys.stdout.write("puerto %d: " % i)
                sys.stdout.flush()
            try:
                # -- Abrir puerto serie
                ser = serial.Serial('COM' + str(i))  ##
                if self.verbose:
                    print("OK --> %s" % ser.portstr)
                    # -- Si no hay errores, anadir el numero y nombre a la lista
                    dispositivos_serie.append(ser.portstr)
                    ser.close()
                    # -- Si hay un error se ignora
            except:
                if self.verbose: print("NO")
            pass
            # -- Devolver la lista de los dispositivos serie encontrados
        return dispositivos_serie

    # Función que conecta el Tremuna al puerto escogido en el ListBox
    def ConnectDevice(self):
        try:
            self.ser = serial.Serial(self.portNumber, baudrate=510000, bytesize=8, parity='N', stopbits=1, timeout=0.1)
            self.ser.write(b'>OFF<')  # Funciona
            self.x_string = self.ReceivedData(self.ser)
            b = ">OK<"
            print('Tratando de Conectarse a Puerto')
            if self.x_string == b:
                print('El Puerto se ha Conectado')
                print(self.x_string)
                self.CheckOn = 1
            else:
                print('El Puerto NO se ha Conectado')
        except:
            if self.CheckOn == 1:
                print("El puerto se conectado anteriormente")
            else:
                print("Hubo un error en la conexión")
        return self.x_string

    def DisonnectDevice(self):

        try:
            print(self.portNumber)
            self.ser.write(b'>OFF<')  # Funciona
            self.x_string = self.ReceivedData(self.ser)

            b = ">OK<"

            print('Tratando de desconectarse al puerto')

            if self.x_string == b:
                print('El puerto se ha desconectado')
                print(self.x_string)
                self.ser.close()
                self.CheckOn = 0
            else:
                print('El puerto no se ha desconectado')
        except:
            if self.CheckOn == 0:
                print("El puerto %s a desconectado anteriormente" % self.ser.portstr)

    def SendDataDevice(self):
        MASK = self.MaskData()
        pass

    def TurnOnDevice(self):
        self.ser.write(b'>ON<')         #>ON<
        self.x_string = self.ReceivedData(self.ser)
        return self.x_string
        pass

    def TurnOffDevice(self):

        self.ser.write(b'>OFF<')        #>OFF<
        self.x_string = self.ReceivedData(self.ser)
        self.sINTERAPPS_EMG.close()
        return self.x_string
        pass

    # Función que Recibe los datos enviados por el Tremuna
    def ReceivedData(self, ser):

        answer = b''
        i = 1
        while i < 5:
            i = i + 1
            # print (i)
            x = ser.read(1)
            if x == b'<':
                answer = answer + x
                break
            else:
                answer = answer + x
        return answer.decode('utf-8')

    # Función que realiza una mascara para dar decir que canal se debe activar
    def MaskData(self):
        print(self.canalsArrayBits)
        # Toma el arreglo de de 1's en string y los junta para luego guardar en una sola variable
        canalsBits = ''.join(self.canalsArrayBits)
        # Toma la variable de string en bits y los pasa a binario para luego pasar lo a entero
        canalsMask = int(canalsBits, 2)
        mask = [62, 83, 65, 59, canalsMask, 60]     #>SA;x<
        self.ser.write(mask)
        return mask
        pass

    def CurrentData(self):
        current = [62, 67, self.canalInt, 59, self.currentReceived, 60]                 #>Cn;c<
        self.ser.write(current)
        pass

    def CurrentsData(self):
        current = [62, 83, 67, 59, self.currents[0], self.currents[1], self.currents[2], self.currents[3], self.currents[4],
                   self.currents[5], self.currents[6], self.currents[7], 60]                #>SC;c1 c2 c3 c4 c5 c6 c7 c8<
        self.ser.write(current)
        print(current)
        print(self.ReceivedData(self.ser))
        #time.sleep(0.05)
        pass

    def FrequencyData(self):
        print(self.frequencyReceived)
        frequency = [62, 70, self.canalInt, 59, self.frequencyReceived, 60]             #>Fn;f<
        self.ser.write(frequency)
        return frequency
        pass

    def FrequenciesData(self):
        frequency = [62, 83, 70, 59, self.frequencies[0], self.frequencies[1], self.frequencies[2], self.frequencies[3], self.frequencies[4],
                     self.frequencies[5], self.frequencies[6], self.frequencies[7], 60]     #>SF;f1 f2 f3 f4 f5 f6 f7 f8<
        self.ser.write(frequency)
        print(self.ReceivedData(self.ser))
        pass

    def PWData(self):
        print(self.pwReceived)
        pw = [62, 87, self.canalInt, 59, self.pwReceived[0], self.pwReceived[1], 60]    #Wn;wh wl<
        self.ser.write(pw)
        return pw
        pass

    def DTData(self):
        print(self.dtReceived)
        dt = [62, 68, self.canalInt, 59, self.dtReceived[0], self.dtReceived[1], 60]
        self.ser.write(dt)
        return dt

    def PNData(self):
        print(self.pnReceived)
        pn = [62, 78, self.canalInt, 59, self.pnReceived[0], self.pnReceived[1], 60]
        self.ser.write(pn)
        return pn
        pass

    # Esta función realiza una configuración conjunta de los parametros
    def EnsembleConfiguration(self):
        
        ce = [62, 83, 80, 59, self.ensembleCurrent[0], self.ensembleFrequency[0], self.ensemblePW_0[0], self.ensemblePW_1[0], self.ensembleDT_0[0], self.ensembleDT_1[0], self.ensemblePN_0[0], self.ensemblePN_1[0],
                              self.ensembleCurrent[1], self.ensembleFrequency[1], self.ensemblePW_0[1], self.ensemblePW_1[1], self.ensembleDT_0[1], self.ensembleDT_1[1], self.ensemblePN_0[1], self.ensemblePN_1[1],
                              self.ensembleCurrent[2], self.ensembleFrequency[2], self.ensemblePW_0[2], self.ensemblePW_1[2], self.ensembleDT_0[2], self.ensembleDT_1[2], self.ensemblePN_0[2], self.ensemblePN_1[2],
                              self.ensembleCurrent[3], self.ensembleFrequency[3], self.ensemblePW_0[3], self.ensemblePW_1[3], self.ensembleDT_0[3], self.ensembleDT_1[3], self.ensemblePN_0[3], self.ensemblePN_1[3],
                              self.ensembleCurrent[4], self.ensembleFrequency[4], self.ensemblePW_0[4], self.ensemblePW_1[4], self.ensembleDT_0[4], self.ensembleDT_1[4], self.ensemblePN_0[4], self.ensemblePN_1[4],
                              self.ensembleCurrent[5], self.ensembleFrequency[5], self.ensemblePW_0[5], self.ensemblePW_1[5], self.ensembleDT_0[5], self.ensembleDT_1[5], self.ensemblePN_0[5], self.ensemblePN_1[5],
                              self.ensembleCurrent[6], self.ensembleFrequency[6], self.ensemblePW_0[6], self.ensemblePW_1[6], self.ensembleDT_0[6], self.ensembleDT_1[6], self.ensemblePN_0[6], self.ensemblePN_1[6],
                              self.ensembleCurrent[7], self.ensembleFrequency[7], self.ensemblePW_0[7], self.ensemblePW_1[7], self.ensembleDT_0[7], self.ensembleDT_1[7], self.ensemblePN_0[7], self.ensemblePN_1[7],
                              60]
        self.ser.write(ce)
        pass

    def EMGConnection(self):

        try:
            # Conexión TCP/IP como Server para la comunicación con el Delsys
            self.sINTERAPPS_EMG = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sINTERAPPS_EMG.bind((self.TCP_IP, self.SERVER_PORT_EMG))
            self.sINTERAPPS_EMG.listen(1)
            conn, addr = self.sINTERAPPS_EMG.accept()
            print('Conexion TCP/IP EMG')
            QUERY_BUFFER_SIZE = 2
           
            while (self.flag==True):
                try:
                    # Recibe el número de caracteres que tiene la trama de datos por ejemplo 140
                    data = conn.recv(QUERY_BUFFER_SIZE)         # self.QUERY_BUFFER_SIZE = 3 y data='140'
                    self.BUFFER_SIZE = int(data.decode('utf-8'))
                    #print(self.BUFFER_SIZE)
                    data = conn.recv(self.BUFFER_SIZE)
                    decodata = (data.decode('utf-8')).split()
                    #print(decodata)


                    self.qsensorsEMG.put(decodata)
                    
                except (OSError, ValueError):
                    print('No se pudo realizar la conexión TCP/IP del Termuna con el Delsys EMG')
                    conn.close()
                    self.sINTERAPPS_EMG.close()
                    self.qsensorsEMG.put([0,0,0,0,0,0,0,0])
                    self.flag = False
                    break
            conn.close()
            self.sINTERAPPS_EMG.close()
        except(OSError):
            print('Ya estableció una conexión TCP/IP del Termuna con el Delsys anteriormente EMG')
            self.qsensorsEMG.put([0, 0, 0, 0, 0, 0, 0, 0])
            self.flag = False
        self.sINTERAPPS_EMG.close()
        self.flag = False
        print('Se terminó la conexión TCP/IP del Termuna con el Delsys EMG')
        pass

    def ACCConnection(self):
        try:
            # Conexión TCP/IP como Server para la comunicación con el Delsys
            self.sINTERAPPS_ACC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sINTERAPPS_ACC.bind((self.TCP_IP, self.SERVER_PORT_ACC))
            self.sINTERAPPS_ACC.listen(1)
            conn, addr = self.sINTERAPPS_ACC.accept()
            print('Conexion TCP/IP ACC')

            QUERY_BUFFER_SIZE = 3

            while (self.flag==True):
                try:
                    # Recibe el número de caracteres que tiene la trama de datos por ejemplo 140
                    data = conn.recv(QUERY_BUFFER_SIZE)         # self.QUERY_BUFFER_SIZE = 3 y data='140'
                    self.BUFFER_SIZE = int(data.decode('utf-8'))
                    data = conn.recv(self.BUFFER_SIZE)
                    decodata = (data.decode('utf-8')).split()
                    self.qsensorsACC.put(decodata)

                except (OSError, ValueError):
                    print('No se pudo realizar la conexión TCP/IP del Termuna con el Delsys ACC')
                    conn.close()
                    self.sINTERAPPS_ACC.close()
                    self.qsensorsACC.put([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
                    self.flag = False
                    break
            conn.close()
            self.sINTERAPPS_ACC.close()

        except(OSError):
            print('Ya estableció una conexión TCP/IP del Termuna con el Delsys anteriormente ACC')
            self.qsensorsACC.put([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            self.flag = False
        self.sINTERAPPS_ACC.close()
        self.flag = False
        print('Se terminó la conexión TCP/IP del Termuna con el Delsys ACC')
        pass


    def CanalsControl(self):
        
        length = 300000  # 6076 muestras en aprox 5 mins, con 150 es 10000 para 180 20000
        var = numpy.zeros((length, 9), dtype=numpy.float)  ## matriz de calculo de valores
        g = 1
        tic = time.perf_counter()
        while(self.flag==True):

            sensorsvalue = self.qsensorsEMG.get()
            
            valor = 2 + numpy.dot(10e7, float(sensorsvalue[0]))
            if valor > 10:
               valor = 10
            
            self.currents[0] = int(numpy.round(valor))
            self.ensembleCurrent[0] = self.currents[0]
            
            valor = 2 + numpy.dot(10e8, float(sensorsvalue[1]))
            if valor > 10:
                valor = 10
            
            self.ensembleCurrent[1] = int(numpy.round(valor))
            
            valor = 2 + numpy.dot(10e7, float(sensorsvalue[2]))
            if valor > 10:
                valor = 10
            
            self.ensembleCurrent[2] = int(numpy.round(valor))
            
            valor = 2 + numpy.dot(10e7, float(sensorsvalue[3]))
            if valor > 10:
                valor = 10
            #self.canalInt = 4
            self.ensembleCurrent[3] = int(numpy.round(valor))
            valor = 2 + numpy.dot(10e7, float(sensorsvalue[4]))
            if valor > 10:
                valor = 10
            #self.canalInt = 5
            self.ensembleCurrent[4] = int(numpy.round(valor))
            
            valor = 2 + numpy.dot(10e7, float(sensorsvalue[5]))
            if valor > 10:
                valor = 10
            self.ensembleCurrent[5] = int(numpy.round(valor))
            
            valor = 2 + numpy.dot(10e7, float(sensorsvalue[6]))
            if valor > 10:
                valor = 10
            self.ensembleCurrent[6] = int(numpy.round(valor))

            valor = 2 + numpy.dot(10e7, float(sensorsvalue[7]))
            if valor > 10:
                valor = 10
            
            self.ensembleCurrent[7] = int(numpy.round(valor))
            self.EnsembleConfiguration()
            
            var[g,1:9] = self.ensembleCurrent[0:8]#self.currents[0:8]
            var[g,0] = time.perf_counter()-tic
            g += 1

        currentTremuna = open('data.txt', 'w')
        
        for v in range(0, g):
            currentTremuna.write("   ".join(map(str, var[v,0:9])))
            currentTremuna.write('\n')

        print('Se han guardado lo datos de los canales')
        print('El número de muestras de corrient %d' % g)

        pass

    def PowerGraspControl(self,qState):

        length = 300000  # 6076 muestras en aprox 5 mins, con 150 es 10000 para 180 20000
        stimulation = numpy.zeros((length, 9), dtype=numpy.float)  ## matriz de valores de estimulación

        values_ACC = numpy.arange(length, dtype=numpy.float)  ## vector de calculo de valores
        values_ACC[0:length] = 0

        array_ACC_x = numpy.arange(150, dtype=numpy.float)
        array_ACC_x[0:150] = 0

        varianceACC_x = numpy.zeros((length, 2), dtype=numpy.float)  ## matriz de calculo de valores en la aceleración
        size_ACCVar = 0

        i_sizeACCVar = 0
        init = 100
        nsample = 136
        g=1     # Comienza desde 1 para dar el valor inicial al vector que guarda los datos de 0
        step = 1
        midstep = False

        self.ensembleCurrent[0] = 0
        # self.ensembleCurrent[3] = 0
        self.ensembleCurrent[4] = 0
        self.ensembleCurrent[5] = 0
        self.ensembleCurrent[6] = 0
        self.ensembleCurrent[7] = 0
        sensorsvalueEMG = self.qsensorsEMG.get()

        Gtic = time.perf_counter()
        while(self.flag==True):
            # Gtic = time.perf_counter()

                sensorsvalueACC = self.qsensorsACC.get()
            #print(sensorsvalueACC)
            # 0         tiempo
            # trama     sensor      i
            # 0,1,2     sensor 1    0
            # 3,4,5     sensor 2    1
            # 6,7,8     sensor 3    2
            # 9,10,11   sensor 4    3
            # 12,13,14  sensor 5    4
            # 15,16,17  sensor 6    5
            # 18,19,20  sensor 7    6
            # 21,22,23  sensor 8    7
            # sensorsvalueACC[(3*i)+1:(3*i)+3]
            #tiempo                 valor sensor 4 de X
                varianceACC_x=float(sensorsvalueACC[3*3])*100 # El eje en X del sensor 4

                sensorsvalueEMG = self.qsensorsEMG.get()
                valor_EMG_Deltoids = float(sensorsvalueEMG[0])*100000000
                valor_EMG_Biceps = float(sensorsvalueEMG[1])*100000000

                # Primer estado del control finito
                # Comienza el control finito de estados teniendo el brazo en reposo a un costado
                if step == 1:
                    if  valor_EMG_Deltoids>self.EMG1 and midstep==False:
                        midstep=True
                    elif  valor_EMG_Biceps>self.EMG2 and midstep==True:
                        step = 2
                        midstep=False
                        self.ensembleCurrent[1] = 0 # Electrodo 2
                    self.ensembleCurrent[2] = 0 # Electrodo 3
                    self.ensembleCurrent[3] = 0 # Electrodo 4

                # Segundo estado del control finito
                # Estimula los músculos extensores y se lleva la mano hacia le mesa al costado del vaso
                elif step == 2:
                    if valor_EMG_Deltoids<self.EMG1 and valor_EMG_Biceps<self.EMG2 and varianceACC_x<=self.ACC1:
                        tic = time.perf_counter()
                        step = 3
                    self.ensembleCurrent[1] = 10    # Electrodo 2
                    self.ensembleCurrent[2] = 0     # Electrodo 3
                    self.ensembleCurrent[3] = 5     # Electrodo 4

                # Tercer estado del control finito
                # Deja de estimular los músculos extensores y la mano esta a un costado del vaso
                elif step == 3:
                    if time.perf_counter()-tic>=3:
                       step=4
                    self.ensembleCurrent[1] = 0     # Electrodo 2
                    self.ensembleCurrent[2] = 0     # Electrodo 3
                    self.ensembleCurrent[3] = 5     # Electrodo 4

                # Cuarto estado del control finito
                # Estimula musculos flexores y toma el objeto sin levantar el brazo
                elif step == 4:
                    if  valor_EMG_Biceps>self.EMG5 and midstep==False:
                        midstep=True
                    elif  valor_EMG_Deltoids>self.EMG6 and midstep==True:
                        midstep=False
                        step = 5
                    self.ensembleCurrent[1] = 0     # Electrodo 2
                    self.ensembleCurrent[2] = 10    # Electrodo 3
                    self.ensembleCurrent[3] = 5     # Electrodo 4

                # Quinto estado del control finito
                # Estimula musculos flexores, teniendo el objeto en la mano lleva el mismo hacia la boca
                elif step == 5:
                    if valor_EMG_Deltoids<self.EMG1 and valor_EMG_Biceps<self.EMG2 and varianceACC_x<=self.ACC1:
                        tic = time.perf_counter()
                        step = 6
                    self.ensembleCurrent[1] = 0     # Electrodo 2
                    self.ensembleCurrent[2] = 10    # Electrodo 3
                    self.ensembleCurrent[3] = 5     # Electrodo 4

                # Sexto estado del control finito
                # Estimula musculos flexores, y tiene el objeto sobre la mesa
                elif step == 6:
                    if time.perf_counter()-tic>3 and varianceACC_x<=self.ACC1:
                        tic = time.perf_counter()
                        step = 7
                    self.ensembleCurrent[1] = 0     # Electrodo 2
                    self.ensembleCurrent[2] = 8    # Electrodo 3
                    self.ensembleCurrent[3] = 5     # Electrodo 4

                # Septimo estado del control finito
                # Deja de estimula musculos flexores y libera el vaso sobre la mesa
                elif step ==7:
                    if time.perf_counter()-tic>1.5 and varianceACC_x>=self.ACC1:
                        step = 8
                    self.ensembleCurrent[1] = 10    # Electrodo 2
                    self.ensembleCurrent[2] = 0     # Electrodo 3
                    self.ensembleCurrent[3] = 5     # Electrodo 4

                elif step==8:
                    if  valor_EMG_Biceps<self.EMG1 and midstep==False:
                        midstep=True
                    elif  valor_EMG_Deltoids<self.EMG2 and midstep==True and varianceACC_x<= self.ACC1:
                        midstep=False
                        step = 9
                    self.ensembleCurrent[1] = 0     # Electrodo 2
                    self.ensembleCurrent[2] = 0     # Electrodo 3
                    self.ensembleCurrent[3] = 0     # Electrodo 4

                elif step == 9:
                    winsound.Beep(450, 1000)

                self.EnsembleConfiguration()
                stimulation[g,1:4] = self.ensembleCurrent[1:4]#self.currents[0:8]
                stimulation[g,0] = time.perf_counter()-Gtic
                g += 1

                qState.put(step)

        qState.put(0)
        self.qsensorsEMG.queue.clear()
        self.qsensorsACC.queue.clear()

        # Crea un archivo .txt donde se guardaran los datos: Terapi, FW, PW, DT, PN y los músculos estimulados
        infTherapy = open('infTherapy.txt', 'w')
        infTherapy.write('AgarrePalmar '+" ".join(map(str,[self.Frequency,self.PW,self.DT,self.PN])))
        infTherapy.write('\n')
        infTherapy.write(" ".join(self.stimulatedMuscles))
        infTherapy.close()

        # Crea un archivo .txt donde se guardaran los valores de estimulación
        stimul = open('stimulation.txt', 'w')
        for v in range(0,g):
            stimul.write(" ".join(map(str, stimulation[v,0:9])))
            stimul.write('\n')
        stimul.close()

    def PinchControl(self,qState):

        length = 300000  # 6076 muestras en aprox 5 mins, con 150 es 10000 para 180 20000
        stimulation = numpy.zeros((length, 9), dtype=numpy.float)  ## matriz de valores de estimulación

        values_ACC = numpy.arange(length, dtype=numpy.float)  ## vector de calculo de valores
        values_ACC[0:length] = 0
        f_size_ACC = 0

        array_ACC_x = numpy.arange(150, dtype=numpy.float)
        array_ACC_x[0:150] = 0

        varianceACC_x = numpy.zeros((length, 2), dtype=numpy.float)  ## matriz de calculo de valores en la aceleración
        size_ACCVar = 0

        i_sizeACCVar = 0
        init = 100
        nsample = 136

        g=1     # Comienza desde 1 para dar el valor inicial al vector que guarda los datos de 0
        d=0

        step = 1

        midstep = False

        self.ensembleCurrent[0] = 0
        # self.ensembleCurrent[3] = 0
        self.ensembleCurrent[4] = 0
        self.ensembleCurrent[5] = 0
        self.ensembleCurrent[6] = 0
        self.ensembleCurrent[7] = 0

        sensorsvalueEMG = self.qsensorsEMG.get()
        Gtic = time.perf_counter()
        while(self.flag==True):
                sensorsvalueACC = self.qsensorsACC.get()
            #print(sensorsvalueACC)
            # 0         tiempo
            # trama     sensor      i
            # 0,1,2     sensor 1    0
            # 3,4,5     sensor 2    1
            # 6,7,8     sensor 3    2
            # 9,10,11   sensor 4    3
            # 12,13,14  sensor 5    4
            # 15,16,17  sensor 6    5
            # 18,19,20  sensor 7    6
            # 21,22,23  sensor 8    7
            # sensorsvalueACC[(3*i)+1:(3*i)+3]
                            #tiempo                 valor sensor 4 de X
                varianceACC_x=float(sensorsvalueACC[3*3])*100 # El eje en X del sensor 4

                sensorsvalueEMG = self.qsensorsEMG.get()
                valor_EMG_Deltoids = float(sensorsvalueEMG[0])*100000000
                valor_EMG_Biceps = float(sensorsvalueEMG[1])*100000000
                valor_EMG_Triceps = float(sensorsvalueEMG[2])*100000000

                # Primer estado del control finito
                # Comienza el control finito de estados teniendo en brazo en reposo a un costado
                if step == 1:
                    if  valor_EMG_Deltoids>self.EMG1 and midstep==False:
                        midstep=True
                    elif  valor_EMG_Biceps>self.EMG2 and midstep==True:
                        step = 2
                        midstep=False
                        #tic = time.perf_counter()
                    self.ensembleCurrent[1] = 0 # Electrodo 2
                    self.ensembleCurrent[2] = 0 # Electrodo 3
                    self.ensembleCurrent[3] = 0 # Electrodo 4

                # Segundo estado del control finito
                # Estimula los músculos extensores y se lleva la mano hacia le mesa al costado del vaso
                elif step == 2:
                    if valor_EMG_Deltoids<self.EMG1 and valor_EMG_Biceps<self.EMG2 and valor_EMG_Triceps>self.EMG3 and varianceACC_x<=self.ACC1:
                        tic = time.perf_counter()
                        step = 3
                    self.ensembleCurrent[1] = 10    # Electrodo 2
                    self.ensembleCurrent[2] = 0     # Electrodo 3
                    self.ensembleCurrent[3] = 5     # Electrodo 4

                # Tercer estado del control finito
                # Deja de estimular los músculos extensores y la mano esta a un costado del vaso
                elif step == 3:
                    if time.perf_counter()-tic>=3:
                        step=4
                    self.ensembleCurrent[1] = 0     # Electrodo 2
                    self.ensembleCurrent[2] = 0     # Electrodo 3
                    self.ensembleCurrent[3] = 5     # Electrodo 4

                # Cuarto estado del control finito
                # Estimula musculos flexores y toma el objeto sin levantar el brazo
                elif step == 4:
                    if  valor_EMG_Biceps>self.EMG5 and midstep==False:
                        midstep=True
                    elif  valor_EMG_Deltoids>self.EMG6 and midstep==True:
                        midstep=False
                        step = 5
                    self.ensembleCurrent[1] = 0     # Electrodo 2
                    self.ensembleCurrent[2] = 11    # Electrodo 3
                    self.ensembleCurrent[3] = 6     # Electrodo 4

                # Quinto estado del control finito
                # Estimula musculos flexores, teniendo el objeto en la mano lleva el mismo hacia la boca
                elif step == 5:
                    if valor_EMG_Deltoids<self.EMG1 and valor_EMG_Biceps<self.EMG2 and valor_EMG_Triceps>self.EMG3 and varianceACC_x<=self.ACC1:
                        tic = time.perf_counter()
                        step = 6
                    self.ensembleCurrent[1] = 0     # Electrodo 2
                    self.ensembleCurrent[2] = 8    # Electrodo 3
                    self.ensembleCurrent[3] = 6     # Electrodo 4

                # Sexto estado del control finito
                # Estimula musculos flexores, y tiene el objeto sobre la mesa
                elif step == 6:
                    if time.perf_counter()-tic>3 and varianceACC_x<=self.ACC1:
                        tic = time.perf_counter()
                        step = 7
                    self.ensembleCurrent[1] = 0     # Electrodo 2
                    self.ensembleCurrent[2] = 7    # Electrodo 3
                    self.ensembleCurrent[3] = 5     # Electrodo 4

                # Septimo estado del control finito
                # Deja de estimula musculos flexores y libera el vaso sobre la mesa
                elif step ==7:
                    if time.perf_counter()-tic>1.5 and varianceACC_x>=self.ACC1:
                        step = 8
                    self.ensembleCurrent[1] = 10    # Electrodo 2
                    self.ensembleCurrent[2] = 0     # Electrodo 3
                    self.ensembleCurrent[3] = 0     # Electrodo 4

                elif step==8:
                    if  valor_EMG_Biceps<self.EMG2 and midstep==False:
                        midstep=True
                    elif  valor_EMG_Deltoids<self.EMG1 and midstep==True and varianceACC_x<= self.ACC1:
                        midstep=False
                        step = 9
                    self.ensembleCurrent[1] = 0     # Electrodo 2
                    self.ensembleCurrent[2] = 0     # Electrodo 3
                    self.ensembleCurrent[3] = 0     # Electrodo 4
                    #print('Estado 8')
                elif step == 9:
                    winsound.Beep(450, 1000)
                self.EnsembleConfiguration()
                stimulation[g,1:4] = self.ensembleCurrent[1:4]#self.currents[0:8]
                stimulation[g,0] = time.perf_counter()-Gtic
                g += 1
                qState.put(step)

        qState.put(0)
        self.qsensorsEMG.queue.clear()
        self.qsensorsACC.queue.clear()

        # Crea un archivo .txt donde se guardaran los datos: Terapi, FW, PW, DT, PN y los músculos estimulados
        infTherapy = open('infTherapy.txt', 'w')
        infTherapy.write('AgarreLateral '+" ".join(map(str,[self.Frequency,self.PW,self.DT,self.PN])))
        infTherapy.write('\n')
        infTherapy.write(" ".join(self.stimulatedMuscles))
        infTherapy.close()

        # Crea un archivo .txt donde se guardaran los valores de estimulación
        stimul = open('stimulation.txt', 'w')
        for v in range(0,g):
            stimul.write(" ".join(map(str, stimulation[v,0:9])))
            stimul.write('\n')
            # print(v)
        stimul.close()