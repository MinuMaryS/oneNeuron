from utils.all_utils import prepare_data, save_model, save_plot
from utils.model import Perceptron
import pandas as pd

def main(data,eta,epochs):
    
    df=pd.DataFrame(data)
    print(df)
    X,y=prepare_data(df)
   
    model=Perceptron(eta=eta,epochs=epochs)
    model.fit(X,y)
    _=model.total_loss()
    
    save_model(model,filename="and.model")
    save_plot(df,"and.png",model)

if __name__=='__main__':
    AND={
        "x1":[0,0,1,1],
        "x2":[0,1,0,1],
        "y":[0,0,0,1]
    } 
    ETA=0.3
    EPOCHS=10
    main(data=AND,eta=ETA,epochs=EPOCHS)
