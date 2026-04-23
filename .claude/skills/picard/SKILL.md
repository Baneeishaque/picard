# picard Development Patterns

> Auto-generated skill from repository analysis

## Overview

This skill covers development patterns for the Picard music tagger application, a Python-based desktop application for organizing and tagging music files. The codebase emphasizes internationalization, UI development with Qt, and modular architecture with consistent code organization patterns.

## Coding Conventions

**File Naming:** Use `snake_case` for all Python files and modules
```
picard/ui/options/interface_toolbar.py
picard/formats/mutagenext/_util.py
```

**Import Style:** Mixed approach with preference for explicit imports
```python
from picard.const import PICARD_VERSION
import picard.formats
from .actions import PicardAction
```

**Export Style:** Mixed patterns depending on module purpose

**Commit Style:** Freeform messages averaging ~48 characters, focusing on clear, concise descriptions of changes

## Workflows

### Dependency Management
**Trigger:** When updating dependencies or changing build configuration  
**Command:** `/update-deps`

1. Update `pyproject.toml` with new dependency versions or requirements
2. Regenerate requirements files using your dependency management tool
3. Update `uv.lock` file to lock specific versions
4. Update CI workflow files in `.github/workflows/` if needed
5. Test the build to ensure compatibility

**Files involved:**
- `pyproject.toml`
- `requirements*.txt` 
- `uv.lock`
- `.github/workflows/*.yml`

### Translation Updates
**Trigger:** When translation strings are updated or new translations are added  
**Command:** `/update-translations`

1. Update the master template `po/picard.pot` with new translatable strings
2. Update all language-specific `.po` files in the `po/` directory
3. Update attribute translations in `po/attributes/*.po`
4. Update country name translations in `po/countries/*.po`
5. Create individual commits for each language update for better tracking

**Files involved:**
- `po/picard.pot`
- `po/*.po`
- `po/attributes/*.po`
- `po/countries/*.po`

### Code Refactoring
**Trigger:** When improving code consistency or applying style fixes across multiple files  
**Command:** `/refactor`

1. Identify the pattern or style issue to be fixed
2. Create a plan for consistent application across the codebase
3. Apply fixes to individual files, grouping logically related changes
4. Create a consolidated commit with a clear description of the refactoring
5. Test to ensure no functionality is broken

**Files involved:**
- `picard/**/*.py`

### UI Feature Development
**Trigger:** When adding new UI functionality, menu items, or toolbar actions  
**Command:** `/add-ui-feature`

1. Add new icons and graphical resources to `resources/` directory
2. Update `picard/ui/mainwindow/actions.py` to define new actions
3. Modify main window code in `picard/ui/mainwindow/__init__.py`
4. Update toolbar configuration in `picard/ui/options/interface_toolbar.py`
5. Update `picard/resources.py` to register new resources
6. Update `resources/picard.qrc` resource file

**Example action definition:**
```python
class SomeNewAction(PicardAction):
    NAME = "some_new_action"
    
    def __init__(self):
        super().__init__()
        self.setText(_("New Feature"))
        self.setIcon(":/images/new-icon.png")
```

**Files involved:**
- `picard/ui/mainwindow/actions.py`
- `picard/ui/mainwindow/__init__.py`
- `picard/ui/options/interface_toolbar.py`
- `picard/resources.py`
- `resources/**/*`
- `resources/picard.qrc`

### Release Preparation
**Trigger:** When preparing for a new software release  
**Command:** `/prepare-release`

1. Update `NEWS.md` with changelog entries for the new release
2. Update version numbers throughout the codebase
3. Update all translation files to ensure completeness
4. Perform final testing and validation
5. Tag the release commit appropriately

**Files involved:**
- `NEWS.md`
- `po/**/*.po`
- Version files (location varies)

## Testing Patterns

Tests follow the pattern `*.test.*` for test files. The specific testing framework is not clearly defined from the analysis, but tests should:

- Be placed alongside the code they test
- Use descriptive names that clearly indicate what is being tested
- Follow the established naming pattern for easy discovery

## Commands

| Command | Purpose |
|---------|---------|
| `/update-deps` | Update project dependencies and build requirements |
| `/update-translations` | Update translation files for internationalization |
| `/refactor` | Apply consistent code style improvements across multiple files |
| `/add-ui-feature` | Add new UI features with actions, menus, and resources |
| `/prepare-release` | Prepare for software release with changelog and version updates |