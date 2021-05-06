our_list = [56, 777, 1213, 24, 797, 43, 12, 23, 100, 55]
str_list = ["banana", "apple", "orange", "pear", "avocado"]
#
# def bubble_sort(un_list):
#     length = len(un_list)-1
#     for num in range(length):
#         change = False
#         for index in range(length-num):
#             # a = un_list[index]
#             if un_list[index] > un_list[index+1]:
#                 un_list[index], un_list[index + 1] = un_list[index + 1], un_list[index]
#                 # un_list[index + 1] = a
#                 change = True
#         print(un_list)
#         if not change:
#             break

#
# bubble_sort(str_list)
#
#
# def selection_sort(un_list):
#     for i in range(len(un_list)):
#         min_num = i
#         for num in range(i + 1, len(un_list)):
#             if un_list[num] < un_list[min_num]:
#                 min_num = num
#         un_list[min_num], un_list[i] = un_list[i], un_list[min_num]
#         print(un_list[min_num])
#         print(un_list[i])
#
#     return un_list
#
#
# selection_sort(our_list)
def merge_sort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist)//2
        left_half = alist[:mid]
        right_half = alist[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i = i + 1
            else:
                alist[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j = j + 1
            k = k + 1

        print("Merging ", alist)

merge_sort(our_list)

# def quick_sort():

