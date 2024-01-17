from django.contrib import admin
from breaks.models import organisations, groups, replacements, dicts, breaks


#########
# INLINES
#########
class ReplacementEmployeeInline(admin.TabularInline):
    model = replacements.ReplacementEmployee
    fields = ('employee', 'status')


@admin.register(organisations.Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director')


@admin.register(groups.Group)
class GroupAdmin(OrganisationAdmin):
    list_display = ('id', 'name', 'manager', 'min_active')


@admin.register(dicts.ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'name', 'sort', 'is_active'
    )


@admin.register(dicts.BreakStatus)
class BreaksStatusAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'name', 'sort', 'is_active'
    )


@admin.register(replacements.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'group', 'date', 'break_start', 'break_end', 'break_max_duration'
    )

    inlines = [ReplacementEmployeeInline]


@admin.register(breaks.Break)
class BreakAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'replacement', 'break_start', 'break_end')
