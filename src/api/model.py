from pydantic import BaseModel

class SendMessageRequest(BaseModel):
    chatId: str
    message: str
    quotedMessageId: str = None
    linkPreview: bool = True

class SendFileRequest(BaseModel):
    chatId: str
    urlFile: str
    fileName: str
    caption: str = None
    quotedMessageId: str = None
