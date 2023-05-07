import logging
import pytest
from _pytest.logging import caplog as caplog
from loguru import logger


pytest_plugins = "pytester"

# this is to make pytest work with loguru
# taken from https://github.com/Delgan/loguru/issues/59
@pytest.fixture
def caplog(caplog):
    class PropogateHandler(logging.Handler):
        def emit(self, record):
            logging.getLogger(record.name).handle(record)

    logger.add(PropogateHandler(), format="{message}")
    yield caplog
