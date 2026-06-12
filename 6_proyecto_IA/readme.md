# PRONOSTICO DE DEMANDA POR PRODUCTO (SKU) CON REGRESION LINEAL
 
 
# IDEA
El tutorial original predice el PRECIO de una accion N dias hacia el futuro usando regresion lineal (features hoy -> valor futuro). Aqui aplicamos la misma logica, pero para predecir la DEMANDA (Order_Demand) de un producto N semanas hacia el futuro. Eso es justo lo que necesita un inventory planner: saber cuanto se va a consumir para definir cuanto pedir.

## Tutorial
- [Introduction](https://pythonprogramming.net/machine-learning-tutorial-python-introduction/)
- [Regression - Intro and Data](https://pythonprogramming.net/regression-introduction-machine-learning-tutorial/)
- [Regression - Features and Labels](https://pythonprogramming.net/features-labels-machine-learning-tutorial/)
- [Regression - Training and Testing](https://pythonprogramming.net/training-testing-machine-learning-tutorial/)
- [Regression - Forecasting and Prediction](https://pythonprogramming.net/forecasting-predicting-machine-learning-tutorial/)

## Datos obtenidos en
https://www.kaggle.com/datasets/felixzhao/productdemandforecasting/data

# PASOS
1. Cargar y limpiar datos reales
2. Construir una serie de tiempo de demanda (resample semanal)
3. Crear FEATURES (lags, medias moviles, indice de tiempo)
4. Crear el LABEL: demanda desplazada -forecast_out (shift)
5. Escalar X, separar train/test
6. Entrenar LinearRegression y medir el score (R^2)
7. Pronosticar las proximas 'forecast_out' semanas
8. Graficar historico + pronostico
