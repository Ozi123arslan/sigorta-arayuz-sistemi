import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
def grafik_goster():
    arac_Degerleri=[400000,400000,500000,800000,1000000]
    kademeler=[1,7,5,2,6]
    primler=[20000,8000,14000,35000,15000]

    X=np.column_stack((arac_Degerleri,kademeler))
    y=np.array(primler)

    model=LinearRegression()
    model.fit(X,y)


    fig=plt.figure(figsize=(10,7))
    ax=fig.add_subplot(111,projection='3d')
    ax.scatter(arac_Degerleri,kademeler,primler,color="red",s=150)

    x_ag=np.linspace(min(arac_Degerleri),max(arac_Degerleri),10)
    y_ag=np.linspace(min(kademeler),max(kademeler),10)
    x_yuzey,y_yuzey =np.meshgrid(x_ag,y_ag)

    z_yuzey=model.predict(np.column_stack((x_yuzey.ravel(),y_yuzey.ravel())))
    z_yuzey=z_yuzey.reshape(x_yuzey.shape)

    ax.plot_surface(x_yuzey,y_yuzey,z_yuzey,color='cyan',alpha=0.5)

    ax.set_xlabel("Arac Degeri (TL)")
    ax.set_ylabel("Hasarsızlık Kademesi (1-7)")
    ax.set_zlabel("Kasko Primi (TL)")
    ax.ticklabel_format(style='plain',axis='x')
    ax.ticklabel_format(style='plain',axis='z')
    plt.show()


