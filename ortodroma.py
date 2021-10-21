from math import *

def ortodroma(s1,d1,s2,d2):
	return acos(sin(s1*pi/180)*sin(s2*pi/180)+cos(s1*pi/180)*cos(s2*pi/180)*cos((d2-d1)*pi/180))*180./pi*60.*1852.

s1=51.854840917528385
d1=19.426153228357965
s2=54.79873234021444
d2=18.40083563249519

D = ortodroma(s1,d1,s2,d2)
print(str(D))