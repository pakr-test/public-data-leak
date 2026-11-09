import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from hello import hello

def test_hello():
    assert hello() == "hello, world"
