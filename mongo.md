## Version
MongoDB 8.0 Community Edition on Ubuntu (8.0.4)

`https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/`

Ubuntu version:
24.04.1 LTS

```bash
>> $mongod --version
db version v8.0.4
Build Info: {
    "version": "8.0.4",
    "gitVersion": "bc35ab4305d9920d9d0491c1c9ef9b72383d31f9",
    "openSSLVersion": "OpenSSL 3.0.13 30 Jan 2024",
    "modules": [],
    "allocator": "tcmalloc-google",
    "environment": {
        "distmod": "ubuntu2404",
        "distarch": "x86_64",
        "target_arch": "x86_64"
    }
}
```

## Create User 

1. connect to Mongo with `mongosh`
2. Switch to admin database `use admin`
3. Create user and pass
```mongo
db.createUser({
  user: "tickex",
  pwd: "tickex",
  roles: [{ role: "root", db: "admin" }]
}) 
```

To create a database, simply run `use tickex`

## Env Variables

```bash
export MONGO_PASS=tickex
export MONGO_URI=127.0.0.1:27017
export MONGO_USER=tickex
```

