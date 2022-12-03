import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

no_of_friends=len(names)

index_of_friend_in_list=random.randint(0,no_of_friends-1)
print(names[index_of_friend_in_list],"is going to buy the meal today!")
