import PySimpleGUI as sg
import numpy as np
from numpy import pi, sin, cos, sqrt, absolute, arccos, arctan, sign
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 

class Interface:

    def hacer_saludo():
        ly_saludo = [
            [sg.Text("Universidad Nacional de Trujillo", text_color="red")],
            [sg.Text("Ingeniería Mecatrónica", text_color="red")],
            [sg.Text("Teoría de Máquinas y Mecanismos", text_color="red")],
            [sg.Image("unt.png")], [sg.Image("mecatronica.png")],
            [sg.Text("Integrantes:", text_color="black")],
            [sg.Text("Calderón Alvarado, Jeremy Lorenzo", text_color="black")],
            [sg.Text("Carrillo Guevara, Abigail Bibiana", text_color="black")],
            [sg.Button("Continuar")],
            [sg.Button("Salir")]
        ]
        return sg.Window("Interfaz gráfica", ly_saludo)
    
    def hacer_inicio1():
        ly_inicio1 = [
            [sg.Text("Mecanismo", text_color="red")],
            [sg.Image("mecanismo.png")],
            [sg.Button("Iniciar")],
            [sg.Button("Salir")]
        ]
        return sg.Window("Mecanismo", ly_inicio1)
    
    def hacer_inicio2():
        ly_inicio2 = [
            [sg.Text("Indicar el valor de los siguientes datos:")],
            [sg.Text("P21x")], [sg.InputText('',key='input_height1')],
            [sg.Text("P21y")], [sg.InputText('',key='input_height2')],
            [sg.Text("P31x")], [sg.InputText('',key='input_height3')],
            [sg.Text("P31y")], [sg.InputText('',key='input_height4')],
            [sg.Text("O2x")], [sg.InputText('',key='input_height5')],
            [sg.Text("O2y")], [sg.InputText('',key='input_height6')],
            [sg.Text("O4x")], [sg.InputText('',key='input_height7')],
            [sg.Text("O4y")], [sg.InputText('',key='input_height8')],
            [sg.Text("theta1 (en sexagesimal)")], [sg.InputText('',key='input_height9')],
            [sg.Text("theta2 (en sexagesimal)")], [sg.InputText('',key='input_height10')],
            [sg.Text("theta3 (en sexagesimal)")], [sg.InputText('',key='input_height11')],
            [sg.Button("Resultados")],
            [sg.Button("Salir")]
        ]
        return sg.Window("Menú Inicio", ly_inicio2)
        
    def calcular_resultados(P21x, P21y, P31x, P31y, O2x, O2y, O4x, O4y, theta1, theta2, theta3):

        # Calculamos valores de alfa
        alfa2 = theta2 - theta1
        alfa3 = theta3 - theta1
        # Calculamos magnitudes y componentes de R1,R2,R3
        r1x = -O2x
        r1y = -O2y
        r1 = np.sqrt((r1x)**2 + (r1y)**2)

        r2x = r1x + P21x
        r2y = r1y + P21y
        r2 = np.sqrt((r2x)**2 + (r2y)**2)

        r3x = r1x + P31x
        r3y = r1y + P31y
        r3 = np.sqrt((r3x)**2 + (r3y)**2)

        # Hallamos los angulos de R (1,2,3)
        phi1 = np.degrees(np.arctan2(r1y,r1x)) # Angulo de R1
        phi2 = np.degrees(np.arctan2(r2y,r2x)) # Angulo de R2
        phi3 = np.degrees(np.arctan2(r3y,r3x)) # Angulo de R3


        C1 = r3*np.cos(np.radians(alfa2 + phi3)) - r2*np.cos(np.radians(alfa3 + phi2))
        C2 = r3*np.sin(np.radians(alfa2 + phi3)) - r2*np.sin(np.radians(alfa3 + phi2))
        C3 = r1*np.cos(np.radians(alfa3 + phi1)) - r3*np.cos(np.radians(phi3))
        C4 = -r1*np.sin(np.radians(alfa3 + phi1)) + r3*np.sin(np.radians(phi3))
        C5 = r1*np.cos(np.radians(alfa2 + phi1)) - r2*np.cos(np.radians(phi2))
        C6 = -r1*np.sin(np.radians(alfa2 + phi1)) + r2*np.sin(np.radians(phi2))

        A1 = -(C3)**2 - (C4)**2
        A3 = -(C4*C6) - (C3*C5)
        A5 = C4*C5 - C3*C6
        A2 = C3*C6 - C4*C5
        A4 = C2*C3 + C1*C4
        A6 = C1*C3 - C2*C4

        K1 = A2*A4 + A3*A6
        K2 = A3*A4 + A5*A6
        K3 = (A1**2-A2**2-A3**2-A4**2-A6**2)/(2)

        beta31 = 2*np.degrees(np.arctan2((K2 + np.sqrt(K1**2 + K2 **2 - K3**2)),(K1+K3)))
        beta32 = 2*np.degrees(np.arctan2((K2 - np.sqrt(K1**2 + K2 **2 - K3**2)),(K1+K3)))

        beta21 = np.degrees(np.arctan2(-((A3*np.sin(np.radians(beta31)) + A2*np.cos(np.radians(beta31))) + A4),-(A5*np.sin(np.radians(beta31))+A3*np.cos(np.radians(beta31))+A6)))
        beta22 = np.degrees(np.arctan2(-((A3*np.sin(np.radians(beta32)) + A2*np.cos(np.radians(beta32))) + A4),-(A5*np.sin(np.radians(beta32))+A3*np.cos(np.radians(beta32))+A6)))

        r1px = -O4x
        r1py = -O4y

        r2px = r1px + P21x
        r2py = r1py + P21y
        r3py = r1py + P31y
        r3px = r1px + P31x

        r1p = np.sqrt((r1px)**2 + (r1py)**2)
        r2p = np.sqrt((r2px)**2 + (r2py)**2)
        r3p = np.sqrt((r3px)**2 + (r3py)**2)

        # Hallamos los angulos de R' (1,2,3)
        phi1p = np.degrees(np.arctan2(r1py,r1px)) # Angulo de R1'
        phi2p = np.degrees(np.arctan2(r2py,r2px)) # Angulo de R2'
        phi3p = np.degrees(np.arctan2(r3py,r3px)) # Angulo de R3'

        C1p = r3p*np.cos(np.radians(alfa2 + phi3p)) - r2p*np.cos(np.radians(alfa3 + phi2p))
        C2p = r3p*np.sin(np.radians(alfa2 + phi3p)) - r2p*np.sin(np.radians(alfa3 + phi2p))
        C3p = r1p*np.cos(np.radians(alfa3 + phi1p)) - r3p*np.cos(np.radians(phi3p))
        C4p = -r1p*np.sin(np.radians(alfa3 + phi1p)) + r3p*np.sin(np.radians(phi3p))
        C5p = r1p*np.cos(np.radians(alfa2 + phi1p)) - r2p*np.cos(np.radians(phi2p))
        C6p = -r1p*np.sin(np.radians(alfa2 + phi1p)) + r2p*np.sin(np.radians(phi2p))

        A1p = -(C3p)**2 - (C4p)**2
        A3p = -(C4p*C6p) - (C3p*C5p)
        A5p = C4p*C5p- C3p*C6p
        A2p = C3p*C6p - C4p*C5p
        A4p = C2p*C3p + C1p*C4p
        A6p = C1p*C3p - C2p*C4p

        K1p = A2p*A4p + A3p*A6p
        K2p = A3p*A4p + A5p*A6p
        K3p = (A1p**2-A2p**2-A3p**2-A4p**2-A6p**2)/(2)

        gamma31 = 2*np.degrees(np.arctan2((K2p + np.sqrt(K1p**2 + K2p**2 - K3p**2)),(K1p+K3p)))
        gamma32 = 2*np.degrees(np.arctan2((K2p - np.sqrt(K1p**2 + K2p**2 - K3p**2)),(K1p+K3p)))

        gamma21 = np.degrees(np.arctan2(-((A3p*np.sin(np.radians(gamma31)) + A2p*np.cos(np.radians(gamma31))) + A4p),-(A5p*np.sin(np.radians(gamma31))+A3p*np.cos(np.radians(gamma31))+A6p)))
        gamma22 = np.degrees(np.arctan2(-((A3p*np.sin(np.radians(gamma32)) + A2p*np.cos(np.radians(gamma32))) + A4p),-(A5p*np.sin(np.radians(gamma32))+A3p*np.cos(np.radians(gamma32))+A6p)))

        P21 = np.sqrt(P21x**2 + P21y**2)
        delta2 = np.degrees(np.arctan2(P21y,P21x))

        P31 = np.sqrt(P31x**2 + P31y**2)
        delta3 = np.degrees(np.arctan2(P31y,P31x))

        beta2 = beta21
        A = np.cos(np.radians(beta2)) - 1
        B = np.sin(np.radians(beta2))
        C = np.cos(np.radians(alfa2)) - 1
        D = np.sin(np.radians(alfa2))
        E = P21*np.cos(np.radians(delta2))
        beta3 = beta31
        F = np.cos(np.radians(beta3)) - 1
        G = np.sin(np.radians(beta3))
        H = np.cos(np.radians(alfa3)) -1
        K = np.sin(np.radians(alfa3))
        L = P31*np.cos(delta3)
        M = P21*np.sin(delta2)
        N = P31*np.sin(delta3)

        MA = np.matrix([[A,-B,C,-D],[F,-G,H,-K],[B,A,D,C],[G,F,K,H]])
        b = np.matrix([[E],[L],[M],[N]])
        x = (MA**-1)*b

        #Longitud del eslabón L2
        w = np.sqrt(x[0]**2 + x[1]**2)

        gamma2 = gamma21
        Ap = np.cos(np.radians(gamma2)) - 1
        Bp = np.sin(np.radians(gamma2))
        Cp = np.cos(np.radians(alfa2)) - 1
        Dp = np.sin(np.radians(alfa2))
        Ep = P21*np.cos(np.radians(delta2))
        gamma3 = gamma31
        Fp = np.cos(np.radians(gamma3)) - 1
        Gp = np.sin(np.radians(gamma3))
        Hp = np.cos(np.radians(alfa3)) -1
        Kp = np.sin(np.radians(alfa3))
        Lp = P31*np.cos(delta3)
        Mp = P21*np.sin(delta2)
        Np = P31*np.sin(delta3)

        MAp = np.matrix([[Ap,-Bp,Cp,-Dp],[Fp,-Gp,Hp,-Kp],[Bp,Ap,Dp,Cp],[Gp,Fp,Kp,Hp]])
        bp = np.matrix([[Ep],[Lp],[Mp],[Np]])
        xp = (MAp**-1)*bp

        #Longitud del eslabón L4
        u = np.sqrt(xp[0]**2 + xp[1]**2)

        zx = x[2]
        zy = x[3]
        sx = xp[2]
        sy = xp[3]

        vx = zx - sx
        vy = zy - sy

        #Longitud del eslabón L3
        v = np.sqrt(vx**2 + vy**2)

        gx = x[0] - vx + xp[0]
        gy = x[1] - vy + xp[1]

        #Longitud del eslabón L1
        g = np.sqrt(gx**2 + gy**2)

        Y = [g, w, v, u]

        f = open("resultados.txt","a")
        for i in Y:
            f.write(f'{i}\n')
        f.close()


    def mostrar_resultados():
        f = open("resultados.txt", "r")
        lineas = f.readlines()

        ly_resultados = [
            [sg.Text(f'L1 = {lineas[0]}')],
            [sg.Text(f'L2 = {lineas[1]}')],
            [sg.Text(f'L3 = {lineas[2]}')],
            [sg.Text(f'L4 = {lineas[3]}')],
            [sg.Button("Finalizar")],
            [sg.Button("Salir")]
        ]
        return sg.Window("Resultados", ly_resultados)

ejecuta = True

while ejecuta:
        
    sg.theme("LightBlue1")
    saludo = Interface.hacer_saludo()
    inicio1 = Interface.hacer_inicio1()
    inicio2 = Interface.hacer_inicio2()
    resultados = Interface.mostrar_resultados()

    try:
        while True:
            event, values = saludo.read()
            if event == "Salir"  or event == sg.WINDOW_CLOSED:
                break
            if event == "Continuar":
                saludo.close()
                while True:
                    event, values = inicio1.read()
                    if event == "Salir"  or event == sg.WINDOW_CLOSED:
                        break
                    if event == 'Iniciar':
                        sg.popup_ok("¿Estás listo/a?")
                        inicio1.close()
                        while True:
                            event, values = inicio2.read()
                            if event == "Salir"  or event == sg.WINDOW_CLOSED:
                                break
                            if event == "Resultados":
                                Interface.calcular_resultados(int(values['input_height1']),int(values['input_height2']),int(values['input_height3']),int(values['input_height4']),int(values['input_height5']),int(values['input_height6']),int(values['input_height7']),int(values['input_height8']),int(values['input_height9']),int(values['input_height10']),int(values['input_height11']))
                                inicio2.close()
                                while True:
                                    event, values = resultados.read()
                                    if event == "Salir"  or event == sg.WINDOW_CLOSED:
                                        break
                                    if event == "Finalizar":
                                        resultados.close() #falta
                            
    except:
        print("Ocurrió algún error")
    finally:
        saludo.close()
        inicio1.close()
        inicio2.close()
        resultados.close()
        print("Todo cerrado")
        ejecuta = False
