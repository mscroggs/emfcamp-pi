from printer import print_string
from printer import print_picture

def hashtag_tweetprinter():
    import json
    results = read_twitter()
    with open("/home/pi/.emf/ids") as f:
        ids = json.load(f)["ids"]
    
    print len(results["statuses"])
    for a in results["statuses"]:
        if a["id"] not in ids and a["text"][:2]!="RT":
#            try:
                print_string("\n@" + a["user"]["screen_name"]+"\n"+a["text"]+"\n")
                print("\n@" + a["user"]["screen_name"]+"\n"+a["text"]+"\n")
                ids.append(a["id"])
                if "media" in a["entities"]:
                    print(a["entities"]["media"][0]["media_url"])
                    print_picture(a["entities"]["media"][0]["media_url"])
                break
 #           except:
  #              print "failed"
   #             pass
    
    with open("/home/pi/.emf/ids","w") as f:
        json.dump({"ids":ids},f)

def read_twitter():
    import twitter
    config = {}
    execfile("/home/pi/emfcamp-pi/config.py", config)
    twox = twitter.Twitter(
            auth = twitter.OAuth(config["access_key"],
                                 config["access_secret"],
                                 config["consumer_key"],
                                 config["consumer_secret"]))
    results = twox.search.tweets(q="#tweetprinter")
    return results
