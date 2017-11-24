'''
 Copyright © 2017 kohei YAMADA
'''

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

    # Trigger
    trigger_dumps = json.dumps(message['Trigger'])
    trigger = json.loads(trigger_dumps)

    # Slack
    url = os.environ['SLACK_WEBHOOK_URL']
    slack = slackweb.Slack(url=url)

    text = u"%s     %s \
		\n `%s` で `%s` を検知しました。 \
		\n> *Description：* %s \
		\n> *AWSAccountId：* %s \
		\n> *StateChangeTime：* %s \
		\n> *Region：* %s \
		\n> *MetricName：* %s \
		\n> *FunctionName：* %s "\
		 % \
		( \
			sns['Timestamp'], \
			sns['TopicArn'], \
			message['AlarmName'], \
			message['NewStateValue'], \
			message['AlarmDescription'], \
			message['AWSAccountId'], \
			message['StateChangeTime'], \
			message['Region'], \
			trigger['MetricName'], \
			trigger['Dimensions'][0]['value'] \
		)
    slack.notify(text=text)

    return { 
        'message' : text
    }  
