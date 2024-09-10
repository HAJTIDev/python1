from pathlib import Path

print(Path.cwd())
path=Path(Path.cwd(),"temp")
path.mkdir()
print(path)
print(path.is_file())
print(path.exists())
print(path.is_dir())