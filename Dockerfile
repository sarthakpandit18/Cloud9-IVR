FROM python
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install requests
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - 
RUN apt-get install -y nodejs
CMD ["sh","/scripts/main.sh"]

