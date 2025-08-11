import pandas as pd
import numpy as np

# Generar rango de fechas
dates = pd.date_range(start="2016-05-09", end="2019-12-03", freq="D")
np.random.seed(0)
page_views = np.random.randint(1000, 30000, size=len(dates))

# Crear DataFrame
df = pd.DataFrame({
    "date": dates,
    "value": page_views
})

# Guardar como CSV
df.to_csv("fcc-forum-pageviews.csv", index=False)