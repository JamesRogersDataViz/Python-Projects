import os
import csv

us_state_abbrev = {
    'Alabama': 'AL',
  	'Alaska': 'AK',
  	'Arizona': 'AZ',
  	'Arkansas': 'AR',
  	'California': 'CA',
  	'Colorado': 'CO',
  	'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

employee_csv = os.path.join("..", "PyBoss", "employee_data.csv")
names_csv = os.path.join("names.csv")

data = []
with open(employee_csv, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")
  
  for line in csvreader:
    data.append(line)

with open(names_csv, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames= ['Emp ID' , 'first_name', 'last_name', 'dob', 'SSN', 'State'])
    writer.writeheader()
    for i in range(1, len(data)):
      emp_id = data[i][0] 
      names = data[i][1].split(' ')    
      emp_dob = data[i][2].split('-') 
      if len(emp_dob[0]) < 2:
        emp_dob[0] = '0' + emp_dob[0]
      if len(emp_dob[1]) < 2:
        emp_dob[1] = '0' + emp_dob[1]  
      dob = emp_dob[0] + '/' + emp_dob[1] + '/' + emp_dob[2]          
      emp_ssn = data[i][3].split('-')
      ssn = '***-**-' + emp_ssn[2]
      state = us_state_abbrev[data[i][4]]
      writer.writerow({'Emp ID': emp_id, 'first_name': names[0], 'last_name': names[1], 'dob': dob, 'SSN': ssn, 'State': state})
      print(i)