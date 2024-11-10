def input_file(txt):
    dict = {}
    with open(txt, 'r') as file:
        for i in file:
            x = i.split()
            node = x[0]
            #print(node)
            heru = int(x[1])
            #print(heru)
            lst_data = []
            for i in range(2, len(x), 2):
                child = x[i]
                dist = int(x[i + 1])
                lst_data.append((child, dist))
            dict[node] = {
                "heru": heru,
                "lst_data": lst_data
            }
            #print(lst_data)
    return dict

#print(input_file(r"C:\Users\prith\Downloads\Lab 1\Inputfile.txt"))




def algorithm_part(dict, start, end):
    lst_data_2 = [(0 + dict[start]["heru"], start, 0, [start])]
    vst = {}
    while lst_data_2:
        f, current_node, g, path = lst_data_2.pop(0)

        if current_node == end:
            return path, g
        for child, dist in dict[current_node]["lst_data"]:

            g_new = g + dist
            heru_new = dict[child]["heru"]
            f_new = g_new + heru_new


            if child not in vst or g_new < vst[child]:
                vst[child] = g_new

                lst_data_2.append((f_new, child, g_new, path + [child]))


        lst_data_2.sort(key=lambda x: x[0])
    # print(lst_data_2)  
    return "NO PATH FOUND"




def run_code():
    txt = r"E:\All Search Algorithm\Inputfile.txt"
    dict = input_file(txt)

    start = input("Start node: ").strip()

    end = input("Destination: ").strip()

    path, total_dist = algorithm_part(dict, start, end)


    if path == "NO PATH FOUND":
        print("NO PATH FOUND")

    else:
        print("Path:", " ---> ".join(path))
        print(f"Total distance: {total_dist} KM")




if __name__ == "__main__":
    run_code()
