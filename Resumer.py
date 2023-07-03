import os
import json

# You must set the path of the following 
# JSON files to use this script.

# The JSON struture

## MEJSON
## {
##   "myself" : "name",
##   "city" : "city",
##   "phone" : "number",
##   "mail" : "email",
##   "summary" : "a brief summary"
## }

## EXPERIENCEJSON
## [ 
##   {
##      "place": "business name",
##      "job": "position",
##      "start": "YYYY-MM-01",
##      "end": "YYYY-MM-01",
##      "where": "city/country",
##      "expertise": [
## 	    	"hosting",
## 	    	"server administration",
## 	    	"linux",
## 	    	"ssh"
## 		]
##   }, ...]

## EDUCATIONJSON
## [
##   {
##      "university": "name",
##      "city": "city",
##      "degree": "Degree name",
##      "course": "what course",
##      "start": "YYYY-MM-01",
##      "end": "YYYY-MM-01"
##   }, ...]

## COURSEJSON
## [
##   {
##      "provider": "coursera",
##      "name": "fundamentos de la escritura",
##      "date": "2021-05-01",
##      "id": "course id",
##      "specialization": null,
##      "order": null,
##      "university": "university name",
##      "link": "link of certificate",
##      "expertise": [
##		  ...
##      ]
##   }, ...]

## SKILLJSON
## { 
##   "skills": [
##     "excel", "linux", "bash", "data analysis",
##     "r", "python", "pandas", "vps servers",
##     "ssh", "nginx", "sqlite3", "microsoft office",
##     "inferential statistics", "data modeling", "math",
##     "statistics", "data science", "java script",
##     "retrieve data", "processing data", "html",
##     "web scraping", "analytical thinking", "problem-solving",
##     "critical thinking", "time management", "public speaking",
##     "attention to detail", "good listening", "to lead others",
##     "to be able to explain certain topics clearly"
##   ]
## }

about = os.environ["MEJSON"]
experience = os.environ["EXPERIENCEJSON"]
education = os.environ["EDUCATIONJSON"]
courses = os.environ["COURSESJSON"]
skills = os.environ["SKILLSJSON"]

def DateMY(date):
	month = [
		'January',
		'February',
		'March',
		'April',
		'May',
		'June',
		'July',
		'August',
		'September',
		'October',
		'November',
		'December'
		]
	DateCourse = date.split("-")
	month = month[int(DateCourse[1]) - 1]
	return "{} {}".format(month, DateCourse[0])

def header(about):
	header = "# {}\n{} | {} | {}".format(about["myself"], about["city"], about["phone"], about["mail"])
	summary = "\n\n## Summary\n\n***\n\n{}".format(about["summary"])
	return header + summary

def education_info(education):
	education_info = list()

	for i in education:
		name = i["university"].capitalize()
		name = " ".join([ j.capitalize() for j in name.split() ])
		city = i["city"].capitalize()
		start = DateMY(i["start"])
		end = DateMY(i["end"])
		degree = i["degree"]
		course = i["course"].capitalize()

		if degree == "bachelors":
			education_info.append("{}, {} - {}\nBachelor's degree in {}\n".format(name, start, end, course)) 
		else:
			education_info.append("{}, {} - {}\n{}\n".format(name, start, end, course)) 


	education_info = "\n\n## Education\n\n***\n\n" + "\n".join(education_info)
	return education_info

def experience_info(experience):
	experience_list = list()
	for i in experience:
		place = i["place"].upper()
		job = " ".join([j.capitalize() for j in i["job"].split()])
		start = DateMY(i["start"])
		if i["end"] == None:
			end = "Current"
		else:
			end = DateMY(i["end"])
		where = i["where"].capitalize()
		skills =  "".join(["- "+j.capitalize() +"\n" for j in i["expertise"]])
		experience_list.append("{}\n{}\n{}\n{} - {}\nRelevant Skills:\n{}\n".format(job, place, where, start, end, skills))
	experience_list = "".join(experience_list)
	return experience_list

def courses_info(courses):
	course_info = list()

	for i in courses:
		name = "**" + i["name"].capitalize() + "**"
		university = "_" + i["university"].capitalize() + "_"
		date = DateMY(i["date"])
		skills = "Relevant skills: " + ", ".join(e.capitalize() for e in i["expertise"])
		course_info.append("{}\n{}, {}\n{}\n\n".format(name, university, date, skills))

	course_info = "## Certifications\n\n***\n\n" + "\n".join(course_info)
	return course_info

def skills_info(skills):
	skills = ["- " + j.capitalize() for j in skills["skills"]]
	skills = "\n".join(skills)
	skills = "## Skills\n\n***\n\n" + skills
	return skills


with open(about, "r") as file:
    about = json.load(file)

with open(education, "r") as education:
    education = json.load(education)

with open(experience, "r") as experience:
    experience = json.load(experience)

with open(courses, "r") as courses:
    courses = json.load(courses)

with open(skills, "r") as skills:
    skills = json.load(skills)


with open("test.md", "w") as file:
   file.write(header(about))
   file.write(education_info(education))
   file.write(experience_info(experience))
   file.write(courses_info(courses))
   file.write(skills_info(skills))