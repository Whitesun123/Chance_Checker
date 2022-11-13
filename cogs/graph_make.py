import matplotlib.pyplot as plt

def graphMaker(i,zp,op,tp,thp,fp,fip,sp,sep,ep,np,tep,elp,twp,thip,fop,fifp):
    """ Makes a graph.

    Args:
        i (int):    Number of tries
        zp (int):   Precentage number
        op (int):   Precentage number
        tp (int):   Precentage number
        thp (int):  Precentage number
        fp (int):   Precentage number
        fip (int):  Precentage number
        sp (int):   Precentage number
        sep (int):  Precentage number
        ep (int):   Precentage number
        np (int):   Precentage number
        tep (int):  Precentage number
        elp (int):  Precentage number
        twp (int):  Precentage number
        thip (int): Precentage number
        fop (int):  Precentage number
        fifp (int): Precentage number
    """
    
    numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    percentages = [zp,op,tp,thp,fp,fip,sp,sep,ep,np,tep,elp,twp,thip,fop,fifp]

    plt.plot(numbers, percentages)
    plt.ylabel('Percentage')
    plt.xlabel('Numbers')                           # Setting up graph
    plt.title(f"Percentage Graph | Tries : {i}")
    plt.show()                                      # Showing the graph