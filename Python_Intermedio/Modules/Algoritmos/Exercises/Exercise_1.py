#Exercise_1
def bubble_sort(sort_list):
<<<<<<< Updated upstream
    for out_item in range(0,len(sort_list)): # O(1)
        print(f"Iteration quantity: {len(sort_list)-out_item}") #O(1)
        change_dectector = False #O(1)
        for index in range(0,len(sort_list)-1): #O(2)
            current_item = sort_list[index]      
            next_item = sort_list[index+1]
            print(f"Iteration: {out_item}/{index}, actual number is: {current_item}, next number is {next_item}")
            if current_item > next_item:
                print("the current number is major than next number, we should change it...")
                sort_list[index] = next_item
                sort_list[index+1] = current_item
                change_dectector = True
=======
    for out_item in range(0,len(sort_list)):     #O(n)
        print(f"Iteration quantity: {len(sort_list)-out_item}") #O(1)
        change_dectector = False #O(1)
        for index in range(0,len(sort_list)-1):  #O(n²)
            current_item = sort_list[index]      #O(1)
            next_item = sort_list[index+1]       #O(1)
            print(f"Iteration: {out_item}/{index}, actual number is: {current_item}, next number is {next_item}") #O(1)
            if current_item > next_item:         #O(1)
                print("the current number is major than next number, we should change it...") #O(1)
                sort_list[index] = next_item     #O(1)
                sort_list[index+1] = current_item #O(1)
                change_dectector = True           #O(1)
>>>>>>> Stashed changes
            else:
                print("The current number is not major than next number... we are going to check the next number") #O(1)
        if not change_dectector: #O(1)
            return
test_list = [40,7,8,50,60,6]
bubble_sort(test_list)
print(test_list)