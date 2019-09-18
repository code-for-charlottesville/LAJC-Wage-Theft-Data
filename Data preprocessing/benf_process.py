import csv

filename = "../Raw data/lajc_wage_claim.csv"

def loadCSV():
	fields = []
	rows = []
	with open(filename, 'r') as csvFile:
		csvReader = csv.reader(csvFile)
		fields = next(csvReader)

		for row in csvReader:
			rows.append(row)

		print("Total no. of rows: %d"%(csvReader.line_num))

	print('Field names are:' + ', '.join(field for field in fields))

def processReturnedClaimsPercentage():
	print("------------------")
	print("Calculating percentage of claims that were ordered to have wages paid...")

	marked = "X"
	wageOrderColumn = 40
	wageOrderCount = 0
	wageOrderValues = {}

	with open(filename, 'r') as csvFile:
		csvReader = csv.reader(csvFile)
		fields = next(csvReader)

		for row in csvReader:
			wageOrderValue = row[wageOrderColumn]

			if wageOrderValue not in wageOrderValues:
				wageOrderValues[wageOrderValue] = 0
			wageOrderValues[wageOrderValue] = wageOrderValues[wageOrderValue] + 1

			if wageOrderValue == marked:
				wageOrderCount += 1

		totalClaims = csvReader.line_num - 1

	print("Values: ", wageOrderValues)
	print("Wages Ordered Count: ", wageOrderCount) 
	print("Wages Ordered Percentage: ", wageOrderValues[marked]/totalClaims)

def processFirstResponseAndFormalInvestigationPercentages():
	print("------------------")
	print("Calculating percentage of claims that received a 1st response and formal investigation...")

	marked = "X"
	firstResponseCount = 0
	firstResponseColumn = 35
	formalInvestigationCount = 0
	formalInvestigationColumn = 36
	receivedBothCount = 0

	with open(filename, 'r') as csvFile:
		csvReader = csv.reader(csvFile)
		fields = next(csvReader)

		for row in csvReader:
			firstResponse = False
			formalInvestigation = False

			if row[firstResponseColumn] == marked:
				firstResponse = True

			if row[formalInvestigationColumn] == marked:
				formalInvestigation = True

			if firstResponse:
				firstResponseCount += 1
			if formalInvestigation:
				formalInvestigation += 1
			if firstResponse and formalInvestigation:
				receivedBothCount += 1

		totalClaims = csvReader.line_num - 1

		print("Received First Response Count: ", firstResponseCount)
		print("Received First Response Percentage: ", firstResponseCount/totalClaims)
		print("Received Formal Investigation Count: ", formalInvestigationCount)
		print("Received Formal Investigation Percentage: ", formalInvestigationCount/totalClaims)
		print("Received Both Count: ", receivedBothCount)
		print("Received Both Percentage: ", receivedBothCount/totalClaims)


def processValidInvalidUndeterminedPercentages():
	print("------------------")
	print("Calculating percentage of claims that were determined valid/invalid/undetermined...")

	marked = "X"
	validCount = 0
	validColumn = 13
	invalidCount = 0
	invalidColumn = 16
	undeterminedCount = 0
	undeterminedColumns = [23, 24, 25, 26, 27, 28, 29, 30]
	unmarked = 0

	dubiousRows = []

	with open(filename, 'r') as csvFile:
		csvReader = csv.reader(csvFile)
		fields = next(csvReader)

		for row in csvReader:
			isValid = False
			isInvalid = False
			isUndetermined = False

			if row[validColumn] == marked:
				isValid = True

			if row[invalidColumn] == marked:
				isInvalid = True

			for column in undeterminedColumns:
				if row[column] == marked:
					isUndetermined = True
					break

			if isValid:
				validCount += 1
				if isInvalid or isUndetermined:
					dubiousRows.append(row)

			if isInvalid:
				invalidCount += 1
				if isValid or isUndetermined:
					dubiousRows.append(row)

			if isUndetermined:
				undeterminedCount += 1
				if isValid or isInvalid:
					dubiousRows.append(row)

			if not any([isValid, isInvalid, isUndetermined]):
				unmarked += 1

		totalClaims = csvReader.line_num - 1

		print("Valid Claims: ", validCount)
		print("Valid Claims Percentage: ", validCount/totalClaims)
		print("Invalid Claims: ", invalidCount)
		print("Invalid Claims Percentage: ", invalidCount/totalClaims)
		print("Undetermined Claims: ", undeterminedCount)
		print("Undetermined Claims Percentage: ", undeterminedCount/totalClaims)
		print("Uncategorized Claims: ", unmarked)
		print("Uncategorized Claims Percentage: ", unmarked/totalClaims)
		print("Dubious Rows... ", dubiousRows)

# TODO: Find average difference between case open/close
# TODO: Find longest difference
# TODO: Find shortest difference
def processLengthOfClaims():
	print("------------------")
	print("Calculating length information of claims...")

	caseOpenColumn = 11
	caseCloseColumn = 33

	with open(filename, 'r') as csvFile:
		csvReader = csv.reader(csvFile)
		fields = next(csvReader)

		for row in csvReader:
			print(row)
		totalClaims = csvReader.line_num - 1

if __name__ == '__main__':
    processReturnedClaimsPercentage()
    processFirstResponseAndFormalInvestigationPercentages()
    processValidInvalidUndeterminedPercentages()