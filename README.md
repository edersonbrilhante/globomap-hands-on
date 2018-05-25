# Globo Map API

Application responsible for reading and writing in ARANGODB. This application has a RESTFul API.

## Starting Project:

### Cloning projects
`$ git clone https://github.com/globocom/globomap-api ` <br>
`$ git clone https://github.com/globocom/globomap-core-loader ` <br>
`$ git clone https://github.com/globocom/globomap-ui ` <br>

### Uping projects
`$ cd globomap-api; docker-compose up -d ` <br>
`$ cd globomap-core-loader; docker-compose up -d ` <br>
`$ cd globomap-ui; docker-compose up -d ` <br>

### Verifying projects 
`$ docker ps `

All projects needed<br>
globomap_api <br>
globomap_db <br>
globomap_keystone <br>
globomap_loader <br>
globomap_loader_api <br>
globomap_loader_db_mysql <br>
globomap_loader_queue <br>
globomap_redis <br>
globomap_ui <br>

## Running Project
### Creating collections, edges and graphs <br>
`$ python3.6 base.py ` <br>

### Insering documents <br>
`$ python3.6 insert.py ` <br>

Open in browser <br>
`http://localhost:8888/` <br>

## Licensing

Globo Map API is under [Apache 2 License](./LICENSE)
