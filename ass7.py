def parser(con):
    """

    :param con: a content of a file
    :return: list of files's name
    """
    # create empty list
    list_of_links = list()
    list_of = list()
    # open the file and extract into content
    content = open(con)
    # create array of file's names
    lines = content.read().splitlines()
    """""
     this loop will go over the lines to find the address of the next site
    """""
    for line in lines:
        if "href=\"" in line:
            address = line
            new_add = address.split('"')
            """""
             this loop will find all the links in every line
            """""
            for k in new_add:
                if "html" in str(k):
                    list_of_links.append(k)
    return list_of_links


def crawler(con, lis, dic):
    """

    :param con: this is the name of the file the crawler is checking
    :param lis: this is a list of the files that the crawler already saw
    :param dic: this is the dictionary of all the files
    :return: a dictionary with all the addresses
    """
    files_names = list()
    # if the file is already been crawled
    if con in lis:
        return dic
    lis.append(con)
    # get the list of the files
    files_names = parser(con)
    # checks if the list is empty
    if len(files_names) == 0:
        dic[con] = files_names
        return dic
    dic[con] = files_names
    """"
    this loop takes each file from the dictionary and crawls on it
    """""
    for file in dic[con]:
        crawler(file, lis, dic)
    return dic


if __name__ == '__main__':
    source_file = input("enter source file:\n")
    this_list = list()
    list_for_file = list()
    new_list = list()
    this_dic = dict()
    this_dic = crawler(source_file, this_list, this_dic)
    # writing the dictionary into a csv file
    with open("results.csv", "w", newline="") as f:
        """"
         this for loop is dividing the dictionary into a list of tuples of key and value
        """""
        for key_val in this_dic.items():
            key_in_dic = key_val[0]
            """"
            this for loop put together the main file and the files that are in this file
            """""
            for val in key_val[1]:
                key_in_dic += ',' + val
            f.write(key_in_dic)
            f.write("\n")
    new_input = input("enter file name:\n")
    new_list = this_dic.get(new_input)
    new_list.sort()
    print(new_list)
