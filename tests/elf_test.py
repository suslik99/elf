from typer.testing import CliRunner
import elf
from elf.console.application import app

runner = CliRunner()


def test_version():
    assert elf.__version__ == "0.1.0"


def test_console():
    result = runner.invoke(app)
    assert result.exit_code == 1
