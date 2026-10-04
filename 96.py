import csv
data=[{'Name':'John','Age':20,'City':'Hyderabad'},
       {'Name': 'Sachin', 'Age': 21, 'City': 'Pune'},    
    {'Name': 'Lucy', 'Age': 40, 'City': 'New York'}    ]
with open('dictwriter-example.csv','w',newline='')as file:
    fieldnames=['Name','Age','City']
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(data)
    print("CSV file created successfully")