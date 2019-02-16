import json

from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from psqlextra.query import ConflictAction

from .models import Device


@csrf_exempt
def index(request):
    try:
        data = json.loads(request.body.decode())
        print(data)

        device_id = data['client_id']

        if data['action'] == 'client_connected':
            Device.objects\
                .on_conflict(['id'], ConflictAction.UPDATE)\
                .insert_and_get(id=device_id,
                                online=True)

        elif data['action'] == 'client_disconnected':
            Device.objects\
                .on_conflict(['id'], ConflictAction.UPDATE)\
                .insert(id=device_id,
                        online=False,
                        last_shutdown_reason=
                        data['reason'] if 'reason' in data and data['reason'] != 'undefined' else 'unknown')
    except:
        pass

    return HttpResponse()
