FROM aerokube/selenoid:latest-release AS selenoid-bin

FROM python:3.9

RUN apt-get update && \
    apt-get install -y chromium chromium-driver ca-certificates && \
    rm -rf /var/lib/apt/lists/*

COPY --from=selenoid-bin /usr/bin/selenoid /usr/bin/selenoid

ENTRYPOINT ["/usr/bin/selenoid"]