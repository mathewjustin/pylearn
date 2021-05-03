#Design a program which reverse an array without using extra memory
#Swap first and end, second and second last..until start and end index are equal

def reverse(nums):
    # pointing to the first item
    start_index=0;
    #pointing to the last item
    end_index=len(nums)-1;

    while end_index>=start_index:
        # Keep swapping the items
     nums[start_index], nums[end_index] = nums[end_index],nums[start_index]
     start_index=start_index+1
     end_index=end_index-1

if __name__ == '__main__':

    n = [1 , 2 , 3, 4]
    reverse(n)
    print(n)





