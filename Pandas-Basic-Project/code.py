# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print (categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print (numerical_var)
# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'],axis=1)
print (banks.isnull().sum())
bank_mode = banks.mode()
banks = banks.fillna('bank_mode')
#code ends here


# --------------
# Code starts here





#pd.to_numeric(banks["LoanAmount"])
avg_loan_amount = pd.pivot_table(banks,index=["Gender","Married","Self_Employed"],values=["LoanAmount"])
#banks.head()


# code ends here



# --------------
# code starts here

#banks.head()
loan_approved_se_temp = banks[banks['Self_Employed'] =='Yes']
loan_approved_se = loan_approved_se_temp[loan_approved_se_temp['Loan_Status']=='Y']

loan_approved_nse_temp = banks[banks['Self_Employed'] =='No']
loan_approved_nse = loan_approved_nse_temp[loan_approved_nse_temp['Loan_Status']=='Y']

percentage_se = (len(loan_approved_se)/614)*100
percentage_nse = (len(loan_approved_nse)/614)*100
# code ends here


# --------------
# code starts here

#def loan_amt_term(i):
#    int(i)
#   i = (i/12)
#  return str(i)


loan_term = banks['Loan_Amount_Term'].apply(lambda x : x/12)
#banks.head()
lst = ((loan_term>=25).tolist())
def count(lst):       
    return lst.count(True) 
big_loan_term = count(lst)
#big_loan_term = len(loan_term>=25)
# code ends here


# --------------
# code starts here
loan_groupby=banks.groupby('Loan_Status')
loan_groupby = loan_groupby[('ApplicantIncome','Credit_History')]
mean_values = loan_groupby.mean()


# code ends here


