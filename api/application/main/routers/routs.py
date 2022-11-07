from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
import requests
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
async def accept_client_trip(client_id: str, price: float):
    r = trips_register_trip('accept-client-trip', client_id, price)
    return r

#If a driver is looking for doing a trip
@router.get("/search-trip")
async def search_trip():
    r = trips_search_trip('search-trip')
    return r

#If a driver is looking for accept a trip
@router.post("/accept-driver-trip")
async def accept_driver_trip(trip_id, driver_id: str):
    r = trips_register_driver('accept-driver-trip', trip_id, driver_id)
    return r

#If a client answer about a driver was found
@router.post("/driver")
async def check_driver_status(trip_id):
    r = trips_get_driver('driver', trip_id)
    return r