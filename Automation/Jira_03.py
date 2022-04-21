from jira import JIRA
import issues as issues

jiraserver = {'server': "https://agaramtech.atlassian.net"}

jira = JIRA(options=jiraserver,basic_auth=("reshma.s@agaramtech.com","MLHoLx3b6bQFrqhA3HeU0703"))

issue = jira.issue('HPCL-2220')
f=open('D:\\Resh JPDC\\Resh JPDC\\SS Bugs\\April\\16-04-2021\\Bug1.png', 'rb')

jira.add_attachment(issue=issue, attachment=f)