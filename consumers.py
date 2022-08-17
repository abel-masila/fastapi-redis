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