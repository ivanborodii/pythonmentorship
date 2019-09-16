import xml.etree.ElementTree as e

def main():
    tree=e.parse(r'mondial-3.0.xml')                              # parsing xml file
    tags=tree.findall('country')                                  # find all tags with attributes where tag = country
    a = task_1(tags)
    b = task_2(tags)
    print('RESULT OF TASK 1:')
    print(a)
    print('')
    print('RESULT OF TASK 2:')
    print(b)

def task_1(tags):
    list_1 = []
    for tag in tags:
        if tag.attrib['government'] not in list_1:               # if government attribute is not found in result list
            list_1.append(tag.attrib['government'].strip())      # then append item to this list
    return list_1

def task_2(tags):
    list_2 = []
    for tag in tags:
        if tag.attrib['government'] not in list_2:                # if government attribute is not found in result list
            if len(tag.attrib['name'].split())>1:                 # if count of words in country name more than 1
                list_2.append(tag.attrib['government'].strip())   # then append item to this list
    return list_2

if __name__=='__main__':
    main()