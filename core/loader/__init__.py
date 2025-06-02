# core/loader/__init__.py

import typer
from .registry import load_all

app = typer.Typer(add_completion=False)


@app.command()
def build():
    """Lua→JSON→Enum/Pydantic 一括ビルド"""
    load_all()


# 以前 data/loader.py にあった実装詳細は
# core/loader/converters/* へ小分けに移していく
if __name__ == "__main__":
    app()
