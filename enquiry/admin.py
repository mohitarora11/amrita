from django.contrib import admin

from models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    exclude = ('done_by',)

    def save_model(self, request, obj, form, change):
        super(ContactUsAdmin, self).save_model(request, obj, form, change)
        obj.done_by = request.user
        obj.save()

admin.site.register(ContactUs,ContactUsAdmin)
