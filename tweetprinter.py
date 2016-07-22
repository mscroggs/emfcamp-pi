def hashtag_tweetprinter():
    results = read_twitter()
    print len(results["statuses"])
    for a in results["statuses"]:
        if a["id"] not in ids and a["text"][:2]!="RT":
            try:
                print_string("\n@" + a["user"]["screen_name"]+"\n"+a["text"]+"\n")
                print("\n@" + a["user"]["screen_name"]+"\n"+a["text"]+"\n")
                ids.append(a["id"])
                if "media" in a["entities"]:
                    print(a["entities"]["media"][0]["media_url"])
                    print_picture(a["entities"]["media"][0]["media_url"])
                break
            except:
                print "failed"
                pass
    
    with open("/home/pi/.emf/ids","w") as f:
        json.dump({"ids":ids},f)
