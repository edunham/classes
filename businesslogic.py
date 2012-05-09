class course:
    def __init__(self, subject, number, prereqs, credits):
        self.subject = subject
        self.number = number
        self.priority = 1
        self.prereqs = prereqs
        self.credits = credits
        self.terms = [fall, winter, spring]
    def display(self):
        print(self.subject + str(self.number) + " for " + str(self.credits) +" credits with weight "+str(self.priority)+ " \n")
    def weight(self, num):
        w = self.priority
        self.priority = w+num
        print "i am "+self.subject+str(self.number)+" and my initial weight is "+str(self.priority)+"\n"
        for c in self.prereqs:
            c.weight(self.priority)
    def get_weight(self):
        return self.priority

class term:
    def __init__(self, cr_min, cr_max, season, year):
        self.classes = []
        self.cr_min = cr_min
        self.cr_max = cr_max
        self.season = season
        self.year = year
        self.cr_sum = 0
    def can_take(self, course):
        if (self.season in course.terms) and (self.cr_sum+course.credits<=self.cr_max):
            for p in course.prereqs:
                if (p in ranked_courses) or (p in self.classes):
                    return False
            return True
        return False
    def schedule(self, course):
        self.classes.append(course)
        self.cr_sum = self.cr_sum + course.credits

fall11 = term(12, 16, fall, 2011)
winter12 = term(15, 19, winter, 2012)
spring12 = term(10, 13, spring, 2012)

terms_available = (fall11, winter12, spring12)

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

# schedule_these = (cs160, cs161, cs162)

schedule_these = [mth111, mth112, mth251, mth252, mth254, mth306, st314,
                    wr121, wr214, wr327, ph211, ph212, ph213]


# WEIGHTING
heaviest = 0
i = len(schedule_these)-1
print "i= "+str(i)+"\n"
while(i>=0):
    schedule_these[i].display()
    schedule_these[i].weight(0)

    if schedule_these[i].priority > heaviest:
        heaviest = schedule_these[i].priority

    i=i-1
    
print("---------------------------\n")
for c in schedule_these:
    c.display()

# SORTING... there's probably a more Pythonic way to do this
j = len(schedule_these)-1
ranked_courses = []
while (j>=0):
    for c in schedule_these:
        if c.priority == heaviest:
            ranked_course.append(c)
            heaviest = heaviest-1

#SCHEDULING

for t in terms_available: 
    for c in ranked_courses: 
        if t.can_take(c):
            t.schedule(c)
            ranked_courses.remove(c)
        if t.credit_sum==t.credit_max:
            break
