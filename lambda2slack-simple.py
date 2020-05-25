import slackweb
import json
import os

def lambda_handler(event, context):

    # SNS
    sns_dumps = json.dumps(event['Records'][0]['Sns'])
    sns = json.loads(sns_dumps)

    # Message
    message_loads = json.loads(sns_dumps)['Message']
    message = json.loads(message_loads)

    # Slack
    url = os.environ['SLACK_WEBHOOK_URL']
    slack = slackweb.Slack(url=url)

    text = sns['Message']
    slack.notify(text=text)

    return { 
        'message' : text
    }  


