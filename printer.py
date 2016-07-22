def print_string(text):
    from time import strftime
    with open("/home/pi/.emf/text","w") as f:
        f.write(strftime("%Y-%m-%d %H:%M"))
        f.write(text.encode('utf8'))

    import cups
    co = cups.Connection()
    pr = co.getPrinters().keys()[0]
    print co.printFile(pr,'/home/pi/.emf/text',"Hello",{})


def print_picture(url):
    import urllib
    import cups
    co = cups.Connection()
    pr = co.getPrinters().keys()[0]
    urllib.urlretrieve(url,"/home/pi/.emf/pic")
    print co.printFile(pr,"/home/pi/.emf/pic","Hollm",{})
