from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime

class User:
    def __init__(self, name:str, contact_info:str):
        self._name = name
        self._contact_info = contact_info
        self._conversations:List["Conversation"] = []

    def create_conversation(self, user: 'User') -> 'Conversation':
        conversation = Conversation([self, user])
        self._conversations.append(conversation)
        user._conversations.append(conversation)
        return conversation

    def send_message(self, message: 'Message', conversation: 'Conversation') -> None:
        conversation.add_message(message)

    def receive_message(self, message: 'Message') -> None:
        print(f"New message for {self._name}: {message.display_content()}")

    def manage_settings(self) -> None:
        print(f"Managing settings for {self._name}")

    def get_conversations(self) -> List['Conversation']:
        return self._conversations

class Conversation:
    def __init__(self, participants: List['User']):
        self._participants = participants
        self._message_history: List['Message'] = []

    def add_message(self, message: 'Message') -> None:
        self._message_history.append(message)
        for user in self._participants:
            user.receive_message(message)

    def add_user(self, user: 'User') -> None:
        if user not in self._participants:
            self._participants.append(user)

    def get_messages(self) -> List['Message']:
        return self._message_history

class Message(ABC):
    def __init__(self, sender: 'User', conversation: 'Conversation', timestamp: datetime):
        self._sender = sender
        self._conversations = conversation
        self._timestamp = datetime.now()

    @abstractmethod
    def display_content(self) -> None:
        pass

    @abstractmethod
    def  get_message_type(self) -> str:
        pass

class TextMessage(Message):
    def __init__(self, sender: 'User', conversation: 'Conversation', timestamp: datetime, content: str):
        super().__init__(sender, conversation, timestamp)
        self._content = content
    
    def display_content(self) -> None:
        return f"[{self._timestamp}] {self._sender._name}: {self._content}"

    def get_message_type(self) -> str: 
        return "Text"

class MultimediaMessage(Message):
    def __init__(self, sender: 'User', conversation: 'Conversation', timestamp: datetime, file_path: str, media_type: str ):
        super().__init__(sender, conversation, timestamp)
        self._file_path = file_path
        self._media_type = media_type
    
    def display_content(self) -> None:
        print(f"[{self._timestamp}] {self._sender._name}: Sent a {self._media_type} file at {self._file_path}")

    def get_message_type(self) -> str: 
        return self._media_type

class MessagingManager(ABC):
    @abstractmethod
    def send_message(self, message: 'Message') -> None:
        pass

    @abstractmethod
    def receive_message(self, message: 'Message') -> None:
        pass

    @abstractmethod
    def view_conversation_history(self, conversation: 'Conversation') -> List['Message']:
        pass