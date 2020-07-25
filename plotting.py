import matplotlib.pyplot as plt 


def gen_plot(nr,nc):
    fig,axis=plt.subplots(nr,nc)
    return fig,axis
    
def plot_car_image(image,fig,axes):
    axes.imshow(image,cmap="gray")
    

def add_borders(border,fig,axes):
    axes.add_patch(border)
    
def show():
    plt.show()
