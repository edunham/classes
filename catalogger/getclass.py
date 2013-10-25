import re
import urllib3
from BeautifulSoup import BeautifulSoup
def get_catalog_url(course):
    """
    Takes a string of a course number, like CS311, and turns it into the 
    catalog url

    >>>get_catalog_url(cs311)
    http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=CS&coursenumber=311

    >>>get_catalog_url("ece 112")
    http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=ECE&coursenumber=112

    TODO: Optionally handle looking-up in previous years' catalogs, 
    & find url format for that
    """ 
    subjectcode = re.search(r'[a-zA-Z]+', course).group()
    coursenum = re.search(r'[1-9]+', course).group()
    return "http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode="+subjectcode+"&coursenumber="+coursenum

def get_page_from_web(course):
    """
    Should in theory handle all the urllib3 parts. 
    TODO: handle errors
    """
    http = urllib3.PoolManager()
    req = http.request('GET', get_catalog_url(course))
    if req.data:
        return req.data
    return

def fill_course_infos(course, DEBUG = False):
    """
    Somehow parse relevant information out of the page we downloaded. This
    will probably need to talk directly with the DB. Stuff about course: 
        course_title = ''
        description = ''
        course_code = ''
        terms_offered = []
        taught_by = []
        has_lab = False
        has_recitation = False
        prereqs = []
        ecampus_terms = []

    """
soup=BeautifulSoup(urlopen("http://weather.yahoo.com/").read())
for x in soup.find(attrs={"id":"myLocContainer"}).findAll("li"):
  print x.a["title"], x.em.contents
  
