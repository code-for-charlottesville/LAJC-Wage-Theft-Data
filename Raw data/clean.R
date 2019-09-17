
# Charlotte McClintock 
# Code for Charlottesville

library(tidyverse)
library(Amelia)

lajc <- read_csv("lajc_wage_claim.csv")

names(lajc) <- str_to_lower(names(lajc))

names(lajc) <- gsub(" ", "", names(lajc))

lajc <- transform(lajc, ext = substr(claimamt, 1, 1), claimamt = substr(claimamt, 2, 10))
lajc <- transform(lajc, ext = substr(verifiedclaimamt, 1, 1), verifiedclaimamt = substr(claimamt, 2, 10))
lajc <- transform(lajc, ext = substr(totamt, 1, 1), totamt = substr(totamt, 2, 10))
lajc <- transform(lajc, ext = substr(wageamt, 1, 1), wageamt = substr(wageamt, 2, 10))
lajc <- transform(lajc, ext = substr(interestamt, 1, 1), interestamt = substr(interestamt, 2, 10))
lajc <- transform(lajc, ext = substr(amt, 1, 1), amt = substr(amt, 2, 10))
lajc <- transform(lajc, ext = substr(totalcmpamt, 1, 1), totalcmpamt = substr(totalcmpamt, 2, 10))
lajc <- transform(lajc, ext = substr(totalinterestamt, 1, 1), totalinterestamt = substr(totalinterestamt, 2, 10))
lajc <- transform(lajc, ext = substr(garnishedamt, 1, 1), garnishedamt = substr(garnishedamt, 2, 10))
lajc <- transform(lajc, ext = substr(judgmentwageamt, 1, 1), judgmentwageamt = substr(judgmentwageamt, 2, 10))
lajc <- transform(lajc, ext = substr(judgementpenaltyamt, 1, 1), judgementpenaltyamt = substr(judgementpenaltyamt, 2, 10))

amtcols <- names(lajc)[str_detect(names(lajc), pattern = "amt")]
lajc[amtcols] <- lapply(lajc[amtcols], function (x) {gsub(",", "", x)}) 
lajc[amtcols] <- lapply(lajc[amtcols], function (x) {as.numeric(x)}) 

missmap(lajc)

