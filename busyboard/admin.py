from flask_admin.contrib.sqla import ModelView


class UserAdminView(ModelView):
    """
    News view in admin page, specifies what is available in CRUD
    """
    form_columns = ('name', 'busy', 'busy_with', 'can_be_disturbed', 'notes')
    form_excluded_columns = ('last_updated')
    column_editable_list = ('name', 'busy', 'busy_with', 'can_be_disturbed', 'notes')
    form_create_rules = ('name', 'busy', 'busy_with', 'can_be_disturbed', 'notes')
    form_edit_rules = ('name', 'busy', 'busy_with', 'can_be_disturbed', 'notes')

    can_create = True