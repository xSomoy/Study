def possibleChanges(usernames):
    # Write your code here
    
    ans=[]
    for i in usernames:
        for j in range(0,len(i)-1):
            if(i[j]>i[j+1]):
                ans.append("YES")
                break
        else:
            ans.append("NO")
    return ans