import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as st
#%matplotlib inline

# Load the data from the XY plot into lists for the X and Y values
# time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# rmsd = [0.2, 0.7, 0.9, 1.1, 1.3, 1.1, 1.7, 1.9, 2.1, 1.3, 2.5]

# df = pd.read_csv("RMSData.csv")

# rmsd = df.DataFrame()

order_p1 = []
order_p2 = []
with open("SASA_Data.dat") as alldata:
# with open("RMSData.dat") as alldata:
    alldata_lines = alldata.readlines()
    for line in alldata_lines:
        data_point = str(line).split("\n")
#         print(float(data_point[0]))
        order_p1.append(float(data_point[0]))
#         order_p1.append(float("{:.4f}".format(line[0])))

with open("Hbond_protein-protein_Data.dat") as alldata:
    alldata_lines = alldata.readlines()
    for line in alldata_lines:
        data_point = str(line).split("\n")
#         print(float(data_point[0]))
        order_p2.append(float(data_point[0]))
#         order_p2.append(float("{:.4f}".format(line[0])))

# graphed = ['order_p1', 'order_p2']
plt.figure(figsize=(20, 9))

a = plt.hist(order_p1, density=True, bins=72, label="RMSD", alpha=0.3)

# # Plot the pdf
# mu, std = np.mean(order_p1), np.std(order_p1)
# x = np.linspace(-5, 5, 100)
# plt.plot(x, 1/(std * np.sqrt(2 * np.pi)) * np)

# plt.style.use('ggplot')
# Show the plot
# plt.show()
# mn, mx = plt.xlim()
# plt.xlim(mn, mx)
# kde_xs = np.linspace(min(order_p1), max(order_p1), 300)

kde_xs = np.linspace(min(order_p1), max(order_p1), 300)
kde = st.gaussian_kde(order_p1)
plt.plot(kde_xs, kde.pdf(kde_xs), label="RMSD.PDF")
plt.legend()

b = plt.hist(order_p2, density=True, bins=40, label="Rg", alpha=0.3)

# order_p1
# plt.hist(order_p1, bins=73)

# Add labels to the X and Y axes
plt.xlabel('RMSD (Å)')
plt.ylabel('Count')


kde_xs = np.linspace(min(order_p2), max(order_p2), 300)
kde = st.gaussian_kde(order_p2)
plt.plot(kde_xs, kde.pdf(kde_xs), label="Rg.PDF")
plt.legend()
plt.ylabel("Probability Density")
plt.xlabel("Data")
plt.title("Histogram")
plt.savefig('testy.png', dpi=300);
