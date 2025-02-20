from youtube_transcript_api import YouTubeTranscriptApi
import os

def get_transcript(youtube_url, language='ja'):
    try:
        video_id = youtube_url.split('v=')[1]
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        transcript = ' '.join([entry['text'] for entry in transcript_list])
        return transcript
    except Exception as e:
        return str(e)

def save_transcript(youtube_url, transcript):
    try:
        video_id = youtube_url.split('v=')[1]
        video_id = video_id.split('&')[0]
        print('hrere')
        file_path = os.path.join(os.path.dirname(__file__), 'data', 'transcripts', f'{video_id}.txt')
        print(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            file.write(transcript)
        return True,video_id
    except Exception as e:
        return False,f"Error saving transcript: {e}"

# Test case
if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=sY7L5cfCWno&list=PLkGU7DnOLgRMl-h4NxxrGbK-UdZHIXzKQ&index=2"
    transcript = get_transcript(youtube_url)
    print(transcript)
    print(save_transcript(youtube_url, transcript))

