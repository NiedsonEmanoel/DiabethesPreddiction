import pandas as pd

import preprocessData as preProcess'
from pycaret.classification import * 

df_diab = pd.read_csv('diabetes.csv')

df_diab = preProcess.meanToData(df_diab)
preProcess.createContinuePlots(df_diab)
preProcess.createContinuePlotsHist(df_diab)
preProcess.correl(df_diab)

mSet = setup(df_diab, target='Outcome', normalize=False, session_id=1)
compare_models()

rf = create_model('rf', fold=10)

plot_model(rf, plot = 'confusion_matrix')

create_app(rf)