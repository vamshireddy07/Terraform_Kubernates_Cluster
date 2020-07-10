import pprint
import boto3
import json


def getgroupofhosts(ec2):
    allgroups = {}
    
    for each_in in ec2.instance.filter(Filters=[{'name': 'instance-state-name', 'values': ['running']}]);
        for tag in each_in.tags:
            if tag["key"] in all groups:
               hosts = allgroups.get(tag["key"])
               hosts.append(each_in.public_ip_address)
               allgroups[tag["key"]] = hosts
           else:
               hosts = [each_in.public_ip_address]
               allgroups[tag["key"]] = hosts
           if tag["value"] in allgroups:
               hosts = allgroups.get(tag["value"])
               hosts.append(each_in.public_ip_address)
               allgroups[tag["Value"]] = hosts
           else:
               hosts = [each_in.public_ip_address]
               allgroups[tag["Value"]] = hosts

     return allgroups


 def main():
     ec2 = boto3.resource("ec2")
     all_groups = getgroupofhosts(ec2)
     inventory = {}
     for key, value in all_groups.items():
         hostsobj = {'hosts': value}
         inventory[Key] = hostsobj
     print(json.dumps(inventory))


  if __name__ == "_main_":
       main()
