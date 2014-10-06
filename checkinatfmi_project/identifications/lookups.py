from ajax_select import LookupChannel
from activities.models import Carrier


class IdentificationLookup(LookupChannel):
    model = Carrier

    def get_query(self,q,request):
        return Carrier.objects.filter(data__icontains=q).order_by('data')
