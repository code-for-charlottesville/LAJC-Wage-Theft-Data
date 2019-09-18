# Import data
import pandas as pd
df = pd.read_csv("\\Raw data\\lajc_wage_claim.csv")
dfhead = df.head(1000)

# Select columns to encode, and then one-hot encode them
to_encode = df[["gender", "Valid", "Informal Resolution", "Bankrupt", "Invalid", "Fringe Benefits", "Independent Agent", "Subcontractor", "False Claim", "Other", "Claim Validity", "Employer Cannot be Located", "Complainant Cannot be Located", "Complainant Dropped Claim", "Paid Prior to Investigation", "Business is Closed", "Other_1", "1st Response Investigation", "Formal Investigation", "Wage Order", "Other_2", "ASSESSED"]]
vars_encoded = pd.get_dummies(to_encode)

# Replace "X" fields with cleaned, encoded fields
df_cleaned = df.copy()
df_cleaned["gender"] = vars_encoded["gender_male"].astype(int) # 1 = male, 0 = female
df_cleaned["Valid"] = vars_encoded["Valid_X"].astype(int)
df_cleaned["Informal Resolution"] = vars_encoded["Informal Resolution_X"].astype(int)
df_cleaned["Bankrupt"] = vars_encoded["Bankrupt_X"].astype(int)
df_cleaned["Invalid"] = vars_encoded["Invalid_X"].astype(int)
df_cleaned["Fringe Benefits"] = vars_encoded["Fringe Benefits_X"].astype(int)
df_cleaned["Independent Agent"] = vars_encoded["Independent Agent_X"].astype(int)
df_cleaned["Subcontractor"] = vars_encoded["Subcontractor_X"].astype(int)
df_cleaned["False Claim"] = vars_encoded["False Claim_X"].astype(int)
df_cleaned["Other"] = vars_encoded["Other_X"].astype(int)
df_cleaned["Claim Validity"] = vars_encoded["Claim Validity_X"].astype(int)
df_cleaned["Employer Cannot be Located"] = vars_encoded["Employer Cannot be Located_X"].astype(int)
df_cleaned["Complainant Cannot be Located"] = vars_encoded["Complainant Cannot be Located_X"].astype(int)
df_cleaned["Complainant Dropped Claim"] = vars_encoded["Complainant Dropped Claim_X"].astype(int)
df_cleaned["Paid Prior to Investigation"] = vars_encoded["Paid Prior to Investigation_X"].astype(int)
df_cleaned["Business is Closed"] = vars_encoded["Business is Closed_X"].astype(int)
df_cleaned["Other_1"] = vars_encoded["Other_1_X"].astype(int)
df_cleaned["1st Response Investigation"] = vars_encoded["1st Response Investigation_X"].astype(int)
df_cleaned["Formal Investigation"] = vars_encoded["Formal Investigation_X"].astype(int)
df_cleaned["Wage Order"] = vars_encoded["Wage Order_X"].astype(int)
#df_cleaned["Other_2"] = vars_encoded["Other_2_X"].astype(int)
df_cleaned["Assessed"] = vars_encoded["ASSESSED_X"].astype(int)

# Convert True/False values to 1/0
df_cleaned["hispanic"] = df_cleaned["hispanic"].astype(int)
df_cleaned["asian"] = df_cleaned["asian"].astype(int)

# Convert currency amounts to type float
def currency_to_float(field):
    data = []
    for i in range(len(df_cleaned)):
        newstr = str.replace(df_cleaned.loc[i, field], "$", "") # remove dollar sign
        newstr = str.replace(newstr, ",", "") # remove comma
        data.append(newstr) 
    
    df_cleaned[field] = pd.DataFrame(data).astype(float)

currency_to_float("CLAIM AMT")
currency_to_float("VERIFIED CLAIM AMT")
currency_to_float("TOT AMT")
currency_to_float("WAGE AMT")
currency_to_float("INTEREST AMT")
currency_to_float("ATTY FEES")











