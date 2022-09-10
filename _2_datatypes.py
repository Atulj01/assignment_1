#num =10                    #int
#salary = 9000.67           #float 
#name ="Bharti"             #string
#comp = 2+4j                #complex
#data = None                #nonetype

#print(type(num))

#salary_type = type(salary)
#print(salary_type)

#name_type = type(name)
#print(name_type)
 
#night_type = type(night)
#print(night_type)

#comp_type = type(comp)
#print(comp_type)

#data_type = type(data)
#print(data_type)

# list
# are used to store more then one value
# []
# indexed - start with 0
# it allows you to store heterogenous data(value of different datatype)
# dupliclate values are allowed
# mutable (modifiable)
#list()
#ORDERED -it considered the same order in which you inserted the value
#iterable

# lst =[2,3,4,5,"Bharati" ,6,7,8] # 4-0 , 5-1, 6-2
# print(lst)

# print(lst[3]) 

# lst[4] = "atul"
# print(lst)

# lst1 =list([1,2,3,4])
# print(lst1 [2])

# print("lst type : ", type(lst))
# print("lst1 type : ",type(lst1))



# tuple
# are usde to store more than one value 
# used ()
# tuple()
# allows you to store hetrogenous  data
# indexed
# ordered
# itreable(meance stored more then 1 data)
# duplicates are allowed
# immutable (cannot modified)
# imp interview Q.= 
# tup = (1,2,3,4,5,5,"A",True)
# print(tup)
# print(tup[0])


# tup1 = tuple((1,2,3))
# print(tup1)



# set
# set is difined using {}
# are used to store more then one value  
# iterable
# unordered
# does not allowes duplicate value
# non-indexed
# we can modified (mutable)
# it allows heterogenous data

# set_demo = {1,4,2,5,3,100,5,"Atul"}
# print(set_demo)

# print(set_demo)





# dict (dictionary)
# {}
# dict()
# {key;value} - item
# key - duplicates are not allowed
# value - duplicate are allowed
# unordered 
# non indexed



students = {1: "Bharati" ,2:567,3:"Atul"}
print(students)

print(students[1])
students[1] = "mahabharat"
print(students)