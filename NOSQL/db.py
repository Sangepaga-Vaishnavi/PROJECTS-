from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
Db=client['MRECWAI']
Collection=Db['Students']
#doc={'name':'cc', 
#    'classs No':'209', 
#   'branch':'AI', 
#  'year':'3rd year', 
# 'courses': ['python','ml / ai']
#}
#Collection.insert_one(doc)

Collection2=Db['Marks']
#markdoc={
#   'name':'ee', 
#     'classs No':'209', 
#    'branch':'AI', 
#    'year':'3rd year', 
#    'courses': ['python','ML/DL'],
#    'marks':99
#    }
#Collection2.insert_one(markdoc)

#to find the student record

#results=Collection.find_one({'name':'aa'})
#print(results)

#insert many records
markdoc=[{
    'name':'aa', 
     'classs No':'209', 
     'branch':'AI', 
     'year':'3rd year', 
     'courses': ['python','ML/DL'],
     'marks':99
     },

    {
    'name':'bb', 
     'classs No':'209', 
     'branch':'AI', 
     'year':'3rd year', 
     'courses': ['python','ML/DL'],
     'marks':97
     },
     
    {
    'name':'cc', 
     'classs No':'209', 
     'branch':'AI', 
     'year':'3rd year', 
     'courses': ['python','ML/DL'],
     'marks':96
     },

     {
    'name':'dd', 
     'classs No':'209', 
     'branch':'AI', 
     'year':'3rd year', 
     'courses': ['python','ML/DL'],
     'marks':92
     },

     {
    'name':'ee', 
     'classs No':'209', 
     'branch':'AI', 
     'year':'3rd year', 
     'courses': ['python','ML/DL'],
     'marks':90
     }

     ]

Collection.insert_many(markdoc)

#to find the student record
results=Collection.find_one({'name':'aa'})
print(results)

#to find the student record
resultall =Collection.find()
#print(resultall)

for stu in resultall:
    print(stu)

#to update the one student record
updatereco = Collection.update_one(
    {'name': 'aa'},    
    {'$set':{'classs No':'210'}}
    )

deletereco = Collection.update_one(
    {'name': 'cc','year': '3rd year'},    
    {'$set':{'classs No':'211'}}
    )


for stu in resultall:
    print(stu)

deletereco=Collection.delete_one(
    {'name':'aa', 'branch':'AI'}
)

deleteall=Collection2.delete_many({})
resultall =Collection.find()
#print(resultall)

for stu in resultall:
    print(stu)




