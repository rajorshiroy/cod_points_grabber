import config
from googleapiclient.discovery import build
from pprint import pprint


def get_channel_id(channel_name: str):
    request = youtube.search().list(q=channel_name, type='channel', part='id')
    response = request.execute()
    try:
        return response['items'][0]['id']['channelId']
    except:
        return None


def get_live_video_url(channel_id: str):
    request = youtube.search().list(channelId=channel_id, type='video', part='id', eventType='live')
    response = request.execute()
    try:
        video_id = response['items'][0]['id']['videoId']
        print(f'channel is live at: https://www.youtube.com/watch?v={video_id}')
        return video_id
    except:
        print('Channel is not live')
        return None


def get_live_chat_id(video_id: str):
    request = youtube.videos().list(
        part="liveStreamingDetails",
        id=video_id
    )
    response = request.execute()
    try:
        return response['items'][0]['liveStreamingDetails']['activeLiveChatId']
    except:
        return None


if __name__ == '__main__':
    youtube = build('youtube', 'v3', developerKey=config.api_key)

    # channel_name = 'jackfrags'
    # channel_id = get_channel_id(channel_name)
    # if channel_id:
    #     get_live_video_url(channel_id)
    # else:
    #     print('channel not found')

    pprint(get_live_chat_id('AtMUOqMlyhg'))
