import geopandas as gpd
from plotter_geoweb import wms
import matplotlib.pyplot as plt

df=gpd.GeoDataFrame.from_file("test_files/mun_15054.shp")

fig,ax=plt.subplots(figsize=(10,10),dpi=120)
ax.set_aspect('equal',anchor="N")
df.plot(column="pob_2010",ax=ax)

#preparar los parametros de consulta del mapa base
params_wms={"url":"http://localhost:8080/geoserver/base/wms","layers":["etiquetas_base"],"srs":"EPSG:4326"}
wms.add_to_axes(ax,fig,str(df.crs),params_wms)


plt.show()