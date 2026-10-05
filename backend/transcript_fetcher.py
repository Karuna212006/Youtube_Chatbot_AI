"""
YouTube Transcript Fetcher
Week 2 - YouTube Data Extraction
"""

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from dotenv import load_dotenv
import re

load_dotenv()


def extract_video_id(url_or_id: str) -> str:
    """Extract video ID from a YouTube URL or return as-is if already an ID."""
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11})",
        r"(?:youtu\.be\/)([0-9A-Za-z_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    return url_or_id  # assume it's already a video ID


def fetch_transcript(url_or_id: str, language: str = "en") -> dict:
    """
    Fetch transcript from a YouTube video.
    
    Args:
        url_or_id: YouTube video URL or video ID
        language: Language code (default: 'en')
    
    Returns:
        dict with video_id, transcript text, and metadata
    """
    video_id = extract_video_id(url_or_id)
    print(f"Fetching transcript for video ID: {video_id}")

    try:
        # v1.x API: instantiate and call .fetch()
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id, languages=[language])

        # Combine all text chunks into full transcript
        full_text = " ".join(snippet.text for snippet in fetched)

        return {
            "video_id": video_id,
            "language": language,
            "transcript": full_text,
            "chunks": [{'text': s.text, 'start': s.start, 'duration': s.duration} for s in fetched],
            "word_count": len(full_text.split()),
            "status": "success"
        }

    except TranscriptsDisabled:
        return {"video_id": video_id, "status": "error", "error": "Transcripts are disabled for this video."}
    except NoTranscriptFound:
        return {"video_id": video_id, "status": "error", "error": f"No transcript found in '{language}'. Try another language."}
    except Exception as e:
        return {"video_id": video_id, "status": "error", "error": str(e)}


if __name__ == "__main__":
    # Test with a sample YouTube video
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with any video URL
    
    result = fetch_transcript(test_url)
    
    if result["status"] == "success":
        print(f"\n[SUCCESS] Transcript fetched successfully!")
        print(f"   Word count : {result['word_count']}")
        print(f"   Language   : {result['language']}")
        print(f"\n--- First 500 characters ---")
        safe_text = result["transcript"][:500].encode("ascii", errors="replace").decode("ascii")
        print(safe_text)
    else:
        print(f"\n[ERROR] {result['error']}")
