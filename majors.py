#!/usr/bin/env python

"""
All courses available need only ever be enumerated once, and that's here.
"""

# Assume that no class has a higher-numbered class as a prereq... 

#MATH
mth111 = course('mth', 111, [], 4)
mth112 = course('mth', 112, [mth111], 4)
mth251 = course('mth', 251, [mth112], 4)
mth252 = course('mth', 252, [mth251], 4)
mth254 = course('mth', 254, [mth252], 4)
mth306 = course('mth', 306, [mth252], 4)
st314  = course('st',  314, [mth252], 4)

#WRITING
wr121 = course('wr', 121, [], 3)
wr214 = course('wr', 214, [wr121], 3)
wr327 = course('wr', 327, [wr121], 3)

#PHYSICS
ph211 = course('ph', 211, [mth251], 5)
ph212 = course('ph', 212, [mth252, ph211], 5)
ph213 = course('ph', 213, [mth254, ph212], 5)


cs160 = course('cs', 160, [], 4)
cs161 = course('cs', 161, [cs160], 4)
cs162 = course('cs', 162, [cs161], 4)

"""
A major is the basic core of requirements for something.
"""
# schedule_these = (cs160, cs161, cs162)

# schedule_these = [mth111, mth112, mth251, mth252, mth254, mth306, st314,
#                    wr121, wr214, wr327, ph211, ph212, ph213]
pre_cs = []
pro_systems = []
pro_info = []
pro_applied = []

pre_ece = []
pro_ece = []


"""
A schedule consists of which terms you'll be around, and a target number of
credits per term. 
"""

fall11 = term(12, 16, fall, 2011)
winter12 = term(15, 19, winter, 2012)
spring12 = term(10, 13, spring, 2012)

terms_available = (fall11, winter12, spring12)


