def pair(arr,value):
    for i in range(len(arr)- 1):
        for j in range(i+1,len(arr)):
            if arr[i] +arr[j]==value:
                print("pair found",(arr[i],arr[j]))


if __name__=="__main__":
    arr=[1,21,3,14,5,60,7,6]
    value = 27

    pair(arr,value)
