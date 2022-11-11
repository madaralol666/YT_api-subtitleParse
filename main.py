from youtube_transcript_api import YouTubeTranscriptApi
import json

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


# video_url = input()
# video_url_id = video_url.split('=')[1]
#
# print(custom_list(video_url_id))
#
#
# sub_titles = YouTubeTranscriptApi.get_transcript(video_url_id)
#
# #Без форматирования
# with open('subtitles_not_formatted.txt', 'w') as file_snf:
#     for item in sub_titles:
#         file_snf.writelines(f"{item['text']}\n")

#форматирование строк
with open('subtitles_not_formatted.txt') as file_snf:
    lines = file_snf.readlines()
    for a in range(0, len(lines)):
        if len(lines[a]) >= 43:
            for i in range(43, len(lines[a])):
                if lines[a][i] == ' ':
                    lines[a] = a[:i] + '\n' + a[i + 1:]
                    break

    non_empty_lines = (line for line in lines if not line.isspace())
    with open('subtitles_formatted.txt', 'w') as file_formatted:
        file_formatted.writelines(non_empty_lines)



