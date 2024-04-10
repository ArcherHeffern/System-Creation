# TODO
- Server handle multiple connections
- Server shuts down connection after each request
- Fix .5 second sleep in ./run - Is hacky

# Running
Execute `./run.sh` to run the client and server. Server is run in the background and is automatically killed when client is killed

# Protocol
```
Request -> (floor_command | ceil_command | cos_command | sin_command) FLOAT


Response -> <success_response> | <failure_response>
Success Response -> "SUCCESS" <result:int>
Failure Response -> "FAILURE" <reason:str>
```
