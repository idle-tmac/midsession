
def label(index, item):

    company_name = item['company_name'].strip()
    if company_name == "":
        return
    
    ret = index.query(company_name)
    if len(ret) != 0:
        item["company_level"] = 1
 
