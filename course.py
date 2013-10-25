class course(Object):
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

class term(Object):
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

class Scheduler(Object):
    # TODO: pick interface with rest of world; get data in; split out printing
    def __init__(self):
        pass
    def schedule(self):
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
    def print(self):
        pass
