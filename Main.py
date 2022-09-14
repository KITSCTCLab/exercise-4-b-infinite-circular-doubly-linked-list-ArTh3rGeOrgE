# Read an integer that denotes the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))
# Write your code here
Original_List = []
count = 0
while len(Original_list) < length_of_circular_linked_list and count < len(circular_linked_list)
  ele = circular_linked_list[count]
  if ele not in Orignal_list:
    Original_list.append(ele)
   count +=1
 
print(len(Orignal_list)
print(" ".join(str(num) for num in Original_list))
