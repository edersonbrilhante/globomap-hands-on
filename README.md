# Globo Map API

Application responsible for reading and writing in ARANGODB. This application has a RESTFul API.

## Starting Project:

Cloning projects
`$ git clone https://github.com/globocom/globomap-api `
`$ git clone https://github.com/globocom/globomap-core-loader `
`$ git clone https://github.com/globocom/globomap-ui `

Uping projects
`$ cd globomap-api; docker-compose up -d `
`$ cd globomap-core-loader; docker-compose up -d `
`$ cd globomap-ui; docker-compose up -d `

Verifying projects 
`$ docker ps `

All projects needed
globomap_api
globomap_db
globomap_keystone
globomap_loader
globomap_loader_api
globomap_loader_db_mysql
globomap_loader_queue
globomap_redis
globomap_ui

## Running Project
Creating collections, edges and graphs
`$ python3.6 base.py `

Insering documents
`$ python3.6 insert.py `

Open in browser
`http://localhost:8888/`

## Licensing

Globo Map API is under [Apache 2 License](./LICENSE)
