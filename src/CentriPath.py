import matplotlib.pyplot as plt
from enum import Enum
from BezierCurve import BezierCurve

class Profiles(Enum):
    HUB = 1,
    MEAN = 2,
    SHROUD = 3


class CentriPath:
    def __init__(self, diam_outlet, width_outlet, diam_hub, diam_suction, len_axial=None):
        self.D_2 = diam_outlet
        self.b_2 = width_outlet
        self.D_hub = diam_hub
        self.len_ax = len_axial if len_axial != None else 0.2*self.D_2
        self.D_S = diam_suction
    
    
    def load_centripath(self, filename : str):
        pass
    

    def plot_inlet_outlet(self, plot_circles=False):
        plt.title(f"Meriodnal Path (D_2 = {self.D_2})")
        # PLOT AXIS 
        plt.hlines(0, -50, 50, linestyles="dotted")
        plt.vlines(0, 0, 0.5*self.D_2*1.15, linestyles="dotted")
        
        # INLET
        plt.plot([-self.len_ax, -self.len_ax], [0.5*self.D_hub, 0.5*self.D_S], color="black")
        
        # OUTELT
        plt.plot([-0.5*self.b_2, 0.5*self.b_2], [0.5*self.D_2, 0.5*self.D_2], color="black")

        # DRAW CIRCLES
        if plot_circles== True:
            mean_inlet = 0.5 *(0.5*self.D_S + 0.5*self.D_hub)
            radius_inlet = 0.25*(self.D_S-self.D_hub)
            radius_outlet = self.b_2*0.5
            Circle_Inlet = plt.Circle((-self.len_ax, mean_inlet), radius_inlet, color='g', fill=False)
            Circle_Outlet = plt.Circle((0, 0.5*self.D_2), radius_outlet, color="g", fill = False)
            
            ax = plt.gca()
            ax.add_patch(Circle_Inlet)
            ax.add_patch(Circle_Outlet)
            
        
        plt.draw()
        ax.set_aspect('equal')
        
    def plot_bezier(self):
        """
        Plots the bezier curve that have been calcualted onto an existing figure.
        """
        plt.gcf()
        plt.plot(self.x_bezier, self.y_bezier, color="red")
        plt.show()

        
   
    
    def create_profile_points(self, profile=Profiles.HUB):
        """Function will take the bezier curve data and 
            create an array for the specified profile
        """
        pass
    
    
    def calc_profile_circles(self, profile=Profiles.HUB):
        """
        Will calculate the constant massflow /Volume flow circles from inlet to outlet
        along the points. 
        Factor for Inlet in x-direction: 1.5*Axial Length of the impeller
        Factor for Outlet in y-direction: 1.5*Outer Radius of the impeller
        """
        pass
    
    
    def add_inletoutlet_points(self):
        """
        Will add additional points for the two profiles at the inlet and outlet.
        These can be used for throughflow methods or for other CFD analysis.
        """
        pass
    
    def calc_bezier_profile(self, profile = Profiles.HUB):
        points = []
        if profile == Profiles.HUB:
            points.append([-self.len_ax, 0.5*self.D_hub])
            points.append([-self.len_ax*0.5, 0.5*self.D_hub])
            points.append([0, 0.5*self.D_hub])
            points.append([0.5*self.b_2, 0.15*self.D_2])
            points.append([0.5*self.b_2, 0.35*self.D_2])
            points.append([0.5*self.b_2, 0.5*self.D_2])
            
            Hub_Bezier = BezierCurve(points)
            self.x_bezier, self.y_bezier = Hub_Bezier.calc_bezierpoints()
            
            
        elif profile == Profiles.SHROUD:
            pass
        
        else:
            print("Wrong profile specified. Only >Hub< and >Shroud< possible.")
            
        
        
    def export_centripath(self):
        FILENAME = "Centri_Path.txt"
        
        pass
    
    def export_profile(self, profile=Profiles.HUB):
        if profile == Profiles.HUB:
            FILENAME = "hub.txt"
        elif profile == Profiles.SHROUD:
            FILENAME == "shroud.txt"
        else:
            print("Worng profile specified. Only Hub and Shroud can be exported")
            
    
        
        
        
test_plot = CentriPath(350, 15, 60, 160, 60)
test_plot.calc_bezier_profile(Profiles.HUB)
test_plot.plot_inlet_outlet(plot_circles=True)
test_plot.plot_bezier()
    
    


        
    