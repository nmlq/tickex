FROM python:3.12-slim AS base
WORKDIR /app
COPY setup.py .
COPY requirements.txt .
COPY tickex/ tickex/
RUN pip install --no-cache-dir --user .

# ---- Test stage ----
FROM base AS test
COPY tests/ tests/
RUN pip install --no-cache-dir --user pytest
ENV PATH=/root/.local/bin:$PATH
CMD ["pytest", "-xvs", "tests/"]

# ---- Runtime stage (slim, no test deps or test files) ----
FROM python:3.12-slim AS runtime
WORKDIR /app
COPY --from=base /root/.local /root/.local
COPY --from=base /app/tickex /app/tickex
ENV PATH=/root/.local/bin:$PATH
ENTRYPOINT ["tickex"]