## Virginia Department of Labor and Industry (DOLI) Wage Claim Data
The raw data is stored in [lajc_wage_claim.csv](lajc_wage_claim.csv). It contains 3,948 rows -- each row is one Payment of Wage Claim, an official complaint that a worker in Virginia can issue to the DOLI if they believe their employer has illegally withheld their wages. See (https://www.doli.virginia.gov/labor-law/payment-of-wage-english/) for more information about issuing a wage-claim. The data contains information regarding who each claim is made against, the amount of the claim, whether DOLI opened an investiagtion, and if so, whether they were able to return any wages to the complainant and how much.

Key variables are **bolded** in the following table.

Prior to posting the raw data on GitHub we edited it to 

* Remove the name, address, state, and ZIP code of the people who issued the complaints

* Add variables that make informed guesses about the gender of each complainant, as well as whether or not each complainant is likely to be Hispanic or Asian

The following table describes each variable in the raw data:

|Variable                               |Description |Values |Notes |
|:--------------------------------------|:-----------|:------|:-----|
|0 ****CLAIM NO**** | A unique ID for each official wage-theft complaint issued to the DOLI | |  |
|1 COMPLAINT  | Whether or not this row represents an official complaint | X if yes  | All rows are complaints, so safe to ignore this variable |
|2 ROUTINE  |  | | Missing everywhere, safe to ignore |
|3 EMPLOYER NAME  | The name of the employer against whom the wage-theft complaint is made | Character  |  |
|4 EMPLOYER CITY  | The employer's city | Character |  |
|5 ST | The employer's state  | Character  |  |
|6 ZIP  | The employer's ZIP code  | Character  |  |
|7 ****gender**** | The ****predicted**** gender of the person issuing the complaint based on first name  | Factor: (male, female)  | Gender is not included in the original data, but the complainants' names are. We used the `gender_df()` function in the `gender` package for R to predict gender from the complainants' first names. This variable is missing if the first name is unusual and `gender_df()` is unable to generate a prediction  |
|8 ****hispanic**** | Whether the complainant is ****predicted**** to be Hispanic based on the last name | Logical: (TRUE, FALSE)  | Race/Ethnicity is not included in the original data. We predicted the race/ethnicity of each complainant from the person's last name using the `predict_race()` function in the `wru` package in R. |
|9 ****asian****  | Whether the complainant is ****predicted**** to be Asian based on the last name | Logical: (TRUE, FALSE) | See above |
|10 ****COMPLAINANT CITY****  | The city of the person issuing the complaint of wage theft | Character |  |
|11 ****ST_1****  | The state in which the person issuing the complaint of wage theft resides| Character | |
|12 ****ZIP_1****  | The zipcode of the person issuing the complaint of wage theft | Character | |
|13 ****CLAIM AMT****  | The amount of money claimed to have been illegally withheld | Character (but easily converted to numeric)  |  |
|14 ****CASE OPEN/RE-OPEN****  | The date the case was opened | Character  |  |
|15 CLAIM RECEIVED | The date the claim was received by DOLI | Character  |  |
|16 ****Valid****  | Whether the claim was deemed by DOLI to be valid | Character: X if valid, missing if not  |  |
|17 Informal Resolution  | Whether an informal resolution between the employer and complainantthe claim was attempted | Character: X if true, missing if false |  |
|18 Bankrupt | Whether the claim is being made against a bankrupt employer | Character: X if true, missing if false | This is one of the reasons DOLI as outside their jurisdiction (https://www.doli.virginia.gov/labor-law/payment-of-wage-english/)  |
|19 Invalid  | Whether DOLI disqualified the claim for one of the following reasons:  | Character: X if true, missing if false  |  |
|20 Fringe Benefits  | Whether DOLI disqualified the claim because it deals with contractual payments beyond a base salary | Character: X if true, missing if false  | This is one of the reasons DOLI as outside their jurisdiction (https://www.doli.virginia.gov/labor-law/payment-of-wage-english/) |
|21 Independent Agent  | Whether DOLI disqualified the claim because it involves a contract worker instead of a direct employee | Character: X if true, missing if false  | This is one of the reasons DOLI as outside their jurisdiction (https://www.doli.virginia.gov/labor-law/payment-of-wage-english/) |
|22 Subcontractor  | Whether DOLI disqualified the claim because it involves a subcontract worker instead of a direct employee | Character: X if true, missing if false  | This is one of the reasons DOLI as outside their jurisdiction (https://www.doli.virginia.gov/labor-law/payment-of-wage-english/) |
|23 False Claim  | Whether DOLI determined that the claim is false | Character: X if true, missing if false  |  |
|24 Other  | Whether DOLI determined that the claim is invalid for another reason | Character: X if true, missing if false  | This is one of the reasons DOLI as outside their jurisdiction (https://www.doli.virginia.gov/labor-law/payment-of-wage-english/)  |
|25 CLAIM INVAL OTHER DESCRIPTION  | The stated reason DOLI found a claim invalid if "other" | Character  |  |
|26 Claim Validity | Whether an undetermined claim is valid | Character: X if true, missing if false  |   An “invalid” claim is one where the investigator can dismiss it by just looking at the claim form. (E.g., the worker said “I am an independent contractor” or left some critical part of the form blank).  A claim whose validity is “undetermined” means this: if everything the worker says on the claim form turned out to be true, the claim would be valid. But after investigating, DOLI believes that there is not enough evidence to determine whether everything the worker says on the claim form is in fact true (i.e., DOLI believes that the worker hasn’t met their burden of proof on some critical part of the claim). |
|27 Employer left State  | Whether a claim is undetermined because the employer left the state | Character: X if true, missing if false  | See above |
|28 Employer Cannot be Located | Whether a claim is undetermined because the employer cannot be located | Character: X if true, missing if false  | See above |
|29 Complainant Cannot be Located  | Whether a claim is undetermined because the complainant cannot be located | Character: X if true, missing if false  | See above |
|30 Complainant Dropped Claim  | Whether a claim is undetermined because the complainant dropped the claim | Character: X if true, missing if false  | See above |
|31 Paid Prior to Investigation  | Whether a claim is undetermined because the employer paid the lost wages prior to the DOLI investigation | Character: X if true, missing if false  | See above |
|32 Business is Closed | Whether a claim is undetermined because the employer's business has closed  | Character: X if true, missing if false | See above |
|33 Other_1  | Whether a claim is undetermined for another reason | Character: X if true, missing if false  | See above |
|34 CLAIM UNDETERMINED OTHER DESCRIPTION | The stated reason for being undetermined if "other" | Character  |  |
|35 ****VERIFIED CLAIM AMT**** | The total amount claimed after verification by DOLI | Character (but easily converted to numeric)  |  |
|36 ****CASE CLOSE/RECLOSE DATE****  | Date case was officially closed | Character |  |
|37 Employer Contested Valid Determination | Whether the employer contested a claim that was found to be valid | Character: X if true, missing if false  |  |
|38 ****1st Response Investigation**** | Whether only a 1st response was conducted | Character: X if true, missing if false  | DOLI conducts a quick "1st response" investigation first to determine if a formal investigation is warranted |
|39 ****Formal Investigation**** | Whether a formal investigation was conducted | Character: X if true, missing if false  |  |
|40 Request Settlement Conference  |  | All missing | No such requests in the data  |
|41 Request Informal Fact Finding  |  | All missing  | No such requests in the data  |
|42 Request Formal Fact Finding  |  | All missing  | No such requests in the data |
|43 ****Wage Order**** | Whether a legal order is given for the employer to pay lost wages | Character: X if true, missing if false  | See page 10, G(1): (http://townhall.virginia.gov/L/GetFile.cfm?File=C:%5CTownHall%5Cdocroot%5CGuidanceDocs%5C181%5CGDoc_DOLI_1780_v5.pdf) |
|44 Informal Conference  |  | All missing | No such actions in the data |
|45 Civil Action for Wages/Penalties |  | All missing  | No such actions in the data  |
|46 Other_2  |  | All missing  | No such actions in the data |
|47 OTHER DISPOSITION DESCRIPTION  |  | All missing  |  |
|48 CASE CLOSED for the REPRESENTATIVE | Date the DOLI labor law representative ended the investigation  | Character |  |
|49 JUDGMENT |  | All missing |  |
|50 DISMISSED  |  | All missing |  |
|51 NON-SUITED |  | All missing |  |
|52 JUDGMENT_1 |  | All missing  |  |
|53 DISMISSED_1  |  | All missing |  |
|54 NON-SUITED_1 |  | All missing |  |
|55 CIVCOURTDTE FOR WAGES/PENALTY  |  | All missing |  |
|56 ****TOT AMT****  | Total amount recovered for the complainant | Character (but easily converted to numeric)  | These columns show the cases where DOLI is successful in collecting wages |
|57 ****WAGE AMT**** | Amount recovered in lost wages for the complainant | Character (but easily converted to numeric)  |  |
|58 INTEREST AMT | Amount recovered in interest on lost wages for the complainant | Character (but easily converted to numeric)  |  |
|59 ATTY FEES  | Amount recovered in reimbursed attorney fees for the complainant | Character (but easily converted to numeric)  |  |
|60 DATE FOR WAGES | Date wages were returned to the complainant | Character  |  |
|61 WAGES APPEALED |  | All missing  |  |
|62 WAGES APPEAL CIRCUIT COURT DATE  |  | All missing  |  |
|63 ASSESSED | Whether the DOLI investigation concludes the employer owes a civil monetary penalty  | Character: X if true, missing if false  | A civil monentary penalty (CMP) is a fine an employer must pay as punishment for wage-theft, in addition to paying back wages and fees |
|64 AMT  | Amount of the CMP owed by the employer | Character (but easily converted to numeric)  | See above |
|65 ATTY FEES_1  | Attorney fees owed by the employer as part of the CMP | Character (but easily converted to numeric)  | See above |
|66 ASSESSED DATE  | Date CMP totals were assessed | Character  | See above |
|67 TOTAL CMP AMT  | CMP + attorney fees | Character (but easily converted to numeric)  | See above |
|68 CMP APPEALED |  | All missing  | See above |
|69 CMP APPEAL CIRCUIT COURT DATE  |  | All missing  | See above |
|70 FINES & COURT COSTS  | Other fines and court costs associated with the CMP | Character (but easily converted to numeric)  | See above |
|71 TOTAL WAGES  | Total wages that the DOLI says have been actually collected | Character (but easily converted to numeric)  | *_We're not sure what to make of these "collection" variables at this point._* After a legal order for an employer to repay wages, the case is referred to a collection agency or to an attorney in charge of collection. These values indicate the amount that has been collected. It includes amounts that have been legally ordered, and amounts that were settled upon in civil court or outside DOLI jurisdiction. |
|72 TOTAL INTEREST AMT | Total interest collected | Character (but easily converted to numeric)  | See above |
|73 TOT WAGES & INTEREST | Wages + interest collected | Character (but easily converted to numeric)  | See above |
|74 GARNISHED AMT  |  | All $0  |  |
|75 JUDGMENT WAGE AMT  | We think these are additional fees for repeat offenders | Character (but easily converted to numeric)  |  |
|76 JUDGEMENT PENALTY AMT  | We think these are additional fees for repeat offenders  | Character (but easily converted to numeric)  |  |
|77 DOCKETED/SENT FOR COLLECTION DATE  |  | All missing  |  |
|78 ACTION TAKEN |  | All missing  |  |
|79 COURT DATE |  | All missing |  |
|80 CONVICTED - DISPOSITION  |  | All missing |  |
|81 DISMISSED - DISPOSITION  |  | All missing  |  |
|82 NOL Prossed  |  | All missing  |  |
|83 CONFINEMENT  |  | All missing  |  |
|84 SUSPENSION |  | All missing  |  |
|85 BOTH - C&F |  | All missing |  |
|86 JUDGMENT_2 |  | All missing  |  |
|87 DISMISSED_2  |  | All missing  |  |
|88 NON-SUITED_2 |  | All missing  |  |
|89 JUDGMENT_3 |  | All missing  |  |
|90 DISMISSED_3  |  | All missing  |  |
|91 NON-SUITED_3 |  | All missing  |  |
