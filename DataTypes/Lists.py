"""
----------------------
--- Lists ---
----------------------
[1] List Items Are Enclosed In Square Items []
[2] Lists Are Ordered ---> Index base --> To Access Items
[3] List Are Mutable ->> Add, delete, Update , Insert
[4] List Items Are Not Unique
[5] List Items can Have Different Data Types
"""

my_list=["Sakan",7,True,7.9]
friends=["Ali","Ahmed","Mohamed","Alaa","Sakan"]
# print(friends[:-2])
# print(my_list[-4])
# friends[1]=7
# print(friends[::3])
# newFriends=["Ali","Ahmed","Mohamed","Alaa","Sakan","Ali",9,9]
# print(newFriends)

myNumbersList=[1,2,3,4,5,6]
myNumbers2List=[9,8,7,6,5,4]

myNumbers3List=[1,2,3,4,5,6]
myNumbers4List=[9,8,7,6,5,4]

""" Lists Methods"""

"""append()"""
# friends.append("Yomna")
# friends.append("Mariem")
# friends.append("Mona")
myNumbersList.append(myNumbers2List) #[1,2,3,4,5,6,987654]   #[1,2,3,4,5,6,myNumbers2List]
print(myNumbersList)
# myNumbers3List.extend(myNumbers4List)
# print(myNumbers3List)
myNumbersList.extend(myNumbers2List) #[1, 2, 3, 4, 5, 6, 9, 8, 7, 6, 5, 4]
print(myNumbersList)
# print(friends)
#
# """extend()"""
# friends.extend("Shyimaa")
# print(friends)
