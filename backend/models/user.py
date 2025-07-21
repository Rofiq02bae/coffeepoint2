from firebase_admin import firestore
from typing import Optional

class User:
    def __init__(self, user_id: str, name: str, points: int = 0):
        self.user_id = user_id
        self.name = name
        self.points = points
        self._db = firestore.client()
        
    @classmethod
    async def get_by_id(cls, user_id: str) -> Optional['User']:
        doc = cls._db.collection('users').document(user_id).get()
        if doc.exists:
            data = doc.to_dict()
            return cls(
                user_id=user_id,
                name=data['name'],
                points=data['points']
            )
        return None
        
    def add_points(self, points: int) -> None:
        self.points += points
        self._db.collection('users').document(self.user_id).update({
            'points': self.points
        })