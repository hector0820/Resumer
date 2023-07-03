 
# About the `Rusumer` script

You must set the path of the JSON files to use this script.
This will produce a md file. that you can use in where into a 
github webpage. 

## The JSON struture

### MEJSON file

```json
{
  "myself" : "name",
  "city" : "city",
  "phone" : "number",
  "mail" : "email",
  "summary" : "a brief summary"
}
```

### EXPERIENCEJSON file

```json
[ 
  {
    "place": "business name",
    "job": "position",
    "start": "YYYY-MM-00",
    "end": "YYYY-MM-00",
    "where": "city/country",
    "expertise": [
      "hosting",
      "server administration",
      "linux",
      "ssh"
    ]
  }, ...]
```

### EDUCATIONJSON file

```json
[
  {
    "university": "name",
    "city": "city",
    "degree": "Degree name",
    "course": "what course",
    "start": "YYYY-MM-00",
    "end": "YYYY-MM-00"
  }, ...]
```

### COURSEJSON file

```json
[
  {
    "provider": "coursera",
    "name": "fundamentos de la escritura",
    "date": "2020-05-01",
    "id": "course id",
    "specialization": null,
    "order": null,
    "university": "university name",
    "link": "link of certificate",
    "expertise": [
      ...
    ]
  }, ...]
```

### SKILLJSON file

```json
{ 
  "skills": [
    "excel", "linux", "bash", "data analysis",
    "r", "python", "pandas", "vps servers",
    "ssh", "nginx", "sqlite2", "microsoft office",
    "inferential statistics", "data modeling", "math",
    "statistics", "data science", "java script",
    "retrieve data", "processing data", "html",
    "web scraping", "analytical thinking", "problem-solving",
    "critical thinking", "time management", "public speaking",
    "attention to detail", "good listening", "to lead others",
    "to be able to explain certain topics clearly"
  ]
}
```
