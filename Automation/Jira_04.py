from jira import JIRA

jiraserver = {'server': "https://agaramtech.atlassian.net"}

jira = JIRA(options=jiraserver,basic_auth=("reshma.s@agaramtech.com","MLHoLx3b6bQFrqhA3HeU0703"))

#comment edit
comment = jira.comment('HPCL-2214', '30012')#print(singleIssue.fields.comment.comments) for comments id
comment.update(body = 'the text here will replace the text in the comment')

#Status update
issue = jira.issue('HPCL-2214')
jira.transition_issue(issue, transition='Resolved')#Resolved(Done),Work In Progress,Hold,Rejected

#Update Assignee

jira.issue('HPCL-2214').update({'assignee': {"id": "5f6d8527d33d760077611250"}})
