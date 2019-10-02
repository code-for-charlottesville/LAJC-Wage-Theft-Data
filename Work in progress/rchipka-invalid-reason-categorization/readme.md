# About

A node.js script to group together various reason strings describing why a particular claim is invalid.

The challenge here is to succinctly categorize differently worded values with the same meaning.

The solution here is to create generalized list of categories and map the reason strings to them using a set of Regular Expression for each category.

Once we have the generalized categories, we can then do further analysis on the data without any false-negatives.

# Installation

`npm install`

Create `lajc-claims` mysql database.

Import `raw-data.sql`

# Run

`node index.js`

# Files

## raw_data.sql

create `raw_data` table representing data within `lajc_wage_claim.csv`

## reasons-raw.txt

sorted and uniqued output of each raw reason string

## reasons-unmapped.txt

reason strings that haven't yet been accounted for by the reason category mapping RegExps.

## index.js

connect to mysql database and map each invalid reason to the distinct sanitized reason category

#### TODO: record reason category for each case and store in mysql for further analysis

## lib/reason-map.js

distinct reason categories and corresponding RegExps to match 

#### TODO: map each unmapped reason string to a reason category
