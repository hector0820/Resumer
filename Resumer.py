import os
import json

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

	education_info = "\n".join(education_info)
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
		experience_list.append("{}\n{}\n{}\n{} - {}\nRelevant Skills:\n{}".format(job, place, where, start, end, skills))
	experience_list = "\n".join(experience_list)
	return experience_list

def courses_info(courses):
	course_info = list()

	for i in courses:
		name = "**" + i["name"].capitalize() + "**"
		university = "_" + i["university"].capitalize() + "_"
		date = DateMY(i["date"])
		skills = "Relevant skills: " + ", ".join(e.capitalize() for e in i["expertise"])
		course_info.append("{}\n{}, {}\n{}\n\n".format(name, university, date, skills))

	course_info = "\n".join(course_info)
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