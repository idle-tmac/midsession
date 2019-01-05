def checksum(item):
    tmp = {}
    for field in item:
        if item[field] in  ("NULL", None):
            continue
        tmp[field] = item[field]

        #other checksum



        #return False, {}
    return True, tmp
 
