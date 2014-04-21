import fitbit
import secret
from datetime import date, timedelta

def prettyPrintTime(minutes):
	hours = minutes / 60
	minutes = minutes % 60
	return "%d:%02d" % (hours, minutes)

client = fitbit.Fitbit(secret.FITBIT_CONSUMER_KEY, secret.FITBIT_CONSUMER_SECRET, resource_owner_key=secret.FITBIT_USER_KEY, resource_owner_secret=secret.FITBIT_USER_SECRET)
datesToCheck = []
for i in range(0, 7):
	datesToCheck.append(date.today() - timedelta(days=i))

totalTimeSlept = 0
for currentDate in datesToCheck:
	timeSlept = client.get_sleep(currentDate)['summary']['totalMinutesAsleep']
	totalTimeSlept += timeSlept
	print unicode(currentDate) + ': ' + prettyPrintTime(timeSlept)
print 'Total time slept: ' + prettyPrintTime(totalTimeSlept)

dailyGoal = raw_input('How much do you want to sleep on average every night (in hours)? ')
if dailyGoal:
	totalGoalTime = int(dailyGoal)*60*len(datesToCheck)
	print 'Total goal time: ' + prettyPrintTime(totalGoalTime)
	print 'Difference between goal and real: ' + prettyPrintTime(totalTimeSlept-totalGoalTime)