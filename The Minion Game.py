def minion_game(string):
    saitler=["A","I","O","U","E"]
    Kevin=0
    Stuart=0
    for i in range(len(string)):
        if string[i] in saitler:
            Kevin+=len(string)-i
        else:
            Stuart+=len(string)-i
    if Kevin>Stuart:
            print("Kevin", Kevin)
    elif Kevin<Stuart:
            print("Stuart", Stuart)
    else:
        print("Draw")  
