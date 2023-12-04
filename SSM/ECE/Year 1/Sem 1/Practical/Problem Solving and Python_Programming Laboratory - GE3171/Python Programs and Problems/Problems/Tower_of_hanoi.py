def hanoi (disks,source,aux,target):
    if(disks == 1):
        print("move disk1 from rod {} to rod {}".format (source, target))
        return
    hanoi(disks-1,source,target,aux)
    print("move disk{} from rod {} to rod {}".format (disks,source, target))
    hanoi(disks-1,aux,source,target)

disks = int(input("Enter number of disks: "))
hanoi(disks,'A','B','C')