from flask import redirect, url_for
from flask_admin.contrib.sqla import ModelView
from busyboard import form
from jinja2 import Markup
import os
import uuid
from werkzeug import secure_filename
from flask_admin import expose, AdminIndexView


def _list_thumbnail(view, context, model, name):
    if not model.filename:
        return ''

    return Markup(
        '<img src="{model.url}" style="width: 150px;">'.format(model=model)
    )


def _imagename_uuid1_gen(obj, file_data):
    _, ext = os.path.splitext(file_data.filename)
    uid = uuid.uuid1()
    return secure_filename('{}{}'.format(uid, ext))


class UserAdminView(ModelView):
    form_columns = ('name', 'busy', 'busy_with', 'can_be_disturbed', 'notes', 'path')
    form_excluded_columns = ('last_updated')
    column_editable_list = ('name', 'busy', 'busy_with', 'can_be_disturbed', 'notes')
    form_create_rules = ('name', 'busy', 'busy_with', 'can_be_disturbed', 'notes', 'path')
    form_edit_rules = ('name', 'busy', 'busy_with', 'can_be_disturbed', 'notes', 'path')

    can_create = True

    column_formatters = {
        'image': _list_thumbnail
    }

    form_extra_fields = {
        'path': form.ImageUploadField(
            'Image',
            base_path='busyboard/static/images',
            url_relative_path='images/',
        )
    }


class CustomIndexView(AdminIndexView):
    def is_visible(self):
        # This view won't appear in the menu structure
        return False

    @expose('/')
    def index(self):
        return redirect(url_for('main_route'))
