from waggle import plugin

import pandas as pd
import numpy as np

plugin.init()

#Read in thermal camera CSV data
file = pd.read_csv("/lcrc/project/waggle/public_html/private/training_data/waggle_area510/mobotix/"
                "thermal/1618776148_000001_right_336x252_14bit.thermal.celsius.csv")

#Unpack image CSV, remove delimters, and sort into lists
image_array = []

for i in range(file.size):
    if i >= 6:
        data = file.values[i][0]
        data = data.split(';')
        array = np.array(data)
        array = array.astype(np.float)
        image_array.append(array)

#Calculate mean, median, maximum, minimum, and standard deviation of the image. 
temp_avg = np.mean(image_array)
temp_med = np.median(image_array)
temp_max = np.max(image_array)
temp_min = np.min(image_array)
temp_std = np.std(image_array)

#Publish statment
plugin.publish("thermal.mean", temp_avg)
plugin.publish("thermal.median", temp_med)
plugin.publish("thermal.max", temp_max)
plugin.publish("thermal.min", temp_min)
plugin.publish("thermal.std", temp_std)