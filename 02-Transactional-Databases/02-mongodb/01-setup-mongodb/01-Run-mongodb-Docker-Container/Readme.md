# How to Run a MongoDB Server With Docker Compose?

## What is Docker Compose?

- **Docker Compose** is a very powerful tool that’s used to manage multiple containers, called services, with a single file.

# Setup

## Step 1: Create a `docker-compose.yml` File

- Create a `docker-compose.yml` file with the following service:

  ```yml
  #docker-compose.yml for mongodb
  version: "2"
  services:
    mongo:
      image: mongo:latest
      container_name: mongo
      environment:
        - MONGO_INITDB_ROOT_USERNAME: root
        - MONGO_INITDB_ROOT_PASSWORD: rootpassword
        - MONGO_INITDB_DATABASE=admin #you can omit this
      ports:
        - "27017:27017"
      volumes:
        - mongo_volume:/data/db
  volumes:
    mongo_data:
  ```

- Where:
  - `MONGO_INITDB_DATABASE`: used to specify the name of the initial database to be created when the **MongoDB container** starts up for the first time. If you don't specify it, MongoDB will default to creating a database named `test`. If you're not planning to create a specific initial database or if you're only working with the default `test` database, you can omit this line from the `docker-compose.yml` file.
  - The `27017:27017` in this command maps the container port to the host port. This allows you to connect to **MongoDB** with a `localhost:27017` connection string.

## Step 2: Start the database service

- start the MongoDB services defined in the compose file by executing the given command:
  ```sh
    docker-compose up --build -d
  ```
- You can view the running mongodb container by `docker ps` command.

## Step 3: Access MongoDB

## Step 3.1: Access MongoDB via MongoDB Compass

- Connection string:

  ```sh
    mongodb://localhost:27017
  ```

- Remarks:
  - If you already installed "MongoDB", and if you accidentally exit from the MongoDB server, then "restart your system".
  - On **Windows**: press `Windows + R`, then type `services.msc` and click "ok", it opens "services" window, and then search for "MongoDB Server" in the list. After you find "MongoDB Server", right-click and choose "start" from the pop-up menu.

## Step 3.2: Connect to the MongoDB Deployment with `mongosh`

- Open the Bash shell inside the running MongoDB container through the following command
  ```sh
    docker exec -it mongo bash
  ```
- Once you're inside the container, you can then start `mongosh`:
  ```bash
    mongosh
  ```
- This command launches the **mongosh shell**, allowing you to interact with the MongoDB instance running inside the container. Sample output is as shown below:

  ```bash
    root@b807fe258a24:/# mongosh
    Current Mongosh Log ID: 665741e84617c7a4672202d7
    Connecting to:          mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.5
    Using MongoDB:          7.0.9
    Using Mongosh:          2.2.5

    For mongosh info see: https://docs.mongodb.com/mongodb-shell/
  ```

- **Remark**:
  - To confirm your **MongoDB** instance is running, run the Hello command:
    ```sh
      db.runCommand({hello: 1})
    ```
  - The result of this command returns a document describing your `mongod` deployment:
    ```sh
      {
        isWritablePrimary: true,
        topologyVersion: {
          processId: ObjectId('66573f5ac9f4dcfbff93864d'),
          counter: Long('0')
        },
        maxBsonObjectSize: 16777216,
        maxMessageSizeBytes: 48000000,
        maxWriteBatchSize: 100000,
        localTime: ISODate('2024-05-29T14:58:41.485Z'),
        logicalSessionTimeoutMinutes: 30,
        connectionId: 21,
        minWireVersion: 0,
        maxWireVersion: 21,
        readOnly: false,
        ok: 1
      }
    ```