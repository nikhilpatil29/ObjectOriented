"""
	Purpose: Program for Reguler Expression using Regx
	@Author Nikhil Patil
"""
import re
class RegulerExpression:

	# Function for validating a Name
	# @param name
	def nameValidate(name):
		if re.search("^[A-Za-z]{2,10}",name):
			return True
		else:
			return False

	# Function for validating a FullName
	# @param fname
	def fnameValidate(fname):
		if re.search("[\wA-Za-z]{2,20}\s\w[A-Za-z]{2,20}",fname):
			return True
		else:
			return False

	# Function for validating a Mobile Numbere
	# @param mno
	def mobileNumberValidate(mno):
		if re.search("\w{2}-\w{10}",mno):
			return True
		else:
			return False

	# Function for validating a Date
	# @param date
	def dateValidatation(date):
		if re.search("^[\d]{2}/[\d]{2}/[\d]{4}",date):
			return True
		else:
			return False

	expression = '''Hello <<name>>, We have your full name as <<full name>> in our system.
	your contact number is 91-xxxxxxxxxx. Please,let us know in case of any clarification.
	Thank you BridgeLabz 01/01/2016.'''

	name = raw_input("enter your name\n")
	fname = raw_input("enter your full name\n")
	mno = raw_input("enter your mobile number\n")

	date = raw_input("enter the date\n")

	nameval = nameValidate(name)
	# name validation
	# if nameval == 0:
	# 	print "name is valid"
	# else:
	# 	print "invalid name"
	fullname = fnameValidate(fname)		# Full_Name validation
	# if fullname == 0:
	# 	print "full name is valid"
	# else:
	# 	print "invalid name"
	mobileNo = mobileNumberValidate(mno)# mobile Number validation
	# if mobileNo == 0:
	# 	print "Mobile number is valid"
	# else:
	# 	print "Mobile number is not valid"
	valDate = dateValidatation(date)	# date validation
	# if valDate == 0:
	# 	print "Given date is valid"
	# else:
	# 	print "Given Date is not valid"
	# executed when all are valid input.

	if nameval and fullname and mobileNo and valDate:
		print "all are correct"
		# new_expr = expression.replace("<<name>>",name).replace("<<full name>>",fname).replace("91-xxxxxxxxxx",mno).replace("01/01/2016",date)
		expression = re.sub("<<name>>",name,expression)
		expression = re.sub("<<full name>>",fname,expression)
		expression = re.sub("91-xxxxxxxxxx",mno,expression)
		expression = re.sub("01/01/2016",date,expression)
		print "new String is\n"
		print expression
	else:
		print "please enter a valid formate"

