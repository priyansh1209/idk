import pandas as pd 
import plotly.express as pe
import numpy as np

yes = pd.read_csv("poject idk\yes.csv")

noper = yes["Marks In Percentage"].tolist()

nodays = yes["Days Present"].tolist()

alsoNo = pe.scatter( yes , x=nodays , y=noper )
 
alsoNo.show()

corelationCoeff = np.corrcoef( [nodays] , [noper])

print("Corelation coefficient --> " , corelationCoeff[0,1] )