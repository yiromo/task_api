import httpx
from fastapi import HTTPException
from dotenv import load_dotenv
import os
from .model import SendMessageRequest

load_dotenv()

apiUrl = os.getenv('API_URL')
mediaUrl = os.getenv('MEDIA_API_URL')

class Api:
    async def get_settings(self, idInstance: str, apiTokenInstance: str):
        url = f"{apiUrl}/waInstance{idInstance}/getSettings/{apiTokenInstance}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        if response.status_code == 200:
            settings = response.json()
            return settings
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
    

    async def get_state_intance(self, idInstance: str, apiTokenInstance: str):
        url = f"{apiUrl}/waInstance{idInstance}/getStateInstance/{apiTokenInstance}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        if response.status_code == 200:
            state = response.json()
            return state
        else:
            raise HTTPException(status_code = response.status_code, detail=response.text)
        
    async def send_message(self, idInstance: str, chatId: str, message: str, quotedMessageId: str = None, linkPreview: bool = True):
        apiTokenInstance = os.getenv('API_TOKEN_INSTANCE')
        url = f"{apiUrl}/waInstance{idInstance}/sendMessage/{apiTokenInstance}"
        payload = {
            "chatId": chatId,
            "message": message,
            "linkPreview": linkPreview
        }
        
        if quotedMessageId and len(quotedMessageId) >= 16:
            payload["quotedMessageId"] = quotedMessageId
        
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload)
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        
    async def send_file_by_url(self, idInstance: str, chatId: str, urlFile: str, fileName: str, caption: str = None, quotedMessageId: str = None):
        apiTokenInstance = os.getenv('API_TOKEN_INSTANCE')
        url = f"{apiUrl}/waInstance{idInstance}/sendFileByUrl/{apiTokenInstance}"
        payload = {
            "chatId": chatId,
            "urlFile": urlFile,
            "fileName": fileName
        }
        if caption:
            payload["caption"] = caption
        if quotedMessageId and len(quotedMessageId) >= 16:
            payload["quotedMessageId"] = quotedMessageId
        
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload)
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

    async def upload_file(self, idInstance: str, file: bytes, content_type: str = None, file_name: str = None):
        apiTokenInstance = os.getenv('API_TOKEN_INSTANCE')
        url = f"{mediaUrl}/waInstance{idInstance}/uploadFile/{apiTokenInstance}"
        headers = {}
        if content_type:
            headers['Content-Type'] = content_type
        if file_name:
            headers['GA-Filename'] = file_name
        
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, content=file)
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

api_service = Api()