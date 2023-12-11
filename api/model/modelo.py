import numpy as np
import pickle
import joblib

class Model:
    
    def carrega_modelo(path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def preditor(model, form):
        """Realiza a predição de um paciente com base no modelo treinado
        """
        X_input = np.array([form.age, 
                            form.anae, 
                            form.crea, 
                            form.diab, 
                            form.ejec,
                            form.high, 
                            form.plate, 
                            form.ser_crea,
                            form.ser_sodi,
                            form.sex,
                            form.smok,                            
                            form.tim                            
                        ])   
        
        # Faremos o reshape para que o modelo entenda que estamos passando
        death = model.predict(X_input.reshape(1, -1))        
        return int(death[0])



       
