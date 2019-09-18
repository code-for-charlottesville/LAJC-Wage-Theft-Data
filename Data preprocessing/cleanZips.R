#libraries 
library(tidyverse)
library(stringr)
library(zipcode)

#load data
lajc <- read.csv(url("https://raw.githubusercontent.com/bkatcher4/LAJC-Wage-Theft-Data/master/Raw%20data/lajc_wage_claim.csv"))

#make variable names consistent 
names(lajc) <- str_to_lower(names(lajc))

#clean up zip codes
clean_zips <-data.frame("zip"=clean.zipcodes(lajc$zip))

#load in zipcode data and merge
data("zipcode")
clean_zips <- full_join(clean_zips,zipcode)
lajc$zip <- as.integer(lajc$zip)
clean_zips$zip <- as.integer(clean_zips$zip)
lajc <- full_join(clean_zips,lajc)

#write to csv
write.csv(lajc, "clean_lajc_zips.csv")