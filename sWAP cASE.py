def swap_case(s):
    new_str=""
    for item in s:
       if (item == item.lower()):
           new_str += item.upper()
       else:
            new_str += item.lower()
    return new_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
