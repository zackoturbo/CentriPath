import matplotlib.pyplot as plt


class CentriPath:
    def __init__(self, diam_outlet, width_outlet, diam_hub, diam_suction, len_axial=None):
        self.D_2 = diam_outlet
        self.b_2 = width_outlet
        self.D_hub = diam_hub
        self.len_ax = len_axial if len_axial != None else 0.2*self.D_2
        self.D_S = diam_suction
    
    
    
    
    def plot_inlet_outlet(self):
        plt.title(f"Meriodnal Path (D_2 = {self.D_2})")
        # PLOT AXIS 
        plt.hlines(0, -50, 50, linestyles="dotted")
        plt.vlines(0, 0, 0.5*self.D_2*1.15, linestyles="dotted")
        
        # INLET
        plt.plot([-self.len_ax, -self.len_ax], [0.5*self.D_hub, 0.5*self.D_S], color="black")
        
        # OUTELT
        plt.plot([-0.5*self.b_2, 0.5*self.b_2], [0.5*self.D_2, 0.5*self.D_2], color="black")
    
        plt.show()
    
    

test_plot = CentriPath(250, 17, 60, 160, 50)
test_plot.plot_inlet_outlet()

        
    