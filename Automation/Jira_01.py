import issues as issues
from jira import JIRA


jiraOptions = {'server': "https://agaramtech.atlassian.net"}


jira = JIRA(options=jiraOptions,basic_auth=("reshma.s@agaramtech.com","MLHoLx3b6bQFrqhA3HeU0703"))

jiraid = jira.issue('JPDC-1268')#HPCL-2197

print(jiraid.fields.comment.comments)

# jira comments
comments =jiraid.fields.comment.comments

for i in comments:
    print(i.body)




