FROM python AS alpine

COPY whatsapp_bot.py .
COPY whatsapp_response.py .
COPY x.png .
COPY green dot.png 
COPY paperclip.png  .

WORKDIR  /WhatsApp
CMD ["whatsapp_bot.py","whatsapp_response.py",]