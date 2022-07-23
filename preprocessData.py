from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

def createContinuePlots(df_diab):
    fig = make_subplots(rows=4, cols=2)
    fig.add_trace(
        go.Box(x=df_diab['Pregnancies'], name='Gravidez'),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Box(
            x=df_diab['Glucose'],
            name='Glicose'
        ),
        row=1,
        col=2
    )

    fig.add_trace(
        go.Box(
            x=df_diab['BloodPressure'],
            name='Pressão sanguínea'
        ),
        row=2,
        col=1
    )

    fig.add_trace(
        go.Box(
            x=df_diab['SkinThickness'],
            name='Busto'
        ),
        row=2,
        col=2
    )

    fig.add_trace(
        go.Box(
            x=df_diab['Insulin'],
            name='Insulina'
        ),
        row=3,
        col=1
    )

    fig.add_trace(
        go.Box(
            x=df_diab['BMI'],
            name='IMC'
        ),
        row=3,
        col=2
    )


    fig.add_trace(
        go.Box(
            x=df_diab['DiabetesPedigreeFunction'],
            name='Predição Diabetes '
        ),
        row=4,
        col=1
    )

    fig.add_trace(
        go.Box(
            x=df_diab['Age'],
            name='Idade'
        ),
        row=4,
        col=2
    )    

    fig.update_layout(height=700, width=900)
    fig.show()

def meanToData(df_diab):
    df_diab['Glucose'] = df_diab['Glucose'].apply(lambda x: df_diab['Glucose'].mean() if x<=0 else x)
    df_diab['BloodPressure'] = df_diab['BloodPressure'].apply(lambda x: df_diab['BloodPressure'].mean() if x<=0 else x)
    df_diab['Insulin'] = df_diab['Insulin'].apply(lambda x: df_diab['Insulin'].mean() if x<=0 else x)
    df_diab["BMI"] = df_diab["BMI"].apply(lambda x: df_diab.BMI.mean() if x>40 else x)
    df_diab['BMI'] = df_diab['BMI'].apply(lambda x: df_diab['BMI'].mean() if x<=0 else x)
    df_diab['SkinThickness'] = df_diab['SkinThickness'].apply(lambda x: df_diab['SkinThickness'].mean() if x<=0 else x)
    df_diab['DiabetesPedigreeFunction'] = df_diab['DiabetesPedigreeFunction'].apply(lambda x: ((x - df_diab['DiabetesPedigreeFunction'].min())/(df_diab['DiabetesPedigreeFunction'].max() - df_diab['DiabetesPedigreeFunction'].min())))
    return df_diab

def correl(df_diab):
    ax = plt.subplots(figsize=(20, 10))
    sns.heatmap(df_diab.corr(), annot=True, cmap='RdYlGn')

def createContinuePlotsHist(df_diab):
    fig, axs = plt.subplots(4, 2, figsize=(15,12))
    axs = axs.flatten()
    sns.distplot(df_diab['Pregnancies'],rug=True,color='#38b000',ax=axs[0])
    sns.distplot(df_diab['Glucose'],rug=True,color='#FF9933',ax=axs[1])
    sns.distplot(df_diab['BloodPressure'],rug=True,color='#522500',ax=axs[2])
    sns.distplot(df_diab['SkinThickness'],rug=True,color='#66b3ff',ax=axs[3])
    sns.distplot(df_diab['Insulin'],rug=True,color='#FF6699',ax=axs[4])
    sns.distplot(df_diab['BMI'],color='#e76f51',rug=True,ax=axs[5])
    sns.distplot(df_diab['DiabetesPedigreeFunction'],color='#03045e',rug=True,ax=axs[6])
    sns.distplot(df_diab['Age'],rug=True,color='#333533',ax=axs[7])
    plt.show()

