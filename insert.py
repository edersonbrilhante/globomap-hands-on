import time
from globomap_loader_api_client.auth import Auth
from globomap_loader_api_client.update import Update

auth_inst = Auth(
    api_url='http://localhost:5003',
    username='u_globomap_api',
    password='u_globomap_api'
)

update = Update(auth=auth_inst, driver_name='python_nordeste')

# Create vip
data = {
    "action": "CREATE",
    "collection": "vip",
    "element": {
        "id": "300",
        "name": "pythonne.globo.com",
        "properties": {
            "ip": "10.0.10.1",
            "ambiente": "Produção BE"
        },
        "provider": "pyne",
        "timestamp": int(time.time())
    },
    "type": "collections"
}
res = update.post(data)

# Create vip_vm
data = {
    "action": "CREATE",
    "collection": "vip_vm",
    "element": {
        "id": "100",
        "name": "vmxpto12 - 10.9.9.1",
        "properties": {
            "porta": "8000"
        },
        "provider": "pyne",
        "timestamp": int(time.time()),
        "from": "vip/pyne_300",
        "to": "vm/pyne_1"
    },
    "type": "edges"
}
res = update.post(data)

# Create vm
data = {
    "action": "CREATE",
    "collection": "vm",
    "element": {
        "id": "1",
        "name": "vmxpto12",
        "properties": {
            "ip": "10.9.9.1",
        },
        "provider": "pyne",
        "timestamp": int(time.time())
    },
    "type": "collections"
}
res = update.post(data)

# Create vm
data = {
    "action": "CREATE",
    "collection": "vm",
    "element": {
        "id": "2",
        "name": "vmxpto13",
        "properties": {
            "ip": "10.10.9.2",
        },
        "provider": "pyne",
        "timestamp": int(time.time())
    },
    "type": "collections"
}
res = update.post(data)

# Create network
data = {
    "action": "CREATE",
    "collection": "network",
    "element": {
        "id": "1",
        "name": "Rede python",
        "properties": {
            "network": "10.9.9.0/24",
        },
        "provider": "pyne",
        "timestamp": int(time.time())
    },
    "type": "collections"
}
res = update.post(data)

# Create network
data = {
    "action": "CREATE",
    "collection": "network",
    "element": {
        "id": "2",
        "name": "Rede mysql",
        "properties": {
            "network": "10.10.9.2/24",
        },
        "provider": "pyne",
        "timestamp": int(time.time())
    },
    "type": "collections"
}
res = update.post(data)

# Create network_vm
data = {
    "action": "CREATE",
    "collection": "network_vm",
    "element": {
        "id": "1",
        "name": "Ip 10.9.9.1",
        "properties": {
            "ip": "10.9.9.1",
        },
        "provider": "pyne",
        "timestamp": int(time.time()),
        "from": "network/pyne_1",
        "to": "vm/pyne_1"
    },
    "type": "edges"
}
res = update.post(data)

# Create network_vm
data = {
    "action": "CREATE",
    "collection": "network_vm",
    "element": {
        "id": "2",
        "name": "Ip 10.9.9.2",
        "properties": {
            "ip": "10.9.9.2",
        },
        "provider": "pyne",
        "timestamp": int(time.time()),
        "from": "network/pyne_2",
        "to": "vm/pyne_2"
    },
    "type": "edges"
}
res = update.post(data)

# Create acl_access
data = {
    "action": "CREATE",
    "collection": "acl_access",
    "element": {
        "id": "1",
        "name": "10.9.9.1 - 10.10.9.2",
        "properties": {
            "porta": "3306",
        },
        "provider": "pyne",
        "timestamp": int(time.time()),
        "from": "vm/pyne_1",
        "to": "vm/pyne_2"
    },
    "type": "edges"
}
res = update.post(data)
