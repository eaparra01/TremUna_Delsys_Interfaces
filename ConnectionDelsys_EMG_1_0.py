
from tkinter import messagebox

import numpy
import decimal
import socket
import time
import queue
import scipy.io as sio


import psutil, os

p = psutil.Process(os.getpid())
p.nice(psutil.HIGH_PRIORITY_CLASS)

class ConnectionDelsys_EMG_1_0():

    # Varibles para la comunicación con el Delsys para los datos EMG y con Tremuna para el envío de los datos de varianza
    TCP_IP = 'localhost'  # "192.168.42.240"
    EMG_PORT = 50041
    BUFFER_SIZE_EMG = 64
    CLIENTE_PORT_EMG = 5005

    # Puerto de comunicación con el Delsys para los datos EMG
    sEMG = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Establish a TCP/IP socket EMG stream
    #MeasuredMuscles = ['Músculo 1','Músculo 2','Músculo 3','Músculo 4','Músculo 5','Músculo 6','Músculo 7','Músculo 8']

    tic = 0

    qData = queue.Queue()          #queue.Queue(maxsize=0)
    # qDatatoSend = queue.Queue()    #queue.Queue(maxsize=0)

    state = False

    def __init__(self):
        #self.powFraction=numpy.array([[2**-1],[2**-2],[2**-3],[2**-4],[2**-5],[2**-6],[2**-7],[2**-8],[2**-9],[2**-10],[2**-11],[2**-12],[2**-13],[2**-14],[2**-15],[2**-16],[2**-17],[2**-18],[2**-19],[2**-20],[2**-21],[2**-22],[2**-23]])
        self.powFraction=numpy.array([[5.0e-01],[2.5e-01],[1.25e-01],[ 6.25e-02],[3.125e-02],[1.5625e-02],[7.8125e-03],[3.90625e-03],[1.9531e-03],[9.7656e-04],[4.8828e-04],[2.4414e-04],[1.2207e-04],[6.1035e-05],[3.0518e-05],[1.5259e-05],[7.6294e-06],[3.8147e-06],[1.9073e-06],[ 9.5367e-07],[4.7684e-07],[2.3842e-07],[1.1921e-07]],dtype=numpy.float32)
        pass

    def DecodificationEMGData(self,dataDevice):
        dataBinary = numpy.unpackbits(numpy.fromstring(dataDevice, dtype=numpy.uint8))
        return numpy.prod([ numpy.power((-1),int(numpy.array(dataBinary[0]))),numpy.add(1,numpy.dot(dataBinary[9:33],self.powFraction)) ,numpy.power(2,int(numpy.packbits(dataBinary[1:9])) - 127,dtype=float)])
        pass

    # Esta funcion toma los datos decidficados de EMG que proviene del Delsys y los decodifica, para luego enviarlos
    # a las funciones
    def StartEMGSample(self):     # Se quietó qdata

        self.sEMG = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sEMG.connect((self.TCP_IP, self.EMG_PORT))

        BUFFER_SIZE_EMG = 64
        length = 410000                     # 303998 portatil y 359338 escritorio muestran en aprox 5 mins
        dataEMGbytes = self.sEMG.recv(BUFFER_SIZE_EMG)
        tic1 = time.perf_counter()

        # value =numpy.array([0, 0, 0, 0, 0, 0, 0, 0, 0],dtype=numpy.dtype(decimal.Decimal))     # se tiene 9 datos uno para tiempo y los demás para sensores
        value = numpy.zeros((length, 9), dtype=numpy.dtype(decimal.Decimal))  # se tiene 9 datos uno para tiempo y los demás para sensores
        #self.sDEVICE.send(b'START\r\n\r\n')
        #dataDEVICE = self.sDEVICE.recv(self.BUFFER_SIZE_DEVICE)
        #print('Comienza la lectura EMG de los Sensores: %s ' % dataDEVICE)
        #print('Comienzo de la lectura de los Sensor')
        print('****  EMG  ****')
        #print('Comienza la lectura EMG de los Sensores')
        i = 1   # Comienza desde 1 para que el valor inicial de la matriz sea cero
        div_f = 2
        while(self.state== True ):
            try:
                dataEMGbytes = self.sEMG.recv(BUFFER_SIZE_EMG)

                if self.DecodificationEMGData(dataEMGbytes[4:8])> 0.000000001 or self.DecodificationEMGData(dataEMGbytes[4:8])< -0.000000001:
                    self.tic = time.perf_counter()
                    while (self.state == True):

                        dataEMGbytes = self.sEMG.recv(BUFFER_SIZE_EMG)
                        if div_f == 2:
                            value[i,0] = time.perf_counter() - self.tic
                            value[i,1] = self .DecodificationEMGData(dataEMGbytes[0:4])
                            value[i,2] = self .DecodificationEMGData(dataEMGbytes[4:8])
                            value[i,3] = self .DecodificationEMGData(dataEMGbytes[8:12])
                            value[i,4] = self .DecodificationEMGData(dataEMGbytes[12:16])
                            value[i,5] = self .DecodificationEMGData(dataEMGbytes[16:20])
                            value[i,6] = self .DecodificationEMGData(dataEMGbytes[20:24])
                            value[i,7] = self .DecodificationEMGData(dataEMGbytes[24:28])
                            value[i,8] = self .DecodificationEMGData(dataEMGbytes[28:32])

                            # f.write(" ".join(map(str, value)))
                            # f.write('\n')
                            #qdata.put(value[i,1:9])
                            self.qData.put(value[i,1:9])
                            div_f = 0
                            i=i+1
                            # if self.state == False:
                            #    break
                        div_f=div_f+1
                        # if self.state == False:
                        #    break
            except(OSError, ValueError):
                print('No se puede establer conexión con el Delsys y realizar la decodificación')
                self.qData.put(value[i, 1:9])
                #messagebox.showwarning('Fallo en conexión y decodificación',
                #                       'No se puede establer conexión con el Delsys y realizar la decodificación, Termine la toma de dados y vuelva a comenzar')
                self.state = False

        self.state = False
        self.qData.put(value[i,1:9])
        tiempo = (time.clock() - tic1)
        print('Terminó muestreo de las señales de EMG')
        print('Tiempo de muestreo de EMG %f' % tiempo)
        print('El número de muestras EMG %d' % i)
        print('Frecuencia de los dados %f' % (i/tiempo))
        # Se guardan los valores de EMG que están en la matriz value[,]

        f = open('dataEMG.txt', 'w')  # Crea un archivo .txt donde se guardaran los datos, opción 'w'

        for v in range(0,i):
            f.write(" ".join(map(str, value[v,0:9])))
            f.write('\n')
            # print(v)
        f.close()
        print('Guardo los datos de EMG en el archivo dataEMG.txt')
        self.sEMG.close()
        # dataList={}
        # dataList.update(MeasuredMuscle=self.MeasuredMuscles,MusclesEMG=value[:i,:])
        # sio.savemat('dataMusclesEMG.mat', dataList)
        # print('Se guardó los datos de EMG en el archivo dataMusclesEMG.mat')
        #print('Andres Parra')
        # self.StopSample()
        pass

    def ReadFunction(self): # Se quietó qdata

        length = 6500             # 6076 muestras en aprox 5 mins, con 150 es 10000 para 180 20000
                                  # 5987 muestras en aprox 5 mins, con ventana 100 y solapamiento 50
        var = numpy.zeros((length, 9), dtype=numpy.float)  ## matriz de calculo de valores
        data1 = numpy.zeros((250, 8), dtype=numpy.float)  ## matriz de calculo de valores
        # var = numpy.array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=numpy.float)

        g = 0
        j = 0
        init = 50  # No puede ser mayor de 20
        nsample = 100
        ##### nsample-init  => 200 - 190
        # tiempo 0.0197 aproxima a 200ms 0.00048 es el tiempo que tarda en procesar una linea de datos con un maximo de init a 41
        # elapse = 0.0197 - 0.000488 * init
        # time.sleep(0.85)  # multiprocessing
        # time.sleep(0.05)
        print('****  Varianza  ****')
        #print('Empezó el cáculo de la varianza')
        #tic = time.perf_counter()
        while (self.state == True):

            #data1[j, :] = qdata.get()
            data1[j, :] = self.qData.get()
            # print(init)
            j = j + 1
            # if(time.perf_counter()-tic > 0.05 ):
            # if(flag==0 and j< 3):
            #    flag=1
            #    j=0
            # if ((time.perf_counter()-tic) >= elapse) and (j>init): # toma aproximadamente 20 y 30 datos para un tiempo de 200ms
            if j >= nsample:  # toma aproximadamente 20 y 30 datos para un tiempo de 200ms

                # var[g, 1] = numpy.sqrt(numpy.mean(numpy.square(data1[:j, 0])))
                # var[g, 2] = numpy.sqrt(numpy.mean(numpy.square(data1[:j, 1])))
                # var[g, 3] = numpy.sqrt(numpy.mean(numpy.square(data1[:j, 2])))
                # var[g, 4] = numpy.sqrt(numpy.mean(numpy.square(data1[:j, 3])))
                # var[g, 5] = numpy.sqrt(numpy.mean(numpy.square(data1[:j, 4])))
                # var[g, 6] = numpy.sqrt(numpy.mean(numpy.square(data1[:j, 5])))
                # var[g, 7] = numpy.sqrt(numpy.mean(numpy.square(data1[:j, 6])))
                # var[g, 8] = numpy.sqrt(numpy.mean(numpy.square(data1[:j, 7])))
                var[g, 1] = numpy.var(data1[:j, 0])
                var[g, 2] = numpy.var(data1[:j, 1])
                var[g, 3] = numpy.var(data1[:j, 2])
                var[g, 4] = numpy.var(data1[:j, 3])
                var[g, 5] = numpy.var(data1[:j, 4])
                var[g, 6] = numpy.var(data1[:j, 5])
                var[g, 7] = numpy.var(data1[:j, 6])
                var[g, 8] = numpy.var(data1[:j, 7])
                # var[g, 1] = numpy.std(data1[:j, 0])
                # var[g, 2] = numpy.std(data1[:j, 1])
                # var[g, 3] = numpy.std(data1[:j, 2])
                # var[g, 4] = numpy.std(data1[:j, 3])
                # var[g, 5] = numpy.std(data1[:j, 4])
                # var[g, 6] = numpy.std(data1[:j, 5])
                # var[g, 7] = numpy.std(data1[:j, 6])
                # var[g, 8] = numpy.std(data1[:j, 7])


                #self.qDatatoSend.put(var[g, 0:8])

                data1[:init, :] = data1[j - init:j, :]
                j = init
                g = g + 1
                var[g, 0] = time.perf_counter()-self.tic
                # Guardas los datos de varianza en un archivos .txt
                # variancef.write('' + str(varS1) + ' ' + str(varS2) + ' ' + str(varS3) + ' ' + str(varS4) + ' ' + str(varS5) + ' ' + str(varS6) + ' ' + str(varS7) + ' ' + str(varS8) + '\n')
                # variancef.write(" ".join(map(str, var)))
                # variancef.write('\n')
                # tic = time.perf_counter()
                # j=0

                # if self.state == False:
                #    self.state= False
                #    break
        self.qData.queue.clear()

        print('Terminó el cáculo de la varianza de EMG')
        print('El número de muestras de la varianza de EMG %d' % g)

        variancef = open('varianceEMG.txt','w')  # Con el archivo .txt creado, coloca filas para cada dato nuevo, opción 'w'
        for b in range(0, g):
            variancef.write(" ".join(map(str, var[b, 0:9])))
            variancef.write('\n')
        print('Se guardaron las valores de Varianza de EMG en varianceEMG.txt')
        # dataList={}
        # dataList.update(varianceEMG=var[:g,:])
        # sio.savemat('varianceEMG.mat', dataList)
        # print('Se guardaron las valores de Varianza en el archivo varianceEMG.mat')
        pass


    def ReadFunctionSendData(self): # Se quietó qdata

        # Puerto de comunicación con el Tremuna para el envío de los datos de varianza
        sINTERAPPS_EMG = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sINTERAPPS_EMG.connect((self.TCP_IP, self.CLIENTE_PORT_EMG))

        length = 6500  # 6076 portatil 10883 escritorio muestras en aprox 5 mins
                        # 5987 muestras en aprox 5 mins, con ventana 100 y solapamiento 50
        var = numpy.zeros((length, 9), dtype=numpy.float)  ## matriz de calculo de valores
        data1 = numpy.zeros((250, 8), dtype=numpy.float)  ## matriz de calculo de valores
        #digit_flag = False
        # var = numpy.array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=numpy.float)
        g = 0
        j = 0
        init = 50 # Se tiene un rango entre 50 y 30 ms
        nsample = 100
        ##### nsample-init  => 200 - 190
        # tiempo 0.0197 aproxima a 200ms 0.00048 es el tiempo que tarda en procesar una linea de datos con un maximo de init a 41
        # elapse = 0.0197 - 0.000488 * init
        # time.sleep(0.85)  # multiprocessing
        # time.sleep(0.05)
        print('****  Enviar Varianza  ****')
        #print('Empezó el cáculo de la varianza Y EMG')

        while (self.state == True):

            #data1[j, :] = qdata.get()
            data1[j, :] = self.qData.get()
            j = j + 1
            # if(time.perf_counter()-tic > 0.05 ):
            # if(flag==0 and j< 3):
            #    flag=1
            #    j=0
            # if ((time.perf_counter()-tic) >= elapse) and (j>init): # toma aproximadamente 20 y 30 datos para un tiempo de 200ms
            if j >= nsample:  # toma aproximadamente 20 y 30 datos para un tiempo de 200ms
                # var[g, 1] = numpy.sqrt(numpy.mean(numpy.square(data1[:j, 0])))
                # var[g, 2] = numpy.sqrt(numpy.mean(numpy.square(data1[:j, 1])))
                # var[g, 3] = numpy.sqrt(numpy.mean(numpy.square(data1[:j, 2])))
                # var[g, 4] = numpy.sqrt(numpy.mean(numpy.square(data1[:j, 3])))
                # var[g, 5] = numpy.sqrt(numpy.mean(numpy.square(data1[:j, 4])))
                # var[g, 6] = numpy.sqrt(numpy.mean(numpy.square(data1[:j, 5])))
                # var[g, 7] = numpy.sqrt(numpy.mean(numpy.square(data1[:j, 6])))
                # var[g, 8] = numpy.sqrt(numpy.mean(numpy.square(data1[:j, 7])))
                var[g, 1] = numpy.var(data1[:j, 0])
                var[g, 2] = numpy.var(data1[:j, 1])
                var[g, 3] = numpy.var(data1[:j, 2])
                var[g, 4] = numpy.var(data1[:j, 3])
                var[g, 5] = numpy.var(data1[:j, 4])
                var[g, 6] = numpy.var(data1[:j, 5])
                var[g, 7] = numpy.var(data1[:j, 6])
                var[g, 8] = numpy.var(data1[:j, 7])
                # var[g, 1] = numpy.std(data1[:j, 0])
                # var[g, 2] = numpy.std(data1[:j, 1])
                # var[g, 3] = numpy.std(data1[:j, 2])
                # var[g, 4] = numpy.std(data1[:j, 3])
                # var[g, 5] = numpy.std(data1[:j, 4])
                # var[g, 6] = numpy.std(data1[:j, 5])
                # var[g, 7] = numpy.std(data1[:j, 6])
                # var[g, 8] = numpy.std(data1[:j, 7])

                data1[:init, :] = data1[j - init:j, :]
                j = init
                var[g, 0] = time.perf_counter() - self.tic

                #self.qDatatoSend.put(var[g, 0:8])
                varS_EMG = ['{:.2e}'.format(var[g,1]), '{:.2e}'.format(var[g,2]), '{:.2e}'.format(var[g,3]),'{:.2e}'.format(var[g,4]), '{:.2e}'.format(var[g,5]), '{:.2e}'.format(var[g,6]), '{:.2e}'.format(var[g,7]), '{:.2e}'.format(var[g,8])]
                #varS = [str(var[g,0]), str(var[g,1]), str(var[g,2]), str(var[g,3]), str(var[g,4]), str(var[g,5]), str(var[g,6]), str(var[g,7])]
                # if digit_flag == False:
                #     #varS = [str(var[0]), str(var[1]), str(var[2]), str(var[3]), str(var[4]), str(var[5]), str(var[6]), str(var[7])]
                #     MESSAGE = ' '.join(varS)
                #     BUFFER_SIZE = str(len(MESSAGE.encode('utf-8')))
                #     print('Número de dígitos')
                #     DIGIT_SIZE = str(len(BUFFER_SIZE.encode('utf-8')))
                #     print(DIGIT_SIZE)
                #     sINTERAPPS.send(DIGIT_SIZE.encode('utf-8'))  # Envía el número de digitos que tiene el valor que indica el # de caracteres
                #     digit_flag = True
                g = g + 1

                MESSAGE = ' '.join(varS_EMG)
                BUFFER_SIZE = str(len(MESSAGE.encode('utf-8')))
                sINTERAPPS_EMG.send(BUFFER_SIZE.encode('utf-8'))
                sINTERAPPS_EMG.send(MESSAGE.encode('utf-8'))
                # Guardas los datos de varianza en un archivos .txt
                # variancef.write('' + str(varS1) + ' ' + str(varS2) + ' ' + str(varS3) + ' ' + str(varS4) + ' ' + str(varS5) + ' ' + str(varS6) + ' ' + str(varS7) + ' ' + str(varS8) + '\n')
                # variancef.write(" ".join(map(str, var)))
                # variancef.write('\n')
                # tic = time.perf_counter()
                # j=0

                # if self.state == False:
                #    self.state= False
                #    break

        sINTERAPPS_EMG.close()

        self.qData.queue.clear()

        print('Terminó el cáculo de la varianza EMG')
        print('El número de muestras de la varianza %d' % g)
        variancef = open('varianceEMG.txt','w')  # Con el archivo .txt creado coloca filas para cada dato nuevo, opción 'a'
        for b in range(0, g):
            variancef.write(" ".join(map(str, var[b, 0:9])))
            variancef.write('\n')
        print('Se guardaron las valores de Varianza de EMG en varianceEMG.txt')
        # dataList={}
        # dataList.update(varianceEMG=var[:g,:])
        # sio.savemat('varianceEMG.mat', dataList)
        # print('Se guardaron las valores de Varianza en el archivo varianceEMG.mat')
        pass

    # def SendData(self):
    #     try:
    #
    #         sINTERAPPS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         sINTERAPPS.connect((self.TCP_IP, self.CLIENTE_PORT))
    #
    #         ##sINTERAPPS.send(b'Conexion Ok')
    #         ##data = sINTERAPPS.recv(11)
    #         ##if data == b'Conexion Ok':
    #
    #         #value = numpy.zeros((100, 9), dtype=numpy.dtype(decimal.Decimal)) ## matriz de calculo de valores
    #         #data1 = numpy.zeros((100, 9), dtype=numpy.dtype(decimal.Decimal))  ## matriz de calculo de valores
    #
    #         #variancef = open('varianceEMG.txt', 'w')  # Con el archivo .txt creado coloca filas para cada dato nuevo, opción 'a'
    #         #meanf = open('meanEMG.txt', 'w')  # Con el archivo .txt creado coloca filas para cada dato nuevo, opción 'a'
    #
    #         #j = 0
    #         #init = 45
    #         #INITIATE = False
    #
    #         #time.sleep(0.85)  # multiprocessing
    #         #time.sleep(0.05)
    #
    #         # Define el número de digitos que tiene el valor que indica  el número de caranteres del mensaje
    #         #  ejemplo 140 caranters se defiene por 3 digitos
    #         varData = self.qDatatoSend.get()
    #         #varS = [str(varData[0]), str(varData[1]), str(varData[2]), str(varData[3]), str(varData[4]),
    #         #        str(varData[5]), str(varData[6]), str(varData[7])]
    #         varS = [str(varData[0]), str(varData[1]),str(varData[2]), str(varData[3]), str(varData[4]), str(varData[5]), str(varData[6]), str(varData[7])]
    #         MESSAGE = ' '.join(varS)
    #         BUFFER_SIZE = str(len(MESSAGE.encode('utf-8')))
    #         print('Número de dígitos')
    #         DIGIT_SIZE = str(len(BUFFER_SIZE.encode('utf-8')))
    #         print(DIGIT_SIZE)
    #         sINTERAPPS.send(DIGIT_SIZE.encode('utf-8')) # Envía el número de digitos que tiene el valor que indica el # de caracteres
    #         #INITIATE = True
    #
    #
    #         while(self.state):
    #                 try:
    #
    #                     #tic = time.perf_counter() aprox 0.008
    #                     #data1[j,:] = self.qDatatoVanriance.get()
    #                     varData= self.qDatatoSend.get()
    #                     #j=j+1
    #                     #if(time.perf_counter()-tic > 0.05 ):
    #                     # Envío de datos TCP/IP como cliente por parte del Delsys para conectarse con el Tremuna
    #                     varS =[str(varData[0]),str(varData[1]),str(varData[2]),str(varData[3]),str(varData[4]),str(varData[5]),str(varData[6]),str(varData[7])]
    #                     #print(type(varS))
    #                     #print(varS[2])
    #                     #print(varS)
    #                     #print('Andres Parra Delsys')
    #                     MESSAGE = ' '.join(varS)
    #                     #print(MESSAGE)
    #                     #print(len(MESSAGE))
    #                     #print(len(MESSAGE.encode('utf-8')))
    #                     #print(MESSAGE.encode('utf-8'))
    #                     BUFFER_SIZE = str(len(MESSAGE.encode('utf-8')))
    #                     #print(BUFFER_SIZE)
    #
    #                     # Éste condicional envía el número de dígitos que indica el número de dígitos totales en la trama de datos
    #                     #if INITIATE == False:
    #                     #   print('Numero de digitos')
    #                     #   DIGIT_SIZE = str(len(BUFFER_SIZE.encode('utf-8')))
    #                     #   print(DIGIT_SIZE)
    #                     #   sINTERAPPS.send(DIGIT_SIZE.encode('utf-8'))
    #                     #   INITIATE = True
    #
    #                     sINTERAPPS.send(BUFFER_SIZE.encode('utf-8'))
    #                     sINTERAPPS.send(MESSAGE.encode('utf-8'))
    #
    #                     #j = init
    #                     #data1[0:init, :] = data1[100 - init:, :]
    #                     # Guardas los datos de varianza y media alculados en archivos .txt
    #                     #variancef.write('' + str(varS1) + ' ' + str(varS2) + ' ' + str(varS3) + ' ' + str(varS4) + ' ' + str(varS5) + ' ' + str(varS6) + ' ' + str(varS7) + ' ' + str(varS8) + '\n')
    #                     #meanf.write('' + str(meanS1) + ' ' + str(meanS2) + ' ' + str(meanS3) + ' ' + str(meanS4) + ' ' + str(meanS5) + ' ' + str(meanS6) + ' ' + str(meanS7) + ' ' + str(meanS8) + '\n')
    #                     #j=0
    #
    #                 except(ValueError,ValueError):
    #                     print('Se terminó la conexión TCP/IP del Delsys con el Tremuna')
    #                     messagebox.showwarning('Fallo en conexión y decodificación',
    #                                            'No se puede establer conexión con el Delsys y realizar la decodificación, Termine la toma de dados y vuelva a comenzar')
    #                     self.state = False
    #         print('Terminó el proceso de lectura del Delsys y envío de datos al Tremuna')
    #         #variancef.close()
    #         #meanf.close()
    #         sINTERAPPS.close()
    #         ##else:
    #         ##    self.state = False
    #         ##    sINTERAPPS.close()
    #     except (ConnectionRefusedError):
    #         print('Habilite la conexción TCP/IP con el Tremuna ')
    #         messagebox.showwarning('Fallo en conexión TCP/IP',
    #                                'No se puede establer conexión TCP/IP entre el Delsys y el Tremuna, Termine la conexión luego habilite la conexión con la interfaz del Tremuna y después bilite la conexión co el Delsys')
    #         self.state = False
    #
    #     pass