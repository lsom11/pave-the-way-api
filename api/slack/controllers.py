from flask import Blueprint, jsonify, request
import os
from slackclient import SlackClient

# SLACK_TOKEN = os.environ.get('SLACK_TOKEN', None)
SLACK_TOKEN = 'FzZDOKGv9Wlr2AHEC8nm314n'
SLACK_WEBHOOK_SECRET = os.environ.get('HF7V6PJ4/VRrDsfK5fZuWJ6xNoANBPDCo')

slack_client = SlackClient(SLACK_TOKEN)

slack_blueprint = Blueprint('slack', __name__)

@slack_blueprint.route('/channels', methods=['GET'])
def list_channels():
    channels_call = slack_client.api_call("channels.list")
    if channels_call['ok']:
        return channels_call['channels']
    return None

@slack_blueprint.route('/channels/<channel_id>', methods=['GET'])
def channel_info(channel_id):
    channel_info = slack_client.api_call("channels.info", channel=channel_id)
    if channel_info:
        return channel_info['channel']
    return None

@slack_blueprint.route('/send_message', methods=['POST'])
def inbound():
    if request.form.get('token') == SLACK_WEBHOOK_SECRET:
        channel = request.form.get('channel_name')
        username = request.form.get('user_name')
        text = request.form.get('text')
        inbound_message = username + " in " + channel + " says: " + text
        print(inbound_message)
    return Response(), 200
