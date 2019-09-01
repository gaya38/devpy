class First(object):
    def method1(self):
        print "Executed First class"
class Second(First):
    def method1(self):
        print "Executed Second class"
class Third(First):
    def method1(self):
        print "Executed Third class"
class Fourth(Second,Third):
    def method1(self):
        print "Executed Fourth class"
print "MRO of First class:",(First.mro())
print "MRO of Second class:",(Second.mro())
print "MRO of Third class:",(Third.mro())
print "MRO of Fourth class:",(Fourth.mro())
