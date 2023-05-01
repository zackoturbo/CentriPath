import math
import matplotlib.pyplot as plt
import scipy.special as sci

class BezierCurve():

    def __init__(self, pnt_List, n=None, u=0.001):
        self.pnt_list = pnt_List  # Punkteliste
        
        self.x_pnt = [self.pnt_list[i][0] for i in range(len(self.pnt_list))] # X-Koord. der Punkte
        self.y_pnt = [self.pnt_list[i][1] for i in range(len(self.pnt_list))] # Y-Koord. der Punkte

        self.n = n # Polynomial Order; Ordnung des Polynoms (n=1 - Linear; n=2 - quadratisch etc.)
        self. i = len(self.pnt_list)
        
        if self.n == None:
            self.n = len(self.x_pnt) -1
        else:
            pass
        

        self.u = u # Intervall für die Kurve
        self.u_len = 1 / self.u


    def setPolynomialDegree(self, n):
        self.n = n


    def calc_bezierpoints(self):
        B_u = []
        x = []
        y = []
        x_u = 0
        y_u = 0
        u_count = 0.0

        while u_count < 1:

            B_u = 0
            x_u = 0
            y_u = 0
            for j in range(self.i):

                B_u = (sci.binom(self.n, j) * (1-u_count)**(self.n-j) * u_count**j)

                x_u += (self.x_pnt[j] * B_u)
                y_u += (self.y_pnt[j] * B_u)

            x.append(x_u)
            y.append(y_u)
            u_count+= self.u

        self.x = x
        self.y = y
        
        return self.x, self.y

    def get_berzier_points(self):
        return self.x, self.y
        
        
    def plotBezier(self):
        plt.plot(self.x_pnt, self.y_pnt, color="black")
        plt.plot([0,1], [0,0], color="black")
        plt.plot(self.x, self.y)
        plt.show()
        





