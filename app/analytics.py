async def check_maintenance_need(db_session, truck_id):
    # SQL logic: Get avg temp for the last 5 minutes
    query = f"""
    SELECT avg(engine_temp) 
    FROM truck_telemetry 
    WHERE truck_id = {truck_id} 
    AND time > NOW() - INTERVAL '5 minutes';
    """
    result = await db_session.execute(query)
    avg_temp = result.scalar()
    
    if avg_temp and avg_temp > 100:
        return True
    return False