import csv

from django.core.management.base import BaseCommand, CommandError
from treeID.models import TreeDataFinal

#Headers:
#['Waypoint', 'Latitude', 'Longitude', 'Alt_ft', 'Tree_ID', 'Zone', 'Tree_Number', 'Group_', 'Leaf_Fall', 'Common_Name', 'Genus', 'Species_Name', 'Family', 'Origin', 'Age_Min', 'Age_Max', 'CBH', 'DBH', 'Tree_Height_ft_min', 'Tree_Height_ft_min', 'Canopy_Radius_ft', 'Root_Zone_Infringement', 'Condition_Class', 'Priority', 'Interest_Houses', 'Trust_Prop', 'Trust_Prop_Address', 'Is_Champion_Tree', 'Is_Memorial_Tree', 'Is_Blue_Mtn_Native', 'Is_Pacific_Slope_Native', 'Staked ', 'Memorial_Tree_person']        
#This script opens the .csv file 
class Command(BaseCommand):
    help = "Import the tree data CSV."
    def handle(self, *args, **options):
        csv_file = open('../New_Whitman_Tree_2020_UTF.csv')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            tree = TreeDataFinal(
                waypoint = row['Waypoint'] or None,
                latitude = row['Latitude'] or None,
                longitude = row['Longitude'] or None,
                altitude = row['Alt_ft'] or None,
                id = row['Tree_ID'] or None,
                zone  = row['Zone'] or None,
                number = row['Tree_Number'] or None,
                group_field = row['Group_'] or None,
                leaf_fall = row['Leaf_Fall'] or None,
                name = row['Common_Name'] or None,
                genus = row['Genus'] or None,
                species_name = row['Species_Name'] or None,
                family = row['Family'] or None,
                origin = row['Origin'] or None,
                age_min = row['Age_Min'] or None,
                age_max = row['Age_Max'] or None,
                cbh = row['CBH'] or None,
                dbh = row['DBH'] or None,
                height_min = row['Tree_Height_ft_min'] or None,
                height_max = row['Tree_Height_ft_max'] or None,
                canopy_radius = row['Canopy_Radius_ft'] or None,
                root_zone_infringement = row['Root_Zone_Infringement'] or None,
                condition = row['Condition_Class'] or None,
                priority = row['Priority'] or None,
                interest_house = row['Interest_Houses'] or None,
                trust_property = row['Trust_Prop'] or None,
                trust_property_address = row['Trust_Prop_Address'] or None,
                is_champion = (True if row["Is_Champion_Tree"] == "1" else False ) or None,
                is_memorial = (True if row["Is_Memorial_Tree"] == "1" else False ) or None,
                is_blue_mtn_native = (True if row["Is_Blue_Mtn_Native"] == "1" else False ) or None,
                is_pacific_slope_native = (True if row["Is_Pacific_Slope_Native"] == "1" else False ) or None,
                staked = row['Staked '] or None,
                memorial_person = row['Memorial_Tree_person'] or None,
                )
            tree.save()
            print(tree.id)

