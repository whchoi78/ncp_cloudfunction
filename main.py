import json
import logging
import os

from base64 import b64decode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def main(args):

    # 슬랙 api 지정
    HOOK_URL = "import slack WEB_HOOK"
    # 슬랙 채널 입력
    SLACK_CHANNEL = "import channel name"

    # api 요청
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 응답 받은 값 정의
    alarm_name = args.get("ruleId", "Infra Notice")
    level = args.get("level", "Info")
    instanceName = args.get("instanceName", "instanceName")
    condition = args.get("condition", "condition")
    value = args.get("value", "value")
    # 슬렉 메시지 정의
    slack_message = {
        'channel': SLACK_CHANNEL,
        'text': "From CloudFunction \n alarm_name  : %s, \n level : %s \n InstanceName : %s, \n condition : %s, \n value : %s \n check server please" % (alarm_name, level, instanceName, condition, value)
    }

    req = Request(HOOK_URL, json.dumps(slack_message).encode('utf-8'))
    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", slack_message['channel'])
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)


    return {"payload": "success"}
