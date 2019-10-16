import pandas as pd

# ===================================================================
# Import data
# ===================================================================
df = pd.read_csv("../Raw data/lajc_clean.csv").set_index("claimID")

# ===================================================================
# Clean cities
# ===================================================================

# This dictionary maps misspelled cities to their correct spellings
replace_dict = {"ALEXANDROA": "ALEXANDRIA",
                "ANNADALE": "ANNANDALE",
                "ARRINGTON": "ARLINGTON",
                "ASHBRUN": "ASHBURN",
                "BEALTETON": "BEALETON",
                "CENTERVILLE": "CENTREVILLE",
                "CHANITILLY": "CHANTILLY",
                "CHARLOTTEVILLE": "CHARLOTTESVILLE",
                "CHARLSTON": "CHARLESTON",
                "CHESAPEAK": "CHESAPEAKE",
                "CHRISTIANBURG": "CHRISTIANSBURG",
                "CORZET": "CROZET",
                "CROFTEN": "CROFTON",
                "DOWNERSGROVE": "DOWNERS GROVE",
                "ELIZABETH": "ELIZABETH CITY",
                "FAIRFAX STATION": "FAIRFAX",
                "FORREST": "FOREST",
                "FREDRICKSBURG": "FREDERICKSBURG",
                "GAINSVILLE": "GAINESVILLE",
                "GEITHSEBURG": "GAITHERSBURG", # ???
                "GRENVILLE": "GREENVILLE",
                "HARRISONBRUG": "HARRISONBURG",
                "HERDON": "HERNDON",
                "KING GEORG": "KING GEORGE",
                "LEESBRUG": "LEESBURG",
                "LUREY": "LURAY",
                "LYNCYBURG": "LYNCHBURG",
                "MANAKIN SABOT": "MANAKIN-SABOT",
                "MANIKAN-SABOT": "MANAKIN-SABOT",
                "MATHEWS": "MATTHEWS",
                "MIDLOTHION": "MIDLOTHIAN",
                "MONETTA": "MONETA",
                "MOSELY": "MOSELEY",
                "MOSLEY": "MOSELEY",
                "N CHESTERFIELD": "NORTH CHESTERFIELD",
                "N. CHESTERFIELD": "NORTH CHESTERFIELD",
                "NEWPORTS NEWS": "NEWPORT NEWS",
                "NEWPROT NEWS": "NEWPORT NEWS",
                "NOFORK": "NORFOLK",
                "NORFILK": "NORFOLK",
                "OWENS BORO": "OWENSBORO",
                "PISCATA WAY": "PISCATAWAY",
                "PITTSBURG": "PITTSBURGH",
                "POQUOSEN": "POQUOSON",
                "PORTSMOUNT": "PORTSMOUTH",
                "PURCELLVLLE": "PURCELLVILLE",
                "RESTEN": "RESTON",
                "RICHMOMD": "RICHMOND",
                "RUSTBURGH": "RUSTBURG",
                "SALAM": "SALEM",
                "SHADY": "SHADY SIDE",
                "SMRYNA": "SMYRNA",
                "SPOTSYIVANIA": "SPOTSYLVANIA",
                "SPRINGIELD": "SPRINGFIELD",
                "STEPHENS": "STEPHENS CITY",
                "STRAFFORD": "STAFFORD",
                "STRASHBURG": "STRASBURG",
                "STUANTON": "STAUNTON",
                "SUFFULK": "SUFFOLK",
                "TYSON'S CORNER": "TYSONS CORNER",
                "VINT HIL": "VINT HILL",
                "VIRGINA BEACH": "VIRGINIA BEACH",
                "VIRGINIA": "VIRGINIA BEACH",
                "VIRGINIA  BEACH": "VIRGINIA BEACH",
                "WALDOLF": "WALDORF",
                "WARRINGTON": "WARRENTON",
                "WASHINGTON, D.C.": "WASHINGTON",
                "WAVERYLY": "WAVERLY",
                "WAYNESBOR0": "WAYNESBORO",
                "WINSTON SALEM": "WINSTON-SALEM",
                "WINSTON SALEN": "WINSTON-SALEM",
                "YORKSOWN": "YORKTOWN",
                "ZIONS CROSSROADS": "ZION CROSSROADS"
                }

# Correct city spellings via above dictionary
df["employercity"] = df["employercity"].replace(replace_dict)

# Fix individual city and state mistakes
df.loc["LLVA59311", "employerstate"] = "VA" # Alexandria, NA --> Alexandria, VA
df.loc["LLVA60000", "employerstate"] = "NC" # Rocky Mount, VA --> Rocky Mount, NC
df.loc["LLVA62833", "employerstate"] = "NC" # Rocky Mount, VA --> Rocky Mount, NC
df.loc["LLVA61796", "employerstate"] = "DC" # Washington, VA --> Washington, DC

# ===================================================================
# Frequencies of distinct city/state pairs
# ===================================================================

# Create table, polish look
freq = df.groupby(["employercity", "employerstate"]).count().iloc[:, 0].sort_values(ascending = False)
freq = pd.DataFrame(freq).reset_index()
freq = freq.rename(
    columns = {"employercity": "City", "employerstate": "State", "employer": "# of Claims"})

freq["City"] = freq["City"].str.title() # convert cities from all-caps to title case, for readability
freq = freq.head(10) # top 10 cities
print(freq.to_string(index = False)) # hides index column in print output

freq = freq.sort_values(by = "# of Claims", ascending = True) # need to sort for graphing purposes

# Bar graph of frequencies (highest to lowest)
import matplotlib.pyplot as plt
plt.barh(
    freq["City"], freq["# of Claims"],
    color = "orange")
plt.xlabel("# of Claims")
plt.ylabel("City")
plt.title("Top " + str(len(freq)) + " Cities in Claims")
plt.tight_layout();
plt.show()
