## Virginia Department of Labor and Industry (DOLI) Wage Claim Data
The raw data is stored in `lajc-wage-claim.csv`. It contains 3,948 rows -- each row is one Payment of Wage Claim, an official complaint that a worker in Virginia can issue to the DOLI if they believe their employer has illegally withheld their wages. See (https://www.doli.virginia.gov/labor-law/payment-of-wage-english/) for more information about issuing a wage-claim. The data contains information regarding who each claim is made against, the amount of the claim, whether DOLI opened an investiagtion, and if so, whether they were able to return any wages to the complainant and how much.

Prior to posting the raw data on GitHub we edited it to 

* Remove the name, address, state, and ZIP code of the people who issued the complaints

* Add variables that use census data to predict the likely gender of each complainant, as well as whether or not each complainant is likely to be Hispanic or Asian

The following table describes each variable in the raw data:

|Variable                               |Description |Values |Notes |
|:--------------------------------------|:-----------|:------|:-----|
|CLAIM NO                               | A unique ID for each official wage-theft complaint issued to the VDOL           |       |      |
|COMPLAINT                              | Whether or not this row represents an official complaint           | X if yes      | All rows are complaints, so safe to ignore this variable     |
|ROUTINE                                |            |       | Missing everywhere, safe to ignore     |
|EMPLOYER NAME                          | The name of the employer against whom the wage-theft complaint is made           | Character      |      |
|EMPLOYER CITY                          | The employer's city           | Character       |      |
|ST                                     | The employer's state            | Character      |      |
|ZIP                                    | The employer's ZIP code            | Character      |      |
|gender                                 | The **predicted** gender of the person issuing the complaint based on first name          | Factor: (male, female)      | Gender is not included in the original data, but the complainants' names are. We used the `gender_df()` function in the `gender` package for R to predict gender from the complainants' first names. This variable is missing if the first name is unusual and `gender_df()` is unable to generate a prediction      |
|hispanic                               | Whether the complainant is **predicted** to be Hispanic based on the last name           | Logical: (TRUE, FALSE)      | Race/Ethnicity is not included in the original data. We predicted the race/ethnicity of each complainant from the person's last name using the `predict_race()` function in the `wru` package in R.     |
|asian                                  | Whether the complainant is **predicted** to be Asian based on the last name           | Logical: (TRUE, FALSE)       | See above     |
|CLAIM AMT                              | The amount of money claimed to have been illegally withheld           | Character (but easily converted to numeric)      |      |
|CASE OPEN/RE-OPEN                      | The date the case was opened           | Character      |      |
|CLAIM RECEIVED                         | The date the claim was received by DOLI           | Character      |      |
|Valid                                  | Whether the claim was deemed by DOLI to be valid           | Character: X if valid, missing if not      |      |
|Informal Resolution                    | Whether the claim was resulted in an informal resolution between the employer and complainant           | Character: X if valid, missing if not       |      |
|Bankrupt                               |            |       |      |
|Invalid                                |            |       |      |
|Fringe Benefits                        |            |       |      |
|Independent Agent                      |            |       |      |
|Subcontractor                          |            |       |      |
|False Claim                            |            |       |      |
|Other                                  |            |       |      |
|CLAIM INVAL OTHER DESCRIPTION          |            |       |      |
|Claim Validity                         |            |       |      |
|Employer left State                    |            |       |      |
|Employer Cannot be Located             |            |       |      |
|Complainant Cannot be Located          |            |       |      |
|Complainant Dropped Claim              |            |       |      |
|Paid Prior to Investigation            |            |       |      |
|Business is Closed                     |            |       |      |
|Other_1                                |            |       |      |
|CLAIM UNDETERMINED OTHER DESCRIPTION   |            |       |      |
|VERIFIED CLAIM AMT                     |            |       |      |
|CASE CLOSE/RECLOSE DATE                |            |       |      |
|Employer Contested Valid Determination |            |       |      |
|1st Response Investigation             |            |       |      |
|Formal Investigation                   |            |       |      |
|Request Settlement Conference          |            |       |      |
|Request Informal Fact Finding          |            |       |      |
|Request Formal Fact Finding            |            |       |      |
|Wage Order                             |            |       |      |
|Informal Conference                    |            |       |      |
|Civil Action for Wages/Penalties       |            |       |      |
|Other_2                                |            |       |      |
|OTHER DISPOSITION DESCRIPTION          |            |       |      |
|CASE CLOSED for the REPRESENTATIVE     |            |       |      |
|JUDGMENT                               |            |       |      |
|DISMISSED                              |            |       |      |
|NON-SUITED                             |            |       |      |
|JUDGMENT_1                             |            |       |      |
|DISMISSED_1                            |            |       |      |
|NON-SUITED_1                           |            |       |      |
|CIVCOURTDTE FOR WAGES/PENALTY          |            |       |      |
|TOT AMT                                |            |       |      |
|WAGE AMT                               |            |       |      |
|INTEREST AMT                           |            |       |      |
|ATTY FEES                              |            |       |      |
|DATE FOR WAGES                         |            |       |      |
|WAGES APPEALED                         |            |       |      |
|WAGES APPEAL CIRCUIT COURT DATE        |            |       |      |
|ASSESSED                               |            |       |      |
|AMT                                    |            |       |      |
|ATTY FEES_1                            |            |       |      |
|ASSESSED DATE                          |            |       |      |
|TOTAL CMP AMT                          |            |       |      |
|CMP APPEALED                           |            |       |      |
|CMP APPEAL CIRCUIT COURT DATE          |            |       |      |
|FINES & COURT COSTS                    |            |       |      |
|TOTAL WAGES                            |            |       |      |
|TOTAL INTEREST AMT                     |            |       |      |
|TOT WAGES & INTEREST                   |            |       |      |
|GARNISHED AMT                          |            |       |      |
|JUDGMENT WAGE AMT                      |            |       |      |
|JUDGEMENT PENALTY AMT                  |            |       |      |
|DOCKETED/SENT FOR COLLECTION DATE      |            |       |      |
|ACTION TAKEN                           |            |       |      |
|COURT DATE                             |            |       |      |
|CONVICTED - DISPOSITION                |            |       |      |
|DISMISSED - DISPOSITION                |            |       |      |
|NOL Prossed                            |            |       |      |
|CONFINEMENT                            |            |       |      |
|SUSPENSION                             |            |       |      |
|BOTH - C&F                             |            |       |      |
|JUDGMENT_2                             |            |       |      |
|DISMISSED_2                            |            |       |      |
|NON-SUITED_2                           |            |       |      |
|JUDGMENT_3                             |            |       |      |
|DISMISSED_3                            |            |       |      |
|NON-SUITED_3                           |            |       |      |
