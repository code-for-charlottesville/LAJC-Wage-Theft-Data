setwd("~/Box Sync/Code for Cville")
library(tidyverse)
library(lubridate)

lajc <- read_csv("lajc_wage_claim.csv")

lajc <- lajc %>%
  rename(claimID = `CLAIM NO`,
         employer = `EMPLOYER NAME`,
         employercity = `EMPLOYER CITY`,
         employerstate = ST,
         employerzip = ZIP,
         claim_amount = `CLAIM AMT`,
         case_open = `CASE OPEN/RE-OPEN`,
         valid = Valid,
         invalid = Invalid,
         verified_claim = `VERIFIED CLAIM AMT`,
         case_close = `CASE CLOSE/RECLOSE DATE`,
         first_response = `1st Response Investigation`,
         formal_investigate = `Formal Investigation`,
         wage_order = `Wage Order`,
         total_rec = `TOT AMT`,
         wage_rec = `WAGE AMT`) %>%
  select(claimID, starts_with("employer"), gender, hispanic, asian, claim_amount, case_open, valid, 
         invalid, verified_claim, case_close, first_response, formal_investigate, wage_order, total_rec, 
         wage_rec, -starts_with("EMPLOYER ")) %>%
  mutate(gender = factor(gender),
         claim_amount = substring(claim_amount, 2),
         verified_claim = substring(verified_claim, 2),
         total_rec = substring(total_rec, 2),
         wage_rec = substring(wage_rec, 2),
         claim_amount = str_remove(claim_amount, ","),
         verified_claim = str_remove(verified_claim, ","),
         total_rec = str_remove(total_rec, ","),
         wage_rec = str_remove(wage_rec, ","),
         claim_amount = as.numeric(claim_amount),
         verified_claim = as.numeric(verified_claim),
         total_rec = as.numeric(total_rec),
         wage_rec = as.numeric(wage_rec),
         case_open = dmy(case_open),
         case_close = dmy(case_close),
         duration = case_close - case_open,
         valid = (valid == "X"),
         invalid = (invalid == "X"),
         first_response = (first_response == "X"),
         formal_investigate = (formal_investigate == "X"),
         wage_order = (wage_order == "X"),
         valid = ifelse(is.na(valid), FALSE, valid),
         invalid = ifelse(is.na(invalid), FALSE, valid),
         first_response = ifelse(is.na(first_response), FALSE, valid),
         wage_order = ifelse(is.na(wage_order), FALSE, valid),
         formal_investigate = ifelse(is.na(formal_investigate), FALSE, valid))
