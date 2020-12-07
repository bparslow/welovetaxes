import csv

file = open('variable_key.csv')
data = list(csv.reader(file))
#split list of versions
for line in data:
  line[11] = line[11].split(';')

# variable_name,description,scope,location_code,form,part,data_type,required,cardinality,rdb_table,xpath,version,production_rule,last_version_modified

def GetFull(var_name, version):
  for line in data: 
    if (var_name == line[0]) & (version in line[11]):
      return line[1], line[3]

print(GetFull('Gaming', '2009v1.7')) 