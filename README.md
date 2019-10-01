Join our Meetup group here: https://www.meetup.com/Code-for-Charlottesvile/

Our slides for tonight: https://tinyurl.com/CFCslides

# Legal Aid Justice Center (LAJC) Wage-Theft Data

**Project Status:** Active

**Links:**

[The Legal Aid Justice Center](justice4all.org)

[Code for Charlottesville](codeforcharlottesville.org)

[Virginia Department of Labor and Industry (DOLI) instructions for submitting a wage claim](https://www.doli.virginia.gov/labor-law/payment-of-wage-english/)

**Schedule:** We will be working with this dataset on

* Tuesday, Sept 17, 6:30-9pm, Dell 1, UVA

* Tuesday, Oct 1, 6:30-9pm, Center for Civic Innovation 

* Tuesday, Oct 15, 6:30-9pm, Dell 1, UVA

## Introduction and Objective
From Wikipedia (https://en.wikipedia.org/wiki/Wage_theft): "Wage theft is the denial of wages or employee benefits rightfully owed to an employee. It can be conducted by employers in various ways, among them failing to pay overtime; violating minimum-wage laws; the misclassification of employees as independent contractors, illegal deductions in pay; forcing employees to work 'off the clock', not paying annual leave or holiday entitlements, or simply not paying an employee at all.

"According to some studies, wage theft is common in the United States, particularly from low wage legal or undocumented immigrant workers. The Economic Policy Institute reported in 2014 that survey evidence suggests wage theft costs US workers billions of dollars a year. Some rights violated by wage theft have been guaranteed to workers in the United States in the 1938 Fair Labor Standards Act (FLSA)."

In Virginia, people who believe they have been the victim of wage theft can file an official complaint with the Virginia Department of Labor and Industry (DOLI). The DOLI is responsible for investigating these complaints and for taking steps to return lost wages if the employer is found to have committed wage theft.

The [Legal Aid Justice Center](justice4all.org) is writing a report on the performance of the DOLI in investigating these official complaints. They filed a Freedom of Information Act (FOIA) request to acquire the raw dataset we will be working with. **Our objective is to produce clean datasets, tables, figures, and advanced analyses** to assist the LAJC in writing this report.

## Data
The raw data is available in the Raw Data folder on this repository, as **lajc_wage_claim.csv**. A codebook is listed here: https://github.com/code-for-charlottesville/LAJC-Wage-Theft-Data/tree/master/Raw%20data

One version of a cleaned dataset is also stored here, as **lajc_clean.csv**.

## Goals
Here's a list of the immediate goals the LAJC wants us to work on. Feel free to focus on one of them, or more if you have time. Also, as you work on the data, you might have ideas for additional goals, and **you should feel free to pursue your ideas.**

1. **Create a map dividing Virginia into eight regions, showing the number/% of cases where the employer is located in each region.** 
Please use the demographic regions used by UVA’s Cooper Center for Public Service, available here https://demographics.coopercenter.org/virginia-regions. (Also note the number/% of cases where the employer is out of state, and the number/% of cases where the employer’s location can’t be determined.)

2. **A table showing a comprehensive overview of the reasons that DOLI has rejected cases over the last five years.** For each reason, we’d like to know the number of cases dismissed on this basis (for example: "47 cases were dismissed because the worker worked some overtime"). (Some cases have more than one reason for dismissal.)

This unfortunately may require a human being to look over the various reasons for dismissal listed in the “Other” columns (columns 21 and 31) and determine how to code each one. This may require a little independent judgment in some cases. For example, DOLI will reject a case if the worker is seeking over $15,000. One DOLI investigator may note this as "$15,000 limit," while another may write "exceeds maximum claim amount." 

The reasons for dismissal that LAJC is most interested are these:

  * The business is closed / out of business (this is different from “business bankrupt”)

  * The worker had a written employment agreement

  * The worker worked overtime in at least one week

  * The work was performed outside of Virginia

  * The worker is seeking tips or was a tipped employee

   * The claim amount is over $15,000
   
  * The worker hired an attorney (this is different from “the worker filed a lawsuit”)

  * The worker did not demand the wages from the employer before filing a complaint with DOLI

  * The worker was an independent agent/subcontractor/self-employed or DOLI was otherwise unable to establish an employer-employee relationship

  * Errors with the claim form (e.g. the form was incomplete, or the worker didn’t provide an exact claim amount, or the worker signed in pencil rather than in pen, etc.)

  * The claim seeks minimum wages

But please track the other reasons as well! (E.g., complainant can’t be found / worker dropped or withdrew their claim / worker got paid / 2-year statute of limitations / insufficient documentation to proceed, etc.)

3. Data about case duration: (Open Date to Case Closed). I’m particularly interested in:

                                                               i.      How many cases closed the same day they were opened

                                                             ii.      Average/median/modal length of time each case is open

                                                           iii.      Longest amount of time that any case was open

                                                           iv.      Distribution of case duration (for cases that were not closed the same day they were open)

                1-10 days open
                11-31 days open
                32-90 days open
                91-120 days open
                Over 120 days open

 

        Data About Case Processing

                                                               i.      Number/% of cases closed after a first-response investigation

                                                             ii.      Number/% of cases closed after a formal investigation, or an informal investigation

                                                           iii.      Number/% of cases closed after a settlement conference

                                                           iv.      Wage Orders issued

                                                             v.      Cases sent to collections/amounts recovered

                                                           vi.      Number of cases where DOLI took the employer to court (civil or criminal)

 

        Data about money recovered.

                                                               i.      Number/% of cases where DOLI recovered some money for the worker

                                                             ii.      In cases where DOLI recovers some money, what’s the average/mean/modal amount recovered? (in terms of wages, interest, and wages-plus-interest).

                                                           iii.      If possible, I’d also like to see this data broken down by each year. (For example, if DOLI recovered all these wages in 2017 and recovered nothing in the other years, that’d be interesting to know).

 

        Some way to make the data publicly accessible/searchable/manipulable
                            


## How to Use GitHub
### If you are already familiar with GitHub (and Git)
Please fork this repo, make edits (with git if you like, or using the GitHub GUI), then issue a **pull request**. We will be checking the repo frequently throughout the evening to merge these pulls into the main repo. If you would like us to merge, and we haven't yet, feel free to tap one of us on the shoulder.

### If you are a beginner with GitHub
GitHub is the most popular website for sharing data and code. But everyone who uses this website remembers how intimidating GitHub can be at first. If you've never seen or used GitHub before, don't worry! You have options:

* You can help us out a lot while skipping the technical stuff by helping to categorize the businesses into industry groups: https://tinyurl.com/yyyfer65

* You can team up with a more experienced volunteer

* Or you can follow these steps to get going with GitHub:

1. Open a new window (so you can still see these instructions), and get a GitHub account here: https://github.com/join?source=header-home

2.  Choose the FREE, **not the paid**, option. Don't select "help me set up an organization" and push Continue. Fill out the survey if you'd like, and verify your email. This will take you to your personal GitHub homepage.

3. Now that you are signed in, navigate back to this Code for Charlottesville GitHub page. In the top-right corner of this page, click the button marked **fork** and click on your GitHub user name.

4. This will take you to a *copy* of this webpage that will exist ONLY on your personal GitHub page. At the top of the screen, it should say *your-user-name/LAJC-Wage-Theft-Data* and NOT *code-for-charlottesville/LAJC-Wage-Theft-Data*.

5. Click "Clone or Download" and "Download ZIP" and unzip the folder. You will now have access to all of the files that exist in this repository on your local machine.

6. The raw data will be in this folder, under the folder named "Raw Data", as *lajc_wage_claim.csv*. If other volunteers have already made scripts to clean the data in Python, R, Stata, SAS, or another program, the scripts will be in the folder named "Data preprocessing". 

7. Use the raw data and cleaning scripts to do whatever work you want to do. Save your files on your local computer for now.

8. When you are done with your work, it's time to bring it back to your GitHub copy of this project repository. On your GitHub page, click on the folder you need:

  * Use "Data preprocessing" to upload a data cleaning script
  
  * Use "Work in progress" for anything you want to save online and come back to later, or anything you want someone else to work on later
  
  * Use "Final products" for anything that is ready to be shared with our community partner
  
Then click on "Upload file" and select the files you want to exist on your GitHub page. At the bottom, you can write a short description of these files if you want. Then select "Commit Changes" to upload the files.

9. When you have uploaded all of the files you want to share, it's time to share these files with the main Code for Charlottesville repository. To do that, click "New Pull Request". Then push "Create pull request". Write a comment about what you did, if you want, and click "Create pull request" again. 

10. One of the adminstrators of the main Code for Charlottesvilee repository will review your files and accept them to be added to the main repository.

If you have any questions, please don't hesitate to speak with one of the co-captains or to one of the more experienced volunteers. For more information on GitHub (and Git) see: https://github.com/UVA-DSI/Open-Data-Lab/tree/master/education/GitHub
