import json

# Open and load the JSON file
with open("sample-data.json") as f:
    data = json.load(f)

# Print header
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<6} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("{:<50} {:<20} {:<6} {:<6}".format("-" * 50, "-" * 20, "-" * 6, "-" * 6))

# Loop through each interface and print its details
for item in data["imdata"]:
    # Adjust keys as necessary based on your JSON structure
    attr = item["l1PhysIf"]["attributes"]
    dn = attr.get("dn", "")
    descr = attr.get("descr", "")
    speed = attr.get("speed", "")
    mtu = attr.get("mtu", "")
    print("{:<50} {:<20} {:<6} {:<6}".format(dn, descr, speed, mtu))
