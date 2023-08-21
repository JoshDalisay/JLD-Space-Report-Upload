def ResultsReader():

    clean_list = []
    cleaned_list = []
    with open(r'\\log-s8mo-1fs\groups\IT Support\Windows 10\Scripts\results.txt', 'r') as file_object:
        contents = file_object.read()
        if len(contents) == 0:
            print('No computers are low on storage.')
        else:
            z = contents.replace(",", "").replace("'", "").replace("]", "] ")
            x = z.split("] [")
            for j in x:
                y = j.replace("[", "").replace("]", "")
                clean_list.append(y)

            for h in clean_list:
                q = h.split()
                a = q[0], q[1] + q[2]
                cleaned_list.append(a)

    return(cleaned_list)
