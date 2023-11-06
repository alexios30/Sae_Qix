
    #pPoint de départ du qix 
    x_qix=300
    y_qix=300
    #Vitesse Qix
    vitesse_qix=10
    #Milieu du Qix
    milieu_qix=30
x_qix,y_qix=deplacement_qix(x_qix,y_qix,vitesse_qix,circuitX1,circuitX2,circuitY1,circuitY2,milieu_qix)
        efface('kong')
        qix(x_qix,y_qix)
        sleep(0.01)
        mise_a_jour()
