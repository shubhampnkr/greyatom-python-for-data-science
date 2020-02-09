# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path,delimiter=",", skip_header=1)
#print("\nData: \n\n", data)
census = np.concatenate([data,new_record])


# --------------
#Code starts here
age = census[:,0]
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)


# --------------
race = census[:,2]

race_0 = census[census[:,2]==0]
#print(race_0)
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

len_0 = race_0[:,2].size
len_1 = race_1[:,2].size
len_2 = race_2[:,2].size
len_3 = race_3[:,2].size
len_4 = race_4[:,2].size

length = np.array([len_0,len_1,len_2,len_3,len_4])
min_length = np.min(length)
index = list(length).index(min_length)

min_race = length[index]
if min_race==len_0:
    minority_race=0
if min_race==len_1:
    minority_race=1
elif min_race==len_2:
    minority_race=2
elif min_race==len_3:
    minority_race=3
elif min_race==len_4:
    minority_race=4


# --------------
#Code starts here
senior_citizens = census[census[:,0] > 60]

working_hours = census[:,6][census[:,0] > 60]
working_hours_sum = sum(working_hours)
senior_citizens_len = len(working_hours)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)
#print(census[senior_citizens])
#working_hours_sum = sum[senior_citizens[:,0]]


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
x = census[:,7][census[:,1]>10]
avg_pay_high = x.mean()
y = census[:,7][census[:,1]<=10]
avg_pay_low = y.mean()
print(avg_pay_low)
np.array_equal(avg_pay_high,avg_pay_low)


