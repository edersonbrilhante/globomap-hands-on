import time
from globomap_loader_api_client.auth import Auth
from globomap_loader_api_client.update import Update

auth_inst = Auth(
    api_url='http://localhost:5003',
    username='u_globomap_api',
    password='u_globomap_api'
)


update = Update(auth=auth_inst, driver_name='talk_globomap')

data = {
    "action": "CLEAR",
    "collection": "vip",
    "element": [
      [
        {
          "field": "timestamp",
          "operator": ">",
          "value": 1
        }
      ]
    ],
    "type": "collections"
  }
res = update.post(data)

data = {
    "action": "CLEAR",
    "collection": "vip_vm",
    "element": [
      [
        {
          "field": "timestamp",
          "operator": ">",
          "value": 1
        }
      ]
    ],
    "type": "edges"
  }
res = update.post(data)

data = {
    "action": "CLEAR",
    "collection": "vm",
    "element": [
      [
        {
          "field": "timestamp",
          "operator": ">",
          "value": 1
        }
      ]
    ],
    "type": "collections"
  }
res = update.post(data)

data = {
    "action": "CLEAR",
    "collection": "network",
    "element": [
      [
        {
          "field": "timestamp",
          "operator": ">",
          "value": 1
        }
      ]
    ],
    "type": "collections"
  }
res = update.post(data)

data = {
    "action": "CLEAR",
    "collection": "network_vm",
    "element": [
      [
        {
          "field": "timestamp",
          "operator": ">",
          "value": 1
        }
      ]
    ],
    "type": "edges"
  }
res = update.post(data)

data = {
    "action": "CLEAR",
    "collection": "acl_access",
    "element": [
      [
        {
          "field": "timestamp",
          "operator": ">",
          "value": 1
        }
      ]
    ],
    "type": "edges"
  }
res = update.post(data)


data = {
    "action": "CLEAR",
    "collection": "vip",
    "element": [
      [
        {
          "field": "timestamp",
          "operator": ">",
          "value": 1
        }
      ]
    ],
    "type": "collections"
  }
res = update.post(data)

data = {
    "action": "CLEAR",
    "collection": "vip_vm",
    "element": [
      [
        {
          "field": "timestamp",
          "operator": ">",
          "value": 1
        }
      ]
    ],
    "type": "edges"
  }
res = update.post(data)

data = {
    "action": "CLEAR",
    "collection": "vm",
    "element": [
      [
        {
          "field": "timestamp",
          "operator": ">",
          "value": 1
        }
      ]
    ],
    "type": "collections"
  }
res = update.post(data)

data = {
    "action": "CLEAR",
    "collection": "network",
    "element": [
      [
        {
          "field": "timestamp",
          "operator": ">",
          "value": 1
        }
      ]
    ],
    "type": "collections"
  }
res = update.post(data)

data = {
    "action": "CLEAR",
    "collection": "network_vm",
    "element": [
      [
        {
          "field": "timestamp",
          "operator": ">",
          "value": 1
        }
      ]
    ],
    "type": "edges"
  }
res = update.post(data)

data = {
    "action": "CLEAR",
    "collection": "acl_access",
    "element": [
      [
        {
          "field": "timestamp",
          "operator": ">",
          "value": 1
        }
      ]
    ],
    "type": "edges"
  }
res = update.post(data)

# Create vip
data = {
    "action": "CREATE",
    "collection": "vip",
    "element": {
        "id": "300",
        "name": "talk_globomap.globo.com",
        "properties": {
            "ip": "10.0.10.1",
            "ambiente": "Produção BE"
        },
        "provider": "talk_globomap",
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
        "provider": "talk_globomap",
        "timestamp": int(time.time()),
        "from": "vip/talk_globomap_300",
        "to": "vm/talk_globomap_1"
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
        "provider": "talk_globomap",
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
        "provider": "talk_globomap",
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
        "provider": "talk_globomap",
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
        "provider": "talk_globomap",
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
        "provider": "talk_globomap",
        "timestamp": int(time.time()),
        "from": "network/talk_globomap_1",
        "to": "vm/talk_globomap_1"
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
        "provider": "talk_globomap",
        "timestamp": int(time.time()),
        "from": "network/talk_globomap_2",
        "to": "vm/talk_globomap_2"
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
        "provider": "talk_globomap",
        "timestamp": int(time.time()),
        "from": "vm/talk_globomap_1",
        "to": "vm/talk_globomap_2"
    },
    "type": "edges"
}
res = update.post(data)
