
import numpy
import decimal
import socket
import time
import scipy.io as sio
import queue
#from multiprocessing import Pool

#import psutil, os

#p = psutil.Process(os.getpid())
#p.nice(psutil.HIGH_PRIORITY_CLASS)

class ConnectionDelsys_ACC_1_0():

    # Varibles para la comunicación con el Delsys para los datos ACC
    TCP_IP = 'localhost'  # "192.168.42.240"
    ACC_PORT = 50042
    CLIENTE_PORT_ACC = 5007
    BUFFER_SIZE_ACC = 192
    # Puerto de comunicación con el Delsys para los datos ACC
    sACC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Establish a TCP/IP socket EMG stream

    tic = 0 #
    qData = queue.Queue()  # queue.Queue(maxsize=0)

    state = False

    def __init__(self):
        #self.powFraction=numpy.array([[2**-1],[2**-2],[2**-3],[2**-4],[2**-5],[2**-6],[2**-7],[2**-8],[2**-9],[2**-10],[2**-11],[2**-12],[2**-13],[2**-14],[2**-15],[2**-16],[2**-17],[2**-18],[2**-19],[2**-20],[2**-21],[2**-22],[2**-23]])
        self.powFraction=numpy.array([[5.0e-01],[2.5e-01],[1.25e-01],[ 6.25e-02],[3.125e-02],[1.5625e-02],[7.8125e-03],[3.90625e-03],[1.9531e-03],[9.7656e-04],[4.8828e-04],[2.4414e-04],[1.2207e-04],[6.1035e-05],[3.0518e-05],[1.5259e-05],[7.6294e-06],[3.8147e-06],[1.9073e-06],[ 9.5367e-07],[4.7684e-07],[2.3842e-07],[1.1921e-07]],dtype=numpy.float32)
        pass

    def DecodificationACCData(self,dataDevice):
        dataBinary = numpy.unpackbits(numpy.fromstring(dataDevice, dtype=numpy.uint8))
        return numpy.prod([ numpy.power((-1),int(numpy.array(dataBinary[0]))),numpy.add(1,numpy.dot(dataBinary[9:33],self.powFraction)) ,numpy.power(2,int(numpy.packbits(dataBinary[1:9])) - 127,dtype=float)])
        pass


    def StartACCSample(self):

        self.sACC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sACC.connect((self.TCP_IP, self.ACC_PORT))

        tic1 = time.perf_counter()
        #p = Pool(1)
        length = 65000         # 44993 muestras en aprox 5 mins
        # _array = numpy.array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=numpy.dtype(decimal.Decimal))
        value = numpy.zeros((length, 25), dtype=numpy.dtype(decimal.Decimal))  # se tiene 9 datos uno para tiempo y los demás para sensores

        print('**** ACC ****')
        i=1 # Comienza desde 1 para que los valores comiencen en cero
        #h=1
        while(self.state==True):
            try:
                dataACCbytes = self.sACC.recv(self.BUFFER_SIZE_ACC)

                if self.DecodificationACCData(dataACCbytes[0:4])>0.0000001 or self.DecodificationACCData(dataACCbytes[0:4])<-0.0000001:
                    self.tic = time.perf_counter() #

                    while (self.state == True):

                        dataACCbytes = self.sACC.recv(self.BUFFER_SIZE_ACC)
                        #if h==1:
                            # No sobre escribir el dato del if para entrar en el bucle while
                            #value[i,0] = time.perf_counter() - tic
                            #print(dataACCbytes)
                            #value[i,1:25]=p.map(self.DecodificationACCData,[dataACCbytes[0:4],dataACCbytes[4:8],dataACCbytes[8:12],dataACCbytes[12:16],
                            #                                              dataACCbytes[16:20],dataACCbytes[20:24],dataACCbytes[24:28],dataACCbytes[28:32],
                            #                                              dataACCbytes[32:36],dataACCbytes[36:40],dataACCbytes[40:44],dataACCbytes[44:48],
                            #                                              dataACCbytes[48:52],dataACCbytes[52:56],dataACCbytes[56:60],dataACCbytes[60:64],
                            #                                              dataACCbytes[64:68],dataACCbytes[68:72],dataACCbytes[72:76],dataACCbytes[76:80],
                            #                                              dataACCbytes[80:84],dataACCbytes[84:88],dataACCbytes[88:92],dataACCbytes[92:96]])
                        value[i, 0] = time.perf_counter() - self.tic #
                        value[i, 1] = self.DecodificationACCData(dataACCbytes[0:4])
                        value[i, 2] = self.DecodificationACCData(dataACCbytes[4:8])
                        value[i, 3] = self.DecodificationACCData(dataACCbytes[8:12])
                        value[i, 4] = self.DecodificationACCData(dataACCbytes[12:16])
                        value[i, 5] = self.DecodificationACCData(dataACCbytes[16:20])
                        value[i, 6] = self.DecodificationACCData(dataACCbytes[20:24])
                        value[i, 7] = self.DecodificationACCData(dataACCbytes[24:28])
                        value[i, 8] = self.DecodificationACCData(dataACCbytes[28:32])
                        value[i, 9] = self.DecodificationACCData(dataACCbytes[32:36])
                        value[i, 10] = self.DecodificationACCData(dataACCbytes[36:40])
                        value[i, 11] = self.DecodificationACCData(dataACCbytes[40:44])
                        value[i, 12] = self.DecodificationACCData(dataACCbytes[44:48])
                        value[i, 13] = self.DecodificationACCData(dataACCbytes[48:52])
                        value[i, 14] = self.DecodificationACCData(dataACCbytes[52:56])
                        value[i, 15] = self.DecodificationACCData(dataACCbytes[56:60])
                        value[i, 16] = self.DecodificationACCData(dataACCbytes[60:64])
                        value[i, 17] = self.DecodificationACCData(dataACCbytes[64:68])
                        value[i, 18] = self.DecodificationACCData(dataACCbytes[68:72])
                        value[i, 19] = self.DecodificationACCData(dataACCbytes[72:76])
                        value[i, 20] = self.DecodificationACCData(dataACCbytes[76:80])
                        value[i, 21] = self.DecodificationACCData(dataACCbytes[80:84])
                        value[i, 22] = self.DecodificationACCData(dataACCbytes[84:88])
                        value[i, 23] = self.DecodificationACCData(dataACCbytes[88:92])
                        value[i, 24] = self.DecodificationACCData(dataACCbytes[92:96])
                            #value[1:25] = p.map(self.DecodificationACCData,[dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4],dataACCbytes[0:4]])

                            #f.write(" ".join(map(str, value)))
                            #f.write('\n')
                        self.qData.put(value[i, 1:25]) #
                        i=1+i
                        #    h=0
                        #h = h + 1
                        #if self.state == False:
                        #    break
                        #self.qACCData.put(value)
                #if self.state == False:
                #    break
            except(OSError):
                self.qData.put(value[i, 1:25]) #
                print('No se puede realizar la decodificación')

        self.qData.put(value[i, 1:25]) #
        self.sACC.close()
        tiempo_proceso = time.clock() - tic1
        print('El número de muestras del ACC %d' % i)
        print('Tiempo de toda de los datos ACC %f'% tiempo_proceso)
        print('Tiempo promedio de toma por cada datos ACC %f' % ((tiempo_proceso)/i))
        print('Terminó la lectura del ACC')
        # i_sizeACCVar = 0
        # f_size_ACC = 136
        # init = 100
        # nsample = 136

        # varianceACC= numpy.zeros((length, 25), dtype=numpy.float)  ## matriz de calculo de valores en la aceleración
        # size_ACCVar = 0
        #
        # while(f_size_ACC <= i-1):
        #
        #     varianceACC[size_ACCVar, :] = (numpy.var(value[i_sizeACCVar:f_size_ACC,:])) * 100
        #     i_sizeACCVar+=36
        #     f_size_ACC+=36
        #
        #
        #     f_size_ACC += 1
        #     if d > nsample:
        #
        #         varianceACC_x[size_ACCVar, 0] = time.perf_counter() - Gtic  # Mirar después tiempos
        #         # array_ACC_x[:init]=array_ACC_x[d-init:d]
        #         size_ACCVar += 1
        #         i_sizeACCVar = f_size_ACC - 1
        #         d = init
        #     d+=1
        #value1 =numpy.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dtype=numpy.dtype(decimal.Decimal))     # se tiene 9 datos uno para tiempo y los demás para sensores
        f = open('dataACC.txt', 'w')  # Crea un archivo .txt donde se guardaran los datos, opción 'w'
        for v in range(0,i):
            f.write(" ".join(map(str, value[v,:])))
            f.write('\n')
        f.close()
        print('Se guardó los datos ACC en dataACC.txt')
        # dataList={}
        # dataList.update(limbAcceleration=value[:i,:])
        # sio.savemat('limbAcceleration.mat', dataList)
        # print('Se guardó los datos de ACC en el archivo limbAcceleration.mat')
        pass

    def ReadFunction(self): # Se quietó qdata

        length = 65000             # 6076 muestras en aprox 5 mins, con 150 es 10000 para 180 20000
        var = numpy.zeros((length, 25), dtype=numpy.float)  ## matriz de calculo de valores
        data1 = numpy.zeros((250, 24), dtype=numpy.float)  ## matriz de calculo de valores
        # var = numpy.array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=numpy.float)

        g = 0
        j = 0
        init = 66
        nsample = 70
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
                var[g, 1] = numpy.var(data1[:j, 0])
                var[g, 2] = numpy.var(data1[:j, 1])
                var[g, 3] = numpy.var(data1[:j, 2])
                var[g, 4] = numpy.var(data1[:j, 3])
                var[g, 5] = numpy.var(data1[:j, 4])
                var[g, 6] = numpy.var(data1[:j, 5])
                var[g, 7] = numpy.var(data1[:j, 6])
                var[g, 8] = numpy.var(data1[:j, 7])
                var[g, 9] = numpy.var(data1[:j, 8])
                var[g, 10] = numpy.var(data1[:j,9])
                var[g, 11] = numpy.var(data1[:j, 10])
                var[g, 12] = numpy.var(data1[:j, 11])
                var[g, 13] = numpy.var(data1[:j, 12])
                var[g, 14] = numpy.var(data1[:j, 13])
                var[g, 15] = numpy.var(data1[:j, 14])
                var[g, 16] = numpy.var(data1[:j, 15])
                var[g, 17] = numpy.var(data1[:j, 16])
                var[g, 18] = numpy.var(data1[:j, 17])
                var[g, 19] = numpy.var(data1[:j, 18])
                var[g, 20] = numpy.var(data1[:j, 19])
                var[g, 21] = numpy.var(data1[:j, 20])
                var[g, 22] = numpy.var(data1[:j, 21])
                var[g, 23] = numpy.var(data1[:j, 22])
                var[g, 24] = numpy.var(data1[:j, 23])
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

        print('Terminó el cáculo de la varianza de ACC')
        print('El número de muestras de la varianza de ACC %d' % g)
        variancef = open('varianceACC.txt','w')  # Con el archivo .txt creado, coloca filas para cada dato nuevo, opción 'w'
        for b in range(0, g):
            variancef.write(" ".join(map(str, var[b, 0:25])))
            variancef.write('\n')
        print('Se guardaron las valores de Varianza de ACC en el txt')
        # dataList={}
        # dataList.update(varianceACC=var[:g,:])
        # sio.savemat('varianceACC.mat', dataList)
        # print('Se guardaron las valores de Varianza en el archivo varianceACC.mat')
        pass

    def ReadFunctionSendData(self):
        # Puerto de comunicación con el Tremuna para el envío de los datos de varianza de ACC
        sINTERAPPS_ACC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sINTERAPPS_ACC.connect((self.TCP_IP, self.CLIENTE_PORT_ACC))

        length = 65000  # 6076 muestras en aprox 5 mins, con 150 es 10000 para 180 20000
        var = numpy.zeros((length, 25), dtype=numpy.float)  ## matriz donde se guarda el valor de varianz
        data1 = numpy.zeros((250, 24), dtype=numpy.float)  ## matriz de calculo de varianza

        g = 0           # Variable que recorre la matriz var
        j = 0
        init = 66      # No puede ser mayor de 20
        nsample = 70
        print('****  Varianza ACC ****')

        while (self.state == True):

            data1[j, :] = self.qData.get()
            j = j + 1

            if j >= nsample:
                var[g, 1] = numpy.var(data1[:j, 0])
                var[g, 2] = numpy.var(data1[:j, 1])
                var[g, 3] = numpy.var(data1[:j, 2])
                var[g, 4] = numpy.var(data1[:j, 3])
                var[g, 5] = numpy.var(data1[:j, 4])
                var[g, 6] = numpy.var(data1[:j, 5])
                var[g, 7] = numpy.var(data1[:j, 6])
                var[g, 8] = numpy.var(data1[:j, 7])
                var[g, 9] = numpy.var(data1[:j, 8])
                var[g, 10] = numpy.var(data1[:j,9])
                var[g, 11] = numpy.var(data1[:j, 10])
                var[g, 12] = numpy.var(data1[:j, 11])
                var[g, 13] = numpy.var(data1[:j, 12])
                var[g, 14] = numpy.var(data1[:j, 13])
                var[g, 15] = numpy.var(data1[:j, 14])
                var[g, 16] = numpy.var(data1[:j, 15])
                var[g, 17] = numpy.var(data1[:j, 16])
                var[g, 18] = numpy.var(data1[:j, 17])
                var[g, 19] = numpy.var(data1[:j, 18])
                var[g, 20] = numpy.var(data1[:j, 19])
                var[g, 21] = numpy.var(data1[:j, 20])
                var[g, 22] = numpy.var(data1[:j, 21])
                var[g, 23] = numpy.var(data1[:j, 22])
                var[g, 24] = numpy.var(data1[:j, 23])

                data1[:init, :] = data1[j - init:j, :]
                j = init
                var[g, 0] = time.perf_counter()-self.tic

                varS_ACC = ['{:.2e}'.format(var[g, 1]), '{:.2e}'.format(var[g, 2]), '{:.2e}'.format(var[g, 3]),
                            '{:.2e}'.format(var[g, 4]), '{:.2e}'.format(var[g, 5]), '{:.2e}'.format(var[g, 6]),
                            '{:.2e}'.format(var[g, 7]), '{:.2e}'.format(var[g, 8]), '{:.2e}'.format(var[g, 9]),
                            '{:.2e}'.format(var[g, 10]), '{:.2e}'.format(var[g, 11]), '{:.2e}'.format(var[g, 12]),
                            '{:.2e}'.format(var[g, 13]), '{:.2e}'.format(var[g, 14]), '{:.2e}'.format(var[g, 15]),
                            '{:.2e}'.format(var[g, 16]), '{:.2e}'.format(var[g, 17]), '{:.2e}'.format(var[g, 18]),
                            '{:.2e}'.format(var[g, 19]), '{:.2e}'.format(var[g, 20]), '{:.2e}'.format(var[g, 21]),
                            '{:.2e}'.format(var[g, 22]), '{:.2e}'.format(var[g, 23]), '{:.2e}'.format(var[g, 24])]
                g = g + 1
                MESSAGE = ' '.join(varS_ACC)
                BUFFER_SIZE = str(len(MESSAGE.encode('utf-8')))
                sINTERAPPS_ACC.send(BUFFER_SIZE.encode('utf-8'))
                sINTERAPPS_ACC.send(MESSAGE.encode('utf-8'))
                # Guardas los datos de varianza en un archivos .txt
                # variancef.write('' + str(varS1) + ' ' + str(varS2) + ' ' + str(varS3) + ' ' + str(varS4) + ' ' + str(varS5) + ' ' + str(varS6) + ' ' + str(varS7) + ' ' + str(varS8) + '\n')
                # variancef.write(" ".join(map(str, var)))
                # variancef.write('\n')
                # tic = time.perf_counter()
                # j=0

                # if self.state == False:
                #    self.state= False
                #    break
        sINTERAPPS_ACC.close()

        self.qData.queue.clear()

        print('Terminó el cáculo de la varianza de ACC')
        print('El número de muestras de la varianza de ACC %d' % g)
        variancef = open('varianceACC.txt','w')  # Con el archivo .txt creado coloca filas para cada dato nuevo, opción 'a'
        for b in range(0, g):
            variancef.write(" ".join(map(str, var[b, 0:25])))
            variancef.write('\n')
        print('Se guardaron las valores de Varianza de ACC en varianceACC.txt')
        # dataList={}
        # dataList.update(varianceACC=var[:g,:])
        # sio.savemat('varianceACC.mat', dataList)
        # print('Se guardaron las valores de Varianza en el archivo varianceACC.mat')
        pass

    # def StartACCSampleSendData(self):
    #
    #     self.sACC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     self.sACC.connect((self.TCP_IP, self.ACC_PORT))
    #
    #     sINTERAPPS_ACC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     sINTERAPPS_ACC.connect((self.TCP_IP, self.CLIENTE_PORT_ACC))
    #
    #     tic1 = time.perf_counter()
    #     #p = Pool(1)
    #     length = 60000         # 44993 muestras en aprox 5 mins
    #     # _array = numpy.array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=numpy.dtype(decimal.Decimal))
    #     value = numpy.zeros((length, 25), dtype=numpy.dtype(decimal.Decimal))  # se tiene 9 datos uno para tiempo y los demás para sensores
    #
    #     print('**** ACC ****')
    #     i=1 # Se cambió de 0 a 1 para que comience desde el punto de origen Cero la matriz value
    #     #h=1
    #     while(self.state==True):
    #         try:
    #             dataACCbytes = self.sACC.recv(self.BUFFER_SIZE_ACC)
    #
    #             if self.DecodificationACCData(dataACCbytes[0:4])>0.0000001 or self.DecodificationACCData(dataACCbytes[0:4])<-0.0000001:
    #                 tic = time.perf_counter()
    #
    #                 while (self.state == True):
    #
    #                     dataACCbytes = self.sACC.recv(self.BUFFER_SIZE_ACC)
    #
    #                     value[i, 0] = time.perf_counter() - tic
    #                     value[i, 1] = self.DecodificationACCData(dataACCbytes[0:4])
    #                     value[i, 2] = self.DecodificationACCData(dataACCbytes[4:8])
    #                     value[i, 3] = self.DecodificationACCData(dataACCbytes[8:12])
    #                     value[i, 4] = self.DecodificationACCData(dataACCbytes[12:16])
    #                     value[i, 5] = self.DecodificationACCData(dataACCbytes[16:20])
    #                     value[i, 6] = self.DecodificationACCData(dataACCbytes[20:24])
    #                     value[i, 7] = self.DecodificationACCData(dataACCbytes[24:28])
    #                     value[i, 8] = self.DecodificationACCData(dataACCbytes[28:32])
    #                     value[i, 9] = self.DecodificationACCData(dataACCbytes[32:36])
    #                     value[i, 10] = self.DecodificationACCData(dataACCbytes[36:40])
    #                     value[i, 11] = self.DecodificationACCData(dataACCbytes[40:44])
    #                     value[i, 12] = self.DecodificationACCData(dataACCbytes[44:48])
    #                     value[i, 13] = self.DecodificationACCData(dataACCbytes[48:52])
    #                     value[i, 14] = self.DecodificationACCData(dataACCbytes[52:56])
    #                     value[i, 15] = self.DecodificationACCData(dataACCbytes[56:60])
    #                     value[i, 16] = self.DecodificationACCData(dataACCbytes[60:64])
    #                     value[i, 17] = self.DecodificationACCData(dataACCbytes[64:68])
    #                     value[i, 18] = self.DecodificationACCData(dataACCbytes[68:72])
    #                     value[i, 19] = self.DecodificationACCData(dataACCbytes[72:76])
    #                     value[i, 20] = self.DecodificationACCData(dataACCbytes[76:80])
    #                     value[i, 21] = self.DecodificationACCData(dataACCbytes[80:84])
    #                     value[i, 22] = self.DecodificationACCData(dataACCbytes[84:88])
    #                     value[i, 23] = self.DecodificationACCData(dataACCbytes[88:92])
    #                     value[i, 24] = self.DecodificationACCData(dataACCbytes[92:96])
    #
    #                     # Se envía el valor de cada acelerómetro pero no se envía el tiempo
    #                     varS_ACC = ['{:.2e}'.format(value[i, 1]), '{:.2e}'.format(value[i, 2]), '{:.2e}'.format(value[i, 3]),
    #                                 '{:.2e}'.format(value[i, 4]), '{:.2e}'.format(value[i, 5]), '{:.2e}'.format(value[i, 6]),
    #                                 '{:.2e}'.format(value[i, 7]), '{:.2e}'.format(value[i, 8]), '{:.2e}'.format(value[i, 9]),
    #                                 '{:.2e}'.format(value[i, 10]), '{:.2e}'.format(value[i, 11]), '{:.2e}'.format(value[i, 12]),
    #                                 '{:.2e}'.format(value[i, 13]), '{:.2e}'.format(value[i, 14]), '{:.2e}'.format(value[i, 15]),
    #                                 '{:.2e}'.format(value[i, 16]), '{:.2e}'.format(value[i, 17]), '{:.2e}'.format(value[i, 18]),
    #                                 '{:.2e}'.format(value[i, 19]), '{:.2e}'.format(value[i, 20]), '{:.2e}'.format(value[i, 21]),
    #                                 '{:.2e}'.format(value[i, 22]), '{:.2e}'.format(value[i, 23]), '{:.2e}'.format(value[i, 24])]
    #
    #                     i = 1 + i
    #
    #                     MESSAGE = ' '.join(varS_ACC)
    #                     BUFFER_SIZE = str(len(MESSAGE.encode('utf-8')))
    #                     sINTERAPPS_ACC.send(BUFFER_SIZE.encode('utf-8'))
    #                     sINTERAPPS_ACC.send(MESSAGE.encode('utf-8'))
    #
    #         except(OSError):
    #             print('No se puede realizar la decodificación')
    #
    #     self.sACC.close()
    #     tiempo_proceso = time.clock() - tic1
    #     print('El número de muestras del ACC %d' % i)
    #     print('Tiempo de toda de los datos ACC %f'% tiempo_proceso)
    #     print('Tiempo promedio de toma por cada datos ACC %f' % ((tiempo_proceso)/i))
    #     print('Terminó la lectura del ACC')
    #     # value1 =numpy.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dtype=numpy.dtype(decimal.Decimal))     # se tiene 9 datos uno para tiempo y los demás para sensores
    #     # f = open('datosACC.txt', 'w')  # Crea un archivo .txt donde se guardaran los datos, opción 'w'
    #     # f.write(" ".join(map(str, value1)))
    #     # f.write('\n')
    #     #
    #     # for v in range(0,i):
    #     #     f.write(" ".join(map(str, value[v,:])))
    #     #     f.write('\n')
    #     # f.close()
    #     # print('Se guardó los datos ACC en txt')
    #     dataList={}
    #     dataList.update(limbAcceleration=value[:i,:])
    #     sio.savemat('limbAcceleration.mat', dataList)
    #     print('Se guardó los datos de ACC en el archivo limbAcceleration.mat')
    #
    #     pass