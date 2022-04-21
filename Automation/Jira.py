from jira import JIRA

jiraserver = {'server': "https://agaramtech.atlassian.net"}

# API token generation: settings->Atlassian acct settings->security->create&manage API tokens->create API token->any name->create
jira = JIRA(options={"server":'https://agaramtech.atlassian.net'}, basic_auth=("reshma.s@agaramtech.com", "qitp1a97T9L7d3x8L3Ml6126"))

jira.create_issue(fields={'project': {'key': 'JPDC'},'issuetype': {"name": "Bug" },'summary': 'test JIRA','description': 'Test Description','assignee':'Reshma S','labels':['Sample_Registration'],'priority':{'name':'Highest'},'versions':[{'name':'JPDC 8.1.0 beta 14 U02'}],'duedate': '2022-03-22','fixVersions':[{'name': 'JPDC 8.1.0 beta 14 U02'}]})

jiraid=jira.issue('JPDC-705')
print(jiraid.fields.reporter)
print(type(jiraid.fields.assignee))

