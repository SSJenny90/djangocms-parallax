from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from parallax.models import Parallax


@plugin_pool.register_plugin
class ParallaxWindowPlugin(CMSPluginBase):
    model = Parallax
    render_template = 'parallax/parallax.html'
    name = _('Parallax Image')
    allow_children = True
    fieldsets = (
        (_('Required'), {
            'fields': (
                'image',
                'include_jquery',
                'min_height',
            )
        }),
        (_('Optional'), {
            'fields': (
                # ('natural_width', 'natural_height'),
                'extra_css',
                'position_x',
                'position_y',
                'speed',
                'z_index',
                'bleed',

                # ('ios_fix', 'android_fix'),
                # 'thumbnail_option'
            ),
        })
    )
