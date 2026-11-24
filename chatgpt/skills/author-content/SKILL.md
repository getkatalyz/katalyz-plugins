---
name: author-content
description: Use when a Katalyz seller wants to create or edit pages, widgets, tasks, visual design, or file assets in an existing dealroom or template.
---

# Author dealroom or template content

Resolve the exact room with `search_dealrooms` or template with `search_dealroom_templates`. If several match, ask the seller to choose. For a new target, wait for its creation status to become `READY`. Read `get_organization_branding` for current organization assets, colors, and selected fonts before creating or restyling content. Read `get_canvas_authoring_guide`, `get_content_overview`, and the relevant `get_content_tree` before writing. Follow the guide's node and design examples instead of inventing classes or widget settings. Read `get_content_design` before changing the target-wide palette or visual preferences.

Create or edit pages with `create_content_page` and `update_content_page`. For native widgets, use `get_content_widget_options` to find authorized references and `get_content_widgets` to read current configuration before `create_content_widget` or `update_content_widget`. Creation returns an unplaced page `blockId`; place it with `patch_content_tree` and `ATTACH_BLOCK_NODE`. Supported task-body widgets attach automatically. Read `get_content_tasks` before updating real action-plan tasks with `update_content_task`; create missing ones with `create_content_task` and attach root steps to an action-plan container. Use `taskId` when editing task bodies. A timeline widget does not create tasks. Use `update_content_design` for target-wide visual settings and `rename_dealroom_template` for template titles. Confirm an exact page or widget before deleting it.

Page widgets need durable library assets. Find them with `search_resources`, or upload original bytes using `prepare_resource_upload` with `destination: "library"`, the exact returned headers and byte size, and `complete_resource_upload` only after a successful 2xx PUT. Keep the single-use upload URL and token private. Temporary AI context resources cannot be attached to widgets. Read `get_resource` before `update_resource`; `delete_resource` permanently removes it and direct references, so obtain explicit confirmation before deletion.

Patch the current page or task-body version with stable node IDs. On a version conflict or uncertain result, reread the tree before deciding what remains to change. Reuse any unplaced native block rather than creating a duplicate. Inspect the saved receipt, then follow the visual-review skill for the changed page: use ChatGPT's authenticated browser when available and the seller has granted `browser:login`, otherwise use `get_content_page_screenshot`. Never echo, publish, or insert a browser login credential URL in content.
