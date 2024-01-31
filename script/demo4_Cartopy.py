# Import the module / 引入套件
import beautifyplot as bp
from matplotlib import pyplot as plt
import numpy as np
import cartopy.crs as ccrs

# Set image path / 設定圖片路徑
img_path = __file__[:-len(__file__.split('\\')[-1])]+ "\\img\\"

# Set pymeili_resouces path / 設定pymeili_resouces路徑
res_path = __file__[:-len(__file__.split('\\')[-1])]+ "\\pymeili_resource\\"

# Set shapefile path / 設定shapefile路徑
CHN_shapefile1 = res_path + "CHN\\gadm36_CHN_1.shp"
SCS_shapefile = res_path + "NCS\\南中国海.shp"

# Set the default mode / 設定預設模式
bp.default()

# Initialize the figure / 初始化圖片
ax = bp.initplot(bp.subplot(111, projection=ccrs.PlateCarree()), figsize=(20, 12), theme='d')
#bp.add_fillcontinents(zorder=12, color='#DDDDDD')
bp.coastlines(zorder=12)
bp.gridlines(labelsize=10, zorder=12)

# Set the extent / 設定範圍
xmin, xmax, ymin, ymax = 70, 140, 0, 60
bp.set_extent([xmin, xmax, ymin, ymax], crs=ccrs.PlateCarree())
bp.add_mapboundary(linewidth=3, zorder=12)

# Add shapefile / 加入shapefile
bp.add_shapefile(CHN_shapefile1, edgecolor='fg', facecolor='bg', zorder=12, linewidth=1)
bp.add_shapefile(SCS_shapefile, edgecolor='fg', facecolor='bg', zorder=12, linewidth=1)

# Add text / 加入文字
bp.text(90, 53, '中國地圖\n(PlateCarree投影)', fontsize=20, ha='center', va='center', zorder=12, color='fg', fonttype='zh')

# Set the title / 設定標題
bp.lefttitle('DEMO 4')
bp.righttitle('Cartopy')

# Add inset map / 加入地圖
axin = bp.inset_axes([0.03, -0.04, 0.4, 0.4], projection=ccrs.PlateCarree(), zorder=13)
bp.initplot(axin, theme='d')

# set global extent / 設定全球範圍
bp.set_global()
bp.add_mapboundary(linewidth=2, zorder=13)

# Add extent box / 框出範圍線
bp.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], color='fg3', linewidth=2, zorder=14)

# fill the extent box / 填滿範圍
bp.fill_between([xmin, xmax], [ymin, ymin], [ymax, ymax], color='fg3', alpha=0.3, zorder=13)

# Save / 儲存圖片
bp.savefig(img_path + 'demo4_Cartopy.png')

# Close the figure / 關閉圖片
bp.close()