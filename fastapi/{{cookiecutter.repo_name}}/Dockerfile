FROM python:3.11.1-bullseye

ENV APP_HOME=/microservice/

RUN  apt update \
  && apt upgrade -y \
  && adduser --home $APP_HOME --shell /bin/bash --system --disabled-password python \
  && chown -R python $APP_HOME \
  && pip install --upgrade pip \
  && curl https://sh.rustup.rs -sSf > install_rust.sh \
  && sh install_rust.sh -y \
  && . "$HOME/.cargo/env"; pip install uvicorn

WORKDIR $APP_HOME

ADD ./dist/*.whl $APP_HOME

RUN . "$HOME/.cargo/env" \
  && pip install *.whl

EXPOSE 8080
USER PYTHON

CMD ["uvicorn", "--workers", "1", "--log-level", "INFO", "--bind", "0.0.0.0:8080", "main:app"]
