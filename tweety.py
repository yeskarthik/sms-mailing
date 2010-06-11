
import urllib

#tweet=str(raw_input("Enter Tweet :"))


tweet=" Hey!! Guess wat? I am tweeting thro Python! @senthilnayagam @sarang05 @vigneshraju @srnyaxz"

constring="http://internatrails:mambalam@twitter.com/statuses/update.json"

tweety=urllib.urlencode({'status':tweet})
f=urllib.urlopen(constring,tweety)
print f.read()
print "Tweeted :)"

