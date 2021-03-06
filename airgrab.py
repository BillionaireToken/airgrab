# Airgrab cross-reference script
# By gluedog

import csv

def getlists(airgrabbers_txt, already_grabbed_txt):

    with open (airgrabbers_txt) as file:
        names_list = file.readlines()

    strip_names_list = []
    strip_already_grabbed = []

    for name in names_list:
        strip_names_list.append(name.strip("\n"))

    del names_list

    with open (already_grabbed_txt) as file:
        already_grabbed  = file.readlines()

    for name in already_grabbed:
        strip_already_grabbed.append(name.strip("\n"))

    del already_grabbed


    return strip_names_list, strip_already_grabbed

def csv_crossreference(names_list, already_grabbed):
    csv_dictionary = {}
    legit_grabbers = {}
    total = 0

    with open('20190119_account_snapshot.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if ( (float(row['total_eos']) >= 100.0) and (row['account_name'].startswith("eosio.") == False) and (row['account_name'] != "b1")):
                csv_dictionary[row['account_name']] = float(row['total_eos'])

    print csv_dictionary

    for name in names_list:
        if (name in csv_dictionary) and (name not in already_grabbed):
            print name,"found in csv_dictionary with",csv_dictionary[name],"eos"
            legit_grabbers[name] = csv_dictionary[name]
        else:
            print name,"not found in csv_dictionary or is already grabbed."

    for grabber in legit_grabbers:
        #print grabber, "will receive", legit_grabbers[grabber] * 0.00122, "XBL"
        print "cleosm push action billionairet issue \'{\"to\":\""+grabber+"\",\"quantity\":\""+str("{0:.4f}".format(legit_grabbers[grabber] * 0.00122))+" XBL\",\"memo\":\"Congratulations! You are a Billionaire! https://BillionaireToken.com\"}\' -p billionairet@active"
        #print "cleosm push action billionairet setgrabbed [\""+grabber+"\"] -p billionairet@active"
        total += legit_grabbers[grabber] * 0.00122

    print "A total of",total,"XBL will be distributed to",len(legit_grabbers), "users."

    # cleosm push action billionairet issue '{"to":"accountnum11","quantity":"100.0000 XBL","memo":"Congratulations! You are a Billionaire!"}' -p billionaire@active
    # cleosm push action billionairet setgrabbed ["accountnum11"] -p billionairet@active





def main():
    names_list, already_grabbed = getlists("grabbers.txt", "already_grabbed.txt")
    csv_crossreference(names_list, already_grabbed)

if __name__ == '__main__':
    main()
