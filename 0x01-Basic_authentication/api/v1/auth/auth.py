#!/usr/bin/env python3
"""a class to manage the API auth
"""
from flask import request, Flask
from typing import List, TypeVar


class Auth():
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """_summary_

        Args:
            path (str): _description_
            excluded_paths (List[str]): _description_

        Returns:
            bool: _description_
        """
        if path is None:
            return False

    def authorization_header(self, request=None) -> str:
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        if request is None:
            return None
