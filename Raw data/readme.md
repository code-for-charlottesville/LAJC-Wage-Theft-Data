## Virginia Department of Labor and Industry (DOLI) Wage Claim Data
The raw data is stored in `[lajc_wage_claim.csv](lajc_wage_claim.csv)`. It contains 3,948 rows -- each row is one Payment of Wage Claim, an official complaint that a worker in Virginia can issue to the DOLI if they believe their employer has illegally withheld their wages. See (https://www.doli.virginia.gov/labor-law/payment-of-wage-english/) for more information about issuing a wage-claim. The data contains information regarding who each claim is made against, the amount of the claim, whether DOLI opened an investiagtion, and if so, whether they were able to return any wages to the complainant and how much.

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
|Claim Validity                         | Whether an undetermined claim is valid           | Character: X if true, missing if false      | A claim is "undetermined" if DOLI finds that it cannot enforce a descision even if a claim is valid.       |
|Employer left State                    | Whether a claim is undetermined because the employer left the state           | Character: X if true, missing if false      | See above     |
|Employer Cannot be Located             | Whether a claim is undetermined because the employer cannot be located           | Character: X if true, missing if false      | See above     |
|Complainant Cannot be Located          | Whether a claim is undetermined because the complainant cannot be located           | Character: X if true, missing if false      | See above     |
|Complainant Dropped Claim              | Whether a claim is undetermined because the complainant dropped the claim           | Character: X if true, missing if false      | See above     |
|Paid Prior to Investigation            | Whether a claim is undetermined because the employer paid the lost wages prior to the DOLI investigation           | Character: X if true, missing if false      | See above     |
|Business is Closed                     | Whether a claim is undetermined because the employer's business has closed          | Character: X if true, missing if false     | See above     |
|Other_1                                | Whether a claim is undetermined for another reason           | Character: X if true, missing if false      | See above     |
|CLAIM UNDETERMINED OTHER DESCRIPTION   | The stated reason for being undetermined if "other"           | Character      |      |
|VERIFIED CLAIM AMT                     | The total amount claimed after verification by DOLI           | Character (but easily converted to numeric)      |      |
|CASE CLOSE/RECLOSE DATE                | Date case was officially closed           | Character     |      |
|Employer Contested Valid Determination | Whether the employer contested a claim that was found to be valid           | Character: X if true, missing if false      |      |
|1st Response Investigation             | Whether only a 1st response was conducted           | Character: X if true, missing if false      | DOLI conducts a quick "1st response" investiagtion first to determine if a formal investigation is warranted     |
|Formal Investigation                   | Whether a formal investigation was conducted           | Character: X if true, missing if false      |      |
|Request Settlement Conference          |            | All missing     | No such requests in the data      |
|Request Informal Fact Finding          |            | All missing      | No such requests in the data      |
|Request Formal Fact Finding            |            | All missing      | No such requests in the data     |
|Wage Order                             | Whether a legal order is given for the employer to pay lost wages           | Character: X if true, missing if false      | See page 10, G(1): (http://townhall.virginia.gov/L/GetFile.cfm?File=C:%5CTownHall%5Cdocroot%5CGuidanceDocs%5C181%5CGDoc_DOLI_1780_v5.pdf)     |
|Informal Conference                    |            | All missing     | No such actions in the data     |
|Civil Action for Wages/Penalties       |            | All missing      | No such actions in the data      |
|Other_2                                |            | All missing      | No such actions in the data       |
|OTHER DISPOSITION DESCRIPTION          |            | All missing      |      |
|CASE CLOSED for the REPRESENTATIVE     | Date the DOLI labor law representative ended the investigation          | Character     |      |
|JUDGMENT                               |            | All missing       |      |
|DISMISSED                              |            | All missing       |      |
|NON-SUITED                             |            | All missing       |      |
|JUDGMENT_1                             |            | All missing      |      |
|DISMISSED_1                            |            | All missing       |      |
|NON-SUITED_1                           |            | All missing       |      |
|CIVCOURTDTE FOR WAGES/PENALTY          |            | All missing       |      |
|TOT AMT                                | Total amount recovered for the complainant           | Character (but easily converted to numeric)      |      |
|WAGE AMT                               | Amount recovered in lost wages for the complainant           | Character (but easily converted to numeric)      |      |
|INTEREST AMT                           | Amount recovered in interest on lost wages for the complainant           | Character (but easily converted to numeric)      |      |
|ATTY FEES                              | Amount recovered in reimbursed attorney fees for the complainant           | Character (but easily converted to numeric)      |      |
|DATE FOR WAGES                         | Date wages were returned to the complainant           | Character      |      |
|WAGES APPEALED                         |            | All missing      |      |
|WAGES APPEAL CIRCUIT COURT DATE        |            | All missing      |      |
|ASSESSED                               | Whether the DOLI investigation concludes the employer owes a civil monetary penalty            | Character: X if true, missing if false      | A civil monentary penalty (CMP) is a fine an employer must pay as punishment for wage-theft, in addition to paying back wages and fees     |
|AMT                                    | Amount of the CMP owed by the employer           | Character (but easily converted to numeric)      | See above     |
|ATTY FEES_1                            | Attorney fees owed by the employer as part of the CMP           | Character (but easily converted to numeric)      | See above     |
|ASSESSED DATE                          | Date CMP totals were assessed           | Character      | See above     |
|TOTAL CMP AMT                          | CMP + attorney fees           | Character (but easily converted to numeric)      | See above     |
|CMP APPEALED                           |            | All missing    | See above     |
|CMP APPEAL CIRCUIT COURT DATE          |            | All missing      | See above     |
|FINES & COURT COSTS                    | Other fines and court costs associated with the CMP           | Character (but easily converted to numeric)      | See above     |
|TOTAL WAGES                            | Total wages that the DOLI says have been actually collected           | Character (but easily converted to numeric)      | *We're not sure what to make of these "collection" variables at this point.* After a legal order for an employer to repay wages, the case is referred to a collection agency or to an attorney in charge of collection. These values indicate the amount that has been collected. It includes amounts that have been legally ordered, and amounts that were settled upon in civil court or outside DOLI jurisdiction.     |
|TOTAL INTEREST AMT                     | Total interest collected           | Character (but easily converted to numeric)      | See above     |
|TOT WAGES & INTEREST                   | Wages + interest collected           | Character (but easily converted to numeric)      | See above     |
|GARNISHED AMT                          |            | All $0      |      |
|JUDGMENT WAGE AMT                      | We think these are additional fees for repeat offenders           | Character (but easily converted to numeric)      |      |
|JUDGEMENT PENALTY AMT                  | We think these are additional fees for repeat offenders            | Character (but easily converted to numeric)      |      |
|DOCKETED/SENT FOR COLLECTION DATE      |            | All missing      |      |
|ACTION TAKEN                           |            | All missing      |      |
|COURT DATE                             |            | All missing     |      |
|CONVICTED - DISPOSITION                |            | All missing     |      |
|DISMISSED - DISPOSITION                |            | All missing      |      |
|NOL Prossed                            |            | All missing      |      |
|CONFINEMENT                            |            | All missing      |      |
|SUSPENSION                             |            | All missing      |      |
|BOTH - C&F                             |            | All missing     |      |
|JUDGMENT_2                             |            | All missing      |      |
|DISMISSED_2                            |            | All missing      |      |
|NON-SUITED_2                           |            | All missing      |      |
|JUDGMENT_3                             |            | All missing      |      |
|DISMISSED_3                            |            | All missing      |      |
|NON-SUITED_3                           |            | All missing      |      |
