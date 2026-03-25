from sqlalchemy import select, func
from geoalchemy2.shape import from_shape
from shapely.geometry import Point

async def is_inside_geofence(db_session, lat, lng, warehouse_id):
    # Create a PostGIS point from incoming coordinates
    point = f'POINT({lng} {lat})'
    
    # Query: Is this point inside the warehouse polygon?
    query = select(Warehouse).where(
        func.ST_Within(func.ST_GeomFromText(point, 4326), Warehouse.geom)
    )
    
    result = await db_session.execute(query)
    return result.scalar_one_or_none() is not None

# Inside your WebSocket Loop:
# is_safe = await is_inside_geofence(db, data['latitude'], data['longitude'], 1)
# if not is_safe:
#     await manager.broadcast_to_admins({"alert": "GEOFENCE_VIOLATION", "truck_id": truck_id})