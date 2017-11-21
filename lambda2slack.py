import slackweb
import json

def lambda_handler(event, context):
    message_dumps = json.dumps(event['Records'][0]['Sns']['Message'])
    message_loads = json.loads(message_dumps)
    message = json.loads(message_loads)

    AlarmName = message['AlarmName']
    NewStateValue = message['NewStateValue']
    StateChangeTime = message['StateChangeTime']
    Region = message['Region']
    Trigger = json.dumps(message['Trigger'])
    MetricName = json.loads(Trigger)['MetricName']
    Dimensions = json.loads(Trigger)['Dimensions']

    text = u"`%s` で `%s` を検知しました。\n\n 内容\n ```\n StateChangeTime：%s\n Region：%s\n MetricName：%s\n FunctionName：%s ```\n" % (AlarmName, NewStateValue, StateChangeTime, Region, MetricName, Dimensions[0]['value'])

    slack = slackweb.Slack(url="https://hooks.slack.com/services/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")

#    slack.notify(text="This is a *test* from lambda2slack.", channel="#coffee", username="coffee-bot", icon_emoji=":coffee", mrkdwn=True)

    slack.notify(text=text)

    return { 
        'message' : text
    }  
