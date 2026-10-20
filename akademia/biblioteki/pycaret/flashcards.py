import pandas as pd
from pycaret.regression import setup, compare_models, plot_model, load_model, predict_model
from pycaret.classification import load_model, predict_model

# jak znaleźć najlepszy model regresji
df = pd.read_csv('data.csf', sep=';')
setup(df, target='price')
best = compare_models()

# jak dokonać predykcji w pycaret dla modelu klasyfikacji
model = load_model('classification_pipeline')
predict_df = pd.read_csv('predict_data.csv', sep=";")
predictions = predict_model(model, data=predict_model)

# jak zwizualizować ważność cech modelu w pycaret
df = pd.read_csv('data.csf', sep=';')
setup(df, target='price')
best = compare_models()
plot_model(best, plot="feature")

# jak zwizualizować model klasyfikacji w pycaret
df = pd.read_csv('data.csf', sep=';')
setup(df, target='sentiment')
best = compare_models()
plot_model(best, plot="confusion_matrix")

# jak dokonać predykcji w pycaret dla modelu klasyfikacji
model = load_model('regression_pipeline')
predict_df = pd.read_csv('predict_data.csv', sep=";")
predictions = predict_model(model, data=predict_df)