from datetime import datetime, timedelta, timezone
class NotificationsActivities:
  def run():
    now = datetime.now(timezone.utc).astimezone()
    results = [{
      'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
      'handle':  'beauty',
      'message': 'how are you',
      'created_at': (now - timedelta(days=2)).isoformat(),
      'expires_at': (now + timedelta(days=5)).isoformat(),
      'likes_count': 5,
      'replies_count': 1,
      'reposts_count': 0,
      'replies': [{
        'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
        'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'handle':  'honey',
        'message': 'I am good',
        'likes_count': 4,
        'replies_count': 0,
        'reposts_count': 2,
        'created_at': (now - timedelta(days=2)).isoformat()
      },
      {
        'uuid': '8c4e7d6e-b17f-11ed-afa1-0242ac120002',
        'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'handle':  'Ilu',
        'message': 'Wonderful',
        'likes_count': 6,
        'replies_count': 0,
        'reposts_count': 8,
        'created_at': (now - timedelta(days=1)).isoformat()
      }
      ],
    }
    ]
    return results