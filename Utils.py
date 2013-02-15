def read_file(filename):
    myfile = open(filename,"r")
    content = myfile.read()
    myfile.close()
    return content


