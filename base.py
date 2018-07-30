from globomap_api_client.auth import Auth
from globomap_api_client.collection import Collection
from globomap_api_client.edge import Edge
from globomap_api_client.graph import Graph
from globomap_api_client.query import Query


auth_inst = Auth(
    api_url='http://localhost:5000',
    username='u_globomap_api',
    password='u_globomap_api'
)
coll = Collection(auth=auth_inst)
edge = Edge(auth=auth_inst)
graph = Graph(auth=auth_inst)
query = Query(auth=auth_inst)
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
query.post({
    "name": "real_by_vip",
    "description": "Servidores de um VIP",
    "query": "FOR doc1 IN @@collection1\n    FILTER doc1.`_id` == @variable\n    LET ports = (\n    FOR doc2 IN @@collection2\n        FILTER doc1.`_id` == doc2.`_from`\n        LET pool = (\n        FOR doc3 IN @@collection3\n            FILTER doc2.`_to` == doc3.`_id`                \n            FOR doc4 IN @@collection4\n                FILTER doc3.`_id` == doc4.`_from`                    \n                FOR doc5 IN @@collection5\n                    FILTER doc4.`_to` == doc5.`_id`\n                    RETURN doc5.name                    \n        )\n        LET name = FIRST(FILTER doc2.properties.l7_rule == 'Default VIP' RETURN '/') || doc2.properties.l7_rule\n        RETURN {\n            'path': name,\n            'port': doc2.properties.port,\n            'servers': pool\n        }\n    )     \n    RETURN {\n        'name': doc1.name,\n        'ports':ports\n    }",
    "params": {
        '@collection1': 'vip',
        '@collection2': 'port',
        '@collection3': 'pool',
        '@collection4': 'pool_comp_unit',
        '@collection5': 'comp_unit'
    },
    "collection": "vip"
})