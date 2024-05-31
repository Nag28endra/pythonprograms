def TowerOfHanoi(disks,start=1,end=3):
    if disks:
        TowerOfHanoi(disks-1,start,6-start-end)
        print(f"move disk-{disks} from peg {start} to peg {end}")
        TowerOfHanoi(disks-1,6-start-end,end)

TowerOfHanoi(disks=4)