import json
from typing import Any, Dict, List, Optional, Union


class RestAPI:
    def __init__(self, database: Optional[Dict[str, Any]] = None):
        users: List[Dict[str, Any]] = database.get('users', []) if database else []
        self._users = {user['name']: user for user in users}

    def get(self, url: str, payload: Optional[str] = None) -> str:
        data: Union[None, List[Any], Dict[str, Any]] = None if not payload else json.loads(payload)
        if url == "/users":
            users: List[Dict[str, Any]] = []
            if not data:
                users = [data for _, data in self._users.items()]
            elif 'users' in data:
                query: List[str] = data['users']
                users = [self._users[name] for name in data['users'] if name in self._users]
            return json.dumps({"users": sorted(users, key=lambda user: user['name'])})
        return ""

    @staticmethod
    def _new_user(name: str) -> Dict[str, Any]:
        return {
            "name": name,
            "owes": {},
            "owed_by": {},
            "balance": 0.0
        }

    def post(self, url: str, payload: Optional[str] = None) -> str:
        data: Union[None, List[Any], Dict[str, Any]] = None if not payload else json.loads(payload)
        if url == "/add":
            user: Dict[str, Any] = RestAPI._new_user(data['user'])
            self._users[user['name']] = user
            return json.dumps(user)
        elif url == "/iou":
            lender_name = data['lender']
            borrower_name = data['borrower']
            lender: Dict[str, Any] = self._users[lender_name]
            borrower: Dict[str, Any] = self._users[borrower_name]
            amount: float = data['amount']

            lender['owed_by'][borrower_name] = lender['owed_by'].get(borrower_name, 0.0) + amount
            lender['balance'] = lender['balance'] + amount
            self._users[data['lender']] = lender

            borrower['owes'][lender_name] = borrower['owes'].get(lender_name, 0.0) + amount
            borrower['balance'] = borrower['balance'] - amount
            self._users[borrower_name] = borrower

            return json.dumps({
                "users": sorted([lender, borrower], key=lambda user: user['name'])
            })
