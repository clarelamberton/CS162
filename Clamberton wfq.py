# Input packets as a string, S = Standard, P = Priority, E = Economy
input_packets = [
    "S Mary", "P Deer", "P Dee", "P Dee", "E Eileen",
    "E Mike", "E Joe", "P Dee", "E Vicky", "E George",
    "P Dee", "P Joe", "E Sally", "P Joe", "S Pete",
    "P Dee", "S Bill", "S Chase", "E Price", "P Dee",
    "E Sue"
]

priority_list = []
standard_list = []
economy_list  = []

for x in input_packets:
    if x[0] == "P":
        priority_list.append(x)
    elif x[0] == "E":
        economy_list.append(x)
    elif x[0] == "S":
        standard_list.append(x)

print("START")
print("priority_list:", priority_list)
print("standard_list:", standard_list)
print("economy_list :", economy_list, "\n")

p_flag = s_flag = e_flag = 0   # 0 = not empty yet, 1 = empty

# keep looping until every flag is 1
while p_flag == 0 or s_flag == 0 or e_flag == 0:


    p_counter = -1
    for _ in priority_list[:]:
        p_counter += 1
        if p_counter > 2:
            break
        print(priority_list[0])
        priority_list.pop(0)
    if len(priority_list) == 0:
        p_flag = 1
    print("priority_list:", priority_list, "p_flag:", p_flag, "\n")


    s_counter = -1
    for _ in standard_list[:]:
        s_counter += 1
        if s_counter > 1:
            break
        print(standard_list[0])
        standard_list.pop(0)
    if len(standard_list) == 0:
        s_flag = 1
    print("standard_list:", standard_list, "s_flag:", s_flag, "\n")


    e_counter = -1
    for _ in economy_list[:]:
        e_counter += 1
        if e_counter > 0:
            break
        print(economy_list[0])
        economy_list.pop(0)
    if len(economy_list) == 0:
        e_flag = 1
    print("economy_list :", economy_list, "e_flag:", e_flag, "\n")
