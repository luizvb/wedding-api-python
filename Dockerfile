FROM python as base

FROM base AS python-deps

ARG MONGO_URI
ARG AWS_ACCESS_KEY
ARG AWS_SECRET_KEY

ENV MONGO_URI ${MONGO_URI}
ENV AWS_ACCESS_KEY ${AWS_ACCESS_KEY}
ENV AWS_SECRET_KEY ${AWS_SECRET_KEY}

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

ADD ./src /src
WORKDIR /src

# Run the application
CMD ["python", "-m", "main"]