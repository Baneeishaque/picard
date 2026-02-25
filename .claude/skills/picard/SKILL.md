# picard Development Patterns

> Auto-generated skill from repository analysis

## Overview

MusicBrainz Picard is a Python-based music tagger application with a Qt-based GUI. The codebase follows established patterns for internationalization, UI management, resource handling, and configuration persistence. Development focuses heavily on translation updates, UI enhancements, and maintaining code quality through modernization efforts.

## Coding Conventions

### File Naming
- Use `snake_case` for all Python files
- Example: `interface_toolbar.py`, `config_upgrade.py`

### Import Style
```python
# Mixed style - external imports first, then internal
import os
import sys
from PyQt5 import QtCore, QtWidgets

from picard import config
from picard.ui.widgets import BaseWidget
```

### Export Style
- Mixed patterns - use explicit `__all__` when needed
- Prefer direct imports over wildcard imports

### Commit Messages
- Freeform style, average 48 characters
- Focus on clear, concise descriptions
- Examples: "Fix toolbar configuration persistence", "Update translation files"

## Workflows

### Translation Update
**Trigger:** When translations are updated from external sources like Weblate
**Command:** `/update-translations`

1. Update PO files via Weblate webhook integration
2. Regenerate POT template file from source code
3. Update specialized translation files:
   - `po/attributes/*.po` - MusicBrainz attributes
   - `po/constants/*.po` - Application constants
   - `po/countries/*.po` - Country names
   - `po/appstream/*.po` - AppStream metadata
4. Create pull request for translation updates
5. Merge after automated checks pass

**Files involved:**
```
po/*.po
po/picard.pot
po/attributes/*.po
po/constants/*.po
po/countries/*.po
po/appstream/*.po
```

### UI Action Enhancement
**Trigger:** When adding new user interface actions or restructuring menus
**Command:** `/add-ui-action`

1. Define new actions in `picard/ui/mainwindow/actions.py`:
```python
def setup_actions(self):
    self.new_action = QtWidgets.QAction("New Action", self)
    self.new_action.triggered.connect(self.handle_new_action)
```

2. Integrate actions into main window (`picard/ui/mainwindow/__init__.py`)
3. Add toolbar configuration options in `picard/ui/options/interface_toolbar.py`
4. Update UI enums if new action types are needed (`picard/ui/enums.py`)
5. Add associated resources/icons if required

**Key pattern:**
- Actions are centrally defined but distributed across UI components
- Always provide toolbar integration options
- Follow Qt signal/slot patterns for event handling

### Icon Resource Addition
**Trigger:** When new UI features need dedicated icons
**Command:** `/add-icon`

1. Create SVG source file in `resources/img-src/`:
```svg
<!-- Example: new-feature.svg -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">
  <!-- Icon content -->
</svg>
```

2. Generate PNG files in multiple sizes:
   - `resources/images/16x16/new-feature.png`
   - `resources/images/22x22/new-feature.png`

3. Update `picard/resources.py`:
```python
def icon(name):
    # Add new icon reference
    return QtGui.QIcon(f":/images/{size}x{size}/{name}.png")
```

4. Update `resources/picard.qrc` Qt resource file
5. Rebuild resources if needed

### Code Modernization
**Trigger:** When performing code cleanup or modernization across multiple files
**Command:** `/modernize-code`

1. Identify files with outdated patterns (e.g., `dict()` vs `{}`, old string formatting)
2. Apply modern Python patterns:
```python
# Old
config = dict()
message = "Value: %s" % value

# New  
config = {}
message = f"Value: {value}"
```

3. Create individual commits per file for easier review
4. Focus on one pattern type per modernization sweep
5. Test thoroughly as changes span multiple modules

**Common modernization targets:**
- Replace `dict()` with `{}`
- Replace `list()` with `[]`
- Update string formatting to f-strings
- Use pathlib for path operations

### Configuration Persistence
**Trigger:** When UI components need to save and restore their state
**Command:** `/fix-config-persistence`

1. Update config upgrade logic in `picard/config_upgrade.py`:
```python
def upgrade_config(config):
    if config.version < target_version:
        # Add new config keys with defaults
        config.setting["new_feature_enabled"] = True
```

2. Modify options handling in `picard/options.py`
3. Implement persistence in UI widgets:
```python
def save_state(self):
    config = get_config()
    config.setting["widget_geometry"] = self.saveGeometry()

def restore_state(self):
    config = get_config() 
    geometry = config.setting["widget_geometry"]
    if geometry:
        self.restoreGeometry(geometry)
```

4. Update version tracking in `picard/__init__.py` if schema changes
5. Test upgrade path from previous versions

## Testing Patterns

- Test files follow pattern: `*.test.*`
- Testing framework not clearly detected from analysis
- Focus on integration testing for UI components
- Translation updates include automated validation

## Commands

| Command | Purpose |
|---------|---------|
| `/update-translations` | Update PO files and translation resources from Weblate |
| `/add-ui-action` | Add new menu/toolbar actions with full integration |
| `/add-icon` | Create and integrate new icons across all required sizes |
| `/modernize-code` | Apply modern Python patterns across multiple files |
| `/fix-config-persistence` | Implement configuration state saving and restoration |