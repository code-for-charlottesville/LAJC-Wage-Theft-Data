# load packages ----------------------------------------------------------------
library(data.table)
library(tidyverse)
library(janitor)
library(lubridate)


# read data --------------------------------------------------------------------
raw_data <- fread("Raw data/lajc_wage_claim.csv") %>%
    clean_names()



# clean data -------------------------------------------------------------------
# parse dates, dollar amounts, and calculate investigation period
clean_data <- raw_data %>%
    mutate(claim_received = dmy(claim_received)) %>%
    mutate(case_open_re_open = dmy(case_open_re_open)) %>%
    mutate(case_close_reclose_date = dmy(case_close_reclose_date)) %>%
    mutate(case_closed_for_the_representative = dmy(case_closed_for_the_representative)) %>%
    # calculate investigation period
    mutate(investigation_period = case_close_reclose_date - case_open_re_open) %>%
    # convert to dollars
    mutate(claim_amt = as.numeric(gsub("[\\$,]", "", claim_amt))) %>%
    mutate(wage_amt = as.numeric(gsub("[\\$,]", "", wage_amt))) %>%
    mutate(tot_amt = as.numeric(gsub("[\\$,]", "", tot_amt))) %>%
    mutate(verified_claim_amt = as.numeric(gsub("[\\$,]", "", verified_claim_amt)))

