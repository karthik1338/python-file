def predict(low = 1, high= 100):
    mid = (low +high)//2
    print(mid)
    update = input("update")
    if update == "lower":
        return predict(low, mid-1)
    elif update == "upper":
        return predict(mid+1, high)
    elif update == "yes":
        print("my guss was right")
        return 
    
predict()

