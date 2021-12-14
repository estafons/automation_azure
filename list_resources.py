from os import popen

def get_resources_ids(resource_type):
    '''popen executes cli command ands queries for all ids of type specified.
    -o tsv returns then as new line seperated strings.'''
    out = popen("az resource list --resource-type {} --query [].id -o tsv".format(resource_type), "r")
    with open('resource_ids.txt', 'w') as sf:
        for i in out:
            sf.write(i)

