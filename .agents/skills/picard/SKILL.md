```markdown
# picard Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches development patterns and workflows for the `picard` TypeScript codebase. You'll learn the project's coding conventions, how to manage translation updates, and how to write and locate tests. This guide is ideal for contributors seeking to maintain consistency and efficiency in the repository.

## Coding Conventions

### File Naming
- Use **camelCase** for file names.
  - Example: `userProfile.ts`, `dataFetcher.ts`

### Imports
- Use **relative imports** for referencing local modules.
  ```typescript
  import { fetchData } from './dataFetcher';
  ```

### Exports
- Use **named exports** rather than default exports.
  ```typescript
  // In dataFetcher.ts
  export function fetchData() { /* ... */ }

  // In another file
  import { fetchData } from './dataFetcher';
  ```

### Commit Messages
- Commit messages are freeform, often concise (~35 characters).
  - Example: `Fix typo in user profile form`

## Workflows

### Update Translation Files via Weblate
**Trigger:** When you want to update or add translations for supported languages.  
**Command:** `/update-translation`

1. Edit or add translations on the [Weblate platform](https://weblate.org/).
2. Pull the updated `.po` files from Weblate.
3. Commit the changes to the relevant files:
   - `po/*.po`
   - `po/appstream/*.po`
   - `po/constants/*.po`
4. Use a commit message referencing Weblate and translation progress.
   - Example: `Update French translations via Weblate`

**Files involved:**
- `po/*.po`
- `po/appstream/*.po`
- `po/constants/*.po`

**Frequency:** Approximately 5 times per month.

## Testing Patterns

- Test files follow the `*.test.*` naming convention.
  - Example: `userProfile.test.ts`
- The testing framework is not explicitly specified.
- To add a test, create a file alongside your module:
  ```typescript
  // userProfile.test.ts
  import { getUserProfile } from './userProfile';

  test('should fetch user profile', () => {
    // test implementation
  });
  ```

## Commands

| Command              | Purpose                                                      |
|----------------------|--------------------------------------------------------------|
| /update-translation  | Update translation files via Weblate and commit the changes.  |
```