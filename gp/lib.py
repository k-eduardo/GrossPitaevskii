def RK4(f):
    return lambda t, y, vy, dt: (
            lambda dy1: (
            lambda dy2: (
            lambda dy3: (
            lambda dy4: (dy1 + 2*dy2 + 2*dy3 + dy4)/6
            )( dt * f( t + dt  , y + dy3 , vy))
	    )( dt * f( t + dt/2, y + dy2/2   , vy))
	    )( dt * f( t + dt/2, y + dy1/2   , vy))
	    )( dt * f( t       , y           , vy))