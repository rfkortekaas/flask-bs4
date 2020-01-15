from markupsafe import Markup

from wtforms.widgets.core import html_params

def _wrap_form(form,
               action='',
               id=None,
               method='post',
               enctype=None,
               **kwargs):
    form_content = f'<form action="{action}" method="{method}" id="{id}" class="form" role="form" enctype="{enctype[0]}">\n'
    form_content += f'{form}\n</form>'

    return form_content

def _wrap_field(field, **kwargs):
    content = ''
    form_type = kwargs.get('form_type', 'basic')
    cols = kwargs.get('horizontal_columns', ('lg', 0, 12))

    if form_type == 'horizontal':
        col1 = 'col-{}-{}'.format(cols[0], cols[1])
        col2 = 'col-{}-{}'.format(cols[0], cols[2])
        off1 = 'offset-{}-{}'.format(cols[0], cols[1])

        content += '<div class="form-group row">\n'
        content += f'\t<div class="{col1}">{field.label}</div>\n'
        content += f'\t<div class="{col2}">{field(class_="form-control")}</div>\n'
        content += _add_description(field, **kwargs)
        content += '</div>\n'
    else:
        content += f'<div class="form-group">{field.label} {field(class_="form-control")}'
        content += _add_description(field, **kwargs)
        content += '</div>\n'
    return content

def _add_description(field, **kwargs):
    content = ''

    form_type = kwargs.get('form_type', 'basic')
    cols = kwargs.get('horizontal_columns', ('lg', 0, 12))

    col1 = f'col-{cols[0]}-{cols[1]}'
    col2 = f'col-{cols[0]}-{cols[2]}'
    off1 = f'offset-{cols[0]}-{cols[1]}'

    content += f'<small id="{ field.name }Help" class="form-text text-muted { off1 } { col2 }">'
    content += f'{ field.description }</small>'

    return content

def _wrap_boolean(field, **kwargs):
    content = ''
    form_type = kwargs.get('form_type', 'basic')
    horizontal_columns = kwargs.get('horizontal_columns', ('lg', 0, 12))

    col1 = 'col-{}-{}'.format(horizontal_columns[0], horizontal_columns[1])
    col2 = 'col-{}-{}'.format(horizontal_columns[0], horizontal_columns[2])
    off1 = 'offset-{}-{}'.format(horizontal_columns[0], horizontal_columns[1])

    content += f'<div class="form-group { "row" if form_type == "horizontal" else "" }">\n'
    content += f'\t<div class="{ off1 if form_type == "horizontal" else "" } { col2 if form_type == "horizontal" else "" }">'
    content += f'<div class="form-check">'
    content += f'{field(class_="form-check-input")}'
    content += f'{field.label(class_="form-check-label")}'
    content += f'</div>'
    content += f'</div>\n'
    content += _add_description(field, **kwargs)
    content += '</div>\n'

    return content

def _wrap_radio(field, **kwargs):
    content = ''
    form_type = kwargs.get('form_type', 'basic')
    horizontal_columns = kwargs.get('horizontal_columns', ('lg', 0, 12))

    col1 = 'col-{}-{}'.format(horizontal_columns[0], horizontal_columns[1])
    col2 = 'col-{}-{}'.format(horizontal_columns[0], horizontal_columns[2])
    off1 = 'offset-{}-{}'.format(horizontal_columns[0], horizontal_columns[1])

    if form_type == 'horizontal':
        content += '<div class="form-group row">\n'
        content += f'\t<legend class="col-form-label {col1} pt-0">{field.label}</legend>\n'
        content += f'\t<div class="form-check {col2}">'
        for key, value in field.choices:
            content += f'<div class="form-check {col2}">\n'
            content += f'<input class="form-check-input" type="radio" name="{field.name}" id="{key}" value="{key}" {"checked" if key == field.default else ""}>\n'
            content += f'<label class="form-check-label" for="{key}">{value}</label>'
            content += f'</div>\n'
        content += '</div>\n'
        content += _add_description(field, **kwargs)
        content += '</div>\n'
    else:
        content += '<div class="form-group">\n'
        content += f'\t<legend class="col-form-label pt-0">{field.label}</legend>\n'
        content += f'\t<div class="form-check">'
        for key, value in field.choices:
            content += f'<div class="form-check">\n'
            content += f'<input class="form-check-input" type="radio" name="{field.name}" id="{key}" value="{key}" {"checked" if key == field.default else ""}>\n'
            content += f'<label class="form-check-label" for="{key}">{value}</label>'
            content += f'</div>\n'
        content += '</div>\n'
        content += _add_description(field, **kwargs)
        content += '</div>\n'

    return content

def _wrap_file(field, **kwargs):
    content = ''
    ft = kwargs.get('form_type', 'basic')
    cols = kwargs.get('horizontal_columns', ('lg', 0, 12))

    col1 = 'col-{}-{}'.format(cols[0], cols[1])
    col2 = 'col-{}-{}'.format(cols[0], cols[2])
    off1 = 'offset-{}-{}'.format(cols[0], cols[1])

    content += f'<div class="form-group { "row" if ft == "horizontal" else "" }">\n'
    content += f'\t<div class="{ col1 if ft == "horizontal" else "" }"></div>\n'
    content += f'\t<div class="{ col2 if ft == "horizontal" else "" }">\n'
    content += f'\t<div class="custom-file">\n'
    content += field(class_='custom-file-input')
    content += field.label(class_='custom-file-label')
    content += f'\n\t</div>\n'
    content += f'\n\t</div>\n'
    content += _add_description(field, **kwargs)
    content += f'</div>\n'

    return content

def _wrap_submit(field, **kwargs):
    content = ''
    form_type = kwargs.get('form_type', 'basic')
    horizontal_columns = kwargs.get('horizontal_columns', ('lg', 0, 12))
    button_map = kwargs.get('button_map', {'submit': 'primary'})

    col1 = 'col-{}-{}'.format(horizontal_columns[0], horizontal_columns[1])
    col2 = 'col-{}-{}'.format(horizontal_columns[0], horizontal_columns[2])
    off1 = 'offset-{}-{}'.format(horizontal_columns[0], horizontal_columns[1])

    content += f'<div class="form-group { "row" if form_type == "horizontal" else "" }">\n'
    content += f'\t<div class="{ col1 if form_type == "horizontal" else "" }"></div>\n'
    content += f'\t<div class="{ col2 if form_type == "horizontal" else "" }">\n'
    content += field(class_=f'btn btn-{ button_map.get(field.name) }')
    content += f'\n\t</div>\n'
    content += _add_description(field, **kwargs)
    content += f'</div>\n'

    return content

def _wrap_csrf(field):
    return field()

def render_form(form, **kwargs):
    form_fields = ''
    _enctype = []

    for field in form:
        if field.type == 'BooleanField':
            form_fields += _wrap_boolean(field, **kwargs)
        elif field.type == 'RadioField':
            form_fields += _wrap_radio(field, **kwargs)
        elif field.type == 'FileField':
            if not _enctype:
                _enctype.append('multipart/form-data')
            form_fields += _wrap_file(field, **kwargs)
        elif field.type == 'SubmitField':
            form_fields += _wrap_submit(field, **kwargs)
        elif field.type == 'CSRFTokenField':
            form_fields += _wrap_csrf(field)
        else:
            form_fields += _wrap_field(field, **kwargs)

    return Markup(_wrap_form(form_fields, enctype=_enctype, **kwargs))