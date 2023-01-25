import json
from pathlib import Path
from typing import Optional

BASE_DIR = Path(__file__).resolve()

def get_secret(
    key: str,
    default_value: Optional[str] = None,
    json_path: str = str("./secrets.json"),
):
    with open(json_path) as f:
        secrets = json.loads(f.read())
    try:
        return secrets[key]
    except KeyError:
        if default_value:
            return default_value
        raise EnvironmentError(f"Set the {key} environment variable.")


POSTGRES_ID = get_secret("POSTGRES_ID")
POSTGRES_PW = get_secret("POSTGRES_PW")


if __name__ == "__main__":
    world = get_secret("hello")