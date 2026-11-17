
def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1  
        elif mid_number > query:
            lo = mid + 1
    
    return -1
#All test will pass except the one which has multiple query location thus we need to wtite with the helper function

def failed_test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, ", mid_number:", mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    
    while lo <= hi:
        print("lo:", lo, ", hi:", hi)
        mid = (lo + hi) // 2
        result = failed_test_location(cards, query, mid)
        
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

# Now all the test cases will pass with 0.05 sec as the time complexity. 

