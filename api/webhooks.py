import json

from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from psqlextra.query import ConflictAction

from .models import Device


@csrf_exempt
def index(request):
    data = json.loads(request.body.decode())
    print(data)

    device_id = data['client_id']

    print(Device.objects.filter(id=device_id))

    if data['action'] == 'client_connected':
        device = Device.objects\
            .on_conflict(['id'], ConflictAction.NOTHING)\
            .insert_and_get(id=device_id, online=True)

        device.temps.create(value=29)
        device.temps.create(value=35)

        device.bps.create(value=520)
        device.bps.create(value=580)
    elif data['action'] == 'client_disconnected':
        Device.objects\
            .on_conflict(['id'], ConflictAction.UPDATE)\
            .insert(id=device_id, online=False)

    return HttpResponse()
