#recursive approach

def tower_of_hanoi(n, source, destination_rod, helper_rod):
    if n == 1:
        print(f"Disk 1 moved from {source} to {destination_rod}")
        return
    tower_of_hanoi(n-1, source, helper_rod, destination_rod)
    print(f"Disk {n} moved from {source} to {destination_rod}")
    tower_of_hanoi(n-1, helper_rod, destination_rod, source)

tower_of_hanoi(3, "A", "C", "B")    