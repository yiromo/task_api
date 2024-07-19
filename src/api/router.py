from fastapi import APIRouter, UploadFile, File
from .service import api_service
from .model import SendMessageRequest, SendFileRequest


router = APIRouter(
    prefix="/greenapi",
    tags=["GreenAPI"] 
)


@router.get("/get-settings/")
async def get_settings(idInstance: str, apiTokenInstance: str):
    return await api_service.get_settings(idInstance, apiTokenInstance)

@router.get("/get-state-intance/")
async def get_state_intance(idInstance: str, apiTokenInstance: str):
    return await api_service.get_state_intance(idInstance, apiTokenInstance)
    
@router.post("/send-message/")
async def send_message(idInstance: str, request: SendMessageRequest):
    return await api_service.send_message(idInstance, request.chatId, request.message, request.quotedMessageId, request.linkPreview)

@router.post("/send-file/")
async def send_file_by_url(idInstance: str,  request: SendFileRequest):
    return await api_service.send_file_by_url(idInstance, request.chatId, request.urlFile, request.fileName, request.caption, request.quotedMessageId)

@router.post("/upload-file/")
async def upload_file(idInstance: str, file: UploadFile = File(...)):
    file_bytes = await file.read()
    content_type = file.content_type
    file_name = file.filename
    return await api_service.upload_file(idInstance, file_bytes, content_type, file_name)