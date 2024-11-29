string = input()

ls = [(int(string[i]), i) for i in range(len(string))]

ls.sort(key=lambda x: x[0])
