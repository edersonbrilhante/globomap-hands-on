from globomap_api_client.auth import Auth
from globomap_api_client.collection import Collection
from globomap_api_client.edge import Edge
from globomap_api_client.graph import Graph


auth_inst = Auth(
    api_url='http://localhost:5000',
    username='u_globomap_api',
    password='u_globomap_api'
)
coll = Collection(auth=auth_inst)
edge = Edge(auth=auth_inst)
graph = Graph(auth=auth_inst)
coll.post({
    'name':'vip',
    'alias': 'vip',
    'icon': 'icon',
})
coll.post({
    'name':'vm',
    'alias': 'vm',
    'icon': 'icon',
})
coll.post({
    'name':'network',
    'alias': 'network',
    'icon': 'icon',
})
edge.post({
    'name':'vip_vm',
    'alias': 'vip_vm',
    'icon': 'icon',
})
edge.post({
    'name':'network_vm',
    'alias': 'network_vm',
    'icon': 'icon',
})
edge.post({
    'name':'acl_access',
    'alias': 'acl_access',
    'icon': 'icon',
})
graph.post({
    "name": "load_balancing",
    "links": [
        {
            "edge": "vip_vm",
            "from_collections": [
                "vip"
            ],
            "to_collections": [
                "vm"
            ]
        }
    ]
})
graph.post({
    "name": "network",
    "links": [
        {
            "edge": "network_vm",
            "from_collections": [
                "network"
            ],
            "to_collections": [
                "vm"
            ]
        }
    ]
})
graph.post({
    "name": "security",
    "links": [
        {
            "edge": "acl_access",
            "from_collections": [
                "vm",
                "network",
            ],
            "to_collections": [
                "vm",
                "network",
                "vip",
            ]
        }
    ]
})
