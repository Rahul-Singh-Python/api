from rest_framework.throttling import UserRateThrottle

class jackRateThrottle(UserRateThrottle):
	scope = 'jack'