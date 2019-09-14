## Raw data

|Variable                               |Description |Values |Notes |
|:--------------------------------------|:-----------|:------|:-----|
|CLAIM NO                               | A unique ID for each official wage-theft complaint issued to the VDOL           |       |      |
|COMPLAINT                              | Whether or not this row represents an official complaint           | X if yes      | All rows are complaints, so safe to ignore this variable     |
|ROUTINE                                |            |       | Missing everywhere, safe to ignore     |
|EMPLOYER NAME                          | The name of the employer against whom the wage-theft complaint is made           | Character      |      |
|EMPLOYER CITY                          | The employer's city           | Character       |      |
|ST                                     | The employer's state            | Character      |      |
|ZIP                                    | The employer's ZIP code            | Character      |      |
|gender                                 | The **predicted** gender of the person issuing the complaint           | Factor: (male, female)      | Gender is not included in the original data, but the complainants' names are. We used the `gender_df()` function in the `gender` package for R to predict gender from the complainants' first names. This variable is missing if the first name is unusual and `gender_df()` is unable to generate a prediction      |
|hispanic                               |            |       |      |
|asian                                  |            |       |      |
|CLAIM AMT                              |            |       |      |
|CASE OPEN/RE-OPEN                      |            |       |      |
|CLAIM RECEIVED                         |            |       |      |
|Valid                                  |            |       |      |
|Informal Resolution                    |            |       |      |
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
