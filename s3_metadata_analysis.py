import json
from datetime import datetime

COST_STANDARD = 0.023

def calculate_unused_days(bucket):
    last_accessed_date = datetime.strptime(bucket["lastAccessed"], "%Y-%m-%d") 

    current_date = datetime.now()

    days_unused = (current_date - last_accessed_date).days
    
    return days_unused

def calculate_bucket_cost(bucket):

    cost = bucket["sizeGB"] * COST_STANDARD

    return cost    

if __name__ == "__main__":  

    with open("buckets.json", "r") as file:
        data = json.load(file)      

    print("\n===== SUMMARY =====\n")    

    for bucket in data["buckets"]:
        print(f"Bucket Name: {bucket['name']}")
        print(f"Region: {bucket['region']}")
        print(f"Size: {bucket['sizeGB']} GB")
        print(f"Versioning: {bucket['versioning']}\n")

    print("===== UNUSED LARGE BUCKETS =====\n")

    current_date = datetime.now()

    for bucket in data["buckets"]:
        days_unused = calculate_unused_days(bucket)

        if days_unused > 90 and bucket["sizeGB"] > 80:

            print(f"Bucket Name: {bucket['name']}")
            print(f"Size: {bucket['sizeGB']} GB")
            print(f"Unused for: {days_unused} days\n")

    print("===== COST REPORT BY REGION =====\n")

    region_costs = {}

    for bucket in data["buckets"]:
        region = bucket["region"]
        cost = calculate_bucket_cost(bucket)

        if region not in region_costs:
            region_costs[region] = 0

        region_costs[region] += cost  

    for region, total_costs in region_costs.items():
        print(f"Bucket Region: {region}")
        print(f"Total Costs: ${total_costs: .2f}\n")

    print("===== COST REPORT BY DEPARTMENT =====\n")

    team_costs = {}

    for bucket in data["buckets"]:
        team = bucket["tags"]["team"]
        cost = calculate_bucket_cost(bucket)

        if team not in team_costs:
            team_costs[team] = 0

        team_costs[team] += cost  

    for team, total_costs in team_costs.items():
        print(f"Department: {team}")
        print(f"Total Costs: ${total_costs: .2f}\n")

    print("===== CLEANUP RECOMMENDATIONS =====\n")

    deletion_queue = []

    for bucket in data["buckets"]:

        days_unused = calculate_unused_days(bucket)

        if bucket["sizeGB"] > 50:
            print(f"Bucket {bucket['name']} needs cleanup recommendation.")

        if bucket["sizeGB"] > 100 and days_unused > 20:
            deletion_queue.append(bucket["name"])
            print(f"Bucket {bucket['name']} added to the deletion queue.")  
        print()      

    print("===== FINAL DELETION QUEUE =====\n")

    for bucket_name in deletion_queue:
        print(f"Bucket to delete: {bucket_name}")

    print("\n===== GLACIER ARCHIVAL RECOMMENDATIONS =====\n")    

    for bucket in data["buckets"]:

        days_unused = calculate_unused_days(bucket)

        if bucket["sizeGB"] > 80 and days_unused > 90:
            print(f"Bucket {bucket['name']} should be moved to Glacier.\n")


