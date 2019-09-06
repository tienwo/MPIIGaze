#ploting mean,std errors
import matplotlib.pyplot as plt
import pandas as pd

skips=[]
for i in range(60):
    if i%10 != 0:
        skips.append(i)
mean_errors = pd.read_csv('test_mean.txt',skiprows=skips).values
std_errors=pd.read_csv('test_stdev.txt',skiprows=skips).values
#print(mean_errors[:,1:])

#data = dataset_train.iloc[:, 1:2].values

# Visualising the results
#plt.plot(real_stock_price, color = 'red', label = 'Real Google Stock Price')
#plt.plot(predicted_stock_price, color = 'blue', label = 'Test mean error during epochs')
plt.title('Angle error(mean) Stock Price Prediction')
plt.xlabel('epochs')
plt.ylabel('mean error')
plt.legend()
plt.grid(alpha=0.5, linestyle=':')
#plt.errorbar(mean_errors[:,1], mean_errors[:,2], std_errors[:,2], linestyle='None', marker='^')
plt.plot(mean_errors[:,1], mean_errors[:,2],color='blue')
plt.plot(mean_errors[:,1], std_errors[:,2],color='red')
plt.show()
