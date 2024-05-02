import json
import os
statsFolder = "C:/Users/payto/Downloads/stats" # Be sure to update this to wherever the new stats folder is

files = os.listdir(statsFolder)

statsData = []
user = []

for file_name in files: # Go through every folder, and build the arrays to store the json files that store stats data
    statsData.append(json.load(open(f"{statsFolder}/{file_name}","r")))
    user.append(file_name[0:-5]) # The uuid of each player is stored in the file name, so I remove the '.json' at the end

def boardBuild(category, subfield, option = 0):
    """The function that builds the leaderboard. Use option 0 for No restrictions, 1 to include Carpet bots, and 2 to only include Players
    Outputs parallel arrays, one for the user, and one for the value"""
    boardVal = []
    userVal = []
    for i in range(len(statsData)):
        CurrentUser, restriction = GetUsername(user[i])
        if restriction < option:
            continue
        val = 0
        try:  # Some values are not defined for some players, trying to access them will error.
            val = statsData[i]['stats']["minecraft:"+category]["minecraft:"+subfield]
            if val == 0:  # Don't include players who don't have a statistic here yet
                continue
        except:
            continue
        boardVal.append(val)
        userVal.append(CurrentUser)
    if len(boardVal) == 0:
        raise Exception("Input invalid or statistic empty. Please try again")
    return bubblesort(boardVal,userVal)

def GetUsername(uuid):
    """Converts a given uuid to a username, using a bunch of dictionaries.
    There are 3 types of players here, the real players, bots that we use to do automatic tasks, and some bots that don't yet have a username attached for irrevalant reasons.
    This function returns the type of player represented as an int, to be sorted out as desired, as well as the username.
    """
    uuids = {'018162fe-5669-4f48-9085-ae8d0e169895':'GraveGecko','284fc0cc-20c6-47ab-b889-b2fff388678c':'TacoDelMar314','2dc8f6e3-e2ee-4e02-ac54-73c0043c0cfa':'NightWolfFur','489b83e2-c484-4dba-b938-4d19cc2601fc':'IcEstr0m','4a4e4171-a820-4309-9457-131b7cd518db':'GameChosen','5318817c-f73b-4d30-9067-f11b1f987053':'Crafty1472','82b62d65-bae7-4687-9f93-f27882175160':'BRIX_','c43b71fc-a18d-40ec-91f8-485b91c368e5':'cobbleminort','c4c42072-7e71-411e-afc7-07cae8d14ac7':'TardotZ','c6df27ee-75a5-4084-916f-36dc10dc1d08':'steve3141592653','cde3d1bc-ffbc-4e44-85b3-ab60016319c7':'TinierTea','d0e0aac2-cff5-4c34-8d3d-a556037c70dd':'BlockyVideogameC','f9cab4e9-b813-4d17-b7ca-2c4b4c8aa4a8':'Neo_Arcu'}
    carpets = {'26dd0066-6501-49e8-91b5-febedde19041':'Quackity','4d9bc813-630d-4db3-8f07-5ab891dd2880':'Obby1',"52ea9354-99ed-4b06-bec2-331e7c0f6f57":'ilmango','5529ca06-71ce-4936-9c48-5cd0e55ed3b6':'Wisp','93b459be-ce4f-4700-b457-c1aa91b3b687':'Etho','a51a8da4-85f8-4e82-b05e-675c26e1de4e':'gnembon','b876ec32-e396-476b-a115-8438d83c67d4':'Technoblade','d6ebd3e3-c0ef-4e5a-80db-6ee537115a17':'WilburSoot','ec70bcaf-702f-4bb8-b48d-276fa52a780c':'Dream','ff5273fa-22b6-4d42-b977-fe6f268045b9':'bread'}
    blanks = ['2aef9ede-35dc-3d95-a068-9b41ba59e267','2f8e620f-b0d3-3c7f-b3ea-38c2333e6837','38be6fb5-cd4b-3e7b-bc74-4ffc99cdfaef','45b4f52a-0b89-3b42-8bfb-0380181075c3','7eb10223-ec02-3b1c-a456-ac3e0dad3fc4']
    if uuid in uuids:
        return uuids[uuid], 2
    elif uuid in carpets:
        return "Bot - " + carpets[uuid], 1
    elif uuid in blanks:
        return "Known blank", 0
    else:
        return uuid, 0

def bubblesort(list1, list2):
    """Inputs two parallel arrays, and sorts by the first one, while keeping the arrays parallel. Sorts into descending order by the first list"""
    for i in range (len(list1)):
        swapped = False
        for j in range(0,len(list1)-i-1):
            if list1[j] < list1[j+1]:
                swapped = True
                list1[j], list1[j+1] = list1[j+1], list1[j]
                list2[j], list2[j+1] = list2[j+1], list2[j]
        if not swapped:
            break
    return list1, list2

