from django.contrib import admin
from .forms import CompanyDescriptionForm

from .models import *

# Register your models here.

class CompanyDescriptionAdmin(admin.ModelAdmin):
    form = CompanyDescriptionForm

admin.site.register(CompanyDescription, CompanyDescriptionAdmin)

# class ClBlockedReasonDictAdmin(admin.ModelAdmin):
#     fields = ['id_cl_blocked_reason_dict', 'blocked_reason_name']
# admin.site.register(ClBlockedReasonDict, ClBlockedReasonDictAdmin)
# 
#
# admin.site.register(ClBlockedReasonDict)
# admin.site.register(ClCommunicationLog)
# admin.site.register(ClCommunicationReason)
# admin.site.register(ClDiscount)
#
# admin.site.register(ClParams)
# admin.site.register(ClPayment)
# admin.site.register(ClPaymentLine)
# admin.site.register(ClUnconfirmed)
# admin.site.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name')
# admin.site.register(Client, ClientAdmin)
# #admin.site.register(Contact)
#
# class ContactInline(admin.TabularInline):
#     model = Contact
#     extra = 2
# class ClientAdmin(admin.ModelAdmin):
#     inlines = (ContactInline, )
# # admin.site.unregister(Client)
# admin.site.register(Client, ClientAdmin)

admin.site.register(CompanyBranch)
# admin.site.register(Address)
# admin.site.register(ContactType)
# admin.site.register(CountryDict)
# admin.site.register(Currrency)
# admin.site.register(DiscountDict)
# admin.site.register(DiscountScope)
admin.site.register(Location)
admin.site.register(LocationType)
# admin.site.register(Machine)
# admin.site.register(MachineType)
# admin.site.register(ResourcesUsage)
# admin.site.register(ResourcesUsageParams)
# admin.site.register(SeDict)
# admin.site.register(SeDiscount)
# admin.site.register(SeRequirement)
# class ServiceAdmin(admin.ModelAdmin):
#     # TODO w rzeczywistosci dobrze by pociagnac nazwe serwisu, nie kod i imie/nazwisko/nazwe klienta,
#     # a nie jego id
#     list_display = ('id_service', 'service_code', 'client')
#     search_fields = ('id_service', 'service_code', 'client')
#     list_filter = ('service_code',)
#     ordering = ('created_datetime',)
#     fields = ('is_confirmed', 'service_code', 'client', 'location', 'create_invoice', 'min_start_datetime', 'planned_start', 'planned_end', 'notes')

# admin.site.register(Service, ServiceAdmin)

# admin.site.register(Service)
# admin.site.register(ServiceArchived)
# admin.site.register(SexDict)
"""
admin.site.register(TClientBlockedListV)
admin.site.register(TClientDetailsV)
admin.site.register(TClientListV)
admin.site.register(TClientNotAcceptedListV)
admin.site.register(TClientParamsV)
admin.site.register(TClientPaymentLineV)
admin.site.register(TClientPaymentListAllV)
admin.site.register(TClientPaymentListClosedV)
admin.site.register(TClientPaymentListPostedUnpaidV)
admin.site.register(TClientPaymentListUnpostedV)
admin.site.register(TClientPaymentV)
admin.site.register(TDiscountV)
admin.site.register(TLocationTypeDetailsV)
admin.site.register(TLocationTypeListV)
admin.site.register(TLocationV)
admin.site.register(TMachineIncomingServicesV)
admin.site.register(TMachineTypeDetailsV)
admin.site.register(TMachineTypeListV)
admin.site.register(TMachineV)
admin.site.register(TPaymentListOverdueV)
admin.site.register(TResourcesUsageListV)
admin.site.register(TResourcesUsageParamsV)
admin.site.register(TServiceAcceptV)
admin.site.register(TServiceDetailsV)
admin.site.register(TServiceDictDetailsV)
admin.site.register(TServiceDictListV)
admin.site.register(TServiceListV)
admin.site.register(TTimeSlotParamsV)
admin.site.register(TWorkdayCalendarV)
admin.site.register(TWorkerAbilityDetailsV)
admin.site.register(TWorkerAbilityDictDetailsV)
admin.site.register(TWorkerAbilityDictListV)
admin.site.register(TWorkerAbilityGroupDictDetailsV)
admin.site.register(TWorkerAbilityGroupDictListV)
admin.site.register(TWorkerAbilityListV)
admin.site.register(TWorkerAbsenceAllV)
admin.site.register(TWorkerAbsenceCalendarV)
admin.site.register(TWorkerAbsenceCurrentV)
admin.site.register(TWorkerAbsenceDetailsV)
admin.site.register(TWorkerAbsenceEndedV)
admin.site.register(TWorkerAbsenceFutureV)
admin.site.register(TWorkerAbsenceHourV)
admin.site.register(TWorkerAbsenceOtherV)
admin.site.register(TWorkerAbsenceRecreationalV)
admin.site.register(TWorkerAbsenceSickV)
admin.site.register(TWorkerDetailsV)
admin.site.register(TWorkerGroupDictDetailsV)
admin.site.register(TWorkerGroupDictListV)
admin.site.register(TWorkerGroupPrivilegeV)
admin.site.register(TWorkerListActiveV)
admin.site.register(TWorkerListAllV)
admin.site.register(TWorkerListInactiveV)
admin.site.register(TWorkerListIncomingLeaveV)
admin.site.register(TWorkerListOnLeaveV)
admin.site.register(TWorkerUserDetailsV)
admin.site.register(TWorkerUserListV)
"""
# # admin.site.register(TimeSlotList)
# admin.site.register(TimeSlotParams)
# admin.site.register(WoAbility)
# admin.site.register(WoAbilityDict)
# # admin.site.register(WoAbilityGroupDict)
# # admin.site.register(WoAbsence)
# # admin.site.register(WoAbsenceType)
# # admin.site.register(WoGroup)
# # admin.site.register(WoGroupDict)
# # admin.site.register(WoGroupPrivilege)
# # admin.site.register(WoNotification)
# # admin.site.register(WoPrivilegeDict)
# # admin.site.register(WoPrivilegeLevelDict)
# # admin.site.register(WoUser)
# admin.site.register(WorkdayCalendar)
# admin.site.register(WorkdayCalendarParams)
# admin.site.register(Worker)
# admin.site.register(ZipCodesDict)
