# FIUBER API GATEWAY

API Gateway connecting Fiuber´s micro-services.

## Routes

- `{gateway}/driver`: Users API, Endpoint about registering and modifing driver users
- `{gateway}/passengers`: Users API, Endpoint about registering and modifing client/passenger users

- `Trips Endpoints` :
`{gateway}/trip` : Info about a trip, finish trips, cancel a trip
`{gateway}/init` : Initializing a trip
`{gateway}/score` : Getting users scores
`{gateway}/accept-client-trip` : Accepting client trips
`{gateway}/accept-driver-trip` : Accepting a driver who wants to do a trip


## Development

### Running the server

**docker build -t fastapi-image  .**

**docker run -d --name fastapi-container -p 8000:8000 fastapi-image**

### Deploy

The pipeline is deployed manually in Heroku with HEROKU CLI

You should create the app on heroku first, install Heroku Cli and run its installation's instructions

