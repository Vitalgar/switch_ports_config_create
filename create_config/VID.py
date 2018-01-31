a = open('VID.txt', 'r') #

for vid in a.readlines():
    vlan = vid[8:12]   #if first row is number port
#    vlan = vid[1:8]   #if second row is VLANID
    VID = vlan.strip()
#    print("config vlan vlanid " + VID + " add tagged 9-10")
    print("config vlan vlanid " + VID + " delete 9-10")


#bash
#cat VID.txt |awk '{print "config vlan vlanid "$1" add tagged 25-28"}'  #or $2
