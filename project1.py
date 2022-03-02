
def cr_list():
    li=[]
    return li
def cr_tuple():
    tup=()
    return tup
def cr_set():
    se=set()
    return se
def cr_dict():
    dict={}
    return dict

print("***************Welcome to Datastructure calculator***************")
print("***************Please select any one Data structure***************")

while True:    
    user_input=int(input("1.List\n2.Tuple\n3.Set\n4.Dictionary\n5.Exit\n"))

    if user_input==1:
        list=cr_list()
        no_of_element_on_list=int(input("Enter no of values you want to add on list :"))
        for i in range(no_of_element_on_list):
                list.append(int(input("Enter the valus of List  : ")))
        print(list)
        while True:
            List_info=int(input("\n1.Append\n2.Extend\n3.Pop\n4.Remove\n5.Insert\n6.Concatenation\n7.Sum/Min/Max\n8.Count\n9.Length\n10.Sorting the list\n11.Exit\n"))
            if List_info==1:
                list.append(input("Enter the number to add with the list : "))
                print(list)
                
            elif List_info==2:
                list2=cr_list()
                no_of_element_on_list2=int(input("Enter no of values you want to add on list2 :"))
                for i in range(no_of_element_on_list2):
                    list2.append(int(input("Enter the valus of List 2 : ")))
                print(list2)
                print(list)
                list.extend(list2)
                print(list)
                
            elif List_info==3:
                user_pop=int(input("1.pop by index value\n2.pop at random"))
                if user_pop == 1:
                    ind = int(input("Enter the index value"))
                    list.pop(ind)
                    print(list)
                elif user_pop == 2:
                    list.pop()
                    print(list)

            elif List_info==4:
                remove_list=int(input("Enter the value to remove from list"))
                if remove_list in list:
                    list.remove(remove_list)
                    print(list)
                else:
                    print("The value is not found on the list")

            elif List_info==5:
                insert_list=int(input("Enter the value to add to the list"))
                list.insert(insert_list)
                print(list)

            elif List_info==6:
                list3=cr_list()
                no_of_element_on_list3=int(input("Enter no of values you want to add on list3 :"))
                for i in range(no_of_element_on_list3):
                    list2.append(int(input("Enter the valus of List 3 : ")))
                print(list3)
                print(list)
                print(list + list3)

            elif List_info==7:
                print(list)
                print("Sum of the list")
                print(sum(list))
                
                print("Minimum value in the list")
                print(min(list))

                print("Maximum value in the list")
                print(max(list))

            elif List_info==8:
                print(list)
                count_list=int(input("Enter the value to count on the list : "))
                if count_list in list:
                    print(list.count(count_list))
                else:
                    print("The value doesn't available in the list")
            
            elif List_info==9:
                print(list)
                print("The length of the list")
                print(len(list))

            elif List_info==10:
                print(list)
                list.sort()
                print(list)
            elif List_info==11:
                break


    elif user_input==2:
        tup=cr_tuple()
        sample_li=[]
        no_of_element_on_tuple=int(input("Enter no of values you want to add on tuple :"))
        for i in range(no_of_element_on_tuple):
                sample_li.append(input("Enter the valus of Tuple  : "))
        tup=tuple(sample_li)       
        print(tup)
        while True:
            Tuple_info=int(input("\n1.To know the index value.\n2.To count a particular value in tuple.\n3.Sum/Min/Max\n4.Printing the tuple reverse format\n5.Concatenation of two tuple\n6.Exit\n"))

            if Tuple_info==1:
                tup_check=int(input("Enter the value to find the index value : "))

                if tup_check in tup:
                    print(tup.index(tup_check))
                else:
                    Print("Sry thr value doesn't found on tuple")
                
            elif Tuple_info==2:
                tup_check1=int(input("Enter the value to find the index value : "))

                if tup_check1 in tup:
                    print(tup.count(tup_check1))
                else:
                    print("Sry thr value doesn't found on tuple")

            elif Tuple_info==3:
                print(tup)
                print("Sum of the tuple")
                print(sum(tup))
                
                print("Minimum value in the tuple")
                print(min(tup))

                print("Maximum value in the tuple")
                print(max(tup))

            elif Tuple_info==4:
                print(tup)
                print(tup[::-1])

            elif Tuple_info==5:
                tup1=cr_tuple()
                sample_li1=[]
                no_of_element_on_tuple_1=int(input("Enter no of values you want to add on tuple :"))
                for i in range(no_of_element_on_tuple_1):
                    sample_li1.append(input("Enter the valus of Tuple  : "))
                tup1=tuple(sample_li1)       
                print(tup)
                print(tup1)

                tup3=tup+tup1
                print(tup3)

            elif Tuple_info==6:
                break


    elif user_input==3:
        
        set1=cr_set()
        no_of_element_on_set=int(input("Enter no of values you want to add on set :"))
        for i in range(no_of_element_on_set):
                set1.add(input("Enter the valus of Set : "))
        print(set1)
        while True:
                Set_info=int(input("\n1.Add value on existing set.\n2.To Update a set.\n3.Min/Max\n4.Clearing the set\n5.Copy the set to another\n6.Exit\n"))

                if Set_info == 1:
                    Add_value_on_set=int(input("Enter the no.of.value you want to add on the existing set : "))
                    for i in range(Add_value_on_set):
                        set1.add(int(input("Enter the valus of Set : ")))
                    print(set1)
                        
                elif Set_info == 2:
                    set2=cr_set()
                    no_of_element_on_set_2=int(input("Enter no of values you want to add on set 2 :"))
                    for i in range(no_of_element_on_set_2):
                        set2.add(int(input("Enter the valus of Set 2 : ")))
                    print(set1)
                    print(set2)
                    set1.update(set2)
                    print(set1)

                elif Set_info == 3:
                    print(set1)
                    print(type(set1))
                    #print("Sum of the set")
                    #print(sum(set1))        
                    print("Minimum value in the set")
                    print(min(set1))
                    print("Maximum value in the set")
                    print(max(set1))

                elif Set_info == 4:
                    print(set1)
                    print(type(set1))
                    set1.clear()
                    print(set1)

                elif Set_info == 5:
                    set3=cr_set()
                    print("The values on new set ")
                    print(set3)
                    print("The values on set 1")
                    print(set1)
                    print("printing the values on new set after coping the set 1")
                    set3=set1.copy()
                    print("The values on new set ")
                    print(set3)
                elif Set_info == 6:
                    break

    elif user_input==4:
           
        no_of_element_on_dictionary=int(input("Enter the no.of.entry you want : "))
        
        dict1=cr_dict()

        for i in range(no_of_element_on_dictionary):        
            keys = input("Enter the key : ")
            values = (input("Enter the value : "))
            dict1[keys] = values
        print(dict1)
        while True:
            Dict_info=int(input("\n1.Finding the values using keys.\n2.Adding a vaule on the existing dicitionary.\n3.POP Method\n4.Copy the another dicitionary with the exisiting\n5.Exit\n"))

            if Dict_info == 1:
                id=input("Enter the key value...\n")

                if id in dict1.keys():

                    print(dict1[id])

                else:
                    print("key doesn't exisit on dicitionary..!")

            elif Dict_info == 2:

                key_already=input("Enter the key ...\n")
                value_new=input("Enter the value...\n")
                
                if key_already in dict1.keys():
                    print("Mentioned key is already used")
                else:
                    dict1[key_already]=value_new
                    print(dict1)
            
                    
            elif Dict_info == 3:
                key_pop=input("Enter the key ...\n")
                
                if key_pop in dict1.keys():
                    dict1.pop(key_pop)
                    print(dict1)
                else:
                    print("Mentioned key is not available")

            
            elif Dict_info == 4:

                dict2=cr_dict()
                no_of_element_on_dictionary=int(input("Enter the no.of.entry you want : "))

                for i in range(no_of_element_on_dictionary):        
                    keys = input("Enter the key : ")
                    values = (input("Enter the value : "))
                    dict1[keys] = values
                print(dict1)
                print(dict2)

                dict1.update(dict2)
                print("Updated dicitionary...\n")
                print(dict1)

            elif Dict_info == 5:
                break


    elif user_input==5:
        print("End of the session...!")
        break
