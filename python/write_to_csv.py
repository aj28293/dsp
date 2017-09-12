import csv

list_of_emails = ['nanditam@mail.med.upenn.edu',
'knashawn@mail.med.upenn.edu',
'propert@mail.med.upenn.edu',
'mputt@mail.med.upenn.edu',
'sratclif@upenn.edu',
'michross@upenn.edu',
'jaroy@mail.med.upenn.edu',
'msammel@cceb.med.upenn.edu']
def write_to_csv(list_of_emails):
    with open("emails.csv", "w") as f:
        writer = csv.writer(f, delimiter='\n')
        writer.writerow(["list of emails"])
		
        writer.writerows([list_of_emails])
		
# def write_to_csv(list_of_emails):
	# email_list = []
	# #for i in list_of_emails:
	# with open("emails1.csv", "w") as f:
		# writer = csv.writer(f, lineterminator='\n')
		# writer.writerow(["list of emails"])
		# writer.writerows([list_of_emails])
		
write_to_csv(list_of_emails)

# for line in list_of_emails:
            # writer.writerows(line)
            # writer.writerows('\n')