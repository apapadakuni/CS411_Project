from pymongo import MongoClient
from pprint import pprint
client = MongoClient('mongodb://localhost:27017')
c = client['SUP']
db = c.courses
i = [{
    "first": 30,
    "second": 40 
}, {
    "first": 50,
    "second": 60
}


]
for j in i:
    db.update({
        "hi": 5
        },
        {'$push':{
            "events":j
        }
        })




# course_array = [
#     {
#     'bitch': 'example1',
#     'sup': 'loool',
#     'price': 5,
#     'checknested':
#         {
#         'true': 'here'
#         }
#     },
#     {
#     'bitch': 'example',
#     'sup': 'loool',
#     'price': 7,
#     'checknested':{
#         'true': 'lol'
#     }
#     }
# ]
# res = courses.insert_many(course_array)
# # for i in res.inserted_ids:
# #     print('Cource aded. id is %s' % str(i))

# cource = courses.find_one({
#     'checknested': 'noway'
#     })
# print(cource==None)
# courses.update({
#     'checknested': {
#         'true':
#         }
#     },
#     {
#         '$set':{
#             'bitch': 'changed value'
#         }
#     }, multi = False)
# # for i in cource:
# #     pprint(i)
# # # if res.acknowledged:
# # #     print('Cource added. id is %s' % str(res.inserted_id))


# # courses.delete_many({
# #     'bitch': 'changed value'
# #     })
