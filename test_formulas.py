import pandas as pd
from timeis import *
import re
import os

def export_ods_with_formulas():

	# help
	# https://help.libreoffice.org/latest/en-GB/text/shared/guide/csv_params.html?DbPAR=SHARED#bm_id181634740978601

	os.popen('cp "/home/bhikkhu/Bodhirasa/Dropbox/dpd/dpd.ods" "/home/bhikkhu/Bodhirasa/Dropbox/dpd/data tests/dpd.ods"')
	
	os.popen('soffice --convert-to csv:"Text - txt - csv (StarCalc)":"9,34,76,,,,,,,true" dpd.ods')
	

def setup_dpd_df():
	input (f"{timeis()} {white}press enter when csv has saved {blue} ")
	print(f"{timeis()} {green}setting up dpd formulas dataframe")
	global df

	df = pd.read_csv("dpd.csv", sep = "\t", dtype = str, header=None)
	df.fillna("", inplace=True)
	# df = df.drop(index=0) #removing first row
	new_header = df.loc[1] #grab the first row for the header
	df = df[2:] #take the data less the header row
	df.columns = new_header #set the header row as the df header
	df.reset_index(inplace = True, drop=True)


def test_formulas():
	print(f"{timeis()} {green}testing root formulas")
	length = len(df)
	for row in range(length):
		headword = df.loc[row, "Pāli1"]
		sk_root = df.loc[row, "Sk Root"]
		sk_root_mn= df.loc[row, "Sk Root Mn"]
		sk_root_cl = df.loc[row, "Cl"]
		pali_root = df.loc[row, "Pāli Root"]
		pali_root_incomps = df.loc[row, "Root In Comps"]
		pali_root_v = df.loc[row, "V"]
		pali_root_grp = df.loc[row, "Grp"]
		pali_root_mn = df.loc[row, "Root Meaning"]

		sk_root = re.sub(fr"\=\$Roots\.\$J\$", "", sk_root)
		sk_root_mn= re.sub(fr"\=\$Roots\.\$K\$", "", sk_root_mn)
		sk_root_cl = re.sub(fr"\=\$Roots\.\$L\$", "", sk_root_cl)
		pali_root = re.sub(fr"\=\$Roots\.\$C\$", "", pali_root)
		pali_root_incomps = re.sub(fr"\=\$Roots\.\$D\$", "", pali_root_incomps)
		pali_root_v = re.sub(fr"\=\$Roots\.\$E\$", "", pali_root_v)
		pali_root_grp = re.sub(fr"\=\$Roots\.\$F\$", "", pali_root_grp)
		pali_root_mn = re.sub(fr"\=\$Roots\.\$I\$", "", pali_root_mn)

		if row%5000 == 0:
			print(f"{timeis()} {row}/{length}\t{headword}")
		
		if sk_root_mn != "" and \
		(pali_root != sk_root or \
		pali_root != sk_root_mn or \
		pali_root != sk_root_cl or \
		pali_root != pali_root_incomps or \
		pali_root != pali_root_v or \
		pali_root != pali_root_grp or \
		pali_root != pali_root_mn):
			print(f"{timeis()} {red}{row}/{length}\t{headword} error")
			print(f"{timeis()} {red}{row}/{length}\t{sk_root} {sk_root_mn} {sk_root_cl} {pali_root} {pali_root_incomps} {pali_root_v} {pali_root_grp} {pali_root_mn}")


# export_ods_with_formulas()
# setup_dpd_df()
# test_formulas()