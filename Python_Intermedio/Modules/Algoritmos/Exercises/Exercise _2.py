#Exercise_2
def bubble_sort(sort_list):
    for out_item in range(0,len(sort_list)):
        print(f"Iteration quantity: {len(sort_list)-out_item}")
        change_dectector = False
        # range(inicio, fin, paso)
        # len(mi_lista) - 1 es el último índice
        # -1 para detenerse antes de llegar al índice -1 (es decir, llega hasta el 0)
#        -1 es el salto hacia atrás
        for index in range(len(sort_list)-1,out_item,-1):
            current_item = sort_list[index]
            next_item = sort_list[index-1]
            print(f"Iteration: {out_item}/{index}, actual number is: {current_item}, next left number is {next_item}")
            if current_item < next_item:
                print("the current number is smaller than next number, let's move it to the left...")
                sort_list[index] = next_item
                sort_list[index-1] = current_item
                print(sort_list)
                change_dectector = True
            else:
                print("The current number is not smaller than next number... we are going to check the next number")
        if not change_dectector:
            return
test_list = [40,7,8,50,60,6]
print(test_list)
bubble_sort(test_list)
print(f"This is the ordered list: {test_list}")