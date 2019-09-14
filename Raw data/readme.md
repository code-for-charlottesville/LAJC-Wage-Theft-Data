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
|Informal Resolution                    | Whether the claim was resulted in an informal resolution between the employer and complainant           | Character: X if true, missing if false       |      |
|Bankrupt                               | Whether the claim is being made against a bankrupt employer           | Character: X if true, missing if false       | This is one of the reasons DOLI as outside their jurisdiction (https://www.doli.virginia.gov/labor-law/payment-of-wage-english/)      |
|Invalid                                | Whether DOLI disqualified the claim for one of the following reasons:            | Character: X if true, missing if false      |      |
|Fringe Benefits                        | Whether DOLI disqualified the claim because it deals with contractual payments beyond a base salary           | Character: X if true, missing if false      | This is one of the reasons DOLI as outside their jurisdiction (https://www.doli.virginia.gov/labor-law/payment-of-wage-english/)       |
|Independent Agent                      | Whether DOLI disqualified the claim because it involves a contract worker instead of a direct employee           | Character: X if true, missing if false      | This is one of the reasons DOLI as outside their jurisdiction (https://www.doli.virginia.gov/labor-law/payment-of-wage-english/)       |
|Subcontractor                          | Whether DOLI disqualified the claim because it involves a subcontract worker instead of a direct employee           | Character: X if true, missing if false      | This is one of the reasons DOLI as outside their jurisdiction (https://www.doli.virginia.gov/labor-law/payment-of-wage-english/)       |
|False Claim                            | Whether DOLI determined that the claim is false           | Character: X if true, missing if false      |      |
|Other                                  | Whether DOLI determined that the claim is invalid for another reason           | Character: X if true, missing if false      | This is one of the reasons DOLI as outside their jurisdiction (https://www.doli.virginia.gov/labor-law/payment-of-wage-english/)      |
|CLAIM INVAL OTHER DESCRIPTION          | The stated reason DOLI found a claim invalid if "other"           | Character      |      |
|Claim Validity                         |            | Character: X if true, missing if false      |      |
|Employer left State                    |            | Character: X if true, missing if false      |      |
|Employer Cannot be Located             |            | Character: X if true, missing if false      |      |
|Complainant Cannot be Located          |            | Character: X if true, missing if false      |      |
|Complainant Dropped Claim              |            | Character: X if true, missing if false      |      |
|Paid Prior to Investigation            |            | Character: X if true, missing if false      |      |
|Business is Closed                     |            | Character: X if true, missing if false     |      |
|Other_1                                |            | Character: X if true, missing if false      |      |
|CLAIM UNDETERMINED OTHER DESCRIPTION   |            | Character      |      |
|VERIFIED CLAIM AMT                     |            | Character (but easily converted to numeric)      |      |
|CASE CLOSE/RECLOSE DATE                |            | Character     |      |
|Employer Contested Valid Determination |            | Character: X if true, missing if false      |      |
|1st Response Investigation             |            | Character: X if true, missing if false      |      |
|Formal Investigation                   |            | Character: X if true, missing if false      |      |
|Request Settlement Conference          |            | Character: X if true, missing if false      |      |
|Request Informal Fact Finding          |            | Character: X if true, missing if false      |      |
|Request Formal Fact Finding            |            | Character: X if true, missing if false      |      |
|Wage Order                             |            | Character: X if true, missing if false      |      |
|Informal Conference                    |            | Character: X if true, missing if false     |      |
|Civil Action for Wages/Penalties       |            | Character: X if true, missing if false      |      |
|Other_2                                |            | Character: X if true, missing if false      |      |
|OTHER DISPOSITION DESCRIPTION          |            | Character: X if true, missing if false      |      |
|CASE CLOSED for the REPRESENTATIVE     |            | Character: X if true, missing if false      |      |
|JUDGMENT                               |            | Character: X if true, missing if false      |      |
|DISMISSED                              |            | Character: X if true, missing if false      |      |
|NON-SUITED                             |            | Character: X if true, missing if false      |      |
|JUDGMENT_1                             |            | Character: X if true, missing if false     |      |
|DISMISSED_1                            |            | Character: X if true, missing if false      |      |
|NON-SUITED_1                           |            | Character: X if true, missing if false      |      |
|CIVCOURTDTE FOR WAGES/PENALTY          |            | Character      |      |
|TOT AMT                                |            | Character (but easily converted to numeric)      |      |
|WAGE AMT                               |            | Character (but easily converted to numeric)      |      |
|INTEREST AMT                           |            | Character (but easily converted to numeric)      |      |
|ATTY FEES                              |            | Character (but easily converted to numeric)      |      |
|DATE FOR WAGES                         |            | Character      |      |
|WAGES APPEALED                         |            | Character: X if true, missing if false      |      |
|WAGES APPEAL CIRCUIT COURT DATE        |            | Character: X if true, missing if false      |      |
|ASSESSED                               |            | Character: X if true, missing if false      |      |
|AMT                                    |            | Character (but easily converted to numeric)      |      |
|ATTY FEES_1                            |            | Character (but easily converted to numeric)      |      |
|ASSESSED DATE                          |            | Character      |      |
|TOTAL CMP AMT                          |            | Character (but easily converted to numeric)      |      |
|CMP APPEALED                           |            | Character: X if true, missing if false      |      |
|CMP APPEAL CIRCUIT COURT DATE          |            | Character      |      |
|FINES & COURT COSTS                    |            | Character (but easily converted to numeric)      |      |
|TOTAL WAGES                            |            | Character (but easily converted to numeric)      |      |
|TOTAL INTEREST AMT                     |            | Character (but easily converted to numeric)      |      |
|TOT WAGES & INTEREST                   |            | Character (but easily converted to numeric)      |      |
|GARNISHED AMT                          |            | Character (but easily converted to numeric)      |      |
|JUDGMENT WAGE AMT                      |            | Character (but easily converted to numeric)      |      |
|JUDGEMENT PENALTY AMT                  |            | Character (but easily converted to numeric)      |      |
|DOCKETED/SENT FOR COLLECTION DATE      |            | Character      |      |
|ACTION TAKEN                           |            | Character: X if true, missing if false      |      |
|COURT DATE                             |            | Character     |      |
|CONVICTED - DISPOSITION                |            | Character: X if true, missing if false      |      |
|DISMISSED - DISPOSITION                |            | Character: X if true, missing if false      |      |
|NOL Prossed                            |            | Character: X if true, missing if false      |      |
|CONFINEMENT                            |            | Character: X if true, missing if false      |      |
|SUSPENSION                             |            | Character: X if true, missing if false      |      |
|BOTH - C&F                             |            | Character: X if true, missing if false      |      |
|JUDGMENT_2                             |            | Character: X if true, missing if false      |      |
|DISMISSED_2                            |            | Character: X if true, missing if false      |      |
|NON-SUITED_2                           |            | Character: X if true, missing if false      |      |
|JUDGMENT_3                             |            | Character: X if true, missing if false      |      |
|DISMISSED_3                            |            | Character: X if true, missing if false      |      |
|NON-SUITED_3                           |            | Character: X if true, missing if false      |      |
