

def reverse(data):
    data=list(data)
    # pointing to the first item
    start_index=0;
    #pointing to the last item
    end_index=len(data)-1;

    while end_index>=start_index:
        # Keep swapping the items
     data[start_index], data[end_index] = data[end_index],data[start_index]
     start_index=start_index+1
     end_index=end_index-1

     return ''.join(data)

def isPalindrome(data):
    return data==reverse(data)

if __name__ == '__main__':

    print( isPalindrome('amal'))





