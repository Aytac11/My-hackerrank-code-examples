def count_substring(string, sub_string):
    count=0
    j=len(sub_string)
    for i in range(0,len(string)):
            if string[i:i+j]==sub_string:
                count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)