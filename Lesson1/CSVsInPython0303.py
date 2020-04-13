import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

#with open(enrollments.csv, 'rb') as f:
#    reader = unicodecsv.DictReader(f)
#    enrollments = list(reader)

#with open(daily_engagement.csv, 'rb') as f:
#    reader = unicodecsv.DictReader(f)
#    daily_engagement = list(reader)
    
#with open(project_submissions.csv, 'rb') as f:
#    reader = unicodecsv.DictReader(f)
#    project_submissions = list(reader)

enrollments= read_csv('enrollments.csv')
daily_engagement= read_csv('daily_engagement.csv')
project_submissions=read_csv('project_submissions.csv')

print(enrollments[0])
print(daily_engagement[0])
print(project_submissions[0])