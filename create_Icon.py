from pathlib import Path
hex_content = Path('ui.ico').read_bytes()
Path('icon.py').write_text(f'icon = {hex_content}')