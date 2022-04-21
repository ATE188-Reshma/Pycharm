from jira import JIRA

jiraserver = {'server': "https://agaramtech.atlassian.net"}

jira = JIRA(options=jiraserver,basic_auth=("reshma.s@agaramtech.com","MLHoLx3b6bQFrqhA3HeU0703"))

# Assignee
jira.create_issue(fields={'project': {'key': 'HPCL'},'issuetype': {"name": "Bug" },'customfield_10027': "2022-03-20","customfield_10020": 391,'summary': 'test JIRA','description': 'Test Description',"assignee": {"id": "62273bd915521d00726d8fbb"},'labels':['Sample_Registration'],'priority':{'name':'Highest'},'versions':[{'name':'HPCL 8.7.0.6 beta 03'}],'duedate': '2022-03-22','fixVersions':[{'name': 'HPCL 8.7.0.6 beta 03'}]})
