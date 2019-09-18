# read in data
unproc_data = read.csv(file.path("Raw data", "lajc_wage_claim.csv"), stringsAsFactors = FALSE)

# Valid = X is TRUE, NA is not
unique(unproc_data$Valid)
unproc_data[is.na(unproc_data$Valid), "Valid"] = FALSE
unproc_data[unproc_data$Valid == "X", "Valid"] = TRUE

# clean up date columns
date_cols = c("CASE.OPEN.RE.OPEN", "CLAIM.RECEIVED", "CASE.CLOSE.RECLOSE.DATE", "CASE.CLOSED.for.the.REPRESENTATIVE", "DATE.FOR.WAGES", "ASSESSED.DATE")
library(lubridate)
test = head(unproc_data[, date_cols[1]])
parse_date_time(test, orders="d-m-y")
# can't get apply to work, doing it with a for loop...
for(i in 1:length(date_cols)){
  unproc_data[, date_cols[i]] = parse_date_time(unproc_data[, date_cols[i]], orders="d-m-y", tz="us")
  print(range(unproc_data[, date_cols[i]], na.rm=TRUE)) # no obvious formatting issues
}

# clean up dollar amount columns
