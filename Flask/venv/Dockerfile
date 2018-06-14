FROM python:3.7-rc-alpine
# FROM python:3

COPY . /app
WORKDIR /app

# Install ca-certificate
# Avoid SSL: CERTIFICATE_VERIFY_FAILED
# RUN apk --no-cache add python ca-certificates
#RUN apk --update upgrade && \
RUN apk update && \
    apk add ca-certificates && \
    update-ca-certificates && \
    rm -rf /var/cache/apk/*

RUN pip3 install -r requirements.txt

ENTRYPOINT python3 /app/Runner.py
EXPOSE 5000
