from oscar.apps.catalogue.admin import *  # noqa
from mainsite.catalogue import models as catalogue_model

admin.site.register(catalogue_model.UNIQLOItem)
admin.site.register(catalogue_model.Application_Records)
admin.site.register(catalogue_model.size)
admin.site.register(catalogue_model.color)




