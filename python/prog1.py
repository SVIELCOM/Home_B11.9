import sys
import json
#from datetime import datetime
#now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
if __name__ == "__main__":
    if len (sys.argv) > 1:
        print (sys.argv[1] * 2)
 #       timestamp = now
        value = sys.argv[1]
        programname = "myprog"
        data = {}
        data['@cee'] = ({
 #           "timestamp" : timestamp,
            "value" : value,
            "programname" : programname
        })
        with open("JOURNAL.json", "w") as write_file:
            json.dump(data, write_file)
    else:
        print ("Integer Parameter required")
