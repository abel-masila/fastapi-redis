import json

def create_delivery(state, event):
    data= json.loads(event.data)
    return  {
        "id":event.delivery_id,
        "budget":int(data["budget"]),
        "notes": data["notes"],
        "status":"ready"
    }

def start_delivery(state, event):
    return state | {
        "status":"active"
    }

CONSUMERS= {
    "CREATE_DELIVERY":create_delivery,
    "START_DELIVERY":start_delivery
}