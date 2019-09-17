# Legal Aid Justice Center (LAJC) Wage-Theft Data

Join our Meetup group here: https://www.meetup.com/Code-for-Charlottesvile/
Our slides for tonight: www.tinyurl.com/cfclaunchnight

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
The raw data is available in the Raw Data folder on this repository. A codebook is listed here: https://github.com/code-for-charlottesville/LAJC-Wage-Theft-Data/tree/master/Raw%20data

## Goals
Here's a list of our immediate goals to help the LAJC. However, as you work on the data, you might have ideas for additional goals, and **you should feel free to pursue your ideas.**

| Goal                                                                    | Timing                   | Status      | Location                     |
|-------------------------------------------------------------------------|--------------------------|-------------|------------------------------|
| Categorize every business into an industry group                        | 9/17, 10/1, 10/15        | In progress | https://tinyurl.com/yyyfer65 |
| Pre-process data                                                        | 9/17, 10/1               | In progress |   https://github.com/code-for-charlottesville/LAJC-Wage-Theft-Data/tree/master/Data%20preprocessing|                          
| Determine what % of claims get wages ordered to be returned  | 9/17, 10/1               | In progress            |                              
| Determine what % of claims get 1st response and formal investigations opened  | 9/17, 10/1               | In progress |                              
| Determine what % of claim are found to be valid, invalid, and undetermined | 9/17, 10/1               | In progress |
| How long does it take to conduct an investigation? | 9/17, 10/1               | In progress |
| How long does it take to get a wage order? | 9/17, 10/1               | In progress |
| If wages are ordered to be returned, what's the distribution of amounts? | 9/17, 10/1               | In progress |
| How do these outcomes listed above depend on ethnicity, gender, and industrial category?   | 9/17, 10/1               | In progress |                                


## How to Use GitHub
### If you are already familiar with GitHub (and Git)
Please fork this repo, make edits (with git if you like, or using the GitHub GUI), then issue a **pull request**. We will be checking the repo frequently throughout the evening to merge these pulls into the main repo. If you would like us to merge, and we haven't yet, feel free to tap one of us on the shoulder.

### If you are a beginner with GitHub
GitHub is the most popular website for sharing data and code. But everyone who uses this website remembers how intimidating GitHub can be. If you've never seen or used GitHub before, don't worry! You have options:

* You can help us out a lot while skipping the technical stuff by helping to categorize the businesses into industry groups: https://tinyurl.com/yyyfer65

* You can team up with a more experienced volunteer

* Or you can follow these steps to get going with GitHub:

1. Open a new window (so you can still see these instructions), and get a GitHub account here: https://github.com/join?source=header-home

2.  Choose the FREE, **not the paid**, option. Don't select "help me set up an organization" and push Continue. Fill out the survey if you'd like, and verify your email. This will take you to your personal GitHub homepage.

3. Now that you are signed in, navigate back to this website. In the top-right corner of this page, click the button marked **fork** and click on your GitHub user name.

4. This will take you to a *copy* of this webpage that will exist ONLY on your personal GitHub page. At the top of the screen, it should say *your-user-name/LAJC-Wage-Theft-Data* and NOT *code-for-charlottesville/LAJC-Wage-Theft-Data*.

5. Click "Clone or Download" and "Download ZIP" and unzip the folder. You will now have access to all of the files that exist in this repository on your local machine.

6. The raw data will be in this folder, under the folder named "Raw Data", as *lajc_wage_claim.csv*. If other volunteers have already made scripts to clean the data in Python, R, Stata, SAS, or another program, the script will be in the folder named "Data preprocessing". 

7. Use the raw data and cleaning scripts to do whatever work you want to do. Save your files on your local computer for now.

8. When you are done with your work, it's time to bring it back to your GitHub copy of this project repository. On your GitHub page, click on the folder you need:

  * Use "Data preprocessing" to upload a data cleaning script
  
  * Use "Work in progress" for anything you want to save online and come back to later, or anything you want someone else to work on later
  
  * Use "Final products" for anything that is ready to be shared with our community partner
  
Then click on "Upload file" and select the files you want to exist on your GitHub page. At the bottom, you can write a short description of these files if you want. Then select "Commit Changes" to upload the files.

9. When you have uploaded all of the files you want to share, it's time to share these files with the main Code for Charlottesville repository. To do that, click "New Pull Request". Then push "Create pull request". Write a comment about what you did, if you want, and click "Create pull request" again. 

10. One of the adminstrators of the main Code for Charlottesvilee repository will review your files and accept them to be added to the main repository.

If you have any questions, please don't hesitate to speak with one of the co-captains or to one of the more experienced volunteers.
