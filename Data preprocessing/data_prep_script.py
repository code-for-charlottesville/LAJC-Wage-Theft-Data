import pandas as pd
import os

df = pd.read_csv(r'C:\Users\cmp2c\Desktop\gitrepos\LAJC-Wage-Theft-Data\Raw data\lajc_wage_claim.csv')

#Filter out non-Virginia claims
df = df[df['ST']=='VA']

#Convert Booleans to 1s and 0s    
boolean_cols = ['COMPLAINT','Valid','Informal Resolution','Bankrupt','Invalid','Fringe Benefits','Independent Agent','Subcontractor','False Claim','Other','Claim Validity','Employer left State','Employer Cannot be Located','Complainant Cannot be Located','Complainant Dropped Claim','Paid Prior to Investigation','Business is Closed','Other_1','Employer Contested Valid Determination','1st Response Investigation','Formal Investigation','Wage Order','ASSESSED']

def convert_to_boolean(val):
    if val == 'X':
        return 1
    else:
        return 0
    
for col in boolean_cols:
    df[col] = df[col].apply(convert_to_boolean)

    
#Get rid of dollar signs and commas to convert values to floats
currency_cols = ['CLAIM AMT','VERIFIED CLAIM AMT','TOT AMT','WAGE AMT','INTEREST AMT','AMT','TOTAL CMP AMT','TOTAL INTEREST AMT','GARNISHED AMT','JUDGMENT WAGE AMT','JUDGEMENT PENALTY AMT','ATTY FEES','FINES & COURT COSTS','TOTAL WAGES','TOT WAGES & INTEREST','ATTY FEES_1']

for col in currency_cols:
    df[col] = df[col].apply(lambda x: x.replace('$','').replace(',','')).astype(float)
    
#Filter out claims < $20
df = df[df['CLAIM AMT']>=20]

#Drop unused columns for now. May remove this later if we need this in the future
df = df.drop(columns = ['ROUTINE','Request Settlement Conference','Request Informal Fact Finding','Request Formal Fact Finding','Informal Conference','Civil Action for Wages/Penalties','Other_2','OTHER DISPOSITION DESCRIPTION','JUDGMENT','DISMISSED','NON-SUITED','JUDGMENT_1','DISMISSED_1','NON-SUITED_1','CIVCOURTDTE FOR WAGES/PENALTY','WAGES APPEALED','WAGES APPEAL CIRCUIT COURT DATE','CMP APPEALED','CMP APPEAL CIRCUIT COURT DATE','GARNISHED AMT','DOCKETED/SENT FOR COLLECTION DATE','ACTION TAKEN','COURT DATE','CONVICTED - DISPOSITION','DISMISSED - DISPOSITION','NOL Prossed','CONFINEMENT','SUSPENSION','BOTH - C&F','JUDGMENT_2','DISMISSED_2','NON-SUITED_2','JUDGMENT_3','DISMISSED_3','NON-SUITED_3'])

