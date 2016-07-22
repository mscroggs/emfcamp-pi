def print_string(text):
    from time import strftime
    with open("/home/pi/.temp/text","w") as f:
        f.write(strftime("%Y-%m-%d %H:%M"))
        f.write(text.encode('utf8'))

    import cups
    co = cups.Connection()
    pr = co.getPrinters().keys()[0]
    print co.printFile(pr,'/home/pi/.temp/text',"Hello",{})


def print_picture(url):
    import urllib
    import cups
    co = cups.Connection()
    pr = co.getPrinters().keys()[0]
    urllib.urlretrieve(url,"/home/pi/.temp/pic")
    print co.printFile(pr,"/home/pi/.temp/pic","Hollm",{})
