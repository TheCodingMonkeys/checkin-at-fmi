import urllib2

FMI_LIBRARY_URL = "http://zala100.sofiapubcrawl.com/API.php"


def getBookForId(book_id):
    url = urllib2.Request(FMI_LIBRARY_URL + '?code=' + str(book_id))
    try:
        request = urllib2.urlopen(url)
    except urllib2.HTTPError, e:
        return False
        
    return request
