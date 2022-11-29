from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from application.initializer import LoggerInstance
# Local imports
from ..services.trips_endpoints import *

router = APIRouter()
logger = LoggerInstance().get_logger(__name__)

@router.get("/")
async def hello_world():
    logger.info('Hello World👍🏻')
    return JSONResponse(content={"message": "Hello World! 👍🏻"}, status_code=200)

#Example: Received travel distance
#Return: Trip price calculated with distance multiplied PRICE_PER_KILOMETER
@router.get("/trip-price")
async def price_calculator(distance: float):
    r = trips_trip_price("trip-price", distance)
    return r

#When a Client accept the travel´s price, we save the travel ID
#in a postgreSQL database waiting for a driver

@router.post("/accept-client-trip")
async def accept_client_trip(client_id: str, price: float,user_lat: float,user_long: float,dest_lat: float, dest_long: float):
    r = trips_register_trip('accept-client-trip', client_id, price, user_lat,user_long,dest_lat, dest_long)
    return r

#If a driver is looking for doing a trip
@router.get("/search-trip")
async def search_trip():
    r = trips_search_trip('search-trip')
    return r

#If a driver is looking for accept a trip
@router.post("/accept-driver-trip")
async def accept_driver_trip(trip_id, driver_id: str, driver_lat: float, driver_long: float):
    r = trips_register_driver('accept-driver-trip', trip_id, driver_id, driver_lat, driver_long)
    return r

#If a client answer about a driver was found
@router.post("/driver")
async def check_driver_status(trip_id):
    r = trips_get_driver('driver', trip_id)
    return r

# A driver needs to update his position
@router.put("/driver/position")
async def update_position(trip_id, driver_lat: float, driver_long: float):
    r = update_pos('driver/position', trip_id, driver_lat, driver_long)
    return r

# A client looking for driver position
@router.get("/trip-driver-position")
async def get_driver_position(trip_id):
    r = get_driver_pos('trip-driver-position', trip_id)
    return r

# A client want trip status = "Running" or "waiting" (for driver)
@router.get("/trip")
async def get_trip(trip_id):
    return get_trip_status('trip', trip_id)

# Init a Trip by setting status on "Running" from driver device
@router.put("/init")
async def init(trip_id):
    r = init_trip('init', trip_id)
    return r

@router.get("/passenger/email")
async def validate_register(email):
    return validate_user_registered('passenger/email', email)

@router.post("/passengers")
async def register_passenger(passenger: Passenger):
    return register_a_passenger('passengers', passenger)

@router.put("/passengers")
async def update_passenger(passenger: PassengerUpdateSchema):
    return update_a_passenger('passengers', passenger)