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

# Analyze data -----------------------------------------------------------------

# percent of wages that are ordered to be returned
clean_data %>%
    group_by(wage_order) %>%
    summarise(count = n()) %>%
    View()

# percent of claims get first response and formal investigation 0%
clean_data %>%
    mutate(x1st_rep_and_formal_inv = if_else(
        x1st_response_investigation == "X" & formal_investigation == "X",
        "X",
        as.character(NA)
        )) %>% 
    select(x1st_rep_and_formal_inv, x1st_response_investigation, formal_investigation) %>%
    group_by(x1st_rep_and_formal_inv) %>%
    summarise(count = n()) %>%
    View()
    

# percent of claims valid, invalid, undetermined
clean_data %>%
    group_by(valid, invalid, claim_validity) %>%
    summarise(count = n()) %>%
    View()

# average investigation period
clean_data %>%
    summarise(avg_inv_per = mean(investigation_period, na.rm = TRUE)) %>%
    View()

# time to get a wage order
clean_data %>%
    group_by(wage_order) %>%
    summarise(avg_inv_per = mean(investigation_period, na.rm = TRUE)) %>%
    View()

# distribution of wage order amounts
clean_data %>%
    filter(wage_order == "X") %>% 
    ggplot(aes(tot_amt)) + geom_histogram(bins = 7)

# percent of claims valid by gender, hispanic, asian
clean_data %>%
    group_by(gender, hispanic, asian, valid) %>% 
    summarise(count = n()) %>%
    ungroup() %>%
    group_by(gender, hispanic, asian) %>%
    mutate(per_valid = count/sum(count)) %>%
    View()
