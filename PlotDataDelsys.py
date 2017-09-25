import numpy
import decimal
import matplotlib.pyplot
import scipy.io as sio

matplotlib.pyplot.interactive(True)

class PlotDataDelsys():

    flagsensor = ['0','0','0','0','0','0','0','0','0']
    MeasuredMuscles = ['Músculo 1','Músculo 2', 'Músculo 3','Músculo 4','Músculo 5','Músculo 6','Músculo 7','Músculo 8']

    def __init__(self):
        print('Andres Parra')
        #self.fichero_EMG=open('datosEMG.txt','r')
        #self.fichero_VAR=open('varianceEMG.txt','r')

    # EMG
    def plotEMGandVar (self):

        data_EMG = open('dataEMG.txt', 'r')
        variance_EMG = open('varianceEMG.txt', 'r')

        #fichero_EMG.readline()
        length = 410000  # 303998 portatil y 359338 escritorio muestran en aprox 5 mins
        value_EMG = numpy.zeros((length, 9), dtype=numpy.dtype(decimal.Decimal))  # se tiene 9 datos uno para tiempo y los demás para sensores
        line='0'
        t_EMG = 0
        while len(line)>0:
            line=numpy.array(data_EMG.readline().split()).astype(float)
            if len(line)>0 :
                value_EMG[t_EMG,:] = line[0:9]
                t_EMG=t_EMG+1
        data_EMG.close()

        # VAR
        length = 20000  # 6076 portatil 10883 escritorio muestras en aprox 5 mins
        value_VAR = numpy.zeros((length, 9), dtype=numpy.float)  ## matriz de calculo de valores
        line='0'
        t_VAR = 0
        while len(line)>0:
            line=numpy.array(variance_EMG.readline().split()).astype(float)
            if len(line)>0 :
                value_VAR[t_VAR,:] = line[0:9]
                t_VAR=t_VAR+1
        variance_EMG.close()
        value_VAR[:,1:9]=value_VAR[:,1:9]*100000000
        print(value_VAR)
        # Imprime al valor de EMG y Varianza
        # mat_contents1 = sio.loadmat('dataMusclesEMG.mat')
        # mat_contents2 = sio.loadmat('varianceEMG.mat')
        #
        # value_EMG=mat_contents1['MusclesEMG']
        # muscle_EMG=mat_contents1['MeasuredMuscle']
        # value_VAR=mat_contents2['varianceEMG']
        #value_VAR[:, 1:9] = value_VAR[:, 1:9] * 10000

        value_transposeEMG = numpy.transpose(value_EMG[0:t_EMG,:])
        value_transposeVAR = numpy.transpose(value_VAR[0:t_VAR,:])

        for i in range (1,9):
            if(self.flagsensor[i-1]=='1'):
                matplotlib.pyplot.figure(i)
                #matplotlib.pyplot.subplot(421)
                matplotlib.pyplot.plot(value_transposeEMG[0,:],value_transposeEMG[i,:],value_transposeVAR[0,:],value_transposeVAR[i,:])
                matplotlib.pyplot.title('Gráficas de los datos de EMG y Varianza de ' + self.MeasuredMuscles[i - 1])
                matplotlib.pyplot.ylabel('Datos de EMG')
                matplotlib.pyplot.xlabel('Tiempo (segundos)')
                matplotlib.pyplot.legend(['Datos EMG ', 'Varianza x10e8'])

            #matplotlib.pyplot.axis([0,20, -10e-1,  10e-1])

        # matplotlib.pyplot.figure(2)
        # #matplotlib.pyplot.subplot(422)
        # matplotlib.pyplot.plot(value_transposeEMG[0,0:t_EMG],value_transposeEMG[2,0:t_EMG],value_transposeVAR[0,0:t_VAR],value_transposeVAR[2,0:t_VAR])
        # matplotlib.pyplot.ylabel('Señal de EMG y Varianza (Amperios)')
        # matplotlib.pyplot.xlabel('Tiempo (segundos)')
        # matplotlib.pyplot.legend(['Señal EMG', 'Varianza X1000'])
        # matplotlib.pyplot.title('Señal de EMG del sensor 2 ')

        # matplotlib.pyplot.subplot(423)
        # matplotlib.pyplot.plot(value_transposeEMG[0,0:t_EMG],value_transposeEMG[3,0:t_EMG],value_transposeVAR[0,0:t_VAR],value_transposeVAR[3,0:t_VAR])
        # #matplotlib.pyplot.ylabel('Señal de EMG (Amperios)')
        # #matplotlib.pyplot.xlabel('Tiempo (segundos)')
        # matplotlib.pyplot.title('Señal de EMG del sensor 3 ')
        #
        # matplotlib.pyplot.subplot(424)
        # matplotlib.pyplot.plot(value_transposeEMG[0,0:t_EMG],value_transposeEMG[4,0:t_EMG],value_transposeVAR[0,0:t_VAR],value_transposeVAR[4,0:t_VAR])
        # #matplotlib.pyplot.ylabel('Señal de EMG (Amperios)')
        # #matplotlib.pyplot.xlabel('Tiempo (segundos)')
        # matplotlib.pyplot.title('Señal de EMG del sensor 4 ')
        #matplotlib.pyplot.show(block=True)

    def plotEMGVar(self):

        variance_EMG = open('varianceEMG.txt', 'r')
        length = 20000  # 6076 portatil 10883 escritorio muestras en aprox 5 mins
        value_VAR = numpy.zeros((length, 9), dtype=numpy.float)  ## matriz de calculo de valores
        line='0'
        t_VAR = 0

        while len(line)>0:
            line=numpy.array(variance_EMG.readline().split()).astype(float)
            if len(line)>0 :
                value_VAR[t_VAR,:] = line[0:9]
                t_VAR=t_VAR+1
        variance_EMG.close()
        # mat_contents1 = sio.loadmat('dataMusclesEMG.mat')
        # mat_contents2 = sio.loadmat('varianceEMG.mat')
        #
        # #value_EMG=mat_contents1['MusclesEMG']
        # muscle_EMG=mat_contents1['MeasuredMuscle']
        # value_VAR=mat_contents2['varianceEMG']

        # Se multiplica value_VAR x10e7 para dismuir el número de dígitos al momento de escribir el número en la
        # terapia para el TremUna
        legendVar = []
        value_VAR[:,1:9]=value_VAR[:,1:9]*100000000
        value_transposeVAR = numpy.transpose(value_VAR[0:t_VAR,:])

        for i in range(1, 9):
            if (self.flagsensor[i - 1] == '1'):
                #matplotlib.pyplot.figure(i)
                # matplotlib.pyplot.subplot(421)
                matplotlib.pyplot.plot(value_transposeVAR[0,:], value_transposeVAR[i, :])
                legendVar.append('Datos de '+self.MeasuredMuscles[i-1])
                #legendVar.append('Músculo ' + muscle_EMG[i - 1])
        matplotlib.pyplot.title('Gráfica de datos de Varianza x10e8')
        matplotlib.pyplot.ylabel('Datos de Varianza')
        matplotlib.pyplot.xlabel('Tiempo (segundos)')
        matplotlib.pyplot.legend(legendVar)
        pass

    def plotACC (self):

        data_ACC = open('dataACC.txt', 'r')
        length = 60000  # 44993 muestras en aprox 5 mins
        value_ACC = numpy.zeros((length, 25), dtype=numpy.dtype(decimal.Decimal))  # se tiene 9 datos uno para tiempo y los demás para sensores

        line='0'
        t_ACC = 0
        while len(line)>0:
            line=numpy.array(data_ACC.readline().split()).astype(float)
            if len(line)>0 :
                value_ACC[t_ACC,:] = line[0:25]
                t_ACC=t_ACC+1
        data_ACC.close()
        # mat_contents = sio.loadmat('LimbAcceleration.mat')
        # value_ACC = mat_contents['limbAcceleration']
        value_transposeACC = numpy.transpose(value_ACC[0:t_ACC,:])

        for i in range(0, 8):
            if (self.flagsensor[i] == '1'):
                matplotlib.pyplot.figure(i+1)
                # matplotlib.pyplot.subplot(421)
                matplotlib.pyplot.plot(value_transposeACC[0,:], value_transposeACC[(3*i)+1, 0:],'b')
                matplotlib.pyplot.plot(value_transposeACC[0,:], value_transposeACC[(3*i)+2, 0:],'g')
                matplotlib.pyplot.plot(value_transposeACC[0,:], value_transposeACC[(3*i)+3, 0:],'r')
                matplotlib.pyplot.title('Gráfica de la datos de ACC para ' + self.MeasuredMuscles[i])
                matplotlib.pyplot.ylabel('Datos de ACC +-1.6*g')
                matplotlib.pyplot.xlabel('Tiempo (segundos)')
                matplotlib.pyplot.legend(['Datos ACC eje X', 'Datos ACC eje Y', 'Datos ACC eje Z'])
        pass

    def plotACCVar(self):

        variance_ACC = open('varianceACC.txt', 'r')
        length = 25000  # 6076 portatil 10883 escritorio muestras en aprox 5 mins
        value_VAR = numpy.zeros((length, 25), dtype=numpy.float)  ## matriz de calculo de valores

        line='0'
        t_VAR = 0

        while len(line)>0:
            line=numpy.array(variance_ACC.readline().split()).astype(float)
            if len(line)>0 :
                value_VAR[t_VAR,:] = line[0:25]
                t_VAR=t_VAR+1
        variance_ACC.close()
        # mat_contents2 = sio.loadmat('varianceACC.mat')
        # legendVar = []
        # #value_EMG=mat_contents1['MusclesEMG']
        # value_VAR=mat_contents2['varianceACC']
        # # Se multiplica value_VAR x10e7 para dismuir el número de dígitos al momento de escribir el número en la
        # # terapia para el TremUna
        value_VAR[:,1:25]=value_VAR[:,1:25]*100
        value_transposeACC = numpy.transpose(value_VAR[0:t_VAR,:])

        for i in range(0, 8):
            if (self.flagsensor[i] == '1'):
                matplotlib.pyplot.figure(i + 7)
                matplotlib.pyplot.plot(value_transposeACC[0, :], value_transposeACC[(3 * i) + 1, 0:], 'b')
                matplotlib.pyplot.plot(value_transposeACC[0, :], value_transposeACC[(3 * i) + 2, 0:], 'g')
                matplotlib.pyplot.plot(value_transposeACC[0, :], value_transposeACC[(3 * i) + 3, 0:], 'r')
                #legendVar.append('Varianza eje X','Varianza eje Y''Varianza eje Z')
                matplotlib.pyplot.title('Gráfica de datos de Varianza del ACC de ' + self.MeasuredMuscles[i] + ' x100')
                matplotlib.pyplot.ylabel('Datos de Varianza')
                matplotlib.pyplot.xlabel('Tiempo (segundos)')
                matplotlib.pyplot.legend(['Varianza eje X', 'Varianza eje Y', 'Varianza eje Z'])
        pass