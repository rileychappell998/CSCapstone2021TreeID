import csv

from django.core.management.base import BaseCommand, CommandError
from treeID.models import TreeDataFinal

#Headers
#['Waypoint', 'Latitude', 'Longitude', 'Alt_ft', 'Tree_ID', 'Zone', 'Tree_Number', 'Group_', 'Leaf_Fall', 'Common_Name', 'Genus', 'Species_Name', 'Family', 'Origin', 'Age_Min', 'Age_Max', 'CBH', 'DBH', 'Tree_Height_ft_min', 'Tree_Height_ft_min', 'Canopy_Radius_ft', 'Root_Zone_Infringement', 'Condition_Class', 'Priority', 'Interest_Houses', 'Trust_Prop', 'Trust_Prop_Address', 'Is_Champion_Tree', 'Is_Memorial_Tree', 'Is_Blue_Mtn_Native', 'Is_Pacific_Slope_Native', 'Staked ', 'Memorial_Tree_person']        
class Command(BaseCommand):
    help = "Import the tree data CSV."
    def handle(self, *args, **options):
        csv_file = open('../New_Whitman_Tree_2020_UTF.csv')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            tree = TreeDataFinal(
                waypoint = row['Waypoint'] or None,
                latitude = row['Latitude'] or None,
                id = row['Tree_ID'] or None,

                )
            tree.save()
            print(tree.id, tree.pk)

