import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# =====================  CONFIGURACION  =======================================
# Ruta al CSV descargado de Kaggle
CSV_PATH = "6_proyecto_IA\\Historical Product Demand.csv"
PRODUCT_CODE = "Product_0992"
# Frecuencia de agregacion: "W" = semanal, "M" = mensual
RESAMPLE_FREQ = "W"
# Cuantos periodos hacia el futuro queremos predecir
FORECAST_OUT = 12  # 12 semanas
# =============================================================================

# Limpiamos los datos del archivo
def cargar_y_limpiar(csv_path):
    """Carga el CSV real y limpia la columna Order_Demand y Date."""
    df = pd.read_csv(csv_path)

    # En este dataset, Order_Demand viene como TEXTO con detalles raros:
    #   - espacios en blanco
    #   - valores negativos escritos entre parentesis, ej. "(100)"
    #   - separador de miles en algunos casos
    df["Order_Demand"] = (
        df["Order_Demand"]
        .astype(str)
        .str.strip()
        .str.replace("(", "-", regex=False)   # (100) -> -100
        .str.replace(")", "", regex=False)
        .str.replace(",", "", regex=False)
    )
    df["Order_Demand"] = pd.to_numeric(df["Order_Demand"], errors="coerce")

    # Fecha a datetime; descartamos filas sin fecha o sin demanda
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date", "Order_Demand"])

    return df

# Elegimos el producto a pronostricar
def elegir_producto(df, product_code):
    """Devuelve el codigo de producto a usar (el indicado o el de mas datos)."""
    if product_code is not None:
        return product_code
    top = df["Product_Code"].value_counts().idxmax()
    print(f"[info] No se especifico PRODUCT_CODE -> se eligio el SKU con mas "
          f"registros: {top}")
    return top

# Construimos la serie de tiempo del producto elegido, agregando por semana/mes
def construir_serie(df, product_code, freq):
    """Filtra un producto y agrega la demanda en una serie de tiempo regular."""
    sub = df[df["Product_Code"] == product_code].copy()
    sub = sub.set_index("Date").sort_index()

    # Sumamos la demanda por periodo (semana/mes). asfreq llena huecos con 0,
    # porque "sin pedidos" en una semana = demanda 0.
    serie = sub["Order_Demand"].resample(freq).sum().fillna(0)
    return serie.to_frame(name="demand")

# Creamos features predictoras a partir de la demanda historica (lags, medias moviles, tendencia)
def crear_features(data):
    """Crea variables predictoras a partir de la demanda (estilo features del tutorial)."""
    df = data.copy()

    # Indice de tiempo numerico (tendencia)
    df["t"] = np.arange(len(df))

    # Lags: demanda de periodos anteriores (lo mas predictivo en series de tiempo)
    df["lag_1"] = df["demand"].shift(1)
    df["lag_2"] = df["demand"].shift(2)
    df["lag_4"] = df["demand"].shift(4)

    # Medias moviles: capturan la tendencia reciente y suavizan el ruido
    df["roll_4"] = df["demand"].rolling(window=4).mean()
    df["roll_12"] = df["demand"].rolling(window=12).mean()

    # Quitamos las primeras filas que quedaron con NaN por los lags/rolling
    df = df.dropna()
    return df


def main():
    # ---- 1 y 2: cargar, limpiar y construir la serie de tiempo --------------
    print("[1/6] Cargando y limpiando datos reales...")
    df = cargar_y_limpiar(CSV_PATH)
    code = elegir_producto(df, PRODUCT_CODE)
    serie = construir_serie(df, code, RESAMPLE_FREQ)
    print(f"[info] Producto: {code} | periodos: {len(serie)} | "
          f"frecuencia: {RESAMPLE_FREQ}")

    if len(serie) < (FORECAST_OUT + 20):
        print("[aviso] Este SKU tiene pocos periodos para un pronostico solido. "
              "Considera elegir otro PRODUCT_CODE con mas historico.")

    # ---- 3: features --------------------------------------------------------
    print("[2/6] Creando features (lags, medias moviles, tendencia)...")
    data = crear_features(serie)

    forecast_col = "demand"
    forecast_out = FORECAST_OUT

    # ---- 4: label = demanda desplazada hacia el futuro (igual que el tutorial)
    data["label"] = data[forecast_col].shift(-forecast_out)

    feature_cols = ["t", "lag_1", "lag_2", "lag_4", "roll_4", "roll_12", "demand"]
    X = np.array(data[feature_cols])

    # ---- 5: escalar X (preprocessing.scale, igual que el tutorial) ----------
    X = preprocessing.scale(X)

    # Las ultimas 'forecast_out' filas NO tienen label (es lo que queremos predecir)
    X_lately = X[-forecast_out:]
    X = X[:-forecast_out]

    data_labeled = data.dropna(subset=["label"])
    y = np.array(data_labeled["label"])

    # ---- 6: train/test + entrenar -------------------------------------------
    print("[3/6] Entrenando regresion lineal...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    clf = LinearRegression()
    clf.fit(X_train, y_train)

    r2 = clf.score(X_test, y_test)
    mae = mean_absolute_error(y_test, clf.predict(X_test))
    print(f"[4/6] Desempeno -> R^2: {r2:.3f} | MAE: {mae:,.1f} unidades")

    # ---- 7: pronostico de las proximas 'forecast_out' semanas ---------------
    print("[5/6] Generando pronostico futuro...")
    forecast_set = clf.predict(X_lately)
    forecast_set = np.clip(forecast_set, 0, None)  # la demanda no es negativa

    # Fechas futuras para el pronostico
    last_date = serie.index[-1]
    step = serie.index.freq or pd.tseries.frequencies.to_offset(RESAMPLE_FREQ)
    future_dates = pd.date_range(
        start=last_date + step, periods=forecast_out, freq=RESAMPLE_FREQ
    )
    forecast_df = pd.DataFrame(
        {"fecha": future_dates, "demanda_pronosticada": np.round(forecast_set, 1)}
    )

    print("\n===== PRONOSTICO DE DEMANDA (proximas "
          f"{forecast_out} {('semanas' if RESAMPLE_FREQ=='W' else 'periodos')}) =====")
    print(forecast_df.to_string(index=False))
    print(f"\nDemanda total pronosticada en el horizonte: "
          f"{forecast_set.sum():,.0f} unidades")

    # ---- 8: grafica historico + pronostico ----------------------------------
    print("[6/6] Guardando grafica 'pronostico_demanda.png'...")
    plt.figure(figsize=(12, 6))
    plt.plot(serie.index, serie["demand"], label="Demanda historica")
    plt.plot(forecast_df["fecha"], forecast_df["demanda_pronosticada"],
             label="Pronostico", linestyle="--", marker="o")
    plt.title(f"Pronostico de demanda - {code}")
    plt.xlabel("Fecha")
    plt.ylabel("Unidades")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("pronostico_demanda.png", dpi=120)
    print("Listo. Revisa 'pronostico_demanda.png' y la tabla de arriba.")


if __name__ == "__main__":
    main()