# Created custom permissions in Book model using Meta class.
# Groups:
# - Viewers: view only
# - Editors: view, add, edit
# - Admins: all actions

### Role-Based Permissions Setup

1. Created 4 custom permissions in `Book` model:
   - can_view
   - can_create
   - can_edit
   - can_delete

2. Created 3 groups:
   - Viewers → can only view books
   - Editors → can view, add, and edit books
   - Admins → can do everything

3. Used `@permission_required` decorator in views to enforce rules.
   Example:
   @permission_required('relationship_app.can_edit', raise_exception=True)
