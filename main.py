from youtube_transcript_api import YouTubeTranscriptApi

#кастом лист с языками
def custom_list(video_id):
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    return str(transcript_list) \
        .partition('(TRANSLATION LANGUAGES)')[0] \
        .partition('languages:')[2] \
        .replace("[TRANSLATABLE]", '') \
        .replace("(", '') \
        .replace(")", '') \
        .strip()


video_url = "https://www.youtube.com/watch?v=1S0aBV-Waeo&ab_channel=Computerphile"

state_id = video_url.split('be')[1][1:] if '.be' in video_url else video_url.split('/')[3][8:]

sub_titles = YouTubeTranscriptApi.get_transcript(state_id)

with open('subtitles.txt', 'w') as file:
    for line in sub_titles:
        file.write(line['text'] + '\n')
