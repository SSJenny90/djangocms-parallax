from cms.models import CMSPlugin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext as _
from filer.fields.image import FilerImageField
from filer.models import ThumbnailOption


class Parallax(CMSPlugin):
    # REQUIRED
    image = FilerImageField(
        verbose_name=_('image'),
        help_text=('Please choose or upload the desired image.'),
        on_delete=models.PROTECT)
    min_height = models.PositiveSmallIntegerField(
        verbose_name=_('Minimum height (px)'),
        help_text=_(
            'Sets the minimum height of the div element (in pixels) to ensure the image is always visible, even without content.'),
        default=400,
    )

    # PARALLAX JS OPTIONS
    position_x = models.CharField(
        verbose_name='positionX',
        help_text=_('This is analogous to the background-position css property. Specify coordinates as top, bottom, right, left, center, or pixel values (e.g. -10px 0px). The parallax image will be positioned as close to these values as possible while still covering the target element.'),
        max_length=10,
        blank=True)
    position_y = models.CharField(
        verbose_name='positionY',
        help_text=_('This is analogous to the background-position css property. Specify coordinates as top, bottom, right, left, center, or pixel values (e.g. -10px 0px). The parallax image will be positioned as close to these values as possible while still covering the target element.'),
        max_length=10,
        blank=True)
    speed = models.FloatField(
        verbose_name='speed',
        help_text=_('The speed at which the parallax effect runs. 0.0 means the image will appear fixed in place, and 1.0 the image will flow at the same speed as the page content.'),
        null=True, blank=True,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(1.0)
        ])
    z_index = models.SmallIntegerField(
        verbose_name='zIndex',
        help_text=_(
            'The z-index value of the fixed-position elements. By default these will be behind everything else on the page.'),
        null=True, blank=True,
        validators=[MaxValueValidator(-1)])
    bleed = models.SmallIntegerField(
        verbose_name='bleed',
        help_text=_('You can optionally set the parallax mirror element to extend a few pixels above and below the mirrored element. This can hide slow or stuttering scroll events in certain browsers.'),
        null=True, blank=True)

    # EXTRA OPTIONS
    extra_css = models.CharField(
        verbose_name=_('extra CSS'),
        help_text=_(
            'Extra CSS classes to attach to the containing <div> element. By default this element contains the .parallax-window CSS class'),
        max_length=255,
        blank=True)
    include_jquery = models.BooleanField(
        verbose_name=_('include JQuery'),
        help_text=_('Parallax.js requires jQuery but this plugin does not include it by default because it\'s assumed you\'re website already includes it.'),
        default=False)
