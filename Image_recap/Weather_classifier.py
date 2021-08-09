

img_arr.shape
X = []
y = []

for cloud in cloudy:
    img = Image.open('dataset2'+'/'+cloud)
    img_arr_cloud = np.array(img, dtype = int)
    img_arr_cloud.flatten()
    X.append(img_arr_cloud)
    y.append(0)

for rain in rainy:
    img = Image.open('dataset2'+'/'+rain)
    img_arr_rain = np.array(img, dtype = int)
    img_arr_rain.flatten()
    X.append(img_arr_rain)
    y.append(1)
    
    
for shine in shiny:
    img = Image.open('dataset2'+'/'+shine)
    img_arr_shine = np.array(img, dtype = int)
    img_arr_shine.flatten()
    X.append(img_arr_shine)
    y.append(2)
    
for sun in sunrise:
    img = Image.open('dataset2'+'/'+sun)
    img_arr_sun = np.array(img, dtype = int)
    img_arr_sun.flatten()
    X.append(img_arr_sun)
    y.append(3)
    
