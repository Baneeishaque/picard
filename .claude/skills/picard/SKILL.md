# picard Development Patterns

> Auto-generated skill from repository analysis

## Overview

This skill teaches the development patterns and workflows for MusicBrainz Picard, a Python-based music tagger application. The codebase follows specific conventions for dependency management, internationalization, UI development, and audio format handling. Key areas include PyQt-based UI components, ID3 tag processing, translation management via Weblate, and multi-platform CI/CD workflows.

## Coding Conventions

### File Naming
- Use `snake_case` for all Python files
- Test files follow the pattern `test_*.py` or `*_test.py`
- UI option files are organized under `picard/ui/options/`
- Format handlers are placed in `picard/formats/`

### Import Style
```python
# Mix of absolute and relative imports
from picard.formats import id3
from picard.ui.options import OptionsPage
from .base import BaseFormat
```

### Project Structure
```
picard/
├── formats/          # Audio format handlers
├── ui/
│   ├── options/      # Settings UI pages
│   └── mainwindow/   # Main application window
├── resources.py      # Resource registry
resources/
├── images/           # PNG resources at multiple resolutions
├── img-src/          # SVG source files
└── picard.qrc       # Qt resource file
```

## Workflows

### Dependency Management Update
**Trigger:** When dependencies need to be updated or cleaned up
**Command:** `/update-deps`

1. Update `pyproject.toml` with new dependency versions or constraints
2. Modify `requirements.txt` and `requirements-dev.txt` as needed
3. Run uv to regenerate `uv.lock` file
4. Test that all dependencies resolve correctly
5. Commit all four files together

```toml
# pyproject.toml example
[project]
dependencies = [
    "mutagen>=1.45.0",
    "PyQt5>=5.15.0",
]
```

### GitHub Actions Workflow Update
**Trigger:** When CI/CD workflows need updates or maintenance
**Command:** `/update-workflows`

1. Update workflow YAML files in `.github/workflows/`
2. Modify action versions (e.g., `actions/checkout@v4`)
3. Update artifact handling and upload/download steps
4. Ensure cross-platform compatibility (Windows, macOS, Linux)
5. Test workflow changes on multiple platforms

```yaml
# Workflow example pattern
- uses: actions/checkout@v4
- uses: actions/setup-python@v4
  with:
    python-version: '3.x'
```

### Image Resource Addition
**Trigger:** When new images need to be added to the application
**Command:** `/add-images`

1. Create or update SVG source files in `resources/img-src/`
2. Generate PNG files at multiple resolutions (16x16, 24x24, 32x32, etc.) in `resources/images/`
3. Update `resources/picard.qrc` to include new image resources
4. Regenerate `picard/resources.py` from the QRC file
5. Reference new resources in UI code

```xml
<!-- picard.qrc example -->
<RCC>
  <qresource prefix="/images">
    <file>16x16/icon.png</file>
    <file>24x24/icon.png</file>
    <file>32x32/icon.png</file>
  </qresource>
</RCC>
```

### ID3 Format Enhancement
**Trigger:** When ID3 tag handling needs to be modified or enhanced
**Command:** `/update-id3`

1. Update `picard/formats/id3.py` with new tag handling logic
2. Add corresponding unit tests in `test/formats/test_id3.py`
3. Update related format files if the changes affect other formats
4. Test with various ID3 versions (v2.3, v2.4)
5. Ensure backward compatibility

```python
# ID3 format example
class ID3File(AudioFile):
    def _load(self, filename):
        # Handle ID3 tag loading
        pass
    
    def _save(self, filename, metadata):
        # Handle ID3 tag saving
        pass
```

### Translation Update
**Trigger:** When translations are updated from the translation service
**Command:** `/update-translations`

1. Pull updated `.po` files from Weblate for all languages
2. Update constants translations in `po/constants/`
3. Update specialized translations (attributes, countries)
4. Regenerate `po/picard.pot` template file
5. Verify translation formatting and encoding

```bash
# Translation workflow commands
msgfmt po/picard.po -o po/picard.mo
xgettext --from-code=UTF-8 -o po/picard.pot picard/**/*.py
```

### UI Options Modification
**Trigger:** When UI options need to be updated or fixed
**Command:** `/update-ui-options`

1. Update option page Python files in `picard/ui/options/`
2. Modify related UI components and layouts
3. Update main window integration in `picard/ui/mainwindow/__init__.py`
4. Apply consistent styling and widget patterns
5. Test option persistence and validation

```python
# Options page example
class MyOptionsPage(OptionsPage):
    NAME = "my_options"
    TITLE = "My Options"
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def load(self):
        # Load settings
        pass
    
    def save(self):
        # Save settings
        pass
```

## Testing Patterns

Tests are organized following the source code structure with `test/` mirroring the main package layout. Test files use the pattern `test_*.py` and focus on:

- Format-specific testing in `test/formats/`
- UI component testing for options and widgets
- Integration tests for tag reading/writing
- Cross-platform compatibility verification

```python
# Test example
class TestID3Format(unittest.TestCase):
    def test_id3_tag_reading(self):
        # Test ID3 tag parsing
        pass
    
    def test_id3_tag_writing(self):
        # Test ID3 tag writing
        pass
```

## Commands

| Command | Purpose |
|---------|---------|
| `/update-deps` | Update Python dependencies and lock files |
| `/update-workflows` | Update GitHub Actions workflow configurations |
| `/add-images` | Add new image resources with multiple resolutions |
| `/update-id3` | Modify ID3 tag format support with tests |
| `/update-translations` | Update translation files from Weblate |
| `/update-ui-options` | Modify UI options and settings pages |