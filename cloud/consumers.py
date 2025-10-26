# your_app/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

import redis
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Extract room name from the URL
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        
        # Construct a unique group name for this room
        self.room_group_name = f'chat_{self.room_name}'
        
        # Add the channel to the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        # Accept the WebSocket connection
        await self.accept()
        
        # Retrieve existing messages for this room
        await self.retrieve_room_messages()
    
    async def retrieve_room_messages(self):
        try:
            # Option 1: Using Django's cache framework
            from django.core.cache import cache
            room_messages = cache.get(f'room_messages_{self.room_name}', [])
            
            # Option 2: Direct Redis connection
            redis_client = redis.Redis(host='localhost', port=6379, db=0)
            room_messages = redis_client.lrange(f'room_messages:{self.room_name}', 0, -1)
            
            # Send retrieved messages to the client
            for message in room_messages:
                await self.send(text_data=json.dumps({
                    'message': message.decode('utf-8') if isinstance(message, bytes) else message
                }))
        
        except Exception as e:
            # Handle any retrieval errors
            await self.send(text_data=json.dumps({
                'error': f'Failed to retrieve messages: {str(e)}'
            }))
    
    async def receive(self, text_data):
        # Handle incoming messages
        data = json.loads(text_data)
        message = data['message']
        
        # Store the message
        await self.store_message(message)
        
        # Broadcast to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
    
    async def store_message(self, message):
        try:
            # Option 1: Using Django's cache framework
            from django.core.cache import cache
            room_messages = cache.get(f'room_messages_{self.room_name}', [])
            room_messages.append(message)
            cache.set(f'room_messages_{self.room_name}', room_messages, timeout=3600)
            
            # Option 2: Direct Redis storage
            redis_client = redis.Redis(host='localhost', port=6379, db=0)
            redis_client.rpush(f'room_messages:{self.room_name}', message)
        
        except Exception as e:
            print(f"Error storing message: {e}")
    
    async def chat_message(self, event):
        # Send message to WebSocket
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
    
    async def disconnect(self, close_code):
        # Remove from room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )